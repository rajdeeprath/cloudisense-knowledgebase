
# Module: LogMonitor

## Name
`logmonitor`

## Location
`modules/logmonitor.py`

## Description

The **LogMonitor** module simplifies and enhances log management within the **Cloudisense** ecosystem. It supports real-time log monitoring, recording, and broadcasting through the core pub-sub communication channel, making logs accessible to clients and modules.

## Features

### Live Tail
- Real-time monitoring of log files using system `tail` functionality.
- Support for multiple logs simultaneously.
- Log data is pushed into the Cloudisense pub-sub system.

### Log Recording
- Record live-tailed data into files.
- Schedule recording tasks with the Reaction Engine or manually control via the Client API.
- Create snapshots for later analysis.

### Bonus Features
- Subscription-ready: clients can subscribe to live log streams.
- Socket integration: forward logs to remote socket servers.
- System-wide access: logs are available across modules.

---

## Configuration

```json
{
    "enabled": true,
    "klass": "LogMonitor",
    "conf": {
        "retry_time_ge_seconds": 5,
        "max_messages_chunks": 20,
        "chunks_collector_interval": 10000,
        "static_targets": [
            {
                "enabled": false,
                "name": "filename.log",
                "log_file_path": "<path-to-log>"
            }
        ]
    }
}
```

## Configuration Properties

| Property                               | Description                                                           | Type     | Default     |
|----------------------------------------|-----------------------------------------------------------------------|----------|-------------|
| `enabled`                              | Enable or disable the module.                                          | Boolean  | `true`      |
| `klass`                                | Python class name for the module.                                      | String   | `LogMonitor`|
| `conf.retry_time_ge_seconds`           | Time to wait before retrying after a failure.                         | Number   | `5`         |
| `conf.max_messages_chunks`             | Maximum in-memory log chunks before writing to disk.                  | Number   | `20`        |
| `conf.chunks_collector_interval`       | Interval (ms) for collecting and writing log chunks to file.           | Number   | `10000`     |
| `conf.static_targets`                  | Predefined static log file targets.                                   | List     | -           |
| `conf.static_targets.enabled`          | Enable or disable a specific static target.                           | Boolean  | `false`     |
| `conf.static_targets.name`             | Unique name for the static log file target.                           | String   | -           |
| `conf.static_targets.log_file_path`    | Full absolute path of the static log file.                             | String   | -           |

---

## Supported Intents

| Intent               | Description                               | Parameters |
|----------------------|-------------------------------------------|------------|
| `list_logs`          | Retrieves a list of available log files.  | None       |

---

The **LogMonitor** module is a core module in **Cloudisense** and cannot be disabled or removed. It ensures robust and scalable log management for distributed and real-time environments.
