# CloudiSENSE Messaging System: Progress Overview

This document outlines the current implementation status of the messaging and communication mechanisms in CloudiSENSE. It highlights which features have been completed, and which remain in progress or not yet started.

---

## ✅ Completed

| Area       | Feature             | Notes                                |
|------------|---------------------|--------------------------------------|
| **RPC**    | Local → Local        | Via WebSocket                        |
|            | Local → Remote       | Forwarded over MQTT                  |
|            | Remote → Local       | Via Federation (MQTT)                |
|            | Remote ↔ Local       | Full RPC cycle supported             |
| **Broadcast** | Local → All Nodes   | serviceId = "*" via MQTT             |
| **PubSub** | Local → Browser      | Event push via WebSocket             |
|            | Remote → Local       | Remote publishes events via MQTT     |

---

## ⏳ Pending / Remaining

| Area           | Feature                                | Status      | Notes                                                                 |
|----------------|----------------------------------------|-------------|-----------------------------------------------------------------------|
| **Event Relay**| Remote → Browser                       | 🟡 Partial  | Event published by remote node must be relayed by local node and pushed to subscribed browser |
| **Subscriptions** | Browser → Remote Subscribe           | 🔄 Designing | Remote subscription request via RPC, local node relays it            |
| **Cleanup**    | Federation Disconnect Cleanup           | 🔄 Designing | Unsubscribe remote clients when they go offline                      |
| **Security**   | Secure Messaging                        | ❌ Not Started | TLS + signed payloads                                                 |
| **AI Ops**     | LLM Integration                         | ❌ Not Started | Let LLM choose nodes and actions                                      |
| **UI**         | Real-time Cluster Dashboard             | ❌ Not Started | Live view of nodes, RPC activity, PubSub stats                        |
| **RPC Relay**  | Browser → Remote & Remote → Browser     | 🔄 Designing | Forward RPC request to remote node and relay response to the browser |

---

## Next Recommended Step

Design and implement:

- **Remote → Browser Event Relay**
  - When a remote CloudiSENSE instance publishes to a topic:
    - Local instance (which browser is connected to) must receive that event
    - Forward it to all subscribed WebSocket clients

This will enable full **remote streaming support** to browser-based dashboards.
