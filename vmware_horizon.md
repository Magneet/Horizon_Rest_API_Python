Module vmware_horizon
=====================

Classes
-------

`Config(url: str, access_token: dict)`
:   Default object for the config class used for the general configuration of VMware Horizon.

    ### Methods

    `delete_federation_access_group(self, id: str)`
    :   Deletes a federation access group.
        
        Requires id of a federation access group
        Available for Horizon 8 2106 and later.

    `delete_ic_domain_account(self, id: str)`
    :   Removes Instant Clone Domain Account from the environment
        
        Requires id of an Instant CLone Domain account
        Available for Horizon 7.11 and later.

    `delete_im_asset(self, im_asset_id: str)`
    :   Deletes image management asset.
        
        Available for Horizon 7.12 and later.

    `delete_im_stream(self, im_stream_id: str)`
    :   Deletes image management stream.
        
        Available for Horizon 7.12 and later.

    `delete_im_tag(self, im_tag_id: str)`
    :   Deletes image management tag.
        
        Available for Horizon 7.12 and later.

    `delete_im_version(self, im_version_id: str)`
    :   Deletes image management version.
        
        Available for Horizon 7.12 and later.

    `get_environment_properties(self) ‑> dict`
    :   Retrieves the environment settings.
        
        Available for Horizon 7.12 and later.

    `get_federation_access_group(self, id) ‑> dict`
    :   Retrieves a federation access group.
        
        Requires the id of an Instant Clone Admin account to be provided as id
        Available for Horizon 8 2106 and later.

    `get_federation_access_groups(self) ‑> list`
    :   Lists all federation access groups.
        
        Available for Horizon 8 2106 and later.

    `get_ic_domain_account(self, id) ‑> dict`
    :   Gets a single instant clone domain account.
        
        Requires the id of an Instant Clone Admin account to be provided as id
        Available for Horizon 7.11 and later.

    `get_ic_domain_accounts(self) ‑> list`
    :   Lists instant clone domain accounts of the environment.
        
        Available for Horizon 7.11 and later.

    `get_im_asset(self, im_asset_id: str) ‑> dict`
    :   Gets image management asset.
        
        Requires im_version_id  as string
        Available for Horizon 7.12 and later.

    `get_im_assets(self, im_version_id: str) ‑> list`
    :   Lists image management assets.
        
        Requires im_version_id  as string
        Available for Horizon 7.12 and later.

    `get_im_stream(self, im_stream_id: str) ‑> dict`
    :   Gets image management stream.
        
        Available for Horizon 7.12 and later.

    `get_im_streams(self) ‑> list`
    :   Lists image management streams.
        
        Available for Horizon 7.12 and later.

    `get_im_tag(self, im_tag_id: str) ‑> dict`
    :   Gets image management stream.
        
        Available for Horizon 7.12 and later.

    `get_im_tags(self, im_stream_id: str) ‑> list`
    :   Lists image management tags.
        
        Available for Horizon 7.12 and later.

    `get_im_version(self, im_version_id: str) ‑> dict`
    :   Gets image management version.
        
        Available for Horizon 7.12 and later.

    `get_im_versions(self, im_stream_id: str) ‑> list`
    :   Lists image management versions.
        
        Available for Horizon 7.12 and later.

    `get_local_access_group(self, local_access_group_id: str) ‑> dict`
    :   Retrieves a local access group.
        
        Requires the id of an local access group as string
        Available for Horizon 8 2103 and later.

    `get_local_access_groups(self) ‑> list`
    :   Lists all local access groups.
        
        Available for Horizon 8 2103 and later.

    `get_settings(self) ‑> dict`
    :   Retrieves the environment settings.
        
        Available for Horizon 7.12 and later.

    `get_settings_feature(self) ‑> dict`
    :   Retrieves the feature settings.
        
        Available for Horizon 7.12 and later.

    `get_settings_general(self) ‑> dict`
    :   Retrieves the general settings.
        
        Available for Horizon 7.12 and later.

    `get_settings_security(self) ‑> dict`
    :   Retrieves the security settings.
        
        Available for Horizon 7.12 and later.

    `get_virtual_centers(self) ‑> list`
    :   Lists Virtual Centers configured in the environment.
        
        Available for Horizon 7.11 and later.

    `new_federation_access_group(self, name: str, description: str)`
    :   Creates federation access group.
        
        Requires name and description as string
        Available for Horizon 8 2106 and later.

    `new_ic_domain_account(self, ad_domain_id: str, username: str, password: str)`
    :   Creates Instant Clone Domain Account
        
        Requires ad_domain_id, username and password in plain text.
        Available for Horizon 7.11 and later.

    `new_im_asset(self, im_stream_id: str, im_version_id: str, clone_type: str, image_type: str, status: str, vcenter_id: str, additional_details_1: str = '', additional_details_2: str = '', additional_details_3: str = '', base_snapshot_id: str = '', base_vm_id: str = '', vm_template_id: str = '')`
    :   Creates image management asset.
        
        Requires all as string:
            im_stream_id
            im_version_id
            clone_type : either FULL_CLONE or INSTANT_CLONE
            image_type : RDSH_APPS, RDSH_DESKTOP or VDI_DESKTOP"
            status : AVAILABLE, DEPLOYING_VM, DEPLOYMENT_DONE, DELETED, DISABLED, FAILED, REPLICATING, RETRY_PENDING or SPECIALIZING_VM
            vcenter_id
            Choice between:
                base_snapshot_id and base_vm_id
                OR
                vm_template_id
            Optional:
                additional_details_1
                additional_details_2
                additional_details_3
        Available for Horizon 7.12 and later.

    `new_im_stream(self, description: str, name: str, operating_system: str, publisher: str, source: str, status: str, additional_details_1: str = '', additional_details_2: str = '', additional_details_3: str = '')`
    :   Creates image management stream.
        
        Requires all as string:
            description
            name
            operating_system :  UNKNOWN, WINDOWS_XP, WINDOWS_VISTA, WINDOWS_7, WINDOWS_8, WINDOWS_10, WINDOWS_SERVER_2003,
                                WINDOWS_SERVER_2008, WINDOWS_SERVER_2008_R2, WINDOWS_SERVER_2012, WINDOWS_SERVER_2012_R2,
                                WINDOWS_SERVER_2016_OR_ABOVE, LINUX_OTHER, LINUX_SERVER_OTHER, LINUX_UBUNTU, LINUX_RHEL, LINUX_SUSE, LINUX_CENTOS
            status : AVAILABLE, DELETED, DISABLED, FAILED, IN_PROGRESS, PARTIALLY_AVAILABLE, PENDING
            publisher
            source : MARKET_PLACE, UPLOADED, COPIED_FROM_STREAM, COPIED_FROM_VERSION
            Optional:
                additional_details_1
                additional_details_2
                additional_details_3
        Available for Horizon 7.12 and later.

    `new_im_tag(self, name: str, im_stream_id: str, im_version_id: str, additional_details_1: str = '', additional_details_2: str = '', additional_details_3: str = '')`
    :   Creates image management tag.
        
        Requires all as string:
            im_stream_id
            im_version_id
            name
            Optional:
                additional_details_1
                additional_details_2
                additional_details_3
        Available for Horizon 7.12 and later.

    `new_im_version(self, description: str, name: str, im_stream_id: str, status: str, additional_details_1: str = '', additional_details_2: str = '', additional_details_3: str = '')`
    :   Creates image management version.
        
        Requires all as string:
            description
            name
            im_stream_id
            status : AVAILABLE, DEPLOYING_VM, DEPLOYMENT_DONE, DELETED, DISABLED, FAILED, PARTIALLY_AVAILABLE, PUBLISHING, REPLICATING
            Optional:
                additional_details_1
                additional_details_2
                additional_details_3
        Available for Horizon 7.12 and later.

    `update_ic_domain_account(self, id: str, password: str)`
    :   Changes password for an Instant Clone Domain account
        
        Requires id of an Instant CLone Domain account and a plain text password.
        Available for Horizon 7.11 and later.

    `update_im_asset(self, im_asset_id: str, clone_type: str, image_type: str, status: str, additional_details_1: str = '', additional_details_2: str = '', additional_details_3: str = '')`
    :   Updates image management asset.
        
        Requires:
            im_assit_id as string
            clone_type : either FULL_CLONE or INSTANT_CLONE
            image_type : RDSH_APPS, RDSH_DESKTOP or VDI_DESKTOP"
            status : AVAILABLE, DEPLOYING_VM, DEPLOYMENT_DONE, DELETED, DISABLED, FAILED, REPLICATING, RETRY_PENDING or SPECIALIZING_VM
            vcenter_id
            Optional:
                additional_details_1
                additional_details_2
                additional_details_3
        Available for Horizon 7.12 and later.

    `update_im_stream(self, im_stream_id: str, description: str, name: str, operating_system: str, publisher: str, source: str, status: str, additional_details_1: str = '', additional_details_2: str = '', additional_details_3: str = '')`
    :   Updates image management stream.
        
        Requires all as string:
            description
            name
            operating_system :  UNKNOWN, WINDOWS_XP, WINDOWS_VISTA, WINDOWS_7, WINDOWS_8, WINDOWS_10, WINDOWS_SERVER_2003,
                                WINDOWS_SERVER_2008, WINDOWS_SERVER_2008_R2, WINDOWS_SERVER_2012, WINDOWS_SERVER_2012_R2,
                                WINDOWS_SERVER_2016_OR_ABOVE, LINUX_OTHER, LINUX_SERVER_OTHER, LINUX_UBUNTU, LINUX_RHEL, LINUX_SUSE, LINUX_CENTOS
            status : AVAILABLE, DELETED, DISABLED, FAILED, IN_PROGRESS, PARTIALLY_AVAILABLE, PENDING
            publisher
            source : MARKET_PLACE, UPLOADED, COPIED_FROM_STREAM, COPIED_FROM_VERSION
            Optional:
                additional_details_1
                additional_details_2
                additional_details_3
        Available for Horizon 7.12 and later.

    `update_im_tag(self, name: str, im_tag_id: str, im_version_id: str, additional_details_1: str = '', additional_details_2: str = '', additional_details_3: str = '')`
    :   Updates image management tag.
        
        Requires all as string:
            im_tag_id
            im_version_id
            name
            Optional:
                additional_details_1
                additional_details_2
                additional_details_3
        Available for Horizon 7.12 and later.

    `update_im_version(self, description: str, name: str, im_version_id: str, status: str, additional_details_1: str = '', additional_details_2: str = '', additional_details_3: str = '')`
    :   Updates] image management version.
        
        Requires all as string:
            description
            name
            im_stream_id
            status : AVAILABLE, DEPLOYING_VM, DEPLOYMENT_DONE, DELETED, DISABLED, FAILED, PARTIALLY_AVAILABLE, PUBLISHING, REPLICATING
            Optional:
                additional_details_1
                additional_details_2
                additional_details_3
        Available for Horizon 7.12 and later.

    `update_settings(self, settings: dict)`
    :   Updates the settings.
        
        Requires a dictionary with updated settings.
        Available settings can be retreived using get_settings()
        Available for Horizon 7.12 and later.

    `update_settings_feature(self, settings: dict)`
    :   Updates the feature settings.
        
        Requires a dictionary with updated settings.
        Available settings can be retreived using get_settings_feature()
        Available for Horizon 7.12 and later.

    `update_settings_general(self, settings: dict)`
    :   Updates the general settings.
        
        Requires a dictionary with updated settings.
        AVailablke settings can be retreived using get_settings_general()
        Available for Horizon 7.12 and later.

    `update_settings_security(self, settings: dict)`
    :   Updates the security settings.
        
        Requires a dictionary with updated settings.
        Available settings can be retreived using get_settings_security()
        Available for Horizon 7.12 and later.

