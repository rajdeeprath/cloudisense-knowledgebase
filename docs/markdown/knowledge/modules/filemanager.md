
# Module: FileManager

## Name
`filemanager`

## Location
`modules/filemanager.py`

## Description
The **FileManager** module manages standard file system operations securely inside a sandbox.  
It provides:
- Controlled read/write access to specific filesystem areas
- Extension-based file operation restrictions
- Secure uploads and downloads
- Temporary file handling and cleanup

**Direct filesystem access is possible but using FileManager is recommended for better security and control.**

---

## Configuration

```json
{
    "enabled": true,
    "klass": "FileManager",
    "order": -9,
    "conf": {
        "auto_clean_tmp_directories": false,
        "tmp_download_dir_prefix": "cloudisense_",
        "accessible_paths": ["/home/user/Downloads/"],
        "downloadable_paths": ["/home/user/Downloads/"],
        "path_conceal_map": {
            "/home": "[HOME]",
            "/usr": "[USER]"
        },
        "allowed_read_extensions": [".properties", ".xml", ".txt", ".js", ".ini", ".log", ".sh", ".bat"],
        "allowed_write_extensions": [".properties", ".xml", ".txt", ".ini", ".log"],
        "upload_dir": "~/uploads/",
        "upload_dir_perm": "0o755",
        "max_streamed_size": 52428800,
        "max_upload_size": 52428800,
        "tmp_downloads_expire_time_seconds": 30,
        "permits_cleanup_interval_seconds": 30,
        "permit_expire_time_milliseconds": 60000,
        "max_parallel_uploads": 10,
        "log_file_errors_count_interval_milliseconds": 60000,
        "update_notification_interval_milliseconds": 10000
    }
}
```

---

## Configuration Properties

| Property | Description | Type | Default |
|:---|:---|:---|:---|
| `enabled` | Enable/disable the module | Boolean | `true` |
| `klass` | Class name | String | `"FileManager"` |
| `conf.auto_clean_tmp_directories` | Auto-clean temp directories | Boolean | `false` |
| `conf.tmp_download_dir_prefix` | Prefix for temp download dirs | String | `"cloudisense_"` |
| `conf.accessible_paths` | Allowed filesystem access paths | List[String] | `["/home/user/Downloads/"]` |
| `conf.downloadable_paths` | Allowed download paths | List[String] | `["/home/user/Downloads/"]` |
| `conf.path_conceal_map` | Filesystem alias mapping | Object | `{ "/home": "[HOME]", "/usr": "[USER]" }` |
| `conf.allowed_read_extensions` | File extensions allowed for reading | List[String] | |
| `conf.allowed_write_extensions` | File extensions allowed for writing | List[String] | |
| `conf.upload_dir` | Upload directory | String | `"~/uploads/"` |
| `conf.upload_dir_perm` | Upload directory permissions | String | `"0o755"` |
| `conf.max_streamed_size` | Max streamed upload size (bytes) | Number | `52428800` |
| `conf.max_upload_size` | Max upload file size (bytes) | Number | `52428800` |
| `conf.tmp_downloads_expire_time_seconds` | Expiry time for temp downloads (seconds) | Number | `30` |
| `conf.permits_cleanup_interval_seconds` | Cleanup interval for upload permits (seconds) | Number | `30` |
| `conf.permit_expire_time_milliseconds` | Upload permit expiry time (milliseconds) | Number | `60000` |
| `conf.max_parallel_uploads` | Max parallel uploads allowed | Number | `10` |
| `conf.log_file_errors_count_interval_milliseconds` | Interval for file error log check (milliseconds) | Number | `60000` |
| `conf.update_notification_interval_milliseconds` | Interval for sending updates to clients (milliseconds) | Number | `10000` |

---

## Supported Intents

| Intent | Description | Parameters |
|:---|:---|:---|
| `read_file` | Read a file and return content | `path` (String), `encoded` (Boolean) |
| `write_file` | Write content to a file | `path` (String), `content` (String), `update` (Boolean), `encoded` (Boolean) |
| `get_accessible_paths` | Return accessible filesystem paths | None |
| `list_content` | List directory contents | `root` (String), `path` (optional, String) |
| `delete_file` | Delete a file | `path` (String) |
| `delete_folder` | Delete a folder | `root` (String), `dirname` (String), `delete_non_empty` (Boolean) |
| `download_file` | Request file download | `mode` (String: static/dynamic), `path` (String) |

---

**Note:**  
FileManager is an internal core module essential for Cloudisense's operation and cannot be disabled or removed.
