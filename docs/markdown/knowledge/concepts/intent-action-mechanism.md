# Intent – Action Mechanism


The **Intent – Action** mechanism is the soul of **Cloudisense**. This mechanism forms the foundation of all request-response systems within Cloudisense.

Traditionally, client-server communication consisted of making an RPC call with parameters, and the server would respond with data or error messages. A major drawback of such systems is the need to remember the method name and parameters. The **Intent – Action** paradigm borrows from chatbot programming. Instead of a method, we have an **Intent**. As the name suggests, an **Intent** declares your intention regarding the request you're making. Parameters are sent as an object containing named attributes with values to the server.

An **Action** is the encapsulation of the actual logic that handles the request. Each **CustomAction** is extended from the base **Action** class, which gives structure to the Action definition.

Every module in Cloudisense will expose **Intents** and **Actions** via standard methods for the module. Intent names and Action names will be the same, with the only difference being prefixes that identify them as **Intent** names and **Action** names. Look at code snippet below.

**Example (code snippet from a module)**

```python

'''
        Returns a list of supported actions
    '''
    def supported_actions(self) -> List[object]:
        return [ActionSample()]


    '''
        Returns a list supported of action names
    '''
    def supported_action_names(self) -> List[Text]:
        return [ACTION_SAMPLE]
    
    
    
    '''
        Returns a list supported of intents
    '''
    def supported_intents(self) -> List[Text]:
        return [INTENT_SAMPLE]



# custom intents
INTENT_SAMPLE = INTENT_PREFIX + "sample_only"


# custom actions
ACTION_SAMPLE = ACTION_PREFIX + "sample_only"


'''
Module action demo
'''
class ActionSample(Action):
    
    
    '''
    Abstract method, must be defined in concrete implementation. action names must be unique
    '''
    def name(self) -> Text:
        return ACTION_SAMPLE 
          
    
    '''
    async method that executes the actual logic
    '''
    async def execute(self, requester:IntentProvider, modules:types.Modules, params:dict=None) -> ActionResponse:
        return ActionResponse(data = None, events=[])

```

When the application starts, each module is polled for available **Intents** and **Actions**. This data is then stored in a lookup table. When a request arrives in the correct format (JSON structure), the **ActionDispatcher** component extracts the **Intent** name and parameters from the request payload. It then looks up the corresponding **Action** to trigger. If the **Action** is found, it will be triggered with the parameters; otherwise, an error response is returned.

---

## Flow Diagram


![Alt text](images/intent-action.png)


Explaination:

* User Interaction: The user interacts with the application via HTTP/WS connections.
* Request Handling: The web server receives the request and forwards it to the Intent Provider.
* Intent Identification: The Intent Provider analyzes the request and identifies the user's * intent.
* Action Triggering: The Intent Processor receives the intent and triggers the appropriate action(s) in the Action Handler.
* Action Execution: The Action Handler executes the specified actions.
* Event Generation: The Reaction Engine generates events based on the actions performed.
* Event Handling: The Reaction Engine processes the generated events and triggers additional actions if necessary.


## Role of Reaction Engine


When you use the client for Cloudisense, the **ActionDispatcher** accepts an **Intent** from the client and maps it to an **Action**. The Reaction Engine **rules** (both data-driven and time-driven) also inject **Intents** into the system. Moreover, whenever an **Action** executes, it returns an **ActionResponse** object, which contains data from the operation and optionally a list of **Event(s)**.

Any generated **Event(s)** are pushed back into the Cloudisense pub/sub pipeline, which in turn can trigger another reaction rule if one is configured to listen to the channel path. Thus, as you can see, using the **Intent-Action** mechanism along with the Reaction Engine module, it is possible to create a complex **chained** sequence of executions.






