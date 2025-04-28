# Client-Side Planning for Multi-Instance Cloudisense Event Management

## Purpose

To design a highly scalable React-based frontend that can:
- Receive thousands of real-time events from Cloudisense.
- Separate and manage events **per instance** (using identity).
- Smoothly handle high event rates without UI freezes.
- Allow switching between monitoring and communicating with different Cloudisense instances.

---

## Core Design Principle

> React Client must buffer, batch, and selectively render incoming data.

No direct rendering on each WebSocket message.

---

## Architecture Overview

```text
WebSocket
    ⇩
Buffer in Memory (Per-Instance Event Queues)
    ⇩ (every 200ms)
Update React State
    ⇩
Render Selected Instance's Live View
    ⇩
Switch Focus as Needed
```

---

## Event Buffering Strategy

- Incoming WebSocket events are buffered into memory.
- Data is organized **per instance**:

```javascript
{
  instances: {
    "cloud-node-7": {
      metrics: [...],
      logs: [...],
      events: [...]
    },
    "cloud-node-501": {
      metrics: [...],
      logs: [...],
      events: [...]
    }
  }
}
```

✅ Prevents frequent React re-renders.  
✅ Allows fast lookup and filtering.

---

## React Update Strategy

- Use **setInterval** to update the rendered data every **200–500ms**.
- Update only visible parts (current instance being viewed).

Example:

```javascript
setInterval(() => {
  updateRenderedData(bufferedData);
}, 200);
```

✅ Smooth rendering.  
✅ Handles thousands of events/sec easily.

---

## Instance Focus Switching

| Mode | Behavior |
|------|----------|
| Monitor Mode | Select an instance → View only that instance's events |
| Communicate Mode | Select an instance → Send RPCs/intents to that instance |
| All Instances (optional) | Grid view with summary data across nodes |

Switching changes the active `selectedInstanceId`.

---

## Event Retention Policy

- Limit history per instance:
  - Example: Keep only last **500 logs**, **1000 metrics**.
- Slice buffer arrays to prevent memory overflow:

```javascript
const logs = logs.slice(-500);
```

✅ Memory safe.  
✅ Good performance even during high traffic.

---

## Performance Capabilities

| Feature | Expected Performance |
|---------|-----------------------|
| Event handling | 500–1000+ events/sec |
| UI updates | Every 200–500ms |
| Log rendering | 10k+ entries using virtualization (`react-window`) |
| Graph plotting | Buffered throttled updates |

✅ React can handle real-time Cloudisense data at scale.

---

## Recommended Tools and Patterns

| Tool/Pattern | Purpose |
|--------------|---------|
| Zustand or Redux | Global event store management |
| react-window | Virtualized rendering of long lists |
| lodash.throttle or debounce | Control update rate |
| WebSocket JSON batch parsing | Efficient event handling |

---

## Subscription Management

- Each client subscribes to event topics with identity scoping:

```text
cloud-node-7/logs
cloud-node-501/metrics
cloud-node-9/events
```

- Supports monitoring **one** or **many** instances flexibly.

---

## Best Practices

- Always **buffer** before updating UI.
- Limit number of events kept in memory per instance.
- Virtualize heavy UI components (logs, metrics).
- Allow fast switching of active monitoring instance.
- Monitor memory and CPU on frontend side during heavy loads.

---

## Conclusion

✅ React can efficiently manage real-time monitoring and interaction with thousands of Cloudisense instances.  
✅ Using **identity-scoped buffering**, **batch updates**, and **smart rendering** ensures a scalable, production-grade system.

---
