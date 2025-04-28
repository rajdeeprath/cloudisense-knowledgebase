# Identity-Based Namespace Scoping in Cloudisense PubSub System

## Purpose

In Cloudisense's federated multi-instance design, **Identity** is used as the core principle to **namespace and scope** all event topics.  
This ensures safe, scalable, and isolated event management across hundreds or thousands of instances.

---

## Why Use Identity for Namespace Scoping?

| Goal | How Identity Helps |
|-----|--------------------|
| Avoid topic collisions | Each Cloudisense instance has a separate namespace |
| Enable multi-tenant behavior | Events are cleanly segregated per node |
| Simplify subscription management | Clients can subscribe to a specific instance's events easily |
| Improve security and access control | Future ability to restrict subscriptions per identity |
| Support federated architecture | Central Cloudisense node can route/aggregate correctly |

---

## Event Topic Structure

Each event in the PubSub system follows this format:

```text
{identity}/{topic_type}
```

### Example Topics

| Identity | Topic |
|----------|-------|
| `cloud-node-1` | `cloud-node-1/logs`, `cloud-node-1/metrics`, `cloud-node-1/events` |
| `cloud-node-7` | `cloud-node-7/stats`, `cloud-node-7/alerts/errors` |

---

## Behavior

- When a Cloudisense instance generates an event:
  - It includes its **Identity** inside the event payload.
  - It publishes to a topic scoped under its **Identity**.
- The Central Cloudisense node:
  - Receives all events.
  - Pushes them into the PubSub system **under the correct identity-prefixed topic**.
- WebSocket Clients:
  - Subscribe to topics under specific identities.

---

## Example Flow

1. Instance `cloud-node-501` generates a metrics update.
2. Event is published to MQTT topic: `cloud-node-501/...../metrics`.
3. Central Cloudisense receives the MQTT pub and queues the event into local PubSub system.
4. local clients subscribed to `/cloud-node-501/...../metrics` receive the update.

---

## Subscription Examples

| Subscription Pattern | What It Receives |
|----------------------|------------------|
| `/cloud-node-1/logs` | Only logs from node 1 |

---

## Best Practices

- Always **prefix topics** with Identity when publishing events.
- Always **include Identity** inside the event payload (for audit/validation).
- **Normalize all inbound events** at the central node before pushing to PubSub.
- Design client-side subscriptions based on Identity+Topic combination.

---

## Benefits

✅ Scalable to thousands of instances  
✅ Simplified topic matching  
✅ Supports fine-grained security  
✅ Enables powerful subscription patterns  
✅ Prevents accidental topic collisions

---
