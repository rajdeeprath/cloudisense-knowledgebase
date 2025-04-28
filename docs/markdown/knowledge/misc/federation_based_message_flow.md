# Cloudisense Cluster Communication Flows

This document describes the complete set of communication flows between browser clients, local Cloudisense nodes, and remote Cloudisense nodes over WebSocket and MQTT. Each section outlines a specific communication type, its step-by-step flow, and the roles of different system components, along with practical use case examples.

---

## 1. Browser Client ➞ Local Cloudisense (Direct RPC)

### Description:
A browser client connected via WebSocket sends an RPC to the local Cloudisense instance.

### Use Case:
A client invokes `getSystemInfo` to display system diagnostics.

### Flow:
1. **Client** sends JSON RPC message via WebSocket.
2. Tornado WebSocket handler parses the message.
3. Calls `MessageRouter.handle_messages(message, client)`.
4. Message is classified as `local_rpc`.
5. Routed to `MessageRouter._process_local_rpc()`.
6. Local `IRPCGateway` handles the message.
7. Response is sent back to the client using `client.message_to_client()`.

---

## 2. Browser Client ➞ Remote Cloudisense (Forwarded RPC)

### Description:
Client wants to trigger an RPC on a remote Cloudisense node.

### Use Case:
A web-based dashboard wants to fetch logs from a remote site.

### Flow:
1. **Client** sends RPC with `serviceId` set to remote node.
2. `MessageRouter.handle_messages()` classifies it as `network_rpc`.
3. `MessageRouter._process_remote_rpc()` is called.
4. Adds `clientId` and `originId` to the message.
5. Stores `(message, client)` in `__message_directory[requestid]`.
6. Forwards the message to the remote node via `FederationGateway.send_message()`.

---

## 3. Remote Cloudisense ➞ Browser Client (RPC Response)

### Description:
Remote node sends a response to a browser-initiated RPC.

### Use Case:
Remote node replies with system logs or metrics.

### Flow:
1. Remote node sends response over MQTT.
2. Federation client on local node receives message.
3. Calls `MessageRouter._handle_remote_message()`.
4. Message added to `__incoming_messages` queue.
5. `__process_messages()` classifies it as `rpc_response`.
6. Retrieves `(message, client)` from `__message_directory`.
7. Calls `handle_remote_response()` to send result/error to browser via WebSocket.

---

## 4. Remote Cloudisense ➞ Local Cloudisense (New RPC Request)

### Description:
A remote node initiates a fresh RPC to the local node.

### Use Case:
A remote instance asks a peer to restart a shared agent.

### Flow:
1. Remote sends message with `type: "rpc"` over MQTT.
2. Federation receives and calls `_handle_remote_message()`.
3. Message queued in `__incoming_messages`.
4. `__process_messages()` detects RPC.
5. Wraps `originId` into `RemoteMessagingClient`.
6. Calls `_process_local_rpc(message, remote_client)`.
7. Local `IRPCGateway` executes RPC.
8. Response is sent back to remote node via MQTT using `remote_client.message_to_client()`.

---

## 5. Local Cloudisense ➞ Remote Cloudisense (Respond to Remote-Initiated RPC)

### Description:
When a remote node calls a local RPC, this is how the local node replies.

### Use Case:
Replying with `restartSuccess` after remote agent restart.

### Flow:
1. In `_process_local_rpc()`, `client` is a `RemoteMessagingClient`.
2. After `IRPCGateway.handleRPC()` returns result/error,
3. `RemoteMessagingClient.message_to_client()` uses `FederationGateway.send_message()` to respond.

---

## 6. Local Cloudisense ➞ Remote Cloudisense (Programmatic RPC)

### Description:
Local service/module initiates a remote RPC (not from browser).

### Use Case:
An automation engine triggers `updateSensorFirmware` on a remote node.

### Flow:
1. Module calls `MessageRouter.initiate_remote_rpc(service_id, method, params, on_response)`.
2. Generates a new `requestid`.
3. Constructs the message with metadata.
4. Stores `on_response` callback in `__message_directory[requestid]`.
5. Sends message to remote node via `FederationGateway.send_message()`.

---

## 7. Remote Cloudisense ➞ Local Cloudisense (RPC Response to Programmatic RPC)

### Description:
The remote node sends a response to a programmatic RPC initiated by the local instance.

### Use Case:
Remote node confirms firmware update completion.

### Flow:
1. Response arrives over MQTT.
2. `_handle_remote_message()` queues it.
3. `__process_messages()` classifies as `rpc_response`.
4. Finds a `Callable` in `__message_directory[requestid]`.
5. Executes the stored `on_response(response)` handler.

---

## 8. One Cloudisense ➞ All Cloudisense (Broadcast RPC)

### Description:
Used for broadcasting events (e.g., alerts, sync requests) to all instances.

### Use Case:
System-wide heartbeat check or configuration sync.

### Flow:
1. Message with `type: "rpc"` and `serviceId: "*"` is published via MQTT.
2. All nodes receive the message via `FederationGateway`.
3. `_handle_remote_message()` queues the message.
4. `__process_messages()` classifies it as `broadcast_rpc`.
5. Calls `_handle_broadcast_rpc()`:
   - Executes `IRPCGateway.handleRPC(None, message)` (fire-and-forget)
6. No response is expected.

---

## Notes
- `RemoteMessagingClient` is used as a virtual client for federation-origin RPCs.
- `__message_directory` tracks both WebSocket client tuples and internal callbacks.
- Federation is based on MQTT (`cloudisense/service/{id}/inbox`).
- All communication is secured via `originId` tagging.

---

This documentation ensures that all message routing paths in a Cloudisense cluster are well understood, traceable, and extendable.
