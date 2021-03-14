# Changelog

08-02-2021
* renamed Settings class to Config
* Config class
    * Added
        * list_virtual_centers
        * get_environment_properties
        * get_settings
        * get_settings-feature
        * get_settings-general
        * get_settings-security
    * Added but not working yet
        * update_settings_general

09-02-2021
* Changed Error handling from returning a value to raising an error for most modules
* found error in disconnect
    * fixed the error in disconnecting
* Config Class
    * rename list_virtual_centers to get_virtual_centers
    * Made the update_settings_general work properly

10-02-2021
* Minor bug fixes
* Inventory Class
    * renamed list_ad_domains to get_ad_domains
* Config Class
    * Added update_settings
    * Added update_settings_security
    * Added update_settings_general
* External Class
    * Renamed list_hvpools to get_hvpools
    * Started work on get_base_vms
        * work in progress!!

11-02-2021
* External Class
    * Got get_base_vms working
    * Added get_datacenters
    * Added get_hosts_or_clusters

12-02-2021
* renamed Pools class to Inventory
* External Class
    * added get_vm_templates

* Inventory class
    * Renamed get_hvpools to get_desktop_pools
    * Added get_desktop_pool
    * Added get_farms
    * Added get_farm
    * Added get_machine
    * Added get_machines
    * started work on get_sessions

13-02-2021
* Inventory Class
    * finalized get_sessions
    * added get_session
    * update get_machines with pagination and filtering

14-02-2021
* Added Dev branch
* Inventory Class
    * Added delete_machines
    * removed print that was left behind in get_machines
    * Added delete_machine

16-02-2021
* Inventory Class
    * Added Machines_enter_maintenance_mode
    * Added Machines_exit_maintenance_mode
    * Added Machines_rebuild
    * Added Machines_reset
    * Added Machines_restart
    * Added Machines_recover
* External Class
    * started work on get_ad_users_or_groups

18-02-2021
* External Class
    * finalized get_ad_users_or_groups
    * added get_ad_user_or_group

19-02-2021
* External Class
    * Applied fix for get_base_vms (issues when datacenter_id was not used)
    * Fixed get_hosts_or_clusters (made the datacenter_id required)
    * Added get_base_snapshots
    * Added get_customization_specifications
    * Added get_datastores
    * Added get_datastore_paths

20-02-2021
* External class
    * Added get_network_labels
    * Added get_resource_pools
    * Added get_vm_folders

21-02-2021
* External Class
    * added get_network_interface_cards
* Inventory Class
    * fixed get_machines
    * Replaced id or ids with better named arguments like machine_id or machine_ids in a lot of methods
    * Renamed delete_machine to machine_delete
    * Renamed delete_machines to machines_delete
    * Added get_application_pools

22-02-2021
* Inventory Class
    * Added get_application_pool
    * Added new_application_pool
    * Added update_application_pool
    * Added delete_application_pool
    * Renamed machine related methods

23-02-2021
* Added Entitlements class
* Inventory Class
    * Added get_application_icon
    * Added get_application_icons
* Entitlements class
    * Added get_application_pool_entitlement
    * Added get_application_pools_entitlements
    * Started work on new_application_pool_entitlements (might already work, haven't tested it yet)

24-02-2021
* Entitlements Class
    * Started work on delete_application_pool_entitlements

25-02-2021
* Inventory class
    * applied fixes to machine actions (needs testing)
    * Removed unneeded prints from get_ad_users_or_groups
    * Added get_desktop_pool_installed_applications
    * Added get_farm_installed_applications
    * started work on disconnect_sessions
* Entitlements Class
    * Finalized new_application_pool_entitlements
    * Finalized delete_application_pool_entitlements
    * Added get_desktop_pools_entitlements
    * Added get_desktop_pool_entitlement
    * Added new_desktop_pools_entitlements
    * Added delete_desktop_pools_entitlements

26-02-2021
* Inventory class
    * Finished disconnect_sessions
    * Added logoff_sessions
    * Added reset_session_machines
    * Added restart_session_machines
    * Added send_message_sessions

27-02-2021
* Inventory Class
    * Added remove_machines
    * Added Add_Machines
    * Added add_machines_by_name
    * Added assign_user_to_machine
    * Added unassign_user_to_machine
    * Fixed bug in new_application_pool

28-02-2021
* Inventory Class
    * Applied fix to get_application_pools
    * Added get_global_desktop_entitlements
    * Added get_global_desktop_entitlement
    * Added get_global_desktop_entitlement_compatible_desktop_pools
    * Added add_global_desktop_entitlement_local_desktop_pools
    * Added get_global_desktop_entitlement_local_desktop_pools
    * Added remove_global_desktop_entitlement_local_desktop_pools

02-03-2021
* Inventory class
    * Added get_global_application_entitlement
    * Added get_global_application_entitlements
    * Added get_global_application_entitlement_compatible_application_pools
    * Added get_global_application_entitlement_local_Application_pools
    * Added remove_global_application_entitlement_local_Application_pools
    * Added add_global_application_entitlement_local_Application_pools

03-03-2021
* Entitlements Class
    * Added add_global_desktop_entitlement
    * Added delete_global_desktop_entitlement
    * Added get_global_desktop_entitlement
    * Added get_global_desktop_entitlements

06-03-2021
* Entitlements class
    * Added get_application_pools_entitlement
    * Added get_application_pools_entitlements
    * Added delete_global_application_entitlement
    * Added new_global_application_entitlement
    * renamed add_global_desktop_entitlement to new_global_desktop_entitlement
    * small fixes to add_global_desktop_entitlement and delete_global_desktop_entitlement

07-03-2021
* Added Federation Class
* Federation Class
    * Added get_cloud_pod_federation
    * Added get_home_sites
    * Added get_site
    * Added get_sites

08-03-2021
* federation class
    * Added update_cloud_pod_federation
    * Added get_home_site
    * Added update_site
    * Added delete_site
    * Added new_site

10-03-2021
* federation class
    * Added get_pods
    * Added get_pod
    * Added update_pod

13-03-2021
* federation class
    * Added get_pod_endpoints
    * Added get_pod_endpoint
    * Added get_tasks
    * Added get_task
    * Added join_cpa
    * Added eject_pod

14-03-2021
* federation class
    * Added unjoin_cpa
    * Added initialize_cpa
    * Added uninitialize_cpa
    * Added get_user_home_site
    * Added delete_home_sites
    * Added new_home_site