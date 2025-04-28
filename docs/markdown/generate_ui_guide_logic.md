
# `generate_ui_guide` Function Explanation

The `generate_ui_guide` function is an asynchronous method that generates a user interface (UI) guide for a specific module or set of modules. The method works by reading and modifying UI templates, adding action items from modules, and filtering pages based on module availability. Here's a breakdown of the function:

## Parameters:

- **`ui_guide_folder`**: The folder path where the UI guide is located.
- **`ui_guide_file`**: The name of the file containing the UI guide.
- **`modules`**: An instance of the `Modules` class, which holds information about available modules.
- **`handler`**: An optional handler parameter, which isn't used in the current method but could be for further customization or event handling.

## Steps:

### 1. **User Role Selection**:
The function starts by determining the user role (for now, it is hardcoded to use the "admin" role):
```python
user_roles: list = built_in_user_roles()
```

### 2. **Construct UI Guide Path**:
The path to the UI guide is built using the `ui_guide_folder`, `ADMIN_ROLE`, and `ui_guide_file`. The `ADMIN_ROLE` indicates that the guide is generated for the admin role specifically:
```python
ui_guide_path = os.path.join(ui_guide_folder, ADMIN_ROLE, ui_guide_file)
```

### 3. **Check If UI Guide Exists**:
It checks if the file exists and is a file:
```python
if os.path.exists(ui_guide_path) and os.path.isfile(ui_guide_path):
```

### 4. **Read UI Guide File**:
If the file exists, the function reads it and loads the content as a dictionary (`ui_guide`). The UI guide contains templates and pages that define the UI structure:
```python
with open(ui_guide_path, 'r+') as json_data_file:
    ui_guide: Dict = json.load(json_data_file)
```

### 5. **Extract Templates**:
The function extracts various templates from the UI guide, including page templates, subpage templates, and action item templates. These templates define the structure and behavior of different UI elements:
```python
templates: Dict = ui_guide["templates"]
subpage_template: Dict = templates["subpage"]
page_template: Dict = templates["page"]
category_template: Dict = templates["category"]
action_item_template = templates["action"]["item"]
```

### 6. **Get Pages and Actions**:
The function retrieves a list of pages from the UI guide and checks for a page related to UI actions (ActionCentre). It also gathers the action items for that page:
```python
ui_pages: list = ui_guide["pages"]
ui_action_page: Dict = self.get_page_by_component_name(ui_pages, UIModeler.UI_CLIENT_COMPONENTS.ActionCentre)
ui_actions: list = ui_action_page["metadata"]["action"]["items"] if ui_action_page is not None else list()
```

### 7. **Build Action Menu**:
For each module, it checks if the module has a `get_ui_actions()` method, which returns a list of actions. These actions are then inserted into the UI action menu:
```python
for module_name in modules.getModuleNames():
    module_instance: IModule = modules.getModule(module_name)
    if hasattr(module_instance, GET_UI_ACTIONS) and callable(getattr(module_instance, GET_UI_ACTIONS)):
        action_definition: List[ActionItem] = module_instance.get_ui_actions()
        if action_definition is not None:
            self.insert_action_menu_item(ui_actions, module_name, action_definition)
```

### 8. **Build Pages**:
The function goes through the pages in the UI guide, checking for specific modules and ensuring that pages related to a module are kept or removed based on the availability of the module. It also creates subpage items for modules that are statistics providers:
```python
for pagenav in list(ui_pages):
    if "formodule" in pagenav:
        required_mod: str = pagenav["formodule"]
        if not modules.hasModule(required_mod):
            ui_pages.remove(pagenav)
        else:
            if required_mod == SYSTEM_MODULE:
                # Additional processing for statistics provider modules
```

### 9. **Remove Action Centre If No Actions**:
If no action items exist, the Action Centre page is removed from the UI:
```python
if len(ui_actions) == 0:
    pagenav: Dict = self.get_page_by_component_name(ui_pages, UIModeler.UI_CLIENT_COMPONENTS.ActionCentre)
    if pagenav is not None:
        ui_pages.remove(pagenav)
```

## Conclusion:

This function is designed to dynamically generate and update a UI guide based on available modules and their associated actions. It ensures that the UI remains consistent with the available modules and updates the layout accordingly.
