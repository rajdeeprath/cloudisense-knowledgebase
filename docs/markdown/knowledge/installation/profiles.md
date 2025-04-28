## Adding a profile
---


# The `install_profile()` Function

The `install_profile()` function is a shell script designed to manage the installation of software profiles. It handles downloading, unpacking, and configuring various components of a "profile," such as modules, rules, and scripts, while ensuring existing configurations are respected or overwritten as necessary.

---

## **1. Initial Setup**
- **Declare Local Variables:**  
  Variables such as `profile_name`, `base_dir`, `force`, `return_status`, and `error` are initialized to handle input arguments and state tracking.
- **Check Current Installation:**  
  The function calls `check_current_installation` to verify if the core program is installed (`program_exists` is used for this check).

---

## **2. Input Validation**
- **Minimum Parameter Check:**  
  If fewer than one parameter is passed, an error message is set, and the function exits.
- **Argument Assignment:**  
  Depending on the number of arguments:
  - `profile_name`: Always assigned from the first argument.
  - `base_dir`: Optionally assigned from the second argument (defaulting to `$DEFAULT_PROGRAM_PATH`).
  - `force`: Optionally assigned from the third argument.

---

## **3. Get Profile URL**
- **Fetch Profile URL:**  
  The `get_profile_url` function retrieves the URL for the specified `profile_name`. If no URL is found, the function sets an error.

---

## **4. Download and Unpack Profile**
- **Temporary Directory:**  
  Creates a temporary directory (`mktemp`) to store the profile archive and unpacked files.
- **Download Profile:**  
  Uses `wget` to download the profile archive (`profile_name.zip`) from the fetched URL.
- **Extract Archive:**  
  Unzips the downloaded archive into a designated temporary path.

---

## **5. Read and Parse Metadata**
- **Metadata File:**  
  Reads the `meta.json` file from the extracted profile package directory.
- **Parse Metadata:**  
  Uses `jq` to extract profile details, including:
  - Modules to add/remove
  - Rules to add/remove
  - Scripts to add/remove

---

## **6. Install Components**
### **Modules**
- **Add Modules:**  
  - Calls `install_module` for each module listed in the metadata.
  - Handles copying custom configuration files from the profile package to the appropriate installation path.
  - Updates configuration files to enable the modules using `jq`.
- **Remove Modules:**  
  - Deletes module files (e.g., `.so`, `.py`) and associated configuration files as listed in the metadata.

### **Rules**
- **Add Rules:**  
  - Copies rule files from the profile package to the installation directory.
  - Prompts the user if the rule already exists and overwriting is required.
- **Remove Rules:**  
  - Deletes unwanted rule files listed in the metadata.

### **Scripts**
- **Add Scripts:**  
  - Moves script files from the profile package to the installation directory.
  - Prompts the user if the script already exists and overwriting is required.
  - Sets appropriate ownership and execution permissions.
- **Remove Scripts:**  
  - Deletes unwanted script files listed in the metadata.

---

## **7. Finalize Installation**
- **Update Installation Metadata:**  
  Records the installed profile name in the program’s installation report file.
- **Restart Service:**  
  Calls `restart_service` to apply the changes.

---

## **8. Error Handling**
- **Module Installation Failure:**  
  If a module fails to install, the function removes all profile-related modules and exits with an error.
- **General Errors:**  
  Reports errors encountered during any phase of the operation using `lecho_err`.

---

## **9. Missing Core Program**
- If the core program is not found (`program_exists` is `0`), the function exits with a message prompting installation of the program.

---

## **Function Flow Summary**
1. Validate input arguments and check the program installation.
2. Fetch the profile URL and download the archive.
3. Extract files and parse metadata.
4. Install or remove modules, rules, and scripts as specified.
5. Update the active profile metadata and restart the service.
6. Handle errors gracefully and roll back changes if necessary.

---

This function ensures that profiles are installed in a consistent, configurable, and error-tolerant manner.



## Removing a profile
---


# The `clear_profile()` Function

The `clear_profile()` function is designed to clear the currently installed profile for a program by removing its associated modules, rules, and scripts. Below is a detailed explanation of each step:

---

## 1. **Define Variables**
- **`base_dir`**: Default program installation path (`$DEFAULT_PROGRAM_PATH`).
- **`return_status`**: Tracks the success or failure of the function (default: `0`).
- **`silent_mode`**: Indicates whether errors are shown (default: `0`).
- **`error`**: Flag to track if an error occurs (default: `0`).
- **`err_message`**: Holds any error messages.

---

## 2. **Check Current Installation**
- The `check_current_installation` function ensures that the program is installed.
- If the program exists:
  - Check if an alternative path is provided as an argument.
  - If provided, ensure the path exists. If not, set an error flag and message.

---

## 3. **Read Installation Metadata**
- Calls `read_installation_meta` to load the metadata for the current installation.
- Retrieves the current profile name (`$CURRENT_INSTALLATION_PROFILE`).

---

## 4. **Validate Profile**
- If no profile is set (`$CURRENT_INSTALLATION_PROFILE` is empty):
  - Set an error flag with a message.
- Otherwise:
  - Fetch the profile URL using `get_profile_url`.
  - If no URL is returned, set an error flag with a message.

---

## 5. **Perform Operations if No Errors**
If there are no errors:
- **Create Temporary Directory**:
  - Use `mktemp` to create a temporary directory for downloading and extracting profile files.

- **Download and Extract Profile**:
  - Download the profile archive (`.zip`) from the URL using `wget`.
  - Extract the contents to the temporary directory using `unzip`.

- **Read `meta.json`**:
  - Parse the profile metadata to retrieve:
    - Profile name.
    - Modules, rules, and scripts to be added or removed.

---

## 6. **Remove Profile Components**
### **Remove Modules**
- Iterate over modules listed in `add_modules`.
- For each module:
  - Remove the module files (`.so` or `.py`) from the installation path.
  - Remove the module's configuration file (`.json`) if it exists.

### **Remove Rules**
- Iterate over rules listed in `add_rules`.
- For each rule:
  - Remove the corresponding rule file (`.json`) from the installation path.
  - If the file does not exist, log a message.

### **Remove Scripts**
- Iterate over scripts listed in `add_scripts`.
- For each script:
  - Remove the script file (`.sh`) from the installation path.
  - If the file does not exist, log a message.

---

## 7. **Update Installation Metadata**
- Mark the current profile as cleared by updating the installation metadata via `update_installation_meta`.
- If the metadata file (`$PROGRAM_INSTALLATION_REPORT_FILE`) does not exist, log an error message.

---

## 8. **Restart the Service**
- Restart the service to apply changes using the `restart_service` function.

---

## 9. **Handle Errors**
- If an error occurs at any step:
  - Log the error message (`$err_message`) or return the error status depending on the mode.
  - If the program core is not found, prompt the user to install the program first.

---

## 10. **Exit Function**
- Exit the function, returning the appropriate status based on success or failure.

---

# How the Function Works:
1. Checks if the program is installed and fetches the current profile.
2. Downloads and extracts the profile archive to a temporary location.
3. Reads the profile metadata to determine which components to remove.
4. Deletes the specified modules, rules, and scripts from the installation path.
5. Updates metadata to reflect the cleared profile and restarts the service.

---


