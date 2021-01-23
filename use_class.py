import requests, getpass
import vmware_horizon

requests.packages.urllib3.disable_warnings()
url = input("URL\n")
username = input("Username\n")
domain = input("Domain\n")
pw = getpass.getpass()


at = vmware_horizon.Connection.hv_connect(username=username,password=pw,url=url,domain=domain)


pools = vmware_horizon.Pools.list_hvpools(url=url, access_token=at)
print(f'The first Desktop pool is {pools[0]["display_name"]}')

vmware_horizon.Connection.hv_disconnect(url=url, access_token=at)
