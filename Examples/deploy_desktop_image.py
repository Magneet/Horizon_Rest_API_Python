import requests, getpass, urllib, time
import vmware_horizon

requests.packages.urllib3.disable_warnings()

url                     = "https://pod2cbr1.loft.lab"
desktop_pool_name       = "Pod02-Pool01"
base_vm_name            = "W10-L-2021-03-19-17-27"
snapshot_name           = "Snap_2"

username = input("Username\n")
domain = input("Domain\n")
pw = getpass.getpass()

hvconnectionobj = vmware_horizon.Connection(username = username,domain = domain,password = pw,url = url)
hvconnectionobj.hv_connect()
print("connected")
monitor = obj=vmware_horizon.Monitor(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
external=vmware_horizon.External(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
inventory=vmware_horizon.Inventory(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)

desktop_pools=inventory.get_desktop_pools()
desktop_pool = next(item for item in desktop_pools if item["name"] == desktop_pool_name)
poolid=desktop_pool["id"]

vcenters = monitor.virtual_centers()
vcid = vcenters[0]["id"]
dcs = external.get_datacenters(vcenter_id=vcid)
dcid = dcs[0]["id"]

base_vms = external.get_base_vms(vcenter_id=vcid,datacenter_id=dcid,filter_incompatible_vms=True)
base_vm = next(item for item in base_vms if item["name"] == base_vm_name)
basevmid=base_vm["id"]

base_snapshots = external.get_base_snapshots(vcenter_id=vcid, base_vm_id=base_vm["id"])
base_snapshot = next(item for item in base_snapshots if item["name"] == snapshot_name)
snapid=base_snapshot["id"]

current_time = time.time()
inventory.desktop_pool_push_image(desktop_pool_id=poolid,parent_vm_id=basevmid,snapshot_id=snapid, start_time=current_time)

end=hvconnectionobj.hv_disconnect()
print(end)











