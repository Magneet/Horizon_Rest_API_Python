import json, requests, ssl
from typing import get_args

class Connection:
    """The Connection class is used to handle connections and disconnections to and from the VMware Horizon REST API's"""
    def __init__(self, username: str, password: str, domain: str, url:str):
        """"The default object for the connection class needs to be created using username, password, domain and url in plain text."""
        self.username = username
        self.password = password
        self.domain = domain
        self.url = url
        self.access_token = ""


    def hv_connect(self):
        """Used to authenticate to the VMware Horizon REST API's"""
        headers = {
            'accept': '*/*',
            'Content-Type': 'application/json',
        }

        data = {"domain": self.domain, "password": self.password, "username": self.username}
        json_data = json.dumps(data)

        response = requests.post(f'{self.url}/rest/login', verify=False, headers=headers, data=json_data)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            data = response.json()
            self.access_token = {
                'accept': '*/*',
                'Authorization': 'Bearer ' + data['access_token']
            }
            return self

    def hv_disconnect(self):
        """"Used to close close the connection with the VMware Horizon REST API's"""
        response = requests.post(f'{self.url}/rest/logout', verify=False, headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)

class Pools:
    def __init__(self, url: str, access_token: dict):
        """Default object for the pools class where all Desktop Pool Actions will be performed."""
        self.url = url
        self.access_token = access_token


    def list_hvpools(self) -> list:
        """Returns a list of dictionaries with all available Desktop Pools. 

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/desktop-pools', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

class Monitor:
    def __init__(self, url: str, access_token: dict):
        """Default object for the monitor class used for the monitoring of the various VMware Horiozn services."""
        self.url = url
        self.access_token = access_token

    def ad_domains(self) -> list:
        """Lists monitoring information related to AD Domains of the environment.

        Available for Horizon 7.10 and later."""
        response = requests.get(f'{self.url}/rest/monitor/ad-domains', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def connection_servers(self) -> list:
        """Lists monitoring information related to Connection Servers of the environment.

        Available for Horizon 7.10 and later."""
        response = requests.get(f'{self.url}/rest/monitor/connection-servers', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def connection_server(self, id: str) ->dict:
        """Lists monitoring information related to a single Connection Server.

        Requires the id of a Connection Server to be provided as id
        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/monitor/v1/connection-servers/{id}', verify=False,  headers=self.access_token)  # Only available in Horion 8.0 2006 and newer
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def event_database(self) -> dict:
        """Returns monitoring information related to Event database of the environment.

        Available for Horizon 7.10 and later."""
        response = requests.get(f'{self.url}/rest/monitor/event-database', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def farms(self) -> list:
        """Lists monitoring information related to RDS Farms of the environment.

        Available for Horizon 7.10 and later."""
        response = requests.get(f'{self.url}/rest/monitor/farms', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def farm(self, id: str) -> dict:
        """Lists monitoring information related to a single RDS Farm.

        Requires the id of a farm to be provided as id
        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/monitor/v1/farms/{id}', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def gateways(self) -> list:
        """Lists monitoring information related to Gateways registered in the environment.

        Available for Horizon 7.10 and later."""
        response = requests.get(f'{self.url}/rest/monitor/gateways', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def gateway(self, id: str) -> dict:
        """Lists monitoring information related to a single gateway.

        Requires the id of a Gateway to be provided as id
        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/monitor/v1/gateways/{id}', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def rds_servers(self) -> list:
        """Lists monitoring information related to RDS Servers of the environment.

        Available for Horizon 7.10 and later."""
        response = requests.get(f'{self.url}/rest/monitor/rds-servers', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def rds_server(self, id: str) -> dict:
        """Lists monitoring information related to a single RDS Server.

        Requires the id of a RDS Server to be provided as id
        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/monitor/v1/rds-servers/{id}', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def saml_authenticators(self) -> list:
        """Lists monitoring information related to SAML Authenticators of the environment.

        Available for Horizon 7.10 and later."""
        response = requests.get(f'{self.url}/rest/monitor/saml-authenticators', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def saml_authenticator(self, id: str) -> dict:
        """Lists monitoring information related to a single SAML Authenticator.

        Requires the id of a SAML Authenticator to be provided as id
        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/monitor/v1/saml-authenticators/{id}', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def view_composers(self) -> list:
        """Lists monitoring information related to View Composers of the environment.

        Available for Horizon 7.10 to Horizon 8 2006."""
        response = requests.get(f'{self.url}/rest/monitor/view-composers', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def view_composer(self, vcId: str):
        """Lists monitoring information related to a single View Composers.

        Requires the id of a Virtual Center to be provided as vcId
        Only available for Horizon 8 2006."""
        response = requests.get(f'{self.url}/rest/monitor/v1/view-composers/{vcId}', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def virtual_centers(self) -> list:
        """Lists monitoring information related to Virtual Centers of the environment.

        Available for Horizon 7.10 and later."""
        response = requests.get(f'{self.url}/rest/monitor/virtual-centers', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def virtual_center(self, id:str) -> dict:
        """Lists monitoring information related to a single Virtual Center.

        Requires the id of a Virtual Center to be provided as id
        Only available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/monitor/v1/virtual-centers/{id}', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def remote_pods(self) -> list:
        """Lists monitoring information related to the remote pods.

        Available for Horizon 7.11 and later."""
        response = requests.get(f'{self.url}/rest/monitor/v1/pods', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def remote_pod(self, id:str) -> dict:
        """Lists monitoring information related to a single remote pod.

        Requires the id of a Remote Pod to be provided as id
        Only available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/monitor/v1/pods/{id}', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def true_sso(self) -> list:
        """Lists monitoring information related to True SSO connectors.

        Available for Horizon 7.11 and later."""
        response = requests.get(f'{self.url}/rest/monitor/v1/true-sso', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

class Config:
    def __init__(self, url: str, access_token: dict):
        """Default object for the config class used for the general configuration of VMware Horizon."""
        self.url = url
        self.access_token = access_token

    def get_ic_domain_accounts(self) -> list:
        """Lists instant clone domain accounts of the environment.

        Available for Horizon 7.11 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/ic-domain-accounts', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def get_ic_domain_account(self,id) -> dict:
        """Gets a single instant clone domain account.

        Requires the id of an Instant Clone Admin account to be provided as id
        Available for Horizon 7.11 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/ic-domain-accounts/{id}', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def new_ic_domain_account(self,ad_domain_id: str,username: str,password: str):
        """Creates Instant Clone Domain Account

        Requires ad_domain_id, username and password in plain text.
        Available for Horizon 7.11 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {"ad_domain_id": ad_domain_id, "password": password, "username": username}
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/config/v1/ic-domain-accounts', verify=False,  headers=headers, data=json_data)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            if response.status_code == 400 or response.status_code == 409:
                response = response.json()
                return "Error: " + str(e) + ", " + response['error_message']
            else:
                return "Error: " + str(e)
        else:
            return response.json()

    def update_ic_domain_account(self,id: str,password: str):
        """Changes password for an Instant Clone Domain account

        Requires id of an Instant CLone Domain account and a plain text password.
        Available for Horizon 7.11 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {"password": password}
        json_data = json.dumps(data)
        response = requests.put(f'{self.url}/rest/config/v1/ic-domain-accounts/{id}', verify=False,  headers=headers, data=json_data)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            if response.status_code == 400:
                response = response.json()
                return "Error: " + str(e) + ", " + response['error_message']
            else:
                return "Error: " + str(e)
        else:
            return response.status_code

    def delete_ic_domain_account(self,id: str):
        """Removes Instant Clone Domain Account from the environment

        Requires id of an Instant CLone Domain account
        Available for Horizon 7.11 and later."""
        response = requests.delete(f'{self.url}/rest/config/v1/ic-domain-accounts/{id}', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            if response.status_code == 400:
                response = response.json()
                return "Error: " + str(e) + ", " + response['error_message']
            else:
                return "Error: " + str(e)
        else:
            return response.json()

    def list_virtual_centers(self) -> list:
        """Lists Virtual Centers configured in the environment.

        Available for Horizon 7.11 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/virtual-centers', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def get_environment_properties(self) -> dict:
        """Retrieves the environment settings.

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/environment-properties', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def get_settings(self) -> dict:
        """Retrieves the environment settings.

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/settings', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def get_settings_feature(self) -> dict:
        """Retrieves the feature settings.

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/settings/feature', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def get_settings_general(self) -> dict:
        """Retrieves the general settings.

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/settings/general', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def get_settings_security(self) -> dict:
        """Retrieves the security settings.

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/settings/security', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()

    def update_settings_general(self,settings: dict):
        """Updates the general settings.

        Requires a dictionary with updated settings
        Available for Horizon 7.12 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(settings)
        response = requests.put(f'{self.url}/rest/config/v1/settings/general', verify=False,  headers=self.access_token, data=json_data)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            if response.status_code == 400:
                response = response.json()
                return "Error: " + str(e) + ", " + response['error_message']
            else:
                return "Error: " + str(e)
        else:
            return response.json()

class External:
    def __init__(self, url: str, access_token: dict):
        """Default object for the External class for resources that are external to Horizon environment."""
        self.url = url
        self.access_token = access_token

    def get_ad_domains(self) -> list:
        """Lists information related to AD Domains of the environment.

        Available for Horizon 7.11 and later."""
        response = requests.get(f'{self.url}/rest/external/v1/ad-domains', verify=False,  headers=self.access_token)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Error: " + str(e)
        else:
            return response.json()
