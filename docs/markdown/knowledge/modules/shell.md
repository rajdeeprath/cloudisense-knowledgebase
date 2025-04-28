# Module: ScriptRunner

## Name
`shell`

## Location
`modules/shell.py`

## Description
The **shell** module handles execution of shell scripts within the platform, managing `start`, `progress`, and `stop` states. It broadcasts script events and their data into the Cloudisense pub/sub system.

> **Note**: Long-running scripts are discouraged due to system architecture constraints.

---

## Configuration

```json
{
    "enabled": true,
    "klass": "ScriptRunner",
    "conf": {
        "max_messages_chunks": 20,
        "script_folder": "scripts",
        "file_types": [".sh"],
        "max_execution_time_seconds": 60
    }
}
```

### Configuration Properties

| **Property** | **Description** | **Type** | **Default Value** |
|--------------|-----------------|----------|-------------------|
| `enabled` | Enables/disables the module | Boolean | `true` |
| `klass` | Python class name | String | `ScriptRunner` |
| `conf.max_messages_chunks` | Max allowed message chunks | Number | `20` |
| `conf.script_folder` | Directory for scripts | String | `"scripts"` |
| `conf.file_types` | Allowed file extensions | List[String] | `[ ".sh" ]` |
| `conf.max_execution_time_seconds` | Max script execution time | Number | `60` |

---

## Supported Intents

| **Intent** | **Description** | **Parameters** |
|------------|-----------------|----------------|
| `start_script_execution` | Starts a script execution | - `name` (String): Script filename |
| `stop_script_execution` | Stops a running script | - `script_id` (String): Running script's ID |

---

## Notes
The **shell** module is an optional module in Cloudisense. It can be installed, uninstalled, enabled, or disabled as needed.