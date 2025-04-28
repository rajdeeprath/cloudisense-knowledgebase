## Troubleshooting

### ❓ Why is my module not loading?
**Answer:**  
If your module is not loading in CloudiSENSE, it is usually due to one of the following reasons:

- There is an **error in your module’s Python code** (syntax error, missing methods, incorrect inheritance, etc.).
- There is a **problem in your module's JSON configuration file** (e.g., missing or invalid fields).
- The module **Python file is not placed in the correct location** (`cdsmaster/modules/`).
- The **configuration file** is missing or not placed under `cdsmaster/modules/conf/`.
- The `"enabled"` field in the configuration JSON is not set to `true`.

CloudiSENSE skips loading any module that has invalid Python code or invalid configuration to avoid system crashes.

Always check server logs for detailed error messages if a module fails to load.


### ❓ How do I reset the CloudiSENSE server?
**Answer:**  
To reset the CloudiSENSE server:

- Simply **restart the CloudiSENSE service** or **restart the server process** manually.
- If you are running it through the installer setup, you can restart using system service commands.
- If running manually (for example via Python directly), stop the running process and start it again.
- If running inside Docker, you can reset by stopping and restarting the container.

Resetting the server will reload all modules, configurations, and refresh WebSocket client connections.

---

**Important Notes:**
- There is no special internal "reset" command at the application level —  
  standard process or container restarts are used for resetting.
- **If any core files are corrupted, missing, or deleted, it is recommended to perform a clean reinstallation**  
  using the official installer:  
  [CloudiSENSE Installer](https://github.com/rajdeeprath/cloudisense-installer)


### ❓ How do I view CloudiSENSE logs?

**Answer:**  
CloudiSENSE logs are stored under the default directory:

```
{CLOUDISENSE_HOME}/log/
```

Inside the `log` directory, you will find:

- **cloudisense.log** — Contains general logs (INFO, DEBUG, WARN).
- **error.log** — Contains only ERROR-level logs.

To view the logs, you can use standard Linux commands:

- To view logs live:
  ```bash
  tail -f {CLOUDISENSE_HOME}/log/cloudisense.log
  ```

- To view error logs:
  ```bash
  tail -f {CLOUDISENSE_HOME}/log/error.log
  ```

---

**Important:**
- The logging behavior, format, and storage location can be customized via `cdsmaster/logging.json`.
- Log rotation is automatically managed to prevent excessive file sizes.

---

**In simple terms:**  
> **Go to the `log/` folder inside your CloudiSENSE installation and open or tail the log files to view runtime and error logs.**

