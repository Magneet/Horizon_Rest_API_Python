## Intro:

With this repo I will try to create a VMware Horion python module using the Horizon REST API's.
development is started from Horizon 8 2006


## Usage:

First define url, username, domain and the password
* url = input("URL\n")
* username = input("Username\n")
* domain = input("Domain\n")
* pw = getpass.getpass()

Than create the Connection object and open the connection
* hvconnectionobj = vmware_horizon.Connection(username = username,domain = domain,password = pw,url = url)
* hvconnectionobj.hv_connect()

Create an object for the class you want to use, Monitor in this case
* obj = vmware_horizon.Monitor(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)

Than perform the query you need, in this example get the COnnection Servers
cs = obj.connection_servers()

## Documentation

[vmware_horizon.md](vmware_horizon.md)

## Changelog

[hangelog.md](changelog.ms)