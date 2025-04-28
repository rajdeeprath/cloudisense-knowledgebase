# CloudiSENSE Configuration Documentation

---

## Overview

CloudiSENSE stores its configuration information primarily in two locations:

- **Master Configuration:** `cdsmaster/configuration.json`
- **Module-Specific Configurations:** Stored in `cdsmaster/modules/conf/`

The master configuration (`configuration.json`) controls application-wide settings such as server behavior, security (SSL), API/WebSocket enablement, Pub/Sub system settings, and core dispatcher settings.

> **NOTE:** Any changes made to the configuration file will require a **restart** of the CloudiSENSE service.

---

## Sample configuration.json File

```json
{
  "configuration": {
    "base_package": "cdsmaster",
    "server": {
      "enabled": true,
      "http_port": 8000,
      "https_port": 8080,
      "bind_host": "127.0.0.1",
      "debug_mode": true,
      "hot_reload": false,
      "api": {
        "enabled": true
      },
      "ws": {
        "enabled": true
      },
      "cors": {
        "allow-origin": "*",
        "allow_headers": "*, x-xsrftoken, x-csrftoken, Origin, X-Auth-Token, X-Requested-With, Content-Type, Accept, Authorization, Custom-Header",
        "allow_methods": "GET, POST, PUT, DELETE, OPTIONS, PUT, PATCH",
        "expose_headers": "*, content-type, location, set-cookie",
        "request_headers": "*",
        "allow_credentials": "true"
      }
    },
    "ssl": {
      "enabled": false,
      "cert_file": "server.crt",
      "private_key": "server.key"
    },
    "modules": {
      "pubsub": {
        "enabled": true,
        "conf": {
          "allow_dynamic_topics": true,
          "message_flush": {
            "batch_size": 30,
            "interval_seconds": 200
          },
          "dynamic_topics": {
            "type": "bidirectional",
            "queue_size": 10000,
            "max_users": 0
          },
          "topics": [
            {
              "name": "/ping",
              "type": "push_message",
              "queue_size": 10000,
              "max_users": 0
            },
            {
              "name": "/stats",
              "type": "push_message",
              "queue_size": 10000,
              "max_users": 0
            },
            {
              "name": "/notification",
              "type": "subscription",
              "queue_size": 10000,
              "max_users": 0
            }
          ]
        }
      }
    },
    "action_dispatcher": {
      "request_queue_size": 40
    }
  }
}
```

---

## Configuration Properties

### General Settings

| **Attribute** | **Description** | **Type** | **Default Value** |
|:---|:---|:---|:---|
| `base_package` | Base Python package used for resolving modules and configs. | String | `cdsmaster` |

### Server Configuration

| **Attribute** | **Description** | **Type** | **Default Value** |
|:---|:---|:---|:---|
| `server.enabled` | Enables/disables the CloudiSENSE web server. | Boolean | `true` |
| `server.http_port` | HTTP port number. | Number | `8000` |
| `server.https_port` | HTTPS (SSL) port number. | Number | `8080` |
| `server.bind_host` | Host/IP to bind to. `0.0.0.0` for all interfaces. | String | `127.0.0.1` |
| `server.debug_mode` | Enables detailed debug logs. | Boolean | `true` |
| `server.hot_reload` | Experimental: reload modules without restarting server. | Boolean | `false` |
| `server.api.enabled` | Enables REST API routes. | Boolean | `true` |
| `server.ws.enabled` | Enables WebSocket server. | Boolean | `true` |

### CORS Configuration

| **Attribute** | **Description** | **Type** | **Default Value** |
|:---|:---|:---|:---|
| `cors.allow-origin` | Allowed CORS origins (`*` means all). | String | `*` |
| `cors.allow_headers` | Allowed CORS headers. | String | Multiple values |
| `cors.allow_methods` | HTTP methods permitted. | String | Multiple methods |
| `cors.expose_headers` | Headers exposed to the browser. | String | Multiple values |
| `cors.request_headers` | Allowed request headers. | String | `*` |
| `cors.allow_credentials` | Allow credentials (cookies, etc.). | String | `true` |

### SSL Configuration

| **Attribute** | **Description** | **Type** | **Default Value** |
|:---|:---|:---|:---|
| `ssl.enabled` | Enables SSL/TLS encryption. | Boolean | `false` |
| `ssl.cert_file` | SSL Certificate file path. | String | `server.crt` |
| `ssl.private_key` | SSL Private Key file path. | String | `server.key` |

### Pub/Sub Module Configuration

| **Attribute** | **Description** | **Type** | **Default Value** |
|:---|:---|:---|:---|
| `modules.pubsub.enabled` | Enables internal Pub/Sub system. | Boolean | `true` |
| `modules.pubsub.conf.allow_dynamic_topics` | Allow creation of dynamic topics at runtime. | Boolean | `true` |
| `modules.pubsub.conf.message_flush.batch_size` | Number of messages batched for flushing. | Number | `30` |
| `modules.pubsub.conf.message_flush.interval_seconds` | Time interval to flush batched messages. | Number | `200` |
| `modules.pubsub.conf.dynamic_topics.type` | Type of dynamic topic: e.g., bidirectional. | String | `bidirectional` |
| `modules.pubsub.conf.dynamic_topics.queue_size` | Queue size for dynamic topics. | Number | `10000` |
| `modules.pubsub.conf.dynamic_topics.max_users` | Maximum users per dynamic topic (0 = unlimited). | Number | `0` |
| `modules.pubsub.conf.topics` | Predefined static topics. | List | `/ping`, `/stats`, `/notification` |

### Action Dispatcher Configuration

| **Attribute** | **Description** | **Type** | **Default Value** |
|:---|:---|:---|:---|
| `action_dispatcher.request_queue_size` | Maximum pending requests allowed in the Action dispatcher queue. | Number | `40` |


---

## Configuration Tips & Tricks

### Allow Binding to All Hosts/IPs

```json
"bind_host": "0.0.0.0"
```

Allow CloudiSENSE to accept requests from any external IP by setting the bind host to `0.0.0.0`.

---

### Disable HTTP API (WebSocket Only Mode)

```json
"api": {
  "enabled": false
}
```

Disables REST HTTP endpoints while still allowing WebSocket operations.

---

### Disable WebSocket Service (HTTP API Only)

```json
"ws": {
  "enabled": false
}
```

Disables WebSocket connections while keeping REST APIs functional.

---

### Full Server Disable (Silent Monitoring Mode)

```json
"server": {
  "enabled": false
}
```

Fully disables the server from accepting HTTP/WS traffic, but background event processing still continues.

---

## Conclusion

The `configuration.json` file in CloudiSENSE provides fine-grained control over the server, networking, security, messaging, and dispatcher system.

By understanding and tuning these settings, administrators can deploy CloudiSENSE efficiently for cloud environments, edge computing, or hybrid setups.

Always remember to restart CloudiSENSE after modifying the configuration!

---