`Connection(username: str, password: str, domain: str, url: str)`
:   The Connection class is used to handle connections and disconnections to and from the VMware Horizon REST API's
    
    "The default object for the connection class needs to be created using username, password, domain and url in plain text.

    ### Methods

    `hv_connect(self)`
    :   Used to authenticate to the VMware Horizon REST API's

    `hv_disconnect(self)`
    :   "Used to close close the connection with the VMware Horizon REST API's

`Entitlements(url: str, access_token: dict)`
:   Default object for the Entitlements class for the entitlement of resources.

    ### Methods

    `delete_application_pools_entitlements(self, application_pool_data: dict)`
    :   Creates an application pool.
        
        Requires application_pool_data as a dict
        Available for Horizon 8 2006 and later.

    `delete_desktop_pools_entitlements(self, desktop_pools_data: list)`
    :   Delete the bulk entitlements for a set of desktop pools.
        
        Requires desktop_pools_data as a list.
        Available for Horizon 8 2006 and later.

    `delete_global_application_entitlement(self, global_application_entitlement_data: list)`
    :   Delete the bulk entitlements for a set of Global Application Entitlements
        
        Requires global_application_entitlement_data as a dict
        Available for Horizon 8 2012 and later.

    `delete_global_desktop_entitlement(self, global_desktop_entitlement_data: list)`
    :   Delete the bulk entitlements for a set of Global Desktop Entitlements.
        
        Requires global_desktop_entitlement_data as a dict
        Available for Horizon 8 2012 and later.

    `get_application_pool_entitlement(self, application_pool_id: str) ‑> list`
    :   Returns the IDs of users or groups entitled to a given application pool
        
        Requires applictaion_pool_id
        Available for Horizon 8 2006 and later.

    `get_application_pools_entitlements(self, maxpagesize: int = 100, filter: dict = '') ‑> list`
    :   Lists the entitlements for Application Pools in the environment.
        
        Allows for filtering, either application_pool id can be used to filter on id key and or ad_user_or_group_ids can be filtered on.
        Available for Horizon 8 2006 and later.

    `get_desktop_pool_entitlement(self, desktop_pool_id: str) ‑> list`
    :   Returns the IDs of users or groups entitled to a given desktop pool
        
        Requires desktop_pool_id
        Available for Horizon 8 2006 and later.

    `get_desktop_pools_entitlements(self, maxpagesize: int = 100, filter: dict = '') ‑> list`
    :   Lists the entitlements for desktop Pools in the environment.
        
        Allows for filtering, either desktop_pool id can be used to filter on id key and or ad_user_or_group_ids can be filtered on.
        Available for Horizon 8 2006 and later.

    `get_global_application_entitlement(self, global_application_entitlement_id: str) ‑> dict`
    :   Gets the user or group entitlements for a Global Application Entitlement.
        
        Available for Horizon 8 2012 and later.

    `get_global_application_entitlements(self, maxpagesize: int = 100, filter: dict = '') ‑> list`
    :   Lists the user or group entitlements for Global Application Entitlements in the environment.
        
        For information on filtering see https://vdc-download.vmware.com/vmwb-repository/dcr-public/f92cce4b-9762-4ed0-acbd-f1d0591bd739/235dc19c-dabd-43f2-8d38-8a7a333e914e/HorizonServerRESTPaginationAndFilterGuide.doc
        Available for Horizon 8 2012 and later.

    `get_global_desktop_entitlement(self, global_desktop_entitlement_id: str) ‑> dict`
    :   Gets the user or group entitlements for a Global Desktop Entitlement.
        
        Available for Horizon 8 2012 and later.

    `get_global_desktop_entitlements(self, maxpagesize: int = 100, filter: dict = '') ‑> list`
    :   Lists the user or group entitlements for Global Desktop Entitlements in the environment.
        
        For information on filtering see https://vdc-download.vmware.com/vmwb-repository/dcr-public/f92cce4b-9762-4ed0-acbd-f1d0591bd739/235dc19c-dabd-43f2-8d38-8a7a333e914e/HorizonServerRESTPaginationAndFilterGuide.doc
        Available for Horizon 8 2012 and later.

    `new_application_pools_entitlements(self, application_pool_data: dict)`
    :   Creates an application pool.
        
        Requires application_pool_data as a dict
        Available for Horizon 8 2006 and later.

    `new_desktop_pools_entitlements(self, desktop_pools_data: list)`
    :   Create the bulk entitlements for a set of desktop pools.
        
        Requires desktop_pools_data as a list
        Available for Horizon 8 2006 and later.

    `new_global_application_entitlement(self, global_application_entitlement_data: list)`
    :   Create the bulk entitlements for a set of Global Application Entitlements
        
        Requires global_application_entitlement_data as a dict
        Available for Horizon 8 2012 and later.

    `new_global_desktop_entitlement(self, global_desktop_entitlement_data: list)`
    :   Create the bulk entitlements for a set of Global Desktop Entitlements.
        
        Requires global_desktop_entitlement_data as a dict
        Available for Horizon 8 2012 and later.

