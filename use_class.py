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


pools = vmware_horizon.Pools(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
#results = pools.list_hvpools()
monitor = vmware_horizon.Monitor(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
print(monitor.connection_servers())

#id = result[0]["id"]
#print(id)
#print(results)
#result2 = monitor.virtual_centers()
#print(result2)
#print(f'The first Desktop pool is {pools[0]["display_name"]}')

hvconnectionobj.hv_disconnect()
