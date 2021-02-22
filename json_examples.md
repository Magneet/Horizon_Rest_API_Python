# json Examples

## Application Pools

{
  "anti_affinity_data": {
    "anti_affinity_count": 10,
    "anti_affinity_patterns": [
      "*pad.exe",
      "*notepad.???"
    ]
  },
  "category_folder_name": "dir1\\dir2\\dir3\\dir4",
  "cs_restriction_tags": [
    "Internal",
    "External"
  ],
  "description": "string",
  "desktop_pool_id": "d795659c-a5dd-4ffb-9240-3ddaf4ef007a",
  "display_name": "Firefox",
  "enable_client_restrictions": false,
  "enable_pre_launch": false,
  "enabled": true,
  "executable_path": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Firefox.lnk",
  "farm_id": "855ea6c5-720a-41e1-96f4-958c90e6e424",
  "max_multi_sessions": 5,
  "multi_session_mode": "DISABLED",
  "name": "Firefox",
  "parameters": "-p myprofile",
  "publisher": "Mozilla Corporation",
  "shortcut_locations": [
    "START_MENU"
  ],
  "start_folder": "string",
  "supported_file_types_data": {
    "enable_auto_update_file_types": true,
    "enable_auto_update_other_file_types": true,
    "file_types": [
      {
        "description": "Firefox Document",
        "type": ".html"
      }
    ],
    "other_file_types": [
      {
        "description": "Firefox URL",
        "name": "https",
        "type": "URL"
      }
    ]
  },
  "version": "72.0.2"
}