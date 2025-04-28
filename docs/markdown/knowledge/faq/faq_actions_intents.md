## Actions And Intents

### ❓ What is an action in CloudiSENSE?
**Answer:**  
In CloudiSENSE, an **Action** is a **self-contained unit of operational logic** that performs a specific task when triggered.

Actions are defined inside modules by creating Python classes that inherit from the `Action` base class.  
They form the foundation for automation, dynamic behavior, and system interaction within CloudiSENSE.

Each Action typically specifies:

- **Name:**  
  A unique identifier for the action within the module.

- **Parameters:**  
  A set of input fields required to perform the action, passed as JSON.

- **Execution Logic:**  
  The specific task that the action performs when triggered (inside the `run()` method).

- **Return Values:**  
  Structured data returned upon action completion, typically wrapped inside an `ActionResponse` object.

---

**Actions contain executable logic to perform real-world tasks, such as:**
- Sending a message or notification
- Editing or saving a configuration file
- Downloading a file from a URL
- Making HTTP API calls to external services
- Executing shell commands
- Querying system metrics
- Orchestrating complex workflows

---

**How Actions are triggered in CloudiSENSE:**  
- Typically, Actions are **invoked as part of RPC (Remote Procedure Calls)**.  
- RPC requests are sent from the UI, clients, or other connected services, targeting a specific Action by name.
- Actions can also be triggered automatically by **Intents** (for natural language commands).

This design makes Actions highly **modular**, **reusable**, and **easy to integrate** into dynamic workflows.

---

**Example structure of an Action:**

```python
class MySampleAction(Action):
    def name(self) -> Text:
        return "sample_action"

    async def run(self, params: Dict) -> ActionResponse:
        # Extract parameters
        value = params.get("value")
        # Perform the operation
        result = value * 2
        return ActionResponse(data={"result": result})
```

### ❓ How do I trigger an action from the UI?
**Answer:**  
To trigger an Action from the CloudiSENSE UI, the client (usually the browser frontend) needs to make an **RPC (Remote Procedure Call)** request to the CloudiSENSE server.

Here’s how it works:

1. **Prepare a Proper JSON RPC Message:**  
   The RPC message should include:
   - A unique **requestid** to track the request-response.
   - The **Intent Name** associated with the Action you want to trigger.
   - The **parameters** expected by the Action.
   - The type field set as `"rpc"`.

2. **Send the RPC Call Over WebSocket:**  
   The CloudiSENSE frontend maintains a WebSocket connection with the server.  
   The RPC message is sent over this WebSocket channel.

3. **Server Receives and Routes the Request:**  
   The server matches the received **Intent** to the corresponding **Action**, validates the parameters, and executes the Action asynchronously.

4. **Receive the Action Response:**  
   Once the Action is executed, the server sends back a response containing the results, associated with the original `requestid`.

---

**Example Correct RPC Message Format:**

```json
{
  "requestid": "abc12345",
  "intent": "sample_action_intent",
  "type": "rpc",
  "params": {
    "param1": "value1",
    "param2": "value2"
  }
}
```

### ❓ Can I trigger actions via HTTP APIs directly?
**Answer:**  
No, in CloudiSENSE you **cannot call an Action directly via HTTP API**.

Actions are primarily designed to be **invoked through Socket RPC communication**, mainly for socket-connected clients like the browser frontend.

Typically, an Action calls internal methods or functions of a module to get a specific task done (e.g., fetch data, perform a calculation, trigger an operation).

If a module defines an **HTTP API** endpoint that internally calls the same functions used by its Actions,  
then triggering that HTTP API **indirectly achieves the same result** as triggering the Action — but **the Action itself is not directly accessible over HTTP**.

---

**Summary of Key Behavior:**
- **Actions** = Designed for **Socket RPC calls** (intent → action flow).
- **HTTP APIs** = Manually exposed by modules as separate Tornado handlers.
- If needed, **both** an Action and an HTTP API can internally use the **same module logic**.
- Developers creating their own modules can **choose to expose functionality both via HTTP and via Actions** — depending on access requirements.

