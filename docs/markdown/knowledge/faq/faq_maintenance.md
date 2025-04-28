## Updating and Maintenance

### ❓ How do I update CloudiSENSE?
**Answer:**

### ❓ How do I back up CloudiSENSE configuration?
**Answer:**  
To back up your CloudiSENSE configuration safely:

1. **Backup the Master Configuration File:**  
   - Copy `cdsmaster/configuration.json` to a secure location.
   
2. **Backup Module-Specific Configuration Files:**  
   - Copy the entire `cdsmaster/modules/conf/` directory, which contains all module-specific settings.

3. **Backup Logging Configuration (Optional):**  
   - Copy `cdsmaster/logging.json` if you have customized logging settings.

4. **Backup SSL Certificates (If Used):**  
   - If you have enabled SSL, also back up the SSL certificate and private key files.

---

**Recommended Backup Locations:**
- External storage devices
- Secure cloud storage
- Version control system (private Git repository)

---

**In simple terms:**  
> **Backup `configuration.json`, the `modules/conf/` folder, and any customized files to safely preserve your CloudiSENSE setup.**


### ❓ How are version updates managed?
**Answer:**  
Coming soon.

---

### ❓ How do I rollback to a previous version?
**Answer:**  
Coming soon.


### ❓ How do I update a module without downtime?
**Answer:**  
Currently, CloudiSENSE does not support hot-swapping modules at runtime.

To update a module safely:

1. Make your changes to the module’s Python code or configuration.
2. Stop the running CloudiSENSE server or container.
3. Replace or update the module files (`cdsmaster/modules/` and optionally `cdsmaster/modules/conf/`).
4. Restart the CloudiSENSE server.

---

**Important:**  
- Restarting CloudiSENSE is necessary to reload the updated module into memory.
- Make sure you back up your original files before making changes.

Hot-reload support is planned for future versions, but is experimental and not recommended for production use at this time.

