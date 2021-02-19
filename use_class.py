import requests, getpass, urllib, json, operator
import vmware_horizon

requests.packages.urllib3.disable_warnings()
#url = input("URL\n")
url="https://loftcbr01.loft.lab"
#url="https://pod2cbr1.loft.lab"
#url="https://pod1cbr1.loft.lab"
#url="https://lofttst01.loft.lab"
#username = input("Username\n")
username = "m_wouter"
#domain = input("Domain\n")
domain = "loft.lab"
pw = getpass.getpass()


hvconnectionobj = vmware_horizon.Connection(username = username,domain = domain,password = pw,url = url)
hvconnectionobj.hv_connect()
print("connected")
monitor = obj=vmware_horizon.Monitor(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
obj=vmware_horizon.External(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
vcenters = monitor.virtual_centers()
vcid = vcenters[0]["id"]
print(vcid)
hoc = obj.get_hosts_or_clusters(vcenter_id=vcid, datacenter_id="datacenter-2")
print(hoc)

#base_vm = list(filter (lambda name : name["name"] == "W10-L-2021-02-01-14-18", basevms))
ds = obj.get_datastore_paths(vcenter_id=vcid,datastore_id="datastore-5681")
print(ds)


# sessions = obj.get_sessions(maxpagesize=1)
#print(obj.rds_servers())
# filter = {}
# filter["type"] = "And"
# filter["filters"] = []
# filter1={}
# filter1["type"] = "Contains"
# filter1["name"] = "name"
# filter1["value"] = "user"

# filter["filters"].append(filter1)


end=hvconnectionobj.hv_disconnect()
print(end)

#id = result[0]["id"]
#print(id)

#result2 = monitor.virtual_centers()
#print(result2)
#print(f'The first Desktop pool is {pools[0]["display_name"]}')


