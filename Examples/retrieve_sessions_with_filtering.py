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

inventory=vmware_horizon.Inventory(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)

filter = {}
filter["type"] = "And"
filter["filters"] = []
filter1={}

filter1["type"] = "Equals"
filter1["name"] = "session_state"
filter1["value"] = "DISCONNECTED"

filter["filters"].append(filter1)

sessions = inventory.get_sessions(filter=filter)
for i in sessions:
    for ii in i:
        print(ii, '=', i[ii] )


end=hvconnectionobj.hv_disconnect()
print(end)
