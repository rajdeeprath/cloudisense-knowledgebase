## Modules

### ❓ What is a module in CloudiSENSE?
**Answer:**  
In CloudiSENSE, a **module** is a **self-contained functional unit** that provides specific capabilities or integrations to the system.  
Modules extend the platform by exposing:

- **Actions** (automation tasks users can trigger),
- **Optional Intents** (for AI/conversational interaction),
- **HTTP APIs** (for server-side communication),
- **Background services** (if needed for monitoring, event processing, etc.).

Each module operates independently but integrates seamlessly with the core CloudiSENSE framework.

Modules can target a wide range of systems, including:

- Cloud services (e.g., AWS, Azure)
- Infrastructure platforms (e.g., Ansible, Docker)
- IoT devices and networks
- Internal software products and APIs
- Edge computing environments

CloudiSENSE modules are highly flexible:  
Developers can easily create new modules to integrate with **any platform or system**, simply by implementing the required action classes and handler interfaces.

This modularity ensures that CloudiSENSE remains **extensible**, **scalable**, and **adaptable** to evolving infrastructure and business needs.


### ❓ How do I create a new module for CloudiSENSE?
**Answer:**  
Creating a new module in CloudiSENSE involves implementing a set of predefined structures that allow your module to expose actions, APIs, background services, or even new UI elements dynamically.

Here are the basic steps:

1. **Create a new Python class that implements the `IModule` interface:**  
   Define the basic module behavior, including initialization, configuration loading, and action registration.

2. **Define Actions:**  
   Implement one or more classes that inherit from the `Action` base class.  
   Each action must define a unique `name()`, describe input parameters, and implement the `run()` logic that executes the action.

3. **(Optional) Define Intents:**  
   If the module should support natural language queries (future AI features), implement intent providers by extending the `IntentProvider` class.

4. **(Optional) Create HTTP Handlers:**  
   If the module needs to expose APIs to clients, define Tornado `RequestHandler` classes, and register them in the `urls()` method.

5. **Use Constants for Action and Intent Names:**  
   Best practice is to define all action and intent names as constants in the module file for maintainability.

6. **Handle Configuration Options:**  
   Read module-specific settings from the main `configuration.json` to allow dynamic behaviors without code changes.

7. **Follow Naming Conventions:**  
   Use clear, consistent naming for module classes, action classes, and handler classes.

8. **Add the Module to Configuration:**  
   Register the module’s name inside the CloudiSENSE `configuration.json` under the `modules` section to enable loading.

9. **Place the Module in the Correct Directory:**  
   Physically place your module inside the `modules/` folder or a custom folder specified in server configs.

10. **Restart the CloudiSENSE Server:**  
    Restarting the server triggers detection and loading of the newly added module.

11. **(Recommended) Test the Module Independently:**  
    Before deployment, run local tests on actions, APIs, and intents to ensure the module behaves as expected.

