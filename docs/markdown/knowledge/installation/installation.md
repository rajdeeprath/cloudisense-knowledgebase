# Workflow

## How to Use This

### What is the Function of the Installer

The installation process involves the following steps:

1. **Downloading the Cloudisense Archive**: The installer fetches the Cloudisense archive from the specified source.
2. **Extracting the Archive**: It extracts the archive onto the file system.
3. **Installing Dependencies**: Ensures that all required dependencies are installed.
4. **Installing Python**: Identifies and installs a suitable version of Python.
5. **Creating a Virtual Environment**: Sets up a virtual environment on the system.
6. **Installing Python Dependencies**: Installs all necessary Python dependencies within the virtual environment.
7. **Registering Cloudisense as a System Service**: Configures Cloudisense to run as a systemd service.

Even after the installation is complete, the installer offers additional functionality, including:

- Installing or uninstalling modules.
- Managing profiles.
- Uninstalling Cloudisense itself.

The installer provides a comprehensive suite of tools to manage your Cloudisense deployment efficiently.


#### Working with Modules
---

Modules add functionality to Cloudisense. Modules are packaged as ZIP files containing the module file (`.py`) and its configuration file (`.json`). The installer downloads the package, unzips it, and places the files in their appropriate locations. Cloudisense will then need to be restarted for the changes to take effect.


#### Working with Profiles
---

A profile is a composite package that includes reaction engine rules, shell scripts, a module, and its configuration. A profile is designed to bundle a complete solution together as a single unit. For example, if you wanted Cloudisense to work with a particular software or system, you would create a module, define reaction rules, write shell scripts, and bundle them as a profile. 

When you install a profile via the installer, it will place all the different types of files in their appropriate locations.


### Update (Future)

#### Update Process

**COMMAND**

```bash
./install.sh -u 1
```


From the installer's standpoint, the update process can broadly be broken down into the following steps:

- Detect the current installation and configurations.
- Fetch and parse the build manifest from the cloud.
- Determine whether the installation is updatable or not.
- Download the payload to disk.
- Use SmartMerge to merge old and new configuration files properly to prepare the latest payload for deployment.
- Check & create a Python virtual environment as needed.
- Install dependencies for the latest build.
- Update the systemd service if necessary.

### SmartMerge

`SmartMerge` is a Python program that is used to merge configuration files from the existing version of the software and the latest version of the software downloaded, without losing the edited configurations. The SmartMerge script reuses the Cloudisense virtual environment for its dependencies and hence does not require setting up a new Python virtual environment.

### AutoUpdater (Future)

AutoUpdate is a useful (experimental) feature of this installer that lets you update your existing Cloudisense installation automatically in an unattended manner.

To activate AutoUpdater:

1. Make sure the `install.sh` script has administrative rights and permissions to execute.
2. Create a CRON job in the Linux system to run the bash script as the administrator automatically once a day at a specific time.
