## Basics

### ❓ What is CloudiSENSE?
**Answer:**  
CloudiSENSE is a modular, dynamic, and AI-enabled cloud automation and infrastructure management platform. It allows users to manage services, execute automations, monitor systems, and integrate AI assistance, all through dynamically rendered UIs and real-time communication protocols like WebSocket and MQTT.

---

### ❓ What platforms does CloudiSENSE support?
**Answer:**  
CloudiSENSE can run on any Linux-based system, including cloud virtual machines, private servers, and embedded platforms like Raspberry Pi. It is designed to be cross-platform and lightweight.

---

### ❓ How are UIs generated in CloudiSENSE?
**Answer:**  
The CloudiSENSE server sends **dynamic JSON layouts** to the client. The client renders the UI based on these layouts, allowing rapid changes and consistent behavior without frontend code modifications.

---

### ❓ What communication protocols are supported?
**Answer:**  
CloudiSENSE supports HTTP, HTTPS, WebSocket, WSS for client-server communication, and MQTT for inter-instance (node-to-node) communication.

---

### ❓ What is a CloudiSENSE module?
**Answer:**  
A module in CloudiSENSE is a self-contained unit that provides specific functionality, such as AWS resource management, Docker orchestration, or Ansible automation. Modules expose **Actions** and optionally **Intents** for internal or external use.

---

### ❓ What is an Action in CloudiSENSE?
**Answer:**  
An Action is a callable unit of work provided by a module. Actions can be triggered via APIs, UI interactions, or other modules. They perform tasks like listing EC2 instances, running Ansible playbooks, or managing Docker containers.

---

### ❓ What is an Intent in CloudiSENSE?
**Answer:**  
An Intent is a higher-level abstraction meant for conversational interfaces or AI agents. Intents map user expressions to specific actions or sequences inside CloudiSENSE.

---

### ❓ How does CloudiSENSE ensure security?
**Answer:**  
CloudiSENSE uses JWT-based authentication for securing API access and SSL/TLS encryption for securing HTTP and WebSocket communications. Access controls and module-specific validations are also supported.

---

### ❓ How does multi-instance communication work?
**Answer:**  
Multiple CloudiSENSE instances can connect over MQTT, enabling them to share data, relay RPC calls, broadcast messages, and synchronize events across distributed systems.

---

### ❓ Can I add or remove modules dynamically?
**Answer:**  
Yes. Modules can be added by placing them in the modules directory and registering them in the configuration. After a server restart, the new modules are loaded automatically.

---

### ❓ Can CloudiSENSE be extended with AI capabilities?
**Answer:**  
Yes. CloudiSENSE has built-in support for integrating LLMs (Large Language Models) via RAG (Retrieval-Augmented Generation) systems, allowing natural language queries, planning, and assistance directly within the platform.

---

### ❓ What is the minimal hardware requirement for running CloudiSENSE?
**Answer:**  
At minimum, a system with 2 cores CPU, 2GB RAM, and 20GB storage is recommended. For larger deployments, higher resources are advised. CloudiSENSE is optimized to run even on resource-constrained devices.

---

### ❓ How do I deploy CloudiSENSE?
**Answer:**  
CloudiSENSE can be deployed via an installer script or Docker container. Configuration files are used to customize modules, networking, authentication, and other parameters.

---

### ❓ How do I troubleshoot if the client is not connecting?
**Answer:**  
- Ensure the WebSocket/HTTP server ports are open and reachable.
- Check SSL/TLS certificates if using HTTPS/WSS.
- Verify server logs for any errors during startup.
- Confirm the server configuration (`configuration.json`) is correct.

---

### ❓ How often are updates released for CloudiSENSE?
**Answer:**  
Updates are versioned and released periodically. Critical fixes and improvements are pushed when necessary. Users can check the CloudiSENSE S3 release manifests or changelogs for latest builds.