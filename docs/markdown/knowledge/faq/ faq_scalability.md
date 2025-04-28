## Performance and Scalability

### ❓ How many concurrent users can CloudiSENSE handle?
**Answer:**  
CloudiSENSE is primarily designed to operate with a **single active frontend client** at a time (typically the browser-based UI).

However, under the hood, it can handle **thousands of concurrent connections** for backend operations — including:
- HTTP requests,
- WebSocket sessions,
- MQTT/federation messages,
- Rule processing,
- Stream event handling.

This scalability is made possible due to the use of the **Tornado framework**, which provides asynchronous, non-blocking I/O and excellent concurrency support.

Thus, while the primary UI is single-client-oriented, the server can efficiently handle very high loads of concurrent communication and automation tasks.