`External(url: str, access_token: dict)`
:   Default object for the External class for resources that are external to Horizon environment.

    ### Methods

    `compute_datastore_requirement(self, desktop_or_farm_id: str, user_assignment: str, vcenter_id: str, pool_size: int, source: str, type: str, base_snapshot_id: str = '', base_vm_id: str = '', use_separate_replica_and_os_disk: bool = False, use_vsan: bool = False, vm_template_id: str = '') ‑> list`
    :   Creates Instant Clone Domain Account
        
        Requirements:
        base_snapshot_id : str - Required when source is INSTANT_CLONE
        base_vm_id : string - Required when source is INSTANT_CLONE
        desktop_or_farm_id: string
        pool_size : int32
        source : string - Required to be either FULL_CLONE or INSTANT_CLONE
        type : string - Required to be DESKTOP_POOL or FARM
        use_separate_replica_and_os_disk : boolean - Ignored for FULL_CLONE or when vSAN is used, defaults to False
        use_vsan : boolean - defaults to False
        user_assignment : string - Required to be DEDICATED or FLOATING
        vcenter_id : string
        vm_template_id : string - Required when source is FULL_CLONE
        
        Available for Horizon 8 2103 and later.

    `delete_auxiliary_account(self, domain_id: str, auxiliary_account_ids: list)`
    :   deletes auxiliary accounts from the untrusted domain
        
        Requires domain_id as string and auxiliary_account_ids as a list
        Available for Horizon 8 2106 and later.

    `get_ad_domains(self) ‑> list`
    :   Lists information related to AD Domains of the environment.
        
        Available for Horizon 7.11 and later.

    `get_ad_domains_v3(self) ‑> list`
    :   Lists information related to AD Domains of the environment.
        
        Available for Horizon 8 2106 and later.

    `get_ad_users_or_group(self, id) ‑> dict`
    :   Get information related to AD User or Group.
        
        Requires id of the user object
        Available for Horizon 7.12 and later.

    `get_ad_users_or_groups(self, maxpagesize: int = 100, filter: dict = '', group_only: bool = '') ‑> list`
    :   Lists AD users or groups information
        
        If group_only is passed as True only groups are returned, if users_only is passed as False only users are returned. If both are passed a True an error will be raised.
        Supports pagination and filtering
        Available for Horizon 7.12 and later.

    `get_audit_events(self, filter: dict = '', maxpagesize: int = 100) ‑> list`
    :   Lists the audit events.
        
        Requires nothing
        Available for Horizon 8 2106 and later.

    `get_base_snapshots(self, vcenter_id: str, base_vm_id: str) ‑> list`
    :   Lists all the VM snapshots from the vCenter for a given VM.
        
        Requires vcenter_id and base_vm_id
        Available for Horizon 8 2006.

    `get_base_vms(self, vcenter_id: str, filter_incompatible_vms: bool = '', datacenter_id: str = '') ‑> list`
    :   Lists all the VMs from a vCenter or a datacenter in that vCenter which may be suitable as snapshots for instant/linked clone desktop or farm creation.
        
        Requires vcenter_id, optionally datacenter id and since Horizon 2012 filter_incompatible_vms was added (defaults to false)
        Available for Horizon 7.12 and later and Horizon 8 2012 for filter_incompatible_vms.

    `get_customization_specifications(self, vcenter_id: str) ‑> list`
    :   Lists all the customization specifications from the vCenter.
        
        Requires vcenter_id
        Available for Horizon 8 2006.

    `get_datacenters(self, vcenter_id: str) ‑> list`
    :   Lists all the datacenters of a vCenter.
        
        Requires vcenter_id
        Available for Horizon 7.12 and later.

    `get_datastore_clusters(self, vcenter_id: str, host_or_cluster_id: str) ‑> list`
    :   Lists all the datastore clusters from the vCenter for the given host or cluster.
        
        Requires host_or_cluster_id and vcenter_id
        Available for Horizon 8 2103 and later.

    `get_datastore_paths(self, vcenter_id: str, datastore_id: str) ‑> list`
    :   Lists all the folder paths within a Datastore from vCenter.
        
        Requires datastore_id and vcenter_id
        Available for Horizon 8 2006 and later.

    `get_datastores(self, vcenter_id: str, host_or_cluster_id: str) ‑> list`
    :   Lists all the datastoress from the vCenter for the given host or cluster.
        
        Requires host_or_cluster_id and vcenter_id
        Available for Horizon 8 2006 and later.

    `get_hosts_or_clusters(self, vcenter_id: str, datacenter_id: str) ‑> list`
    :   Lists all the hosts or clusters of the datacenter.
        
        Requires vcenter_id and datacenter id
        Available for Horizon 7.12 and later.

    `get_network_interface_cards(self, vcenter_id: str, base_snapshot_id: str = '', base_vm_id: str = '', vm_template_id: str = '') ‑> list`
    :   Returns a list of network interface cards (NICs) suitable for configuration on a desktop pool/farm.
        
        Requires vcenter_id and either vm_template_id or (base_vm_id and base_snapshot_id).
        Available for Horizon 8 2006 and later.

    `get_network_labels(self, vcenter_id: str, host_or_cluster_id: str, network_type: str = '') ‑> list`
    :   Retrieves all network labels on the given host or cluster.
        
        Requires host_or_cluster_id, vcenter_id and optionally a network type.
        Valid options for network_type are: NETWORK, OPAQUE_NETWORK, DISTRUBUTED_VIRTUAL_PORT_GROUP
        Available for Horizon 8 2006 and later.

    `get_resource_pools(self, vcenter_id: str, host_or_cluster_id: str) ‑> list`
    :   Lists all the resource pools from the vCenter for the given host or cluster.
        
        Requires host_or_cluster_id and vcenter_id.
        Available for Horizon 8 2006 and later.

    `get_virtual_machines(self, vcenter_id: str) ‑> list`
    :   Lists all the VMs from a vCenter.
        
        Requires datacenter_id and vcenter_id.
        Available for Horizon 8 2006 and later.

    `get_vm_folders(self, vcenter_id: str, datacenter_id: str) ‑> list`
    :   Lists all the VM folders from the vCenter for the given datacenter.
        
        Requires datacenter_id and vcenter_id.
        Available for Horizon 8 2006 and later.

    `get_vm_templates(self, vcenter_id: str, datacenter_id: str = '') ‑> list`
    :   Lists all the VM templates from a vCenter or a datacenter for the given vCenter which may be suitable for full clone desktop pool creation.
        
        Requires vcenter_id and datacenter id
        Available for Horizon 7.12 and later.

    `new_auxiliary_account(self, domain_id: str, username: str, password: str)`
    :   Add auxiliary accounts to the untrusted domain
        
        Requires domain_id, username and password as string
        Available for Horizon 8 2106 and later.

    `update_auxiliary_account(self, auxiliary_account_id: str, password: str)`
    :   updates auxiliary accounts of the untrusted domain
        
        Requires auxiliary_account_id and password as string
        Available for Horizon 8 2106 and later.

