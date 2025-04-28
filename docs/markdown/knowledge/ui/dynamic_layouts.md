# Dynamic Layouts


## About

The Cloudisense service, in conjunction with the Cloudisense client, implements a powerful dynamic layout system that enables the creation of user interfaces (UIs) using simple, structured JSON. This JSON, referred to as a `UI Guide`, is provided to the client when it first establishes a connection with the service.

The client engine processes the UI Guide to dynamically construct its interface using reusable components and predefined page design patterns. Once the layout is constructed, the service either pushes data passively or sends it actively to the client. The client then renders the received data in the appropriate components, ensuring a seamless and responsive user experience directly in the browser.
---

## Reusable Components

### Data Components

| **Name**                | **Description**                                               | **Comments**                                    |
|--------------------------|-------------------------------------------------------------|------------------------------------------------|
| `PercentageWidget`      | Displays a percentage value with a title and footnote.       | Used for metrics like CPU load or similar data.|
| `StatsWidget`           | Shows a summary with an icon, title, and footnote.           | Commonly used for displaying stats like time.  |
| `TextInfoWidget`        | Displays detailed text information with a title and subtitle.| Suitable for descriptive or system info.       |
| `LineChartWidget`       | Renders a line chart for visualizing trends over time.       | Used for data like CPU or memory usage trends. |
| `PieChartWidget`        | Displays data as a pie chart with a title and legend.        | Good for proportionate data like disk usage.   |
| `ThermometerWidget`     | Visual representation of temperature in degrees.             | Specialized for temperature-related data.      |
| `GaugeChartWidget`      | Displays a gauge chart for monitoring levels (e.g., windspeed).| Great for threshold-based values.             |


| **Name**                | **Description**                                               | **Comments**                                    |
|--------------------------|-------------------------------------------------------------|------------------------------------------------|
| `RuleEditor`            | Component for editing rules in the system.                   | Specific to the reaction engine module.        |
| `RulesView`             | Displays an overview of existing rules.                      | Allows viewing and management of rules.        |


| **Name**                | **Description**                                               | **Comments**                                    |
|--------------------------|-------------------------------------------------------------|------------------------------------------------|
| `ActionCentre`          | Interface for managing and performing actions.               | Supports categorized and custom actions.       |


| **Name**                | **Description**                                               | **Comments**                                    |
|--------------------------|-------------------------------------------------------------|------------------------------------------------|
| `LogView`               | Used for viewing system logs.                                | Part of the log monitoring module.             |
| `SummaryView`           | Provides a summary of key statistics.                        | Part of the statistics module.                 |
| `DiskUsageView`         | Displays detailed information on disk usage.                 | Focused on storage statistics.                 |
| `NetworkStatsView`      | Shows network-related statistics.                            | Ideal for monitoring bandwidth or connections. |
| `FileEditor`            | Enables editing files.                                       | Works with file manager for granular changes.  |
| `AdvanceFilemanagerView`| Provides a detailed file explorer interface.                 | Supports advanced file management.             |
| `SettingsView`          | Interface for managing application settings.                 | Part of the core system module.                |


### Page Patterns

| **Name**                | **Description**                                               | **Comments**                                    |
|--------------------------|-------------------------------------------------------------|------------------------------------------------|
| `DashPattern`           | A dashboard layout pattern.                  | Enables modular dashboard designs.             |
| `EditorViewPattern`     | Template for creating editor-based views.                     | Helps in structured editing interfaces.        |
| `DetailsViewPattern`    | Used to display detailed information about an entity.         | Ideal for feature-specific details.            |
| `FTAPattern`            | A table-based component for displaying records and actions for those records.   | Includes features like edit, delete or custom actions.|
| `FormDataPattern`       | Component for creating and managing forms.                    | Suitable for configurations or settings.       |



## Sample UI Guide

