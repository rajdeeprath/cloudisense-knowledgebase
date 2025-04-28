# Module: GenericNotifier

## Name
`genericnotifier`

## Location
`modules/genericnotifier.py`

## Overview
The **GenericNotifier** module handles dispatching notifications to smartphones and servers.  
It supports multiple channels like **Telegram** and **HTTP/HTTPS webhooks**.  
No need for direct code interaction — broadcasting specific intents automatically triggers notifications.

## Configuration

```json
{
    "enabled": true,
    "klass": "GenericNotifierModule",
    "conf": {
        "api": {
            "enabled": false
        },
        "notification": {
            "telegram": {
                "bot_token": "",
                "chat_id": []
            },
            "http": {
                "webhook": [],
                "method": "GET"
            }
        }
    }
}
```

## Configuration Properties

| **Property** | **Description** | **Type** | **Default** |
|:-------------|:-----------------|:---------|:------------|
| `enabled` | Enable/disable the module | Boolean | `true` |
| `klass` | Python class name | String | `GenericNotifierModule` |
| `conf.api.enabled` | Enable/disable API for pushing notifications | Boolean | `true` |
| `conf.notification.telegram.bot_token` | Telegram [bot token](https://core.telegram.org/bots#3-how-do-i-create-a-bot) | String | Empty |
| `conf.notification.telegram.chat_id` | List of Telegram [chat IDs](https://core.telegram.org/bots/api#chat) | List[String] | `[]` |
| `conf.notification.http.webhook` | List of HTTP/HTTPS endpoints for notifications | List[String] | `[]` |
| `conf.notification.http.method` | HTTP method for webhook (`GET`, `POST`, etc.) | String | `GET` |

## Supported Intents

| **Intent** | **Description** | **Parameters** |
|:-----------|:----------------|:---------------|
| `simple_telegram_notify` | Sends a Telegram notification to a chatroom, group, or channel | - `bot_token`: Bot token<br>- `chat_id`: Target chat ID |
| `simple_http_notify` | Sends a notification to HTTP/HTTPS endpoints | - `webhook`: List of URLs<br>- `method`: HTTP method (`GET`, `POST`, `PUT`, `DELETE`) |

## Notes
- The **GenericNotifier** is essential to **Cloudisense** operations and cannot be disabled or removed.