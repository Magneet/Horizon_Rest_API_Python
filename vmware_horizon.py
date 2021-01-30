import json, requests, ssl

class Connection:
    def __init__(self, username, password, domain, url):
        self.username = username
        self.password = password
        self.domain = domain
        self.url = url
        self.access_token = ""


    def hv_connect(self):
        headers = {
            'accept': '*/*',
            'Content-Type': 'application/json',
        }

        data = {"domain": self.domain, "password": self.password, "username": self.username}
        json_data = json.dumps(data)

        response = requests.post(f'{self.url}/rest/login', verify=False, headers=headers, data=json_data)
        data = response.json()

        self.access_token = {
            'accept': '*/*',
            'Authorization': 'Bearer ' + data['access_token']
        }
        return self

    def hv_disconnect(self):
        requests.post(f'{self.url}/rest/logout', verify=False, headers=self.access_token)

class Pools:
    def __init__(self, url, access_token):
        self.url = url
        self.access_token = access_token


    def list_hvpools(self):
        response = requests.get(f'{self.url}/rest/inventory/v1/desktop-pools', verify=False,  headers=self.access_token)
        return response.json()

class Monitor:
    def __init__(self, url, access_token):
        self.url = url
        self.access_token = access_token

    def ad_domain(self):
        response = requests.get(f'{self.url}/rest/monitor/ad-domains', verify=False,  headers=self.access_token)
        return response.json()

    def connection_servers(self):
        response = requests.get(f'{self.url}/rest/monitor/connection-servers', verify=False,  headers=self.access_token)
        return response.json()

    def connection_server(self, id):
        response = requests.get(f'{self.url}/rest/monitor/v1/connection-servers/{id}', verify=False,  headers=self.access_token)  # Only available in Horion 8.0 2006 and newer
        return response.json()

    def event_database(self):
        response = requests.get(f'{self.url}/rest/monitor/event-database', verify=False,  headers=self.access_token)
        return response.json()

    def farms(self):
        response = requests.get(f'{self.url}/rest/monitor/farms', verify=False,  headers=self.access_token)
        return response.json()

    def farm(self, id):
        response = requests.get(f'{self.url}/rest/monitor/v1/farms/{id}', verify=False,  headers=self.access_token)   # Only available in Horion 8.0 2006 and newer
        return response.json()

    def gateways(self):
        response = requests.get(f'{self.url}/rest/monitor/gateways', verify=False,  headers=self.access_token)
        return response.json()

    def gateway(self, id):
        response = requests.get(f'{self.url}/rest/monitor/v1/gateways/{id}', verify=False,  headers=self.access_token)    # Only available in Horion 8.0 2006 and newer
        return response.json()

    def rds_servers(self):
        response = requests.get(f'{self.url}/rest/monitor/rds-servers', verify=False,  headers=self.access_token)
        return response.json()

    def rds_server(self, id):
        response = requests.get(f'{self.url}/rest/monitor/v1/rds-servers/{id}', verify=False,  headers=self.access_token) # Only available in Horion 8.0 2006 and newer
        return response.json()

    def saml_authenticators(self):
        response = requests.get(f'{self.url}/rest/monitor/saml-authenticators', verify=False,  headers=self.access_token)
        return response.json()

    def saml_authenticator(self, id):
        response = requests.get(f'{self.url}/rest/monitor/v1/saml-authenticators/{id}', verify=False,  headers=self.access_token) # Only available in Horion 8.0 2006 and newer
        return response.json()

    def view_composers(self):
        response = requests.get(f'{self.url}/rest/monitor/view-composers', verify=False,  headers=self.access_token)  # Only available in Horion 8.0 2006 and newer
        return response.json()

    def view_composer(self, vcId):
        response = requests.get(f'{self.url}/rest/monitor/v1/view-composers/{id}', verify=False,  headers=self.access_token) # Only available in Horion 8.0 2006
        return response.json()

    def virtual_centers(self):
        response = requests.get(f'{self.url}/rest/monitor/virtual-centers', verify=False,  headers=self.access_token)
        return response.json()

    def virtual_center(self, id):
        response = requests.get(f'{self.url}/rest/monitor/v1/virtual-centers/{id}', verify=False,  headers=self.access_token) # Only available in Horion 8.0 2006 and newer
        return response.json()

    def remote_pods(self):
        response = requests.get(f'{self.url}/rest/monitor/v1/pods', verify=False,  headers=self.access_token) # Only available in Horion 7.11 and newer
        return response.json()

    def remote_pod(self, id):
        response = requests.get(f'{self.url}/rest/monitor/v1/pods/{id}', verify=False,  headers=self.access_token)    # Only available in Horion 8.0 2006 and newer
        return response.json()

    def true_sso(self):
        response = requests.get(f'{self.url}/rest/monitor/v1/true-sso', verify=False,  headers=self.access_token) # Only available in Horion 7.11 and newer
        return response.json()