```json

{
	"sessionid": "",
	"datetime": "",
	"role": "",
	"pages": [{
			"path": "/dashboard",
			"layout": "/admin",
			"name": "Dashboard",
			"icon": "nc-icon nc-chart-pie-35",
			"component": "Dashboard",
			"metadata": {
				"layout":{
					"render":{
						"rows":[
							[{
								"spacing": "lg=3&sm=6",
								"component": "PercentageWidget",
								"datakey": null,
								"data": {
									"title": "CPU Load",
									"summary": "75%",
									"footnote": "Waiting fior data...",
									"schema": {
										"datasets": [
											{
											  "backgroundColor": [
												"rgba(50,205,50, 0)",
												"rgba(220,20,60, 1)"
											  ],
											  "borderColor": [
												"rgba(50,205,50, 1)",
												"rgba(220,20,60, 1)"
											  ],
											  "borderWidth": 0.5
											}
										  ]
									}
								}
							},
							{
								"spacing": "lg=3&sm=6",
								"component": "StatsWidget",
								"datakey": "human_readabale_system_time",
								"data": {
									"icon": "nc-watch-time",
									"iconmood": "success",
									"summary": "System Time",
									"footnote": "Waiting for data..."
								}
							},
							{
							   "spacing": "lg=3&sm=6",
								"component": "StatsWidget",
								"datakey": "cloudisense_error_count",
								"data": {
									"icon": "nc-vector",
									"iconmood": "danger",
									"summary": "Cloudisense Errors",
									"footnote": "Waiting for data..."
								}
							},
							{
								"spacing": "lg=3&sm=6",
								"component": "StatsWidget",
								"datakey": "enabled_rules_count",
								"data": {
									"icon": "nc-notes",
									"iconmood": "primary",
									"summary": "Reaction Rules",
									"footnote": "Waiting for data..."
								}
							}],	
							[
								{
									"spacing": "md=6",
									"component": "TextInfoWidget",
									"datakey": "software_version_info",
									"data": {
										"title": "Software Details",
										"subtitle": "Program Details",
										"footnote": "Waiting for data..."
									}
								},
								{
									"spacing": "md=6",
									"component": "TextInfoWidget",
									"datakey": "system_information",
									"data": {
										"title": "System Information",
										"subtitle": "Misc Information",
										"footnote": "Waiting for data..."
									}
								}
							],
							[{
								"spacing": "md=6",
								"component": "LineChartWidget",
								"datakey": "cpu_usage_samples",
								"data": {
									"title": "CPU Usage",
									"subtitle": "CPU Usage over time",
									"footnote": "Waiting for data...",
									"chartheading": "CPU Usage",
									"legendpos": "bottom",
									"fillarea": false,
									"labels" : [],									
									"schema" : {
										"datasets": [
										  {
											"label": "CPU Usage",
											"borderColor": "rgb(255, 99, 132)",
											"backgroundColor": "rgba(255, 99, 132, 0.5)"
										  }
										]
									  }
								}
							},
							{
								"spacing": "md=6",
								"component": "LineChartWidget",
								"datakey": "memory_usage_samples",
								"data": {
									"title": "Memory Usage",
									"subtitle": "Memory Usage over time",
									"footnote": "Waiting for data...",
									"chartheading": "Memory Usage",
									"legendpos": "bottom",
									"fillarea": true,
									"labels" : [],									
									"schema" : {
										"datasets": [
										  {
											"label": "Memory Usage",
											"borderColor": "rgb(184, 255, 0.5)",
											"backgroundColor": "rgba(0, 184, 255, 0.5)"
										  }
										]
									  }
								}
							}],
							[{
								"spacing": "lg=4",
								"component": "PieChartWidget",
								"datakey": "disk_usage_percentage",
								"data": {
									"title": "Disk Usage",
									"subtitle": "Disk Usag eDetails",
									"footnote": "Waiting for data...",
									"chartheading": "Disk Usage",
									"legendpos": "bottom",
									"labels": ["Used", "Free"],
									"schema": {
										"datasets": [
											{      
											"backgroundColor": [
												"rgba(255, 99, 132, 0.2)",
												"rgba(54, 162, 235, 0.2)"
											],
											"borderColor": [
												"rgba(255, 99, 132, 1)",
												"rgba(54, 162, 235, 1)"
											],
											"borderWidth": 1
											}
										]
									}
								}
							},
							{
								"spacing": "lg=3&sm=6",
								"component": "ThermometerWidget",
								"datakey": "weather_temperature",
								"data": {
									"title": "Temperature",
									"subtitle": "Deg celcius",
									"footnote": "Waiting for data...",
									"schema": {
										"theme": "light",
										"max": "100",										
										"steps": "2",
										"format": "°C",
										"size": "normal",
										"height": 300
									}
								}
							},
							{
								"spacing": "lg=3&sm=6",
								"component": "GaugeChartWidget",
								"datakey": "weather_windspeed",
								"data": {
									"title": "Wind Speed",
									"subtitle": "Current Speed",
									"footnote": "Waiting for data...",
									"levelcount": 20
								}
							}]
						]
					}
				}
			}
		},
		{
			"path": "/rules/:id",
			"layout": "/admin",
			"name": "Rules Editor",
			"icon": "nc-icon nc-chart-pie-35",
			"hidden": true,
			"component": "RuleEditor",
			"formodule": "reaction_engine"
		},
		{
			"path": "/rules",
			"layout": "/admin",
			"name": "Rules",
			"exact": true,
			"icon": "nc-icon nc-chart-pie-35",
			"component": "RulesView",
			"formodule": "reaction_engine"
		},
		{
			"path": "/logs",
			"layout": "/admin",
			"name": "Logs",
			"icon": "nc-icon nc-chart-pie-35",
			"component": "LogView",
			"formodule": "log_monitor"
		},
		{
			"path": "/actions",
			"layout": "/admin",
			"name": "Actions",
			"exact": true,
			"icon": "nc-icon nc-tap-01",
			"component": "ActionCentre",
			"metadata": {
				"action": {
					"items": [{
							"label": "Top Level Menu 1",
							"is_category": true,
							"children": [
								"{module-menu}",
								"{module-menu}"
							],
							"data": null
						},
						{
							"label": "Top Level Menu 2",
							"is_category": true,
							"children": [
								"{module-menu}",
								"{module-menu}",
								"{custom_actions}"
							],
							"data": null
						},
						{
							"label": "Top Level Menu 3",
							"is_category": true,
							"children": [{
								"label": "My Item",
								"is_category": false,
								"children": [],
								"data": {
									"intent": "TEST_INTENT",
									"params": []
								}
							}],
							"data": null
						}
					]
				}
			}
		},
		{
			"collapse": true,
			"path": "/statistics",
			"name": "Statistics",
			"state": "openStats",
			"icon": "nc-icon nc-chart-bar-32",
			"formodule": "sysmon",
			"views": [{
					"path": "/statistics/summary",
					"layout": "/admin",
					"name": "Overview",
					"mini": "O",
					"component": "SummaryView"
				},
				{
					"path": "/statistics/disk",
					"layout": "/admin",
					"name": "Disk",
					"mini": "D",
					"component": "DiskUsageView"
				},
				{
					"path": "/statistics/network",
					"layout": "/admin",
					"name": "Network",
					"mini": "N",
					"component": "NetworkStatsView"
				}
			]
		},
		{
			"path": "/files/:id",
			"layout": "/admin",
			"name": "File Editor",
			"icon": "nc-icon nc-notes",
			"hidden": true,
			"component": "FileEditor",
			"formodule": "file_manager"
		},
		{
			"path": "/files",
			"layout": "/admin",
			"exact": true,
			"name": "Explorer",
			"icon": "nc-icon nc-bag",
			"component": "AdvanceFilemanagerView",
			"formodule": "file_manager"
		},
		{
			"collapse": true,
			"path": "/custom",
			"name": "Custom",
			"state": "openCustom",
			"icon": "nc-icon nc-app",
			"views": [{
					"path": "/custom/overview",
					"layout": "/admin",
					"name": "Overview",
					"mini": "O",
					"component": "DashPattern",
					"metadata": {
						"layout":{
							"render":{
								"rows":[
									[{
										"spacing": "lg=3&sm=6",
										"component": "PercentageWidget",
										"datakey": null,
										"data": {
											"title": "CPU Load",
											"summary": "75%",
											"footnote": "Waiting fior data...",
											"schema": {
												"datasets": [
													{
													  "backgroundColor": [
														"rgba(50,205,50, 0)",
														"rgba(220,20,60, 1)"
													  ],
													  "borderColor": [
														"rgba(50,205,50, 1)",
														"rgba(220,20,60, 1)"
													  ],
													  "borderWidth": 0.5
													}
												  ]
											}
										}
									},
									{
										"spacing": "lg=3&sm=6",
										"component": "StatsWidget",
										"datakey": "human_readabale_system_time",
										"data": {
											"icon": "nc-watch-time",
											"iconmood": "success",
											"summary": "System Time",
											"footnote": "Waiting for data..."
										}
									},
									{
									   "spacing": "lg=3&sm=6",
										"component": "StatsWidget",
										"datakey": "cloudisense_error_count",
										"data": {
											"icon": "nc-vector",
											"iconmood": "danger",
											"summary": "Cloudisense Errors",
											"footnote": "Waiting for data..."
										}
									},
									{
										"spacing": "lg=3&sm=6",
										"component": "StatsWidget",
										"datakey": "enabled_rules_count",
										"data": {
											"icon": "nc-notes",
											"iconmood": "primary",
											"summary": "Reaction Rules",
											"footnote": "Waiting for data..."
										}
									}]
								]
							}
						}
					}
				},
				{
					"path": "/custom/feature/edit/:id",
					"layout": "/admin",
					"name": "Custom Edit",
					"icon": "nc-icon nc-chart-pie-35",
					"hidden": true,
					"component": "EditorViewPattern"
				},
				{
					"path": "/custom/feature/details/:id",
					"layout": "/admin",
					"name": "Custom Details",
					"icon": "nc-icon nc-chart-pie-35",
					"hidden": true,
					"component": "DetailsViewPattern"
				},
				{
					"path": "/custom/feature",
					"exact": true,
					"layout": "/admin",
					"name": "Feature",
					"mini": "F",
					"component": "FTAPattern",
					"metadata": {
						"layout":{
							"render":{
								"navbar": {
									"brand": "Records"
								},
								"table": {																	
									"title": "Sample Records",
									"headers": [],
									"data":{											
										"datakey": null,
										"intent": "get_sample_records",
										"uid": "ID"
									},
									"action": [
										{
											"name": "delete",
											"type": "delete",
											"mood": "danger",
											"icon": "fa-times",
											"path": null,
											"intent": "delete_sample_records"
										}	
									]									
								}
							}
						}	
					}
				},
				{
					"path": "/custom/settings",
					"exact": true,
					"layout": "/admin",
					"name": "Config",
					"mini": "F",
					"component": "FormDataPattern",
					"metadata": {}
				}				
			]
		},
		{
			"path": "/settings",
			"layout": "/admin",
			"name": "Settings",
			"icon": "nc-icon nc-settings-90",
			"component": "SettingsView",
			"formodule": "systemcore"
		}		
	]
}

```
