# Module: SystemMonitor

## Name
`system`

## Location
`modules/system.py`

## Description
The **SystemMonitor** module collects and monitors system statistics like CPU, memory, network, and disk. It primarily uses shell commands, with Python fallbacks for non-standard environments. It also allows centralized system reporting by aggregating additional internal or external stats.

---

## Configuration

```json
{
    "enabled": true,
    "klass": "SystemMonitor",
    "conf": {
        "stats_via_shell": true,
        "snapshot_interval_seconds": 10,
        "nic_stats_per_nic": true
    }
}
```

### Configuration Properties

| Property | Description | Type | Default |
|:---------|:------------|:-----|:--------|
| `enabled` | Enable or disable the module | Boolean | `true` |
| `klass` | Python class name for the module | String | `SystemMonitor` |
| `conf.stats_via_shell` | Use shell commands for stats collection | Boolean | `true` |
| `conf.snapshot_interval_seconds` | Interval between stats snapshots (seconds) | Number | `10` |
| `conf.nic_stats_per_nic` | Provide per-NIC stats if true, else aggregate | Boolean | `true` |

---

## Supported Intents

| Intent | Description | Parameters |
|:-------|:------------|:-----------|
| `check_process` | Check if a system process is active/inactive | `name` (String): Process name |

---

## Stats Gathering Methods

- **Python-Based**: Uses system libraries to collect stats.
- **Shell-Based**: Uses scripts from `[CLOUDISENSE_HOME]/scripts/`.

## Sample JSON Stats Output

```json
{
  "system": {
    "os": { "arch": "x86_64", "name": "Ubuntu", "type": "Linux", "version": "22.04" },
    "cpu": { "count": 16, "percent": 8 },
    "memory": { "total": 16049288, "used": 4624672, "percent": 28.81 },
    "disk": [...],
    "network": [...]
  }
}
```

---

## Collected Stats Overview

- **OS Info**: Architecture, Name, Type, Version, Boot Time, Uptime
- **CPU Info**: Core Count, Usage (%), Max Frequency
- **Memory Info**: Total, Used, Free, Usage %, Swap Stats
- **Disk Info**: Mount Point, Filesystem, Usage
- **Network Info**: Bytes/Packets Sent/Received, Errors, Drops

---

The **SystemMonitor** module is a built-in, essential module of **Cloudisense**.