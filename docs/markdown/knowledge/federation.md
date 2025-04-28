## Federation Communication

# Cloudisense Communication Types

| #  | Direction                                      | Medium              | Type                        | Description                                                                 |
|----|-----------------------------------------------|---------------------|-----------------------------|-----------------------------------------------------------------------------|
| 1  | Browser Client ➝ Local Cloudisense            | WebSocket           | RPC Request                 | Client sends RPC directly to its connected Cloudisense node                 |
| 2  | Browser Client ➝ Remote Cloudisense           | WebSocket → MQTT    | Forwarded RPC               | RPC sent via local node to a remote instance using federation               |
| 3  | Remote Cloudisense ➝ Browser Client           | MQTT → WebSocket    | RPC Response                | Response to forwarded RPC routed back to browser                            |
| 4  | Remote Cloudisense ➝ Local Cloudisense        | MQTT                | Incoming RPC Request        | Remote instance initiates a new RPC to local node                           |
| 5  | Local Cloudisense ➝ Remote Cloudisense        | MQTT                | RPC Response                | Local node responds to remote RPC                                           |
| 6  | Local Cloudisense ➝ Remote Cloudisense        | MQTT                | Internal Programmatic RPC   | Node internally triggers an RPC on a remote instance                        |
| 7  | Remote Cloudisense ➝ Local Cloudisense        | MQTT                | Response to Internal RPC    | Remote node replies to programmatic RPC                                     |
| 8  | One Cloudisense ➝ All Cloudisense             | MQTT (Broadcast)    | Broadcast RPC               | One node broadcasts to all others (e.g., heartbeat, config push)           |
| 9  | Browser Client ➝ Remote Cloudisense (Subscribe)| WebSocket → MQTT    | PubSub Subscribe RPC        | Browser asks to subscribe to remote pubsub channel                          |
| 10 | Remote Cloudisense ➝ Browser Client (Stream)  | MQTT → WebSocket    | PubSub Event Push           | Remote publishes events to browser via local node                           |
| 11 | Local Cloudisense ➝ Remote Cloudisense        | MQTT                | Internal PubSub Subscribe   | Internal service subscribes to a remote topic                               |
| 12 | Remote Cloudisense ➝ Local Cloudisense        | MQTT                | PubSub Publish              | Remote publishes events to topics local node is subscribed to               |


