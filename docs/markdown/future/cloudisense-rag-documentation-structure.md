# CloudiSENSE RAG Knowledge Base Documentation Guide

## Objective

This document defines how to build an effective, structured **knowledge base** for developing an **LLM + RAG** based internal help/assistant system inside **CloudiSENSE**.

The goal is to make the LLM intelligent about CloudiSENSE operations, modules, actions, APIs, and user workflows — enabling it to assist users accurately.

---

## Overall Strategy

- Collect and organize documents around **Modules**, **Actions**, **Intents**, **UI Pages**, **System Concepts**, **APIs**, **Installation Guides**, and **Troubleshooting FAQs**.
- Ensure the documents are **machine-readable** (YAML, JSON, or structured Markdown).
- Each document must be **self-contained**, **short**, and **specific**.

---

## Knowledge Base Structure

```
knowledgebase/
├── modules/
│   ├── ansiblemodule.yaml
│   ├── awsmodule.yaml
│   └── dockermodule.yaml
├── system/
│   ├── actions.yaml
│   ├── apis.yaml
│   └── concepts.yaml
├── ui/
│   ├── pages.yaml
│   └── components.yaml
├── guides/
│   ├── installation.yaml
│   ├── configuration.yaml
│   └── faq.yaml
```

---

## Document Types and Their Contents

### 1. Module Documentation (`modules/*.yaml`)

Each module should include:

- **Module Name**
- **Description**
- **Supported Actions**:
  - Name
  - Description
  - Input Parameters
  - Output/Returns
- **Supported Intents** (optional)

#### Example:

```yaml
module: aws
name: AWS Module
version: 1.0
purpose: Manage AWS resources like EC2, S3, VPC.
actions:
  - name: aws_list_ec2
    description: List EC2 instances.
    params: [region, filters]
    returns: List of EC2 instances.
intents:
  - name: query_ec2
    description: Answer questions about EC2 states.
```

---

### 2. System-Level Action Documentation (`system/actions.yaml`)

All global system actions must be documented:

- **Action Name**
- **Description**
- **Parameters**
- **Return Values**

#### Example:

```yaml
action: system_logout
description: Logout a user.
params: []
returns: Status message.
```

---

### 3. UI Pages and Components (`ui/pages.yaml`, `ui/components.yaml`)

- **Page Name**
- **Description**
- **Key Components**

#### Example:

```yaml
page: dashboard
description: Shows system status, modules, and health metrics.
components:
  - server_status
  - connected_modules
  - notifications
```

---

### 4. System Concepts and Terminology (`system/concepts.yaml`)

Define CloudiSENSE fundamentals:

- **Concept**
- **Definition/Explanation**

#### Example:

```yaml
concept: action
description: Actions are callable automation units provided by modules.
```

---

### 5. API Endpoints Documentation (`system/apis.yaml`)

For internal and external APIs:

- **Endpoint**
- **Method**
- **Description**
- **Parameters**

#### Example:

```yaml
endpoint: /api/module/aws/list_instances
method: POST
description: List EC2 instances based on filters.
params:
  - region
  - filters
```

---

### 6. Installation and Configuration Guides (`guides/installation.yaml`, `guides/configuration.yaml`)

- **Topic**
- **Step-by-Step Instructions**

#### Example:

```yaml
topic: install new module
steps:
  - Copy module to /opt/cloudisense/modules/.
  - Add module to configuration.json.
  - Restart CloudiSENSE server.
```

---

### 7. Troubleshooting and FAQ (`guides/faq.yaml`)

Common issues and resolutions:

- **Problem**
- **Solution**

#### Example:

```yaml
question: Why can't my browser connect to CloudiSENSE?
answer: Ensure WebSocket port 8080 is open and accessible.
```

---

## Priorities for Documentation

| Document Type | Importance | Priority |
|:---|:---|:---|
| Modules and Actions | 🌟🌟🌟🌟🌟 | Very High |
| System Concepts | 🌟🌟🌟🌟🌟 | Very High |
| UI Pages | 🌟🌟🌟🌟 | High |
| APIs | 🌟🌟🌟 | Medium |
| Installation Guides | 🌟🌟🌟 | Medium |
| Troubleshooting | 🌟🌟🌟 | Medium |

---

## Best Practices

- Keep documents short and focused.
- Maintain consistent YAML or JSON structure.
- Update documents whenever a module, action, or UI changes.
- Prefer descriptive field names.
- Build retriever indexes (FAISS/Chroma) on these documents regularly.

---

## Next Steps

1. Start by documenting existing modules (e.g., AnsibleModule, AWSModule).
2. Then document system-wide actions and concepts.
3. Create UI page mappings and installation guides.
4. Populate initial FAQs.
5. Connect this knowledgebase to your retriever and LLM.

---

**This knowledge base will make CloudiSENSE Assistant smart, reliable, and context-aware from Day 1!**

---

*Document created on: 2025-04-26*

---

