## Adding a module
---


## The `install_module` Function

### **1. Initialization**
The function starts by initializing several variables:
- `module_name`: Empty string initially, will hold the name of the module to be installed.
- `base_dir`: This is set to the default program path (`$DEFAULT_PROGRAM_PATH`).
- `force`: A flag initialized to `false`. It determines whether the installation should overwrite existing modules.
- `return_status`: This is set to `0` by default. It indicates the status of the operation.
- `error`: Set to `0`, this will hold any error status encountered during the installation.
- `err_message`: An empty string that will hold any error message if the installation fails.
- `silent_mode`: Initially set to `0`. It controls whether the function operates silently or not.

### **2. Check Current Installation**
The function checks if the program is already installed by calling `check_current_installation`. If the program is not installed (`$program_exists -eq 0`), it will stop further execution.

### **3. Argument Parsing and Validation**
The function parses and validates the arguments passed to it:

- If no arguments are passed (`$# -lt 0`), it will raise an error:
  ```bash
  error=1
  err_message="Minimum of 1 parameter is required!"
  ```

- If there are more than one argument, the arguments are assigned to corresponding variables:
  - `module_name` is the first argument.
  - `base_dir` is the second argument.
  - `force` (optional) is the third argument, and it can be set to `true` if `return_status` or `silent_mode` is `1`.
  - `return_status` (optional) is the fourth argument.
  - `silent_mode` (optional) is the fifth argument.

### **4. Check if Module Exists**
The function checks whether the module already exists:
- It constructs the path where the module should be deployed:
  ```bash
  deploy_path="$base_dir/cdsmaster/modules"
  ```
- It then checks if the module configuration file exists (`$module_conf`). If the module already exists, and the `force` flag is not set, it prompts the user for confirmation:
  ```bash
  read -r -p "Do you wish to continue? [y/N] " response
  ```
  If the user chooses not to overwrite, an error message is displayed, and the installation process stops:
  ```bash
  error=1
  err_message="Module installation cancelled!"
  ```

### **5. Module Installation Process**
If all checks pass and no errors are found, the function proceeds with the installation process:

1. **Temporary Directory Creation**: A temporary directory is created to store the downloaded module files:
   ```bash
   tmp_dir=$(mktemp -d -t ci-XXXXXXXXXX)
   ```

2. **Download and Unzip the Module**: The module is downloaded from the provided URL and unzipped into the temporary directory:
   ```bash
   wget -O "$module" "$url"
   unzip "$module" -d "$dest"
   ```

3. **Install Dependencies**: If a `requirements.txt` file is present in the unzipped module, the function installs any necessary dependencies:
   ```bash
   if [ -f "$module_requirements_file" ]; then
       install_module_dependencies "$module_requirements_file"
   fi
   ```

4. **Move Module Files**: The module files are moved from the temporary directory to their correct locations:
   - For Python `.py` and `.so` files, they are moved to the `deploy_path` directory:
     ```bash
     mv "$j" "$deploy_path/$module_name.py"
     mv "$j" "$deploy_path/$module_name.so"
     ```
   - If any `.py` and `.so` versions of the module exist, the function ensures only one version is kept, removing the other version.

### **6. Successful Installation**
If all steps are successful:
- The `module_install_success` flag is set to `1` to indicate success.
- If the `return_status` flag is set to `1`, the error status is set to `0`, and the function ends without any further output. If `silent_mode` is not `1`, a success message is displayed:
  ```bash
  lecho "Processing completed. You may want to restart $PROGRAM_NAME service"
  ```

### **7. Error Handling**
If any error occurs during the process, the function sets the `error` flag to `1` and displays an appropriate error message. If `return_status` is `1`, it will return the error status:
```bash
lecho_err "An error occurred. $err_message"
```

### **8. Program Not Installed**
If the main program is not installed, the function will output an error message and stop further execution:
```bash
lecho_err "Program core was not found. Please install the program before attempting to install modules."
```


## Removing a module
---


# The `remove_module` Function

The `remove_module` function is designed to remove the files associated with a specific module from the system. It does so by identifying the relevant files and deleting them. Here's a step-by-step breakdown of the function:

## 1. Function Definition

```bash
remove_module()
```

- This is the declaration of the function `remove_module`. It takes a single argument, which is the name of the module to be removed.

## 2. Local Variable Initialization

```bash
local module_name=$1
local deploy_path="$DEFAULT_PROGRAM_PATH/cdsmaster/modules"
local found=false
```

- `module_name=$1`: The first argument passed to the function is assigned to the variable `module_name`. This is the name of the module that will be removed.
- `deploy_path="$DEFAULT_PROGRAM_PATH/cdsmaster/modules"`: This variable holds the path where the modules are deployed. It's constructed using the default program path, which is stored in the `DEFAULT_PROGRAM_PATH` variable.
- `found=false`: A boolean flag used to track whether the module files are found during the removal process. It's initially set to `false`.

## 3. Finding Relevant Files

```bash
files_to_remove=$(find "$deploy_path" -type f \( -name "*$module_name.so" -o -name "*$module_name.json" -o -name "*$module_name.py" \))
```

- This command uses the `find` command to search for files in the `deploy_path` directory.
- It looks for files with names that match the module's name and have the extensions `.so`, `.json`, or `.py`. These are the typical file types for the module's runtime, configuration, and Python scripts.
- The results of this search are stored in the `files_to_remove` variable.

## 4. Looping Through the Files

```bash
while IFS= read -r file; do
    local name
    name=$(basename -- "$file")
```

- The `while` loop iterates over each file path stored in `files_to_remove`.
- `IFS= read -r file`: This reads each file path line by line into the `file` variable.
- `local name`: A new local variable `name` is defined to store the base name of the file (i.e., the file name without its path).
- `name=$(basename -- "$file")`: This extracts the base name of the file using the `basename` command.

## 5. Removing the Module Files

```bash
found=true
lecho "Removing module file $file"
rm -rf "$file"
```

- `found=true`: This sets the `found` flag to `true` to indicate that at least one matching file was found and will be removed.
- `lecho "Removing module file $file"`: A message is printed to indicate the file being removed.
- `rm -rf "$file"`: The `rm -rf` command is used to remove the identified file.

## 6. End of Loop

```bash
done <<< "$files_to_remove"
```

- The `done <<< "$files_to_remove"` part marks the end of the loop. The `<<<` operator feeds the list of files into the loop, allowing it to process each file.

## 7. Check if Files Were Found and Removed

```bash
if $found; then
    lecho "Processing completed. You may want to restart $PROGRAM_NAME service"
else
    lecho "Module not found. Nothing was removed"
fi
```

- The `if $found; then` statement checks if any files were found and removed.
  - If `found=true`, a message is printed indicating that the processing is complete and suggests restarting the program's service.
  - If no files were found, a message is printed indicating that no module was found and nothing was removed.

## Summary

- The `remove_module` function is used to remove files associated with a specific module.
- It searches for `.so`, `.json`, and `.py` files based on the module name.
- After identifying the files, it deletes them and provides feedback on the process.