---

**In simple terms:**  
> **Actions are for socket RPC clients. HTTP APIs are independent and must be manually exposed if required.**

This separation allows CloudiSENSE to keep internal automation and external HTTP exposure flexible and modular.


### ❓ What is the difference between actions and intents?
**Answer:**  
In CloudiSENSE, **Actions** and **Intents** serve different but complementary roles.

---

**Actions:**  
- Actions are the **core executable logic blocks** in CloudiSENSE.
- They perform real operations — like sending a message, modifying a config file, executing a script, making an HTTP request, etc.
- Actions are implemented as Python classes by inheriting from the `Action` base class.
- They are triggered typically through **Socket RPC calls** or internally from the server logic.
- Each Action is identified by a **globally unique action name**.

**Example:**  
An Action might be defined to "restart a service" or "copy a file."

---

**Intents:**  
- Intents are **abstract, human-friendly identifiers** that map to one or more Actions.
- They act as a **bridge** between external clients (like UI or AI assistants) and internal Actions.
- When a client sends an RPC request with an Intent name, the server looks up which Action the Intent is mapped to and triggers that Action internally.
- Intents make it easier to allow flexible UI interaction, AI integration, or external command mappings without exposing internal Action details.

**Example:**  
An Intent called `"restart_service_intent"` might map internally to an Action that restarts the server.

---

**Important Concept:**  
- The use of an **Intent** — instead of directly invoking a function — means that you are **communicating your intention** to CloudiSENSE.
- CloudiSENSE then **decides** which Action(s) to trigger internally based on that intention.
- This design allows CloudiSENSE to be **more flexible, decoupled, and modular**, making it easy to change internal behavior without changing the client-side code.

---

**Key Differences Summary:**

| Aspect | Action | Intent |
|:---|:---|:---|
| Purpose | Perform the actual work | Provide a human-friendly command |
| Triggered by | Socket RPC, internal server logic | RPC call from client or UI |
| Directly executable? | Yes | No (requires mapping to an Action) |
| Implementation | Python class (`Action`) | Configuration or class (`IntentProvider`) |
| Example | Restarting a server | \"Restart the service\" command from UI |

---

**In simple terms:**  
> **Actions do the work. Intents tell the system what work to do.**

An Intent is like **asking** CloudiSENSE to do something,  
and an Action is **actually performing** that task inside the system.


### ❓ How are parameters passed to an action?
**Answer:**  
In CloudiSENSE, parameters are passed to an Action through the **`params`** field of an **RPC request**.

When a client (such as the UI) wants to trigger an Action, it sends an RPC message that includes:
- the **Intent name**,
- a unique **request ID**,
- and the **parameters** required for the Action inside a `params` dictionary.

The server receives the RPC call, locates the corresponding Action, and passes the `params` dictionary into the Action's `run()` method.

---

**Example RPC Message Format:**

```json
{
  "requestid": "abc12345",
  "intent": "restart_service_intent",
  "type": "rpc",
  "params": {
    "service_name": "nginx"
  }
}
```

### ❓ What happens if an action fails?
**Answer:**  
If an Action fails during execution in CloudiSENSE, it **raises an exception** internally.

When this happens:
1. The server **captures the exception** during the RPC handling process.
2. It automatically generates an **error response**.
3. The error response is sent back to the client, associated with the original `requestid`.

This informs the client that the Action execution failed, along with a descriptive error message explaining what went wrong.

---

**Important Points:**
- CloudiSENSE does **not crash** when an Action fails — only the specific request fails gracefully.
- The error message originates from the exception raised inside the Action’s `run()` method.
- Clients receive an error response over the socket and can handle it appropriately (for example, displaying an error to the user).
- Normal server operations continue unaffected even if an Action fails.

---

**In simple terms:**  
> **If an Action fails, CloudiSENSE catches the error and sends a structured error response to the client, without interrupting the server or other clients.**
