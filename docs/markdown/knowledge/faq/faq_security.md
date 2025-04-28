## Security

### ❓ How does CloudiSENSE authenticate users?
**Answer:**  
CloudiSENSE authenticates users using a simple **username/password** combination.

- The default credentials are:
  - **Username:** `administrator`
  - **Password:** `changeme`

- User credentials are stored securely in the configuration file:  
  `cdsmaster/modules/security.json`

During login, clients send their credentials to the server, and upon successful verification, a **JWT token** is issued, which is then used for authenticated real-time communication (such as over WebSocket).

You are strongly advised to change the default password before deploying CloudiSENSE in a production environment.


### ❓ How does CloudiSENSE encrypt communication?
**Answer:**  
CloudiSENSE supports encrypted communication via **SSL/TLS**.

To enable encryption:
- You must deploy CloudiSENSE with valid **SSL certificates**.
- SSL settings are configured in the master configuration file:  
  `cdsmaster/configuration.json`, under the `ssl` section.

Example configuration:

```json
"ssl": {
    "enabled": false,
    "cert_file": "server.crt",
    "private_key": "server.key"
}
```

### ❓ Can I enable IP whitelisting in CloudiSENSE?
**Answer:**  
No, IP whitelisting is not currently supported at the **CloudiSENSE application level**.

If you need to restrict access based on IP addresses, you must implement it at the **network level** (such as firewall rules, security group settings, or reverse proxy configurations).

Application-level IP access control may be considered for future versions.


---

## Multi-Instance Setup

### ❓ How do I connect two CloudiSENSE instances?
**Answer:**

### ❓ Can I run a multi-node CloudiSENSE cluster?
**Answer:**  
CloudiSENSE is designed with future support for multi-node clustering in mind.

At the current stage, **basic inter-instance communication** is possible using **MQTT federation** between separate CloudiSENSE instances.

However, full multi-node clustering features — such as automatic load balancing, shared state management, and distributed job execution — are **not yet fully available**.

These capabilities are planned for future development to enable CloudiSENSE to operate as a scalable clustered platform.

For now, multiple instances can communicate and coordinate basic tasks over MQTT.


### ❓ How does pub/sub messaging work between instances?
**Answer:**  
Pub/Sub messaging between CloudiSENSE instances works through the **federation network**.

- A **source CloudiSENSE instance** makes an **RPC request over the federation network**, specifying:
  - An **intent** (what action to perform),
  - And the necessary **parameters**.

- The **destination CloudiSENSE instance** receives the federated message, maps the intent to the appropriate action, and processes the request.

- After execution, the destination instance sends back a **success** or **error** response to the source instance through the federation network.

This mechanism allows instances to trigger actions on each other reliably using asynchronous pub/sub messaging without requiring direct socket connections.


### ❓ What is a broadcast message in CloudiSENSE?
**Answer:**  
A **broadcast message** in CloudiSENSE is a type of message sent over the **federation network** that is intended to reach **all connected instances** instead of a specific single instance.

When a CloudiSENSE instance sends a broadcast:
- The message is published to a **shared topic** on the federation network.
- All subscribed CloudiSENSE instances receive the broadcast simultaneously.
- Each receiving instance can choose to process the broadcast if it matches the expected intent and parameters.

Broadcasts are useful for:
- Sending system-wide notifications,
- Propagating global state changes,
- Triggering coordinated behaviors across multiple instances.

Unlike a normal RPC, broadcast messages are **not targeted to a specific instance** and **do not expect a direct response**.
