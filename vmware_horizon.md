Module vmware_horizon
=====================

Classes
-------

`Config(url: str, access_token: dict)`
:   Default object for the config class used for the general configuration of VMware Horizon.

    ### Methods

    `delete_ic_domain_account(self, id: str)`
    :   Removes Instant Clone Domain Account from the environment
        
        Requires id of an Instant CLone Domain account
        Available for Horizon 7.11 and later.

    `get_environment_properties(self) ‑> dict`
    :   Retrieves the environment settings.
        
        Available for Horizon 7.12 and later.

    `get_ic_domain_account(self, id) ‑> dict`
    :   Gets a single instant clone domain account.
        
        Requires the id of an Instant Clone Admin account to be provided as id
        Available for Horizon 7.11 and later.

    `get_ic_domain_accounts(self) ‑> list`
    :   Lists instant clone domain accounts of the environment.
        
        Available for Horizon 7.11 and later.

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

    `new_ic_domain_account(self, ad_domain_id: str, username: str, password: str)`
    :   Creates Instant Clone Domain Account
        
        Requires ad_domain_id, username and password in plain text.
        Available for Horizon 7.11 and later.

    `update_ic_domain_account(self, id: str, password: str)`
    :   Changes password for an Instant Clone Domain account
        
        Requires id of an Instant CLone Domain account and a plain text password.
        Available for Horizon 7.11 and later.

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

`External(url: str, access_token: dict)`
:   Default object for the External class for resources that are external to Horizon environment.

    ### Methods

    `get_ad_domains(self) ‑> list`
    :   Lists information related to AD Domains of the environment.
        
        Available for Horizon 7.11 and later.

    `get_base_vms(self, vcenter_id: str, filter_incompatible_vms: bool = '', datacenter_id: str = '') ‑> list`
    :   Lists all the VMs from a vCenter or a datacenter in that vCenter which may be suitable as snapshots for instant/linked clone desktop or farm creation.
        
        Requires vcenter_id, optionally datacenter id and since Horizon 2012 filter_incompatible_vms was added (defaults to false)
        Available for Horizon 7.12 and later and Horizon 8 2012 for filter_incompatible_vms.

    `get_datacenters(self, vcenter_id: str) ‑> list`
    :   Lists all the datacenters of a vCenter.
        
        Requires vcenter_id
        Available for Horizon 7.12 and later.

    `get_hosts_or_clusters(self, vcenter_id: str, datacenter_id: str = '') ‑> list`
    :   Lists all the hosts or clusters of the datacenter.
        
        Requires vcenter_id and datacenter id
        Available for Horizon 7.12 and later.

    `get_vm_templates(self, vcenter_id: str, datacenter_id: str = '') ‑> list`
    :   Lists all the VM templates from a vCenter or a datacenter for the given vCenter which may be suitable for full clone desktop pool creation.
        
        Requires vcenter_id and datacenter id
        Available for Horizon 7.12 and later.

`Inventory(url: str, access_token: dict)`
:   Default object for the pools class where all Desktop Pool Actions will be performed.

    ### Methods

    `get_desktop_pool(self, id: str) ‑> dict`
    :   Gets the Desktop Pool information.
        
        Requires id of a desktop pool
        Available for Horizon 7.12 and later.

    `get_desktop_pools(self) ‑> list`
    :   Returns a list of dictionaries with all available Desktop Pools. 
        
        Available for Horizon 7.12 and later.

    `get_farm(self, id: str) ‑> dict`
    :   Gets the Farm information.
        
        Available for Horizon 7.12 and later.

    `get_farms(self) ‑> list`
    :   Lists the Farms in the environment.
        
        Available for Horizon 7.12 and later.

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
