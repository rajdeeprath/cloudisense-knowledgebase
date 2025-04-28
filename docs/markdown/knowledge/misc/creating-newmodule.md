# Creating a Custom Module

## Overview

To create a new module in **Cloudisense**, you need to use the provided sample module template (`sample.py`) located in the `modules` folder. Follow these steps to create and register a new module with Cloudisense.

---

## Basic

### Steps to Create and Register a Module

#### Create a New Module File

1. Navigate to the `cdsmaster/modules/` folder.

2. Make a copy of the **sample module file** (`sample.py`) and give it a new name that reflects your module's purpose. For example:

#### Create a Configuration File

1. Navigate to the `cdsmaster/modules/conf/` folder.

2. Make a copy of the **sample configuration file** (`sample.json`) and name it to match your new module. For example: `cdsmaster/modules/conf/newmodule.json`


#### Edit the Module File

1. Open the newly created `newmodule.py` file in your code editor.

2. Set the value of the `NAME` variable to a unique identifier for your module. This name will be used internally to register the module. Use a single word or words separated by underscores. Example:

```py

NAME = "newmodule"

```

3. Locate the initialize method in your module file. Add a debug statement to help verify the module initialization, like so:


```py

self.logger.debug("newmodule init")

```

#### Restart Cloudisense

1. Save all your changes.

2. Restart the Cloudisense service.


#### Verify Module Registration


1. Check the log file at `cdsmaster/log/cloudisense.log`.

2. Look for the following line to confirm that your module has been registered and initialized successfully:

```sh
newmodule init
```

## Advance

# Extending Your Module in Cloudisense

Now that we have a simple module registered, let's explore additional features to leverage the **Cloudisense architecture** effectively.

In this section, we will cover the following topics:

1. **Creating an API Endpoint** in your module.
2. **Registering a Custom `Intent`** and an accompanying `Action` in your module.
3. **Dispatching a Data Event** from your module.

----

### Creating an API Endpoint in Your Module

The Cloudisense software architecture already provisions for HTTP/HTTPS API endpoints. Each module simply needs to implement its API endpoint path, the parameters it will accept, the HTTP method it will be tied to (GET, POST, PUT, DELETE), and the logic it will execute. Finally, we expose the API path to the Cloudisense core, which will register your API for accepting HTTP traffic. Let us look at the steps:


* **Create a web request handler class in your module** as shown below:

```python
class DoorBellHandler(BaseRequestHandler):
    
    def initialize(self): 
        pass
        
    async def post(self):        
        event = DataEvent("/smarthome/doorbell", {"message": "hello world"})        
        await self.application.handle_event(event)
        self.finish()
```


The above web request handler class, `DoorBellHandler`, extends `BaseRequestHandler` and implements the `POST` handler -> `async def post(self):`. This means it will handle POST requests only. When the method is called, it will create a `DataEvent` and ask the Cloudisense application core to handle it.



* Expose the handler to Cloudisense's web request handling mechanism along with an API path to map the request. To do so, we use the `get_url_patterns` method. This method is called by the Cloudisense core when it loads the module. The method must return a `list` of `url` tuples containing the API `path` and the handler `class` to map to, as shown below:


```py
def get_url_patterns(self)->List:
        return [ url(r"/smarthome/doorbell", DoorBellHandler)]
```

So now, if someone invokes the URL endpoint `{HOST}:{PORT}/modules/smarthome/doorbell` using HTTP `POST`, it will directly run the logic placed in the `post` method.

---

### Registering a Custom `Intent` and an Accompanying `Action` in Your Module

In Cloudisense, modules react to requests within the system through the **Intent-Action** mechanism. The **Intent** defines "what you want," while the **Action** defines "what has to be done." In a module, you always declare an `Intent` and an `Action` in matching pairs. This means **1 Action for 1 Intent**. 

Let us see an example:

* In the `newmodule` define two constants. One will be for the intent name and the other for the action name. Both constant values are the same, just the `prefixes` are different.

```py
# custom intents
INTENT_SMARTHOME_NOTIFY = "intent_smarthome_notify"

# custom actions
ACTION_SMARTHOME_NOTIFY = "action_smarthome_notify"
```

* Next, we define a custom action as a class in the module body that extends `Action`, as shown below.


```py

class ActionSmartHomeNotify(Action):
    
    
    '''
    Abstract method, must be defined in concrete implementation. action names must be unique
    '''
    def name(self) -> Text:
        return ACTION_SMARTHOME_NOTIFY    
    
    '''
    async method that executes the actual logic
    '''
    async def execute(self, requester:IntentProvider, modules:types.Modules, params:dict=None) -> ActionResponse:
        service_bot = None
        
        if modules.hasModule("service_bot"):
            service_bot = modules.getModule("service_bot")
            message:Text = params["__event__"]["data"]["message"]        
            await service_bot.send_notification(message)
            return ActionResponse(data = None, events=[])
        else:
            raise ModuleNotFoundError("`service_bot` module does not exist")
        pass

```

The constructor function will return the name of the action, which will be the constant we defined - `ActionSmartHomeNotify`.


* Expose an **instance** of the action class to Cloudisense core, through the `supported_actions` method.


```py
    def supported_actions(self) -> List[object]:
        return [ActionSmartHomeNotify()]
```


* Finally, expose the supported `Intent` and the `Action` names to Cloudisense core, through the `supported_intents` and `supported_action_names` functions respectively.


```py

    '''
        Returns a list supported of action names
    '''
    def supported_action_names(self) -> List[Text]:
        return [ACTION_SMARTHOME_NOTIFY]
    
    
    
    '''
        Returns a list supported of intents
    '''
    def supported_intents(self) -> List[Text]:
        return [INTENT_SMARTHOME_NOTIFY]

```


So now Cloudisense core engine knows the list of intents and actions that your module offers. Whenever there is a client request or reaction rule trigger with the intent value `intent_smarthome_notify`, Cloudisense will invoke the `execute` method of the `ActionSmartHomeNotify` action. The execution can return an error or an `ActionResponse`:


```py
return ActionResponse(data = None, events=[])
```

In the case of a client request, the **data** is returned to the intent requester, while the **events** are pushed down the internal events channel to subscribing components such as the reaction engine. If the requester was the reaction engine, then both **data** and **events** will be pushed down the internal events channel.


---

### Dispatch a data event from your module

Each module in Cloudisense has the capability to dispatch events into the internal pub/sub subsystem on-demand. This can be used to forcefully trigger reaction rules. The `handle_event` method on the application core will handle the dispatch. Here is an example of the dispatch:


```py
    event = DataEvent("/smarthome/plantpump", {"message": "hello world"})
    await self.application.handle_event(event)
```

> Once the event is pushed into the pub/sub subsystem, an appropriate reaction rule can be triggered and another `Action` can be invoked. This sort of allows you to chain multiple data executions from a single event.
