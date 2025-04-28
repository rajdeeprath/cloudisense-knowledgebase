# Module: ReactionEngine

## Name
`reaction_engine`

## Location
- `modules/reaction.py`
- `modules/reaction.so` (Encrypted version)

## Description
The **ReactionEngine** module enables **Cloudisense** to dynamically react to **events** and **intents**. It manages **data-driven** and **time-driven** rules that map triggers to system responses.

It integrates deeply into the Cloudisense pub/sub system and can trigger actions based on incoming data or scheduled times.

---

## Configuration

```json
{
  "enabled": true,
  "klass": "ReactionEngine",
  "conf": {
    "topics_of_interest": ["*"],
    "events_of_interest": ["*"]
  }
}
```

| Property                  | Description                                          | Type    | Default    |
|----------------------------|------------------------------------------------------|---------|------------|
| `enabled`                  | Enable/Disable the module                            | Boolean | `true`     |
| `klass`                    | Class name of the module                             | String  | `ReactionEngine` |
| `conf.topics_of_interest`  | Topics the engine monitors                           | Array   | `["*"]`    |
| `conf.events_of_interest`  | Events the engine monitors                           | Array   | `["*"]`    |

---

## Supported Intents

| Intent              | Description                                | Parameters |
|---------------------|--------------------------------------------|------------|
| `write_rule`         | Write a new rule into the rules store      | JSON object with `id`, `trigger`, `response`, etc. |
| `list_rules`         | List available rules                      | `head` (Boolean, optional) |
| `reload_rules`       | Reload all rules                          | None |
| `reload_rule`        | Reload a specific rule                    | `rule_id` (String) |
| `delete_rule`        | Delete a rule                             | `rule_id` (String) |
| `read_rule`          | Read a specific rule's JSON configuration | `rule_id` (String) |
| `generate_sample`    | Generate a basic rule template            | None |

---

## Rules Overview

A **reaction rule** is a JSON configuration that links an **event** to an **intent**.

| Property                        | Description                                       | Type    |
|----------------------------------|---------------------------------------------------|---------|
| `id`                             | Unique rule ID                                   | String  |
| `description`                    | Brief description of the rule                    | String  |
| `listen-to`                      | Channel or event the rule listens to             | String  |
| `enabled`                        | Enable or disable the rule                       | Boolean |
| `trigger.on-payload-object.key`   | Key in the payload to check                      | String  |
| `trigger.on-payload-object.on-content` | Content condition to match                  | String  |
| `trigger.on-payload-object.on-condition` | Condition to apply (e.g., equals)            | String  |
| `trigger.evaluator`              | Optional custom trigger evaluator               | Object  |
| `response.intent`                | Intent name to trigger                          | String  |
| `response.parameters`            | Parameters to pass with the intent              | Object  |

---

## Types of Rules

### Data-Driven Rule Example

```json
{
  "id": "rule-http-notify",
  "description": "Trigger HTTP notification on new data",
  "listen-to": "/httpcapture/path",
  "enabled": true,
  "trigger": {
    "on-payload-object": {
      "key": "data",
      "on-content": "*",
      "on-condition": "equals"
    },
    "evaluator": null
  },
  "response": {
    "intent": "simple_http_notify",
    "parameters": {
      "http": {
        "webhook": ["http://localhost/receiver"],
        "method": "GET"
      }
    }
  }
}
```

### Time-Driven Rule Example

```json
{
  "id": "rule-script-exec-demo",
  "description": "Trigger script execution every 5 minutes",
  "listen-to": "{time}",
  "enabled": true,
  "trigger": {
    "on-time-object": {
      "recurring": true,
      "using-expression": "*/5 * * * *"
    },
    "evaluator": null
  },
  "response": {
    "intent": "start_script_execution",
    "parameters": {
      "name": "test.sh"
    }
  }
}
```

---

## Notes
- ReactionEngine listens to pub/sub channels and triggers system actions.
- It supports both real-time reactions and scheduled tasks.
- It is a **core module** and cannot be disabled or removed.