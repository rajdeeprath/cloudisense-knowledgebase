## Extending and Developing

### ❓ How do I build a custom module?
**Answer:**  
To build a custom module in CloudiSENSE, you typically follow these steps:

1. **Create a Python Class:**  
   - Inherit from the `IModule` base class provided by CloudiSENSE.
   - Implement required methods like `getname()` and `initialize()`.

2. **Define Actions:**  
   - Create Action classes by inheriting from the `Action` base class.
   - Define `name()` and `run()` methods to handle specific operations.

3. **Create Intents:**  
   - Optionally create an Intent Provider that maps intents to your module's actions.

4. **Create Configuration Files:**  
   - Add a module configuration file under `cdsmaster/modules/conf/` to control module loading.
   - Set `"enabled": true` to activate your module.

5. **Register HTTP APIs (Optional):**  
   - If needed, define Tornado HTTP Handlers inside your module for REST API endpoints.

6. **Deploy:**  
   - Place your module Python file inside `cdsmaster/modules/`.
   - Restart CloudiSENSE to load the new module.

---

**Important Notes:**
- Follow the existing module structures for best practices.
- Use the Reaction Engine if you want your module to react to events.
- You can expose your functionality via Actions, HTTP APIs, or both.

---

For a detailed step-by-step guide, refer to:  
[Creating a New CloudiSENSE Module](https://cloudisense.com/creating-new-module/)

You can also contact the developer for further assistance if needed.


