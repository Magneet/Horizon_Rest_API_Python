import vmware_horizon

import requests, getpass, urllib, json, operator, inspect

requests.packages.urllib3.disable_warnings()
url = input("URL\n")

username = input("Username\n")

domain = input("Domain\n")

pw = getpass.getpass()

list={}
hvconnectionobj = vmware_horizon.Connection(username = username,domain = domain,password = pw,url = url)
hvconnectionobj.hv_connect()
print("connected")
monitor = vmware_horizon.Monitor(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
external = vmware_horizon.External(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
inventory = vmware_horizon.Inventory(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
config = vmware_horizon.Config(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
entitlements = vmware_horizon.Entitlements(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
# for i in (dir(inventory)):
#     print(dir(i))
inventory_list = [func for func in dir(inventory) if callable(getattr(inventory, func)) and not func.startswith("__")]
external_list = [func for func in dir(external) if callable(getattr(external, func)) and not func.startswith("__")]
monitor_list = [func for func in dir(monitor) if callable(getattr(monitor, func)) and not func.startswith("__")]
config_list = [func for func in dir(config) if callable(getattr(config, func)) and not func.startswith("__")]
entitlements_list = [func for func in dir(entitlements) if callable(getattr(entitlements, func)) and not func.startswith("__")]
list["monitor"] = monitor_list
list["inventory"] = inventory_list
list["external"] = external_list
list["config"] = config_list
list["entitlements"] = entitlements_list
for i in list["entitlements"]:
    print(i)




end=hvconnectionobj.hv_disconnect()
print(end)