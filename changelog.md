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
    * Renamed machine related methods