`Federation(url: str, access_token: dict)`
:   Default object for the pools class where all Desktop Pool Actions will be performed.

    ### Methods

    `delete_home_sites(self, homesite_ids: list) ‑> list`
    :   Creates the given home site in the pod federation.
        
        Requires ad_user_or_group_id, global_application_entitlement_id, global_desktop_entitlement_id, site_id as strings
        Available for Horizon 8 2012 and later.

    `delete_site(self, site_id: str)`
    :   Retrives a given site.
        
        Available for Horizon 8 2012 and later.

    `eject_pod(self, pod_id: str)`
    :   Removes a pod from Cloud Pod Federation.
        
        Requires pod_id as a string
        Available for Horizon 8 2012 and later.

    `get_cloud_pod_federation(self) ‑> dict`
    :   Retrieves the pod federation details.
        
        Available for Horizon 8 2012 and later.

    `get_home_site(self, home_site_id: str) ‑> dict`
    :   Retrieves a given home site in the pod federation.
        
        Requires a home_site_id as a string
        Available for Horizon 8 2012 and later.

    `get_home_sites(self, maxpagesize: int = 100, filter: dict = '') ‑> list`
    :   Lists all the home sites in the pod federation.
        
        For information on filtering see https://vdc-download.vmware.com/vmwb-repository/dcr-public/f92cce4b-9762-4ed0-acbd-f1d0591bd739/235dc19c-dabd-43f2-8d38-8a7a333e914e/HorizonServerRESTPaginationAndFilterGuide.doc
        Available for Horizon 8 2012 and later.

    `get_pod(self, pod_id: str) ‑> dict`
    :   Retrieves a given pod from the pod federation.
        
        Requires pod_id as a string
        Available for Horizon 8 2012 and later.

    `get_pod_endpoint(self, pod_id: str, endpoint_id: str) ‑> dict`
    :   Lists all the pod endpoints for the given pod.
        
        Requires pod_id and endpoint_id as a string
        Available for Horizon 8 2012 and later.

    `get_pod_endpoints(self, pod_id: str) ‑> list`
    :   Lists all the pod endpoints for the given pod.
        
        Requires pod_id as a string
        Available for Horizon 8 2012 and later.

    `get_pods(self) ‑> list`
    :   Lists all the pods in the pod federation.
        
        Available for Horizon 8 2012 and later.

    `get_site(self, site_id: str) ‑> dict`
    :   Retrives a given site.
        
        Available for Horizon 8 2012 and later.

    `get_sites(self) ‑> list`
    :   Lists all the sites in the pod federation.
        
        Available for Horizon 8 2012 and later.

    `get_task(self, task_id: str) ‑> dict`
    :   Retrieves the information for a given task.
        
        Available for Horizon 8 2012 and later.

    `get_tasks(self) ‑> list`
    :   Lists all the CPA tasks in the pod federation.
        
        Available for Horizon 8 2012 and later.

    `get_user_home_site(self, user_id: str, global_application_entitlement_id: str = '', global_desktop_entitlement_id: str = '') ‑> list`
    :   Creates the given home site in the pod federation.
        
        Requires global_application_entitlement_id, global_desktop_entitlement_id, user_id as strings
        Available for Horizon 8 2012 and later.

    `initialize_cpa(self) ‑> dict`
    :   Initialize Cloud Pod Federation.
        
        Available for Horizon 8 2012 and later.

    `join_cpa(self, remote_pod_address: str, username: str, password: str) ‑> dict`
    :   Join Cloud Pod Federation.
        
        Requires remote_pod_address (fqdn), username (domain\username) and password as str
        Available for Horizon 8 2012 and later.

    `new_home_site(self, ad_user_or_group_id: str, global_application_entitlement_id: str, global_desktop_entitlement_id: str, site_id: str) ‑> list`
    :   Creates the given home site in the pod federation.
        
        Requires ad_user_or_group_id, global_application_entitlement_id, global_desktop_entitlement_id, site_id as strings
        Available for Horizon 8 2012 and later.

    `new_site(self, name: str, description: str)`
    :   creates a site.
        
        Requires the name and description as strings
        Available for Horizon 8 2012 and later.

    `uninitialize_cpa(self) ‑> dict`
    :   Initialize Cloud Pod Federation.
        
        Available for Horizon 8 2012 and later.

    `unjoin_cpa(self) ‑> dict`
    :   Initialize Cloud Pod Federation.
        
        Available for Horizon 8 2012 and later.

    `update_cloud_pod_federation(self, name: str)`
    :   Updates a Pod Federation
        
        Requires a new name of the cpa as a string
        Available for Horizon 8 2012 and later.

    `update_pod(self, pod_id: str, description: str, site_id: str, name: str, cloud_managed: bool = '')`
    :   Updates the given pod in the pod federation.
        
        Requires pod_id, site_id, the name and description as strings, cloud_managed needs to be a bool
        Available for Horizon 8 2012 and later.

    `update_site(self, site_id: str, name: str, description: str)`
    :   Updates a site.
        
        Requires site_id, the name and description as strings
        Available for Horizon 8 2012 and later.

