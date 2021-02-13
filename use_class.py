import requests, getpass, urllib, json
import vmware_horizon

requests.packages.urllib3.disable_warnings()
#url = input("URL\n")
#url="https://loftcbr01.loft.lab"
url="https://pod2cbr1.loft.lab"
#username = input("Username\n")
username = "m_wouter"
#domain = input("Domain\n")
domain = "loft.lab"
pw = getpass.getpass()


hvconnectionobj = vmware_horizon.Connection(username = username,domain = domain,password = pw,url = url)
hvconnectionobj.hv_connect()
# #print(hvconnectionobj)
# obj = vmware_horizon.Inventory(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
obj = vmware_horizon.Inventory(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
# sessions = obj.get_sessions(maxpagesize=1)
#print(obj.rds_servers())
filter = {}
filter["type"] = "And"
filter["filters"] = []
filter1={}
filter1["type"] = "Contains"
filter1["name"] = "name"
filter1["value"] = "Pod02"
print(filter1)
filter["filters"].append(filter1)
print(filter)
tmp = json.dumps(filter,separators=(', ', ':'))
print(tmp)
filter_url = urllib.parse.quote(tmp)
print(filter_url)
# bla = urllib.parse.urlencode(filter)
# print(bla)
machines = obj.get_machines(maxpagesize=1, filter = filter)
for i in machines:
    print(i)



# print(dc)

#print(obj.get_settings_general())





# settings=vmware_horizon.Config(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
# results = settings.get_ic_domain_accounts()
# for i in results:
#     if i["username"] == "m_wouter":
#         id=i["id"]


# result=settings.update_ic_domain_account(id=id, password=pw)
# print(result)

# print(settings.get_ic_domain_accounts())
#print(results)
end=hvconnectionobj.hv_disconnect()
print(end)

#id = result[0]["id"]
#print(id)

#result2 = monitor.virtual_centers()
#print(result2)
#print(f'The first Desktop pool is {pools[0]["display_name"]}')


