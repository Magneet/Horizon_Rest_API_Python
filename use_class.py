import requests, getpass
import vmware_horizon

requests.packages.urllib3.disable_warnings()
#url = input("URL\n")
url="https://loftcbr01.loft.lab"
#username = input("Username\n")
username = "m_wouter"
#domain = input("Domain\n")
domain = "loft.lab"
pw = getpass.getpass()


hvconnectionobj = vmware_horizon.Connection(username = username,domain = domain,password = pw,url = url)
hvconnectionobj.hv_connect()
print(hvconnectionobj)
obj = vmware_horizon.Config(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
print(obj.get_settings_security())

changes = {}
changes["re_auth_secure_tunnel_after_interruption"] = True
print(changes)
result = obj.update_settings_security(settings=changes)
print(result)
#print(obj.get_settings_general())





settings=vmware_horizon.Config(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
results = settings.get_ic_domain_accounts()
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


