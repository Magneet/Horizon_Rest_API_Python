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
