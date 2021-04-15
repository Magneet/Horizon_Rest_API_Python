import requests, getpass, urllib, json

import vmware_horizon

requests.packages.urllib3.disable_warnings()
url = input("URL\n")

username = input("Username\n")

domain = input("Domain\n")

pw = getpass.getpass()

hvconnectionobj = vmware_horizon.Connection(username = username,domain = domain,password = pw,url = url)
hvconnectionobj.hv_connect()
print("connected")

monitor = obj=vmware_horizon.Monitor(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
external=vmware_horizon.External(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
inventory=vmware_horizon.Inventory(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
config=vmware_horizon.Config(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)

with open('/mnt/d/homelab/farm.json') as f:
    data = json.load(f)

vcenters = monitor.virtual_centers()
vcid = vcenters[0]["id"]
dcs = external.get_datacenters(vcenter_id=vcid)
dcid = dcs[0]["id"]

base_vms = external.get_base_vms(vcenter_id=vcid,datacenter_id=dcid,filter_incompatible_vms=True)

base_vm = next(item for item in base_vms if item["name"] == "srv2019-p1-2020-10-13-08-44")
basevmid=base_vm["id"]

base_snapshots = external.get_base_snapshots(vcenter_id=vcid, base_vm_id=base_vm["id"])

base_snapshot = next(item for item in base_snapshots if item["name"] == "Created by Packer")

snapid=base_snapshot["id"]

host_or_clusters = external.get_hosts_or_clusters(vcenter_id=vcid, datacenter_id=dcid)
for i in host_or_clusters:
    if (i["details"]["name"]) == "Cluster_Pod1":
        host_or_cluster = i

resource_pools = external.get_resource_pools(vcenter_id=vcid, host_or_cluster_id=host_or_cluster["id"])
for i in resource_pools:
    # print(i)
    if (i["type"] == "CLUSTER"):
        resource_pool = i

vm_folders = external.get_vm_folders(vcenter_id=vcid, datacenter_id=dcid)
for i in vm_folders:
    children=(i["children"])
    for ii in children:
        # print(ii["name"])
        if (ii["name"]) == "Pod1":
            vm_folder = i

datastore_list = []
datastores = external.get_datastores(vcenter_id=vcid, host_or_cluster_id=host_or_cluster["id"])
for i in datastores:
    # print(i)
    if (i["name"] == "VDI-500") or i["name"] == "VDI-200":
        ds = {}
        ds["datastore_id"] = i["id"]
        datastore_list.append(ds)

local_access_group = next(item for item in (config.get_local_access_groups()) if item["name"] == "Root")
ic_domain_account = next(item for item in (config.get_ic_domain_accounts()) if item["username"] == "administrator")

data["access_group_id"] = local_access_group["id"]
data["automated_farm_settings"]["customization_settings"]["ad_container_rdn"] = "OU=Pod1,OU=RDS,OU=VMware,OU=EUC"
data["automated_farm_settings"]["customization_settings"]["reuse_pre_existing_accounts"] = True
data["automated_farm_settings"]["customization_settings"]["instant_clone_domain_account_id"] = ic_domain_account["id"]
data["automated_farm_settings"]["enable_provisioning"] = False
data["automated_farm_settings"]["max_sessions"] = 50
data["automated_farm_settings"]["min_ready_vms"] = 3
data["automated_farm_settings"]["pattern_naming_settings"]["max_number_of_rds_servers"] = 4
data["automated_farm_settings"]["pattern_naming_settings"]["naming_pattern"] = "farmdemo-{n:fixed=3}"
data["automated_farm_settings"]["provisioning_settings"]["base_snapshot_id"] = snapid
data["automated_farm_settings"]["provisioning_settings"]["parent_vm_id"] = basevmid
data["automated_farm_settings"]["provisioning_settings"]["host_or_cluster_id"] = host_or_cluster["id"]
data["automated_farm_settings"]["provisioning_settings"]["resource_pool_id"] = resource_pool["id"]
data["automated_farm_settings"]["provisioning_settings"]["vm_folder_id"] = vm_folder["id"]
data["automated_farm_settings"]["provisioning_settings"]["datacenter_id"] = dcid
data["automated_farm_settings"]["stop_provisioning_on_error"] = True
data["automated_farm_settings"]["storage_settings"]["datastores"] = datastore_list
data["automated_farm_settings"]["transparent_page_sharing_scope"] = "GLOBAL"
data["automated_farm_settings"]["vcenter_id"] = vcid
data["description"] = "Python_demo_farm"
data["display_name"] = "Python_demo_farm"
data["display_protocol_settings"]["allow_users_to_choose_protocol"] = True
data["display_protocol_settings"]["default_display_protocol"] = "BLAST"
data["display_protocol_settings"]["session_collaboration_enabled"] = True
data["enabled"] = False
data["load_balancer_settings"]["cpu_threshold"] = 12
data["load_balancer_settings"]["disk_queue_length_threshold"] = 16
data["load_balancer_settings"]["disk_read_latency_threshold"] = 12
data["load_balancer_settings"]["disk_write_latency_threshold"] = 16
data["load_balancer_settings"]["include_session_count"] = True
data["load_balancer_settings"]["memory_threshold"] = 12
data["name"] = "Python_demo_farm"
data["session_settings"]["disconnected_session_timeout_minutes"] = 5
data["session_settings"]["disconnected_session_timeout_policy"] = "NEVER"
data["session_settings"]["empty_session_timeout_minutes"] = 6
data["session_settings"]["empty_session_timeout_policy"] = "AFTER"
data["session_settings"]["logoff_after_timeout"] = False
data["session_settings"]["pre_launch_session_timeout_minutes"] = 12
data["session_settings"]["pre_launch_session_timeout_policy"] = "AFTER"
data["type"] = "AUTOMATED"

inventory.new_farm(farm_data=data)

end=hvconnectionobj.hv_disconnect()
print(end)
