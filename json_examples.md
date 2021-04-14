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

## RDS Farm

{
  "access_group_id": "6fd4638a-381f-4518-aed6-042aa3d9f14c",
  "automated_farm_settings": {
    "customization_settings": {
      "ad_container_rdn": "CN=Computers",
      "cloneprep_customization_settings": {
        "post_synchronization_script_name": "cloneprep_postsync_script",
        "post_synchronization_script_parameters": "p1 p2 p3",
        "power_off_script_name": "cloneprep_poweroff_script",
        "power_off_script_parameters": "p1 p2 p3",
        "priming_computer_account": "a219420d-4799-4517-8f78-39c74c7c4efc"
      },
      "instant_clone_domain_account_id": "6f85b3a5-e7d0-4ad6-a1e3-37168dd1ed51",
      "reuse_pre_existing_accounts": false
    },
    "enable_provisioning": true,
    "max_session_type": "LIMITED",
    "max_sessions": 50,
    "min_ready_vms": 0,
    "nics": [
      {
        "network_interface_card_id": "c9896e51-48a2-4d82-ae9e-a0246981b473",
        "network_label_assignment_specs": [
          {
            "enabled": true,
            "max_label": 1,
            "max_label_type": "LIMITED",
            "network_label_name": "vm-network"
          }
        ]
      }
    ],
    "pattern_naming_settings": {
      "max_number_of_rds_servers": 5,
      "naming_pattern": "vm-{n}-sales"
    },
    "provisioning_settings": {
      "base_snapshot_id": "snapshot-1",
      "datacenter_id": "datacenter-1",
      "host_or_cluster_id": "domain-s425",
      "im_stream_id": "6f85b3a5-e7d0-4ad6-a1e3-37168dd1ed51",
      "im_tag_id": "3d45b3a5-e7d0-4ad6-a1e3-37168dd1ed51",
      "parent_vm_id": "vm-2",
      "resource_pool_id": "resgroup-1",
      "vm_folder_id": "group-v1"
    },
    "stop_provisioning_on_error": true,
    "storage_settings": {
      "datastores": [
        {
          "datastore_id": "datastore-1"
        }
      ],
      "replica_disk_datastore_id": "datastore-1",
      "use_separate_datastores_replica_and_os_disks": false,
      "use_view_storage_accelerator": false,
      "use_vsan": false
    },
    "transparent_page_sharing_scope": "VM",
    "vcenter_id": "f148f3e8-db0e-4abb-9c33-7e5205ccd360"
  },
  "description": "Farm Description",
  "display_name": "ManualFarm",
  "display_protocol_settings": {
    "allow_users_to_choose_protocol": true,
    "default_display_protocol": "PCOIP",
    "grid_vgpus_enabled": true,
    "session_collaboration_enabled": false
  },
  "enabled": true,
  "load_balancer_settings": {
    "cpu_threshold": 10,
    "disk_queue_length_threshold": 15,
    "disk_read_latency_threshold": 10,
    "disk_write_latency_threshold": 15,
    "include_session_count": true,
    "memory_threshold": 10
  },
  "name": "ManualFarm",
  "rds_server_ids": [
    "5134796a-322g-5fe5-343f-4daa5d25ebfe",
    "2a43f96c-102b-4ed3-953f-35deg43d43b0ge"
  ],
  "server_error_threshold": 0,
  "session_settings": {
    "disconnected_session_timeout_minutes": 5,
    "disconnected_session_timeout_policy": "NEVER",
    "empty_session_timeout_minutes": 5,
    "empty_session_timeout_policy": "AFTER",
    "logoff_after_timeout": false,
    "pre_launch_session_timeout_minutes": 10,
    "pre_launch_session_timeout_policy": "AFTER"
  },
  "type": "MANUAL",
  "use_custom_script_for_load_balancing": false
}