`Inventory(url: str, access_token: dict)`
:   Default object for the pools class where all Desktop Pool Actions will be performed.

    ### Methods

    `add_global_application_entitlement_local_Application_pools(self, global_application_entitlement_id: str, application_pool_ids: list)`
    :   Adds a local Application pool to a GLobal Application Entitlement
        
        Requires global_application_entitlement_id as a string and application_pool_ids as a list
        Available for Horizon 8 2012 and later.

    `add_global_desktop_entitlement(self, global_desktop_entitlement_data: dict)`
    :   Creates a Global Desktop Entitlement.
        
        Requires global_desktop_entitlement_data as a dict
        Available for Horizon 8 2006 and later.

    `add_global_desktop_entitlement_local_desktop_pools(self, global_desktop_entitlement_id: str, desktop_pool_ids: list)`
    :   Adds a local desktop pool to a GLobal desktop Entitlement
        
        Requires global_desktop_entitlement_id as a string and desktop_pool_ids as a list
        Available for Horizon 8 2012 and later.

    `add_machines(self, desktop_pool_id: str, machine_ids: list)`
    :   Adds machines to the given manual desktop pool.
        
        Requires list of machine_ids and desktop_pool_id to add them to
        Available for Horizon 8 2006 and later.

    `add_machines_by_name(self, desktop_pool_id: str, machine_data: list)`
    :   Adds machines to the given manual desktop pool.
        
        Requires requires desktop_pool_id and list of of dicts where each dict has name and user_id.
        Available for Horizon 8 2006 and later.

    `add_physical_machine(self, description: str, dns_name: str, operating_system: str)`
    :   Registers the Physical Machine.
        
        Requires ad_domain_id, username and password in plain text.
        Available for Horizon 7.11 and later.

    `add_rds_server(self, description: str, dns_name: str, operating_system: str, farm_id: str)`
    :   Registers the RDS Server.
        
        Requires description, dns_name, operating_system and farm_id as string
        Available for Horizon 8 2012 and later.

    `assign_user_to_machine(self, machine_id: str, user_ids: list)`
    :   Assigns the specified users to the machine.
        
        Requires machine_id of the machine and list of user_ids.
        Available for Horizon 8 2006 and later.

    `cancel_desktop_pool_push_image(self, desktop_pool_id: str)`
    :   Lists Local Application Pools which are assigned to Global Application Entitlement.
        
        Available for Horizon 8 2012 and later.

    `cancel_desktop_pool_task(self, desktop_pool_id: str, task_id: str) ‑> dict`
    :   Cancels the instant clone desktop pool push image task.
        
        Available for Horizon 8 2012 and later.

    `check_application_name_availability(self, application_name: str) ‑> dict`
    :   Checks if the given name is available for application pool creation.
        
        Requires the name of the application to test as string
        Available for Horizon 8 2103 and later.

    `check_desktop_pool_name_availability(self, desktop_pool_name: str) ‑> dict`
    :   Checks if the given name is available for desktop pool creation.
        
        Requires the name of the desktop pool to test as string
        Available for Horizon 8 2103 and later.

    `check_farm_name_availability(self, farm_name: str) ‑> dict`
    :   Checks if the given name is available for farm creation.
        
        Requires the name of the farm to test as string
        Available for Horizon 8 2103 and later.

    `check_machine_name_availability(self, machine_name: str) ‑> dict`
    :   Checks if the given name is available for machine creation.
        
        Requires the name of the application to test as string
        Available for Horizon 8 2103 and later.

    `check_rds_server_name_availability(self, machine_name: str) ‑> dict`
    :   Checks if the given prefix is available for RDS Server creation.
        
        Requires the name of the RDS Server to test as string
        Available for Horizon 8 2103 and later.

    `delete_application_pool(self, application_pool_id: str)`
    :   Deletes an application pool.
        
        Requires application_pool_id as a str
        Available for Horizon 8 2006 and later.

    `delete_application_pool_icon(self, application_pool_id: str)`
    :   Removes the associated custom icon from the application pool.
        
        Requires application_pool_id as string
        Available for Horizon 8 2103 and later.

    `delete_farm(self, farm_id: str) ‑> list`
    :   Deletes a farm.
        
        Requires id of a RDS Farm
        Available for Horizon 8 2103 and later.

    `delete_machine(self, machine_id: str, delete_from_multiple_pools: bool = False, force_logoff: bool = False, delete_from_disk: bool = False)`
    :   Deletes a machine.
        
        Requires id of the machine to delete machine
        Optional arguments (all default to False): delete_from_multiple_pools, force_logoff and delete_from_disk
        Available for Horizon 7.12 and later.

    `delete_machines(self, machine_ids: list, delete_from_multiple_pools: bool = False, force_logoff: bool = False, delete_from_disk: bool = False)`
    :   deletes the specified machines
        
        Requires list of ids of the machines to remove 
        Optional arguments (all default to False): delete_from_multiple_pools, force_logoff and delete_from_disk
        Available for Horizon 8 2006 and later.

    `delete_physical_machine(self, physical_machine_id: str)`
    :   Deletes the Physical Machine.
        
        Available for Horizon 8 2012 and later.

    `delete_rds_server(self, rds_server_id: str) ‑> dict`
    :   Deletes the RDS Server.
        
        Available for Horizon 8 2012 and later.

    `desktop_pool_push_image(self, desktop_pool_id: str, start_time: str, add_virtual_tpm: bool = False, im_stream_id: str = '', im_tag_id: str = '', logoff_policy: str = 'WAIT_FOR_LOGOFF', parent_vm_id: str = '', snapshot_id: str = '', stop_on_first_error: bool = True)`
    :   Schedule/reschedule a request to update the image in an instant clone desktop pool
        
        Requires start_time in epoch, desktop_pool_id as string and either im_stream_id and im_tag_id OR parent_vm_id and snapshit_id as string.
        Optional: stop_on_first_error as bool, add_virtual_tpm as bool, logoff_policy as string with these options: FORCE_LOGOFF or WAIT_FOR_LOGOFF
        Available for Horizon 8 2012 and later.

    `disconnect_sessions(self, session_ids: list)`
    :   Disconnects user sessions.
        
        Requires list of session ids
        Available for Horizon 8 2006 and later.

    `get_application_icon(self, application_icon_id: str) ‑> dict`
    :   Gets application icon
        
        Requires application_icon_id
        Available for Horizon 8 2006 and later.

    `get_application_icons(self, application_pool_id: str) ‑> list`
    :   Lists the application icons for the given application pool.
        
        Requires Application_pool_id
        Available for Horizon 8 2006 and later.

    `get_application_pool(self, application_pool_id: str) ‑> dict`
    :   Gets a single Application pool
        
        Requires Application_pool_id
        Available for Horizon 8 2006 and later.

    `get_application_pools(self, maxpagesize: int = 100, filter: dict = '') ‑> list`
    :   Lists the application pools in the environment.
        
        For information on filtering see https://vdc-download.vmware.com/vmwb-repository/dcr-public/f92cce4b-9762-4ed0-acbd-f1d0591bd739/235dc19c-dabd-43f2-8d38-8a7a333e914e/HorizonServerRESTPaginationAndFilterGuide.doc
        Available for Horizon 8 2006 and later.

    `get_desktop_pool(self, desktop_pool_id: str) ‑> dict`
    :   Gets the Desktop Pool information.
        
        Requires id of a desktop pool
        Available for Horizon 7.12 and later.

    `get_desktop_pool_installed_applications(self, desktop_pool_id: str) ‑> list`
    :   Lists the installed applications on the given desktop pool.
        
        Requires id of a desktop pool
        Available for Horizon 8 2006 and later.

    `get_desktop_pool_task(self, desktop_pool_id: str, task_id: str) ‑> dict`
    :   Gets the task information on the desktop pool.
        
        Available for Horizon 8 2012 and later.

    `get_desktop_pool_tasks(self, desktop_pool_id: str) ‑> list`
    :   Lists the tasks on the desktop pool.
        
        Available for Horizon 8 2012 and later.

    `get_desktop_pools(self) ‑> list`
    :   Returns a list of dictionaries with all available Desktop Pools. 
        
        Available for Horizon 7.12 and later.

    `get_farm(self, farm_id: str) ‑> dict`
    :   Gets the Farm information.
        
        Requires id of a RDS Farm
        Available for Horizon 7.12 and later.

    `get_farm_installed_applications(self, farm_id: str) ‑> list`
    :   Lists the installed applications on the given farm.
        
        Requires id of a RDS Farm
        Available for Horizon 7.12 and later.

    `get_farms(self) ‑> list`
    :   Lists the Farms in the environment.
        
        Available for Horizon 7.12 and later.

    `get_global_application_entitlement(self, global_application_entitlement_id: str) ‑> dict`
    :   Gets the Global Application Entitlement in the environment.
        
        Available for Horizon 8 2012 and later.

    `get_global_application_entitlement_compatible_application_pools(self, global_application_entitlement_id: str) ‑> list`
    :   Lists Local Application Pools which are compatible with Global Application Entitlement.
        
        Available for Horizon 8 2012 and later.

    `get_global_application_entitlement_local_Application_pools(self, global_application_entitlement_id: str) ‑> list`
    :   Lists Local Application Pools which are assigned to Global Application Entitlement.
        
        Available for Horizon 8 2012 and later.

    `get_global_application_entitlements(self, maxpagesize: int = 100, filter: dict = '') ‑> list`
    :   Lists the Global Application Entitlements in the environment.
        
        For information on filtering see https://vdc-download.vmware.com/vmwb-repository/dcr-public/f92cce4b-9762-4ed0-acbd-f1d0591bd739/235dc19c-dabd-43f2-8d38-8a7a333e914e/HorizonServerRESTPaginationAndFilterGuide.doc
        Available for Horizon 8 2006 and later.

    `get_global_desktop_entitlement(self, global_desktop_entitlement_id: str) ‑> dict`
    :   Gets the Global Desktop Entitlement in the environment.
        
        Available for Horizon 8 2012 and later.

    `get_global_desktop_entitlement_compatible_desktop_pools(self, global_desktop_entitlement_id: str) ‑> list`
    :   Lists Local Application Pools which are compatible with Global Application Entitlement.
        
        Available for Horizon 8 2012 and later.

    `get_global_desktop_entitlement_local_desktop_pools(self, global_desktop_entitlement_id: str) ‑> list`
    :   Lists Local Desktop Pools which are assigned to Global Desktop Entitlement.
        
        Available for Horizon 8 2012 and later.

    `get_global_desktop_entitlements(self, maxpagesize: int = 100, filter: dict = '') ‑> list`
    :   Lists the Global Application Entitlements in the environment.
        
        For information on filtering see https://vdc-download.vmware.com/vmwb-repository/dcr-public/f92cce4b-9762-4ed0-acbd-f1d0591bd739/235dc19c-dabd-43f2-8d38-8a7a333e914e/HorizonServerRESTPaginationAndFilterGuide.doc
        Available for Horizon 8 2006 and later.

    `get_machine(self, machine_id: str) ‑> dict`
    :   Gets the Machine information.
        
        Requires id of a machine
        Available for Horizon 7.12 and later.

    `get_machines(self, maxpagesize: int = 100, filter: dict = '') ‑> list`
    :   Lists the Machines in the environment.
        
        For information on filtering see https://vdc-download.vmware.com/vmwb-repository/dcr-public/f92cce4b-9762-4ed0-acbd-f1d0591bd739/235dc19c-dabd-43f2-8d38-8a7a333e914e/HorizonServerRESTPaginationAndFilterGuide.doc
        Available for Horizon 8 2006 and later.

    `get_physical_machine(self, physical_machine_id: str) ‑> dict`
    :   Gets the Physical Machine information.
        
        Available for Horizon 8 2012 and later.

    `get_physical_machines(self, maxpagesize: int = 100, filter: dict = '') ‑> list`
    :   Lists the Physical Machines in the environment.
        
        For information on filtering see https://vdc-download.vmware.com/vmwb-repository/dcr-public/f92cce4b-9762-4ed0-acbd-f1d0591bd739/235dc19c-dabd-43f2-8d38-8a7a333e914e/HorizonServerRESTPaginationAndFilterGuide.doc
        Available for Horizon 8 2012 and later.

    `get_rds_server(self, rds_server_id: str) ‑> dict`
    :   Gets the RDS Server information.
        
        Available for Horizon 8 2012 and later.

    `get_rds_servers(self, maxpagesize: int = 100, filter: dict = '') ‑> list`
    :   Lists the RDS Servers in the environment.
        
        For information on filtering see https://vdc-download.vmware.com/vmwb-repository/dcr-public/f92cce4b-9762-4ed0-acbd-f1d0591bd739/235dc19c-dabd-43f2-8d38-8a7a333e914e/HorizonServerRESTPaginationAndFilterGuide.doc
        Available for Horizon 8 2012 and later.

    `get_session(self, session_id: str) ‑> dict`
    :   Gets the Session information.
        
        Requires session_id
        Available for Horizon 8 2006 and later.

    `get_sessions(self, filter: dict = '', maxpagesize: int = 100) ‑> list`
    :   Lists the Session information in the environment.
        
        Will default to 1000 results with a pagesize of 100, max pagesize is 1000.
        Available for Horizon 8 2006 and later, filtering available since Horizon 2103.

    `logoff_sessions(self, session_ids: list, forced_logoff: bool = False)`
    :   Logs user sessions off.
        
        Requires list of session ids optional to set forced to True to force a log off (defaults to False)
        Available for Horizon 8 2006 and later.

    `machines_enable_maintenance_mode(self, machine_ids: list)`
    :   Puts a machine in maintenance mode.
        
        Requires a List of Machine Ids representing the machines to be put into maintenance mode.
        Available for Horizon 8 2006 and later.

    `machines_exit_maintenance_mode(self, machine_ids: list)`
    :   Takes a machine out of maintenance mode.
        
        Requires a List of Machine Ids representing the machines to be taken out of maintenance mode.
        Available for Horizon 8 2006 and later.

    `new_application_icon(self, data: str, height: str, width: str) ‑> dict`
    :   Creates an application icon.
        
        Requires data, width and height as string
        Data needs to be Base64 encoded binary data of the image
        Available for Horizon 8 2103 and later.

    `new_application_pool(self, application_pool_data: dict)`
    :   Creates an application pool.
        
        Requires application_pool_data as a dict
        Available for Horizon 8 2006 and later.

    `new_farm(self, farm_data: dict)`
    :   Creates a farm.
        
        Requires farm_data as a dict
        Available for Horizon 8 2103 and later.

    `rebuild_machines(self, machine_ids: list)`
    :   Rebuilds the specified machines.
        
        Requires a List of Machine Ids representing the machines to be rebuild.
        Available for Horizon 8 2006 and later.

    `recover_machines(self, machine_ids: list)`
    :   Recovers the specified machines.
        
        Requires a List of Machine Ids representing the machines to be recovered.
        Available for Horizon 8 2006 and later.

    `recover_rds_servers(self, rds_server_ids: list) ‑> list`
    :   Recovers the specified RDS Servers.
        
        Available for Horizon 8 2012 and later.

    `remove_global_application_entitlement_local_Application_pools(self, global_application_entitlement_id: str, application_pool_ids: list)`
    :   Removes Local Application Pools from Global Application Entitlement.
        
        Requires global_application_entitlement_id as a string and application_pool_ids as a list
        Available for Horizon 8 2012 and later.

    `remove_global_desktop_entitlement_local_desktop_pools(self, global_desktop_entitlement_id: str, desktop_pool_ids: list)`
    :   Removes Local Desktop Pools from Global Desktop Entitlement.
        
        Requires global_desktop_entitlement_id as a string and desktop_pool_ids as a list
        Available for Horizon 8 2012 and later.

    `remove_machines(self, desktop_pool_id: str, machine_ids: list)`
    :   Removes machines from the given manual desktop pool.
        
        Requires list of machine_ids and desktop_pool_id to remove them from
        Available for Horizon 8 2006 and later.

    `reset_machines(self, machine_ids: list)`
    :   Resets the specified machines.
        
        Requires a List of Machine Ids representing the machines to be reset.
        Available for Horizon 8 2006 and later.

    `reset_session_machines(self, session_ids: list)`
    :   Resets machine of user sessions. The machine must be managed by Virtual Center and the session cannot be an application or an RDS desktop session.
        
        Requires list of session ids
        Available for Horizon 8 2006 and later.

    `restart_machines(self, machine_ids: list)`
    :   Restarts the specified machines.
        
        Requires a List of Machine Ids representing the machines to be restarted.
        Available for Horizon 8 2006 and later.

    `restart_session_machines(self, session_ids: list)`
    :   Restarts machine of user sessions. The machine must be managed by Virtual Center and the session cannot be an application or an RDS desktop session.
        
        Requires list of session ids
        Available for Horizon 8 2006 and later.

    `send_message_sessions(self, session_ids: list, message: str, message_type: str = 'INFO')`
    :   Sends the message to user sessions
        
        Requires list of session ids, message type (INFO,WARNING,ERROR) and a message
        Available for Horizon 8 2006 and later.

    `set_application_pool_icon(self, application_pool_id: str, icon_id: str)`
    :   Associates a custom icon to the application pool.
        
        Requires application_pool_id and asicon_id as string
        Available for Horizon 8 2103 and later.

    `unassign_user_to_machine(self, machine_id: str, user_ids: list)`
    :   Unassigns the specified users to the machine.
        
        Requires machine_id of the machine and list of user_ids.
        Available for Horizon 8 2006 and later.

    `update_application_pool(self, application_pool_id: str, application_pool_data: dict)`
    :   Updates an application pool.
        
        The following keys are required to be present in the json: multi_session_mode, executable_path and enable_pre_launch
        Requires ad_domain_id, username and password in plain text.
        Available for Horizon 8 2006 and later.

    `update_farm(self, farm_data: dict, farm_id: str)`
    :   Updates a farm.
        
        Requires farm_data as a dict
        Available for Horizon 8 2103 and later.

    `update_rds_server(self, rds_server_id: str, max_sessions_count_configured: int, max_sessions_type_configured: str, enabled: bool = True)`
    :   Schedule/reschedule a request to update the image in an instant clone desktop pool
        
        Requires the rds_server_id as string, enabled as booleanm max_sessions_count_configured as int and max_sessions_type_configured as string
        enabled defaults to True, the options for max_sessions_type_configured are: UNLIMITED, LIMITED, UNCONFIGURED
        Available for Horizon 8 2012 and later.

