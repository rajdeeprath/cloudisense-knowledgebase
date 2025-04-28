
# Cloudisense Multi-Instance Monitoring UI Design

## 🧠 Current State

- Single-instance monitoring dashboard.
- Shows:
  - CPU Load
  - Memory Usage
  - System Info
  - Logs
  - Rules
  - Statistics
- Data arrives via WebSocket (one Cloudisense instance connected).

---

## 🛠 Target: Multi-Instance Monitoring

We need to extend the UI to support **monitoring multiple CloudiSENSE instances at the same time**.

---

## ✅ Design Plan

### 1. Top-Level Instance Switcher

- Add **Dropdown** or **Tab bar** at the top.
- Allow user to select an instance to view.
- Default selection: "All Instances" Overview.

Example:
```
[ Select Instance ▼ ]
Instance-1 | Instance-2 | Instance-3 | ...
```

---

### 2. Per-Instance Dashboards

- After selecting an instance:
  - Display CPU, Memory, Logs etc. **only for that instance**.
- Use `identity` field in incoming WebSocket events to map data.

---

### 3. "All Instances" Overview Mode

- If "All Instances" selected:
  - Show aggregated dashboard.
  - Use cards/tables to summarize:

| Instance | CPU | Memory | Uptime | Errors |
|----------|-----|--------|--------|--------|
| node-1   | 5%  | 38%    | 2d     | 3      |
| node-2   | 15% | 70%    | 10d    | 1      |
| node-3   | 3%  | 20%    | 4d     | 0      |

---

### 4. Data Model Changes (Frontend)

Instead of flat variables, maintain:

```javascript
instances = {
    "instance_id_1": {
        cpu_usage: {...},
        memory_usage: {...},
        logs: [...],
        stats: {...}
    },
    "instance_id_2": {
        ...
    }
}
```

✅ Easy instance switching
✅ Data scoped cleanly

---

### 5. Backend Design (Server Side)

- Already done.
- WebSocket event includes `identity`.
- No changes needed server-side.

---

### 6. Disconnected/Offline Instance Handling

- If no data from an instance for timeout period:
  - Show as "Offline" in UI.
  - Gray out that instance card.

Example:
```
[Instance-2] - Offline
[Instance-3] - Online
```

---

## 📈 Full Flow Diagram

```
Instances --> (MQTT/WS Federation) --> Local Cloudisense --> (WebSocket) --> Browser UI
                                      (Adds 'identity' field)
```

---

## ✅ Action Checklist

- [ ] Add Instance Selector (Dropdown/Tab)
- [ ] Track instance-wise data in memory
- [ ] Build per-instance dashboard pages
- [ ] Build aggregated overview page
- [ ] Handle offline instances gracefully
- [ ] Monitor scaling/performance at 50+ instances

---

## 🎯 Final Notes

You are preparing CloudiSENSE UI for **real cluster management**!

- Cluster dashboard
- Real-time updates
- Multi-node management
- Production-grade scalability

🚀