For a full detailed tutorial and sample code, you can refer to the CloudiSENSE official guide:  
👉 [How to Create a New Module in CloudiSENSE](https://cloudisense.com/creating-new-module/)

CloudiSENSE modules are highly extensible — they allow you to integrate cloud services, internal APIs, IoT devices, automation workflows, or even create full management systems by simply developing custom modules.

### ❓ Can modules be updated without restarting the server?
**Answer:**  
No, modules cannot be updated dynamically without restarting CloudiSENSE at the current stage.

While you can **add** new modules or **remove** existing modules by placing or deleting them in the appropriate directory,  
any changes made to a module's code — such as:

- Editing action logic,
- Adding new actions or intents,
- Modifying HTTP handlers,
- Changing internal module behavior,

**require a server restart** for CloudiSENSE to detect and load the updated module properly.

The restart ensures that the module’s classes, actions, and API handlers are re-registered cleanly without runtime inconsistencies.

In future versions, dynamic hot-reloading capabilities may be considered, but currently a controlled restart is required after any module update.


### ❓ How are modules loaded at startup?
**Answer:**  
Modules in CloudiSENSE are loaded during server startup through a **bootstrap mechanism**.

Here is the process:

1. **Read Active Module Configurations:**  
   At startup, CloudiSENSE first looks for active module configuration files (`.json`) in a designated modules configuration directory.

2. **Locate Module Python Files:**  
   Based on the configuration, it identifies the physical locations of the corresponding Python files that implement the modules.

3. **Load Module Classes into Memory:**  
   Once the Python files are found, CloudiSENSE dynamically imports the module classes into memory.

4. **Initialize Modules:**  
   After loading, CloudiSENSE invokes the necessary initialization functions (`initialize()`, action registration, URL registration, etc.) to prepare each module for operation.

5. **Error Handling:**  
   If a module's configuration is invalid, or if there is an error in loading its Python code,  
   CloudiSENSE **logs the error** and **skips loading that specific module**.  
   The rest of the system continues to boot normally without interruption.

6. **Make Modules Available to the System:**  
   Successfully loaded modules become active and are available for use by the server, client UIs, and automation workflows.

This bootstrap design ensures that only properly configured and functional modules are loaded into the system, maintaining stability, modularity, and resilience against partial failures.


### ❓ What modules are available by default?
**Answer:**  
By default, CloudiSENSE provides a core set of essential system modules that handle infrastructure management, internal operations, messaging, and basic automation capabilities.

The default modules include:

- **federation.py:**  
  Lays the foundation for inter-instance federation and communication over MQTT (planned extension).

- **filesystem.py:**  
  Provides actions to interact with the file system — reading, writing, managing files and directories.

- **genericadapter.py:**  
  Acts as a bridge or adapter for integrating external systems into CloudiSENSE using standard APIs.

- **genericnotifier.py:**  
  Provides mechanisms for sending notifications (internal system notifications, alerts).

- **logmonitor.py:**  
  Enables log file monitoring and analysis, allowing real-time alerting based on log patterns.

- **pinger.py:**  
  Provides actions to check network availability and system reachability (ping utilities).

- **reaction.py:**  
  Core of the CloudiSENSE **Reaction Engine** — allows event-driven automation based on system states, triggers, and conditions.

- **rpcgateway.py:**  
  Enables Remote Procedure Call (RPC) routing between different clients and services.

- **sample.py:**  
  A minimal sample module provided as a development reference for building new modules.

- **security.py:**  
  Handles authentication, session management, access control, and other security functions.

- **shell.py:**  
  Provides actions to execute shell commands safely through the system, under controlled conditions.

- **system.py:**  
  Offers system-level actions like server status reporting, uptime monitoring, configuration introspection.

- **systemcore.py:**  
  Core internal operations of the CloudiSENSE platform — foundational system behaviors and initializations.

---

CloudiSENSE is built to be modular and extensible — new modules can easily be added without modifying the core, enabling flexible growth over time.


### ❓ How can I disable a module temporarily?
**Answer:**  
In CloudiSENSE, each module has its own configuration file located under the `cdsmaster/modules/conf/` directory.

To temporarily disable a module:

1. **Locate the Module's Configuration File:**  
   Go to the `cdsmaster/modules/conf/` folder and find the JSON file corresponding to the module you want to disable.

2. **Edit the Configuration File:**  
   Open the module's JSON file.  
   You will see a structure like this:

   ```json
   {
     "enabled": true,
     "klass": "SampleModule",
     "conf": {
       // module-specific configuration goes here
     }
   }
   ```

3. **Set `enabled` to `false`:**  
   Modify the `enabled` field:

   ```json
   {
     "enabled": false,
     "klass": "SampleModule",
     "conf": {
       // module-specific configuration goes here
     }
   }
   ```

4. **Save the Configuration File:**  
   Save the file after editing.

5. **Restart the CloudiSENSE Server:**  
   Restarting the server is necessary for the change to take effect.  
   Upon restart, any module with `enabled: false` will be skipped during the loading phase.

---

**Important Notes:**
- You do **not** need to delete or move the module's code files.
- Disabling happens cleanly at the configuration level without modifying module code.
- **Default system modules** (such as `system.py`, `systemcore.py`, `reaction.py`, `security.py`, etc.) **must not be disabled**.  
  Disabling critical core modules can cause the system to malfunction or fail to start properly.

Only disable **optional** or **custom** modules if needed temporarily.