`Monitor(url: str, access_token: dict)`
:   Default object for the monitor class used for the monitoring of the various VMware Horiozn services.

    ### Methods

    `ad_domains(self) ‑> list`
    :   Lists monitoring information related to AD Domains of the environment.
        
        Available for Horizon 7.10 and later.

    `connection_server(self, id: str) ‑> dict`
    :   Lists monitoring information related to a single Connection Server.
        
        Requires the id of a Connection Server to be provided as id
        Available for Horizon 8 2006 and later.

    `connection_servers(self) ‑> list`
    :   Lists monitoring information related to Connection Servers of the environment.
        
        Available for Horizon 7.10 and later.

    `event_database(self) ‑> dict`
    :   Returns monitoring information related to Event database of the environment.
        
        Available for Horizon 7.10 and later.

    `farm(self, id: str) ‑> dict`
    :   Lists monitoring information related to a single RDS Farm.
        
        Requires the id of a farm to be provided as id
        Available for Horizon 8 2006 and later.

    `farms(self) ‑> list`
    :   Lists monitoring information related to RDS Farms of the environment.
        
        Available for Horizon 7.10 and later.

    `gateway(self, id: str) ‑> dict`
    :   Lists monitoring information related to a single gateway.
        
        Requires the id of a Gateway to be provided as id
        Available for Horizon 8 2006 and later.

    `gateways(self) ‑> list`
    :   Lists monitoring information related to Gateways registered in the environment.
        
        Available for Horizon 7.10 and later.

    `get_desktop_pool_metrics(self, desktop_pool_ids: list) ‑> list`
    :   Lists metrics of desktop pools (except RDS desktop pools).
        
        Available for Horizon 8 2012 and later.

    `rds_server(self, id: str) ‑> dict`
    :   Lists monitoring information related to a single RDS Server.
        
        Requires the id of a RDS Server to be provided as id
        Available for Horizon 8 2006 and later.

    `rds_servers(self) ‑> list`
    :   Lists monitoring information related to RDS Servers of the environment.
        
        Available for Horizon 7.10 and later.

    `remote_pod(self, id: str) ‑> dict`
    :   Lists monitoring information related to a single remote pod.
        
        Requires the id of a Remote Pod to be provided as id
        Only available for Horizon 8 2006 and later.

    `remote_pods(self) ‑> list`
    :   Lists monitoring information related to the remote pods.
        
        Available for Horizon 7.11 and later.

    `saml_authenticator(self, id: str) ‑> dict`
    :   Lists monitoring information related to a single SAML Authenticator.
        
        Requires the id of a SAML Authenticator to be provided as id
        Available for Horizon 8 2006 and later.

    `saml_authenticators(self) ‑> list`
    :   Lists monitoring information related to SAML Authenticators of the environment.
        
        Available for Horizon 7.10 and later.

    `true_sso(self) ‑> list`
    :   Lists monitoring information related to True SSO connectors.
        
        Available for Horizon 7.11 and later.

    `view_composer(self, vcId: str)`
    :   Lists monitoring information related to a single View Composers.
        
        Requires the id of a Virtual Center to be provided as vcId
        Only available for Horizon 8 2006.

    `view_composers(self) ‑> list`
    :   Lists monitoring information related to View Composers of the environment.
        
        Available for Horizon 7.10 to Horizon 8 2006.

    `virtual_center(self, id: str) ‑> dict`
    :   Lists monitoring information related to a single Virtual Center.
        
        Requires the id of a Virtual Center to be provided as id
        Only available for Horizon 8 2006 and later.

    `virtual_centers(self) ‑> list`
    :   Lists monitoring information related to Virtual Centers of the environment.
        
        Available for Horizon 7.10 and later.
