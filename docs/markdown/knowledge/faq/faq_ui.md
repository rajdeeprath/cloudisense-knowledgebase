## Contents

### ❓ How is the CloudiSENSE UI dynamically generated?
**Answer:**  
The CloudiSENSE UI is generated dynamically through a structured JSON layout called a **UI Guide**.

When a client connects to the server, it receives the UI Guide, which describes pages, components, layouts, and data bindings.

The client engine interprets this UI Guide and constructs the user interface dynamically using **reusable components** (like widgets, charts, tables) and **predefined page patterns**.

Each page layout, component placement, and data mapping is determined entirely by the server-driven JSON, eliminating the need for hardcoded UIs.

As the server sends live data updates, the client renders the data into the appropriate components in real time.

This architecture allows CloudiSENSE to rapidly modify or extend the user interface without requiring changes on the client side.

It also enables modular, extensible dashboards, management screens, and real-time monitoring views directly in the browser.

The result is a flexible, responsive, and server-controlled UI system.


### ❓ Can I customize the client layout?
**Answer:**  
Yes.

### ❓ How can I add a new page to the UI?
**Answer:**  
In CloudiSENSE, the client supports a set of fixed page types based on popular design patterns.

To add a new page, you define it in the **layout JSON** by specifying:
- The page type (pattern) you want to instantiate.
- Additional parameters to configure how the page behaves and receives data from the server.

Each page must conform to one of the supported UI patterns (e.g., DashboardPattern, FTAPattern, DetailsViewPattern, etc.).

A detailed step-by-step guide is outside the scope of this FAQ.  
It will be published in the future.  
You can also contact the developer if you require more information or assistance.
