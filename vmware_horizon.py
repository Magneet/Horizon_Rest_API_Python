import json, requests, ssl, urllib
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
        self.refresh_token = ""


    def hv_connect(self):
        """Used to authenticate to the VMware Horizon REST API's"""
        headers = {
            'accept': '*/*',
            'Content-Type': 'application/json',
        }

        data = {"domain": self.domain, "password": self.password, "username": self.username}
        json_data = json.dumps(data)

        response = requests.post(f'{self.url}/rest/login', verify=False, headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                data = response.json()
                self.access_token = {
                    'accept': '*/*',
                    'Authorization': 'Bearer ' + data['access_token']
                }
                self.refresh_token = data['refresh_token']
                return self


    def hv_disconnect(self):
        """"Used to close close the connection with the VMware Horizon REST API's"""
        headers = {
            'accept': '*/*',
            'Content-Type': 'application/json',
        }
        data = {'refresh_token': self.refresh_token}
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/logout', verify=False, headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status_code

class Inventory:
    def __init__(self, url: str, access_token: dict):
        """Default object for the pools class where all Desktop Pool Actions will be performed."""
        self.url = url
        self.access_token = access_token


    def get_desktop_pools(self) -> list:
        """Returns a list of dictionaries with all available Desktop Pools. 

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/desktop-pools', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_desktop_pool(self, desktop_pool_id: str) -> dict:
        """Gets the Desktop Pool information.

        Requires id of a desktop pool
        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/desktop-pools/{desktop_pool_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_farms(self) -> list:
        """Lists the Farms in the environment.

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/farms', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_farm(self, farm_id:str) -> dict:
        """Gets the Farm information.

        Requires id of a RDS Farm
        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/farms/{farm_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_machine(self, machine_id:str) -> dict:
        """Gets the Machine information.

        Requires id of a machine
        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/machines/{machine_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_machines(self, maxpagesize:int=100, filter:dict="") -> list:
        """Lists the Machines in the environment.

        For information on filtering see https://vdc-download.vmware.com/vmwb-repository/dcr-public/f92cce4b-9762-4ed0-acbd-f1d0591bd739/235dc19c-dabd-43f2-8d38-8a7a333e914e/HorizonServerRESTPaginationAndFilterGuide.doc
        Available for Horizon 8 2006 and later."""

        def int_get_machines(self, page:int, maxpagesize: int, filter:list="") ->list:
            if filter != "":
                filter_url = urllib.parse.quote(json.dumps(filter,separators=(', ', ':')))
                add_filter = f"?filter={filter_url}"
                response = requests.get(f'{self.url}/rest/inventory/v1/machines{add_filter}&page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            else:
                response = requests.get(f'{self.url}/rest/inventory/v1/machines?page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            if response.status_code == 400:
                error_message = (response.json())["error_message"]
                raise Exception(f"Error {response.status_code}: {error_message}")
            elif response.status_code != 200:
                raise Exception(f"Error {response.status_code}: {response.reason}")
            else:
                try:
                    response.raise_for_status()
                except requests.exceptions.RequestException as e:
                    raise "Error: " + str(e)
                else:
                    return response
        if maxpagesize > 1000:
            maxpagesize = 1000
        page = 1
        response = int_get_machines(self,page = page, maxpagesize= maxpagesize,filter = filter)
        results = response.json()
        while 'HAS_MORE_RECORDS' in response.headers:
            page += 1
            response = int_get_machines(self,page = page, maxpagesize= maxpagesize, filter = filter)
            results += response.json()
        return results

    def delete_machine(self, machine_id:str, delete_from_multiple_pools:bool=False, force_logoff:bool=False, delete_from_disk:bool=False):
        """Deletes a machine.

        Requires id of the machine to delete machine
        Optional arguments (all default to False): delete_from_multiple_pools, force_logoff and delete_from_disk
        Available for Horizon 7.12 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data={}
        data["allow_delete_from_multi_desktop_pools"] = delete_from_multiple_pools
        data["archive_persistent_disk"] = False
        data["delete_from_disk"] = delete_from_disk
        data["force_logoff_session"] = force_logoff
        json_data = json.dumps(data)
        response = requests.delete(f'{self.url}/rest/inventory/v1/machines/{machine_id}', verify=False,  headers=self.access_token, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def delete_machines(self, machine_ids:list, delete_from_multiple_pools:bool=False, force_logoff:bool=False, delete_from_disk:bool=False):
        """deletes the specified machines

        Requires list of ids of the machines to remove 
        Optional arguments (all default to False): delete_from_multiple_pools, force_logoff and delete_from_disk
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data={}
        machine_delete_data={}
        machine_delete_data["allow_delete_from_multi_desktop_pools"] = delete_from_multiple_pools
        machine_delete_data["archive_persistent_disk"] = False
        machine_delete_data["delete_from_disk"] = delete_from_disk
        machine_delete_data["force_logoff_session"] = force_logoff
        data["machine_delete_data"] = machine_delete_data
        data["machine_ids"] = machine_ids
        json_data = json.dumps(data)
        response = requests.delete(f'{self.url}/rest/inventory/v1/machines', verify=False,  headers=self.access_token, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def machines_enable_maintenance_mode(self, machine_ids:list):
        """Puts a machine in maintenance mode.

        Requires a List of Machine Ids representing the machines to be put into maintenance mode.
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(machine_ids)
        response = requests.post(f'{self.url}/rest/inventory/v1/machines/action/enter-maintenance', verify=False,  headers=self.access_token, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def machines_exit_maintenance_mode(self, machine_ids:list):
        """Takes a machine out of maintenance mode.

        Requires a List of Machine Ids representing the machines to be taken out of maintenance mode.
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(machine_ids)
        response = requests.post(f'{self.url}/rest/inventory/v1/machines/action/exit-maintenance', verify=False,  headers=self.access_token, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def rebuild_machines(self, machine_ids:list):
        """Rebuilds the specified machines.

        Requires a List of Machine Ids representing the machines to be rebuild.
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(machine_ids)
        response = requests.post(f'{self.url}/rest/inventory/v1/machines/action/rebuild', verify=False,  headers=self.access_token, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def recover_machines(self, machine_ids:list):
        """Recovers the specified machines.

        Requires a List of Machine Ids representing the machines to be recovered.
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(machine_ids)
        response = requests.post(f'{self.url}/rest/inventory/v1/machines/action/recover', verify=False,  headers=self.access_token, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def reset_machines(self, machine_ids:list):
        """Resets the specified machines.

        Requires a List of Machine Ids representing the machines to be reset.
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(machine_ids)
        response = requests.post(f'{self.url}/rest/inventory/v1/machines/action/reset', verify=False,  headers=self.access_token, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def restart_machines(self, machine_ids:list):
        """Restarts the specified machines.

        Requires a List of Machine Ids representing the machines to be restarted.
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(machine_ids)
        response = requests.post(f'{self.url}/rest/inventory/v1/machines/action/restart', verify=False,  headers=self.access_token, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def get_sessions(self, maxpagesize:int=100) -> list:
        """Lists the Session information in the environment.

        Will default to 1000 results with a pagesize of 100, max pagesize is 1000.
        Available for Horizon 8 2006 and later."""

        def int_get_sessions(self, page:int, maxpagesize: int) ->list:
            response = requests.get(f'{self.url}/rest/inventory/v1/sessions?page={page}&size={maxpagesize}', verify=False,  headers=self.access_token)
            if response.status_code == 400:
                error_message = (response.json())["error_message"]
                raise Exception(f"Error {response.status_code}: {error_message}")
            elif response.status_code != 200:
                raise Exception(f"Error {response.status_code}: {response.reason}")
            else:
                try:
                    response.raise_for_status()
                except requests.exceptions.RequestException as e:
                    raise "Error: " + str(e)
                else:
                    return response
        if maxpagesize > 1000:
            maxpagesize = 1000
        page = 1
        response = int_get_sessions(self,page = page, maxpagesize= maxpagesize)
        results = response.json()
        while 'HAS_MORE_RECORDS' in response.headers:
            page += 1
            response = int_get_sessions(self,page = page, maxpagesize= maxpagesize)
            results += response.json()
        return results

    def get_session(self, session_id: str) -> dict:
        """Gets the Session information.

        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/sessions/{session_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_application_pools(self, maxpagesize:int=100, filter:dict="") -> list:
        """Lists the application pools in the environment.

        For information on filtering see https://vdc-download.vmware.com/vmwb-repository/dcr-public/f92cce4b-9762-4ed0-acbd-f1d0591bd739/235dc19c-dabd-43f2-8d38-8a7a333e914e/HorizonServerRESTPaginationAndFilterGuide.doc
        Available for Horizon 8 2006 and later."""

        def int_get_application_pools(self, page:int, maxpagesize: int, filter:list="") ->list:
            if filter != "":
                filter_url = urllib.parse.quote(json.dumps(filter,separators=(', ', ':')))
                add_filter = f"?filter={filter_url}"
                response = requests.get(f'{self.url}/rest/inventory/v1/application-pools{add_filter}&page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            else:
                response = requests.get(f'{self.url}/rest/inventory/v1/application-pools?page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            if response.status_code == 400:
                error_message = (response.json())["error_message"]
                raise Exception(f"Error {response.status_code}: {error_message}")
            elif response.status_code != 200:
                raise Exception(f"Error {response.status_code}: {response.reason}")
            else:
                try:
                    response.raise_for_status()
                except requests.exceptions.RequestException as e:
                    raise "Error: " + str(e)
                else:
                    return response
        if maxpagesize > 1000:
            maxpagesize = 1000
        page = 1
        response = int_get_application_pools(self,page = page, maxpagesize= maxpagesize,filter = filter)
        results = response.json()
        while 'HAS_MORE_RECORDS' in response.headers:
            page += 1
            response = int_get_application_pools(self,page = page, maxpagesize= maxpagesize, filter = filter)
            results += response.json()
        return results

    def get_application_pool(self, application_pool_id: str) -> dict:
        """Gets a single Application pool

        Requires Application_pool_id
        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/application-pools/{application_pool_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code == 403:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def new_application_pool(self,application_pool_data:dict):
        """Creates an application pool.

        Requires application_pool_data as a dict
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(application_pool_data)
        response = requests.post(f'{self.url}/rest/inventory/v1/application-pools', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 409:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 201:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status_code

    def update_application_pool(self, application_pool_id:str, application_pool_data:dict):
        """Updates an application pool.

        The following keys are required to be present in the json: multi_session_mode, executable_path and enable_pre_launch
        Requires ad_domain_id, username and password in plain text.
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(application_pool_data)
        response = requests.put(f'{self.url}/rest/inventory/v1/application-pools/{application_pool_id}', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_messages"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 401:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status_code

    def delete_application_pool(self,application_pool_id:str):
        """Deletes an application pool.

        Requires application_pool_id as a str
        Available for Horizon 8 2006 and later."""
        response = requests.delete(f'{self.url}/rest/inventory/v1/application-pools/{application_pool_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 401:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status_code


class Monitor:
    def __init__(self, url: str, access_token: dict):
        """Default object for the monitor class used for the monitoring of the various VMware Horiozn services."""
        self.url = url
        self.access_token = access_token

    def ad_domains(self) -> list:
        """Lists monitoring information related to AD Domains of the environment.

        Available for Horizon 7.10 and later."""
        response = requests.get(f'{self.url}/rest/monitor/ad-domains', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def connection_servers(self) -> list:
        """Lists monitoring information related to Connection Servers of the environment.

        Available for Horizon 7.10 and later."""
        response = requests.get(f'{self.url}/rest/monitor/connection-servers', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def connection_server(self, id: str) ->dict:
        """Lists monitoring information related to a single Connection Server.

        Requires the id of a Connection Server to be provided as id
        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/monitor/v1/connection-servers/{id}', verify=False,  headers=self.access_token)  # Only available in Horion 8.0 2006 and newer
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def event_database(self) -> dict:
        """Returns monitoring information related to Event database of the environment.

        Available for Horizon 7.10 and later."""
        response = requests.get(f'{self.url}/rest/monitor/event-database', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def farms(self) -> list:
        """Lists monitoring information related to RDS Farms of the environment.

        Available for Horizon 7.10 and later."""
        response = requests.get(f'{self.url}/rest/monitor/farms', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def farm(self, id: str) -> dict:
        """Lists monitoring information related to a single RDS Farm.

        Requires the id of a farm to be provided as id
        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/monitor/v1/farms/{id}', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def gateways(self) -> list:
        """Lists monitoring information related to Gateways registered in the environment.

        Available for Horizon 7.10 and later."""
        response = requests.get(f'{self.url}/rest/monitor/gateways', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def gateway(self, id: str) -> dict:
        """Lists monitoring information related to a single gateway.

        Requires the id of a Gateway to be provided as id
        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/monitor/v1/gateways/{id}', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()
    def rds_servers(self) -> list:
        """Lists monitoring information related to RDS Servers of the environment.

        Available for Horizon 7.10 and later."""
        response = requests.get(f'{self.url}/rest/monitor/rds-servers', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def rds_server(self, id: str) -> dict:
        """Lists monitoring information related to a single RDS Server.

        Requires the id of a RDS Server to be provided as id
        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/monitor/v1/rds-servers/{id}', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def saml_authenticators(self) -> list:
        """Lists monitoring information related to SAML Authenticators of the environment.

        Available for Horizon 7.10 and later."""
        response = requests.get(f'{self.url}/rest/monitor/saml-authenticators', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def saml_authenticator(self, id: str) -> dict:
        """Lists monitoring information related to a single SAML Authenticator.

        Requires the id of a SAML Authenticator to be provided as id
        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/monitor/v1/saml-authenticators/{id}', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def view_composers(self) -> list:
        """Lists monitoring information related to View Composers of the environment.

        Available for Horizon 7.10 to Horizon 8 2006."""
        response = requests.get(f'{self.url}/rest/monitor/view-composers', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def view_composer(self, vcId: str):
        """Lists monitoring information related to a single View Composers.

        Requires the id of a Virtual Center to be provided as vcId
        Only available for Horizon 8 2006."""
        response = requests.get(f'{self.url}/rest/monitor/v1/view-composers/{vcId}', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def virtual_centers(self) -> list:
        """Lists monitoring information related to Virtual Centers of the environment.

        Available for Horizon 7.10 and later."""
        response = requests.get(f'{self.url}/rest/monitor/virtual-centers', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def virtual_center(self, id:str) -> dict:
        """Lists monitoring information related to a single Virtual Center.

        Requires the id of a Virtual Center to be provided as id
        Only available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/monitor/v1/virtual-centers/{id}', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def remote_pods(self) -> list:
        """Lists monitoring information related to the remote pods.

        Available for Horizon 7.11 and later."""
        response = requests.get(f'{self.url}/rest/monitor/v1/pods', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def remote_pod(self, id:str) -> dict:
        """Lists monitoring information related to a single remote pod.

        Requires the id of a Remote Pod to be provided as id
        Only available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/monitor/v1/pods/{id}', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def true_sso(self) -> list:
        """Lists monitoring information related to True SSO connectors.

        Available for Horizon 7.11 and later."""
        response = requests.get(f'{self.url}/rest/monitor/v1/true-sso', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
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
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_ic_domain_account(self,id) -> dict:
        """Gets a single instant clone domain account.

        Requires the id of an Instant Clone Admin account to be provided as id
        Available for Horizon 7.11 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/ic-domain-accounts/{id}', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
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
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 409:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 201:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status_code

    def update_ic_domain_account(self,id: str,password: str):
        """Changes password for an Instant Clone Domain account

        Requires id of an Instant CLone Domain account and a plain text password.
        Available for Horizon 7.11 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {"password": password}
        json_data = json.dumps(data)
        response = requests.put(f'{self.url}/rest/config/v1/ic-domain-accounts/{id}', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status_code

    def delete_ic_domain_account(self,id: str):
        """Removes Instant Clone Domain Account from the environment

        Requires id of an Instant CLone Domain account
        Available for Horizon 7.11 and later."""
        response = requests.delete(f'{self.url}/rest/config/v1/ic-domain-accounts/{id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status_code

    def get_virtual_centers(self) -> list:
        """Lists Virtual Centers configured in the environment.

        Available for Horizon 7.11 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/virtual-centers', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_environment_properties(self) -> dict:
        """Retrieves the environment settings.

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/environment-properties', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_settings(self) -> dict:
        """Retrieves the environment settings.

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/settings', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_settings_feature(self) -> dict:
        """Retrieves the feature settings.

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/settings/feature', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_settings_general(self) -> dict:
        """Retrieves the general settings.

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/settings/general', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_settings_security(self) -> dict:
        """Retrieves the security settings.

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/settings/security', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def update_settings_general(self,settings: dict):
        """Updates the general settings.

        Requires a dictionary with updated settings.
        AVailablke settings can be retreived using get_settings_general()
        Available for Horizon 7.12 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        config = self.get_settings_general()
        for key, value in settings.items():
            if key in config:
                config[key] = value
            else:
                error_key = key
                raise Exception(f"{error_key} is not a valid setting")

        json_data = json.dumps(config)
        response = requests.put(f'{self.url}/rest/config/v1/settings/general', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status_code

    def update_settings_feature(self,settings: dict):
        """Updates the feature settings.

        Requires a dictionary with updated settings.
        Available settings can be retreived using get_settings_feature()
        Available for Horizon 7.12 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        config = self.get_settings_feature()
        for key, value in settings.items():
            if key in config:
                config[key] = value
            else:
                error_key = key
                raise Exception(f"{error_key} is not a valid setting")

        json_data = json.dumps(config)
        response = requests.put(f'{self.url}/rest/config/v1/settings/feature', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status_code

    def update_settings_security(self,settings: dict):
        """Updates the security settings.

        Requires a dictionary with updated settings.
        Available settings can be retreived using get_settings_security()
        Available for Horizon 7.12 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        config = self.get_settings_security()
        for key, value in settings.items():
            if key in config:
                config[key] = value
            else:
                error_key = key
                raise Exception(f"{error_key} is not a valid setting")

        json_data = json.dumps(config)
        response = requests.put(f'{self.url}/rest/config/v1/settings/security', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status

    def update_settings(self,settings: dict):
        """Updates the settings.

        Requires a dictionary with updated settings.
        Available settings can be retreived using get_settings()
        Available for Horizon 7.12 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        config = self.get_settings()
        for key, value in settings.items():
            if key in config:
                config[key] = value
            else:
                error_key = key
                raise Exception(f"{error_key} is not a valid setting")

        json_data = json.dumps(config)
        response = requests.put(f'{self.url}/rest/config/v1/settings', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status

class External:
    def __init__(self, url: str, access_token: dict):
        """Default object for the External class for resources that are external to Horizon environment."""
        self.url = url
        self.access_token = access_token

    def get_ad_domains(self) -> list:
        """Lists information related to AD Domains of the environment.

        Available for Horizon 7.11 and later."""
        response = requests.get(f'{self.url}/rest/external/v1/ad-domains', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_base_vms(self, vcenter_id : str,filter_incompatible_vms: bool="", datacenter_id:str="" ) -> list:
        """Lists all the VMs from a vCenter or a datacenter in that vCenter which may be suitable as snapshots for instant/linked clone desktop or farm creation.

        Requires vcenter_id, optionally datacenter id and since Horizon 2012 filter_incompatible_vms was added (defaults to false)
        Available for Horizon 7.12 and later and Horizon 8 2012 for filter_incompatible_vms."""

        if (filter_incompatible_vms == True or filter_incompatible_vms == False) and datacenter_id != "":
            response = requests.get(f'{self.url}/rest/external/v1/base-vms?datacenter_id={datacenter_id}&filter_incompatible_vms={filter_incompatible_vms}&vcenter_id={vcenter_id}', verify=False,  headers=self.access_token)
        elif (filter_incompatible_vms != True or filter_incompatible_vms != False) and datacenter_id != "":
            response = requests.get(f'{self.url}/rest/external/v1/base-vms?filter_incompatible_vms={filter_incompatible_vms}&vcenter_id={vcenter_id}', verify=False,  headers=self.access_token)
        elif datacenter_id != "":
            response = requests.get(f'{self.url}/rest/external/v1/base-vms?datacenter_id={datacenter_id}&vcenter_id={vcenter_id}', verify=False,  headers=self.access_token)
        else:
            response = requests.get(f'{self.url}/rest/external/v1/base-vms?vcenter_id={vcenter_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_base_snapshots(self, vcenter_id : str, base_vm_id:str ) -> list:
        """Lists all the VM snapshots from the vCenter for a given VM.

        Requires vcenter_id and base_vm_id
        Available for Horizon 8 2006."""

        response = requests.get(f'{self.url}/rest/external/v1/base-snapshots?base_vm_id={base_vm_id}&vcenter_id={vcenter_id}', verify=False,  headers=self.access_token)

        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_customization_specifications(self, vcenter_id : str) -> list:
        """Lists all the customization specifications from the vCenter.

        Requires vcenter_id
        Available for Horizon 8 2006."""

        response = requests.get(f'{self.url}/rest/external/v1/customization-specifications?vcenter_id={vcenter_id}', verify=False,  headers=self.access_token)

        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_datacenters(self, vcenter_id: str) -> list:
        """Lists all the datacenters of a vCenter.

        Requires vcenter_id
        Available for Horizon 7.12 and later."""

        response = requests.get(f'{self.url}/rest/external/v1/datacenters?vcenter_id={vcenter_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_hosts_or_clusters(self, vcenter_id : str, datacenter_id:str) -> list:
        """Lists all the hosts or clusters of the datacenter.

        Requires vcenter_id and datacenter id
        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/external/v1/hosts-or-clusters?datacenter_id={datacenter_id}&vcenter_id={vcenter_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_vm_templates(self, vcenter_id : str, datacenter_id:str="" ) -> list:
        """Lists all the VM templates from a vCenter or a datacenter for the given vCenter which may be suitable for full clone desktop pool creation.

        Requires vcenter_id and datacenter id
        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/external/v1/vm-templates?datacenter_id={datacenter_id}&vcenter_id={vcenter_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_ad_users_or_groups(self, maxpagesize:int=100, filter:dict="", group_only:bool = "") -> list:
        """Lists AD users or groups information

        If group_only is passed as True only groups are returned, if users_only is passed as False only users are returned. If both are passed a True an error will be raised.
        Supports pagination and filtering
        Available for Horizon 7.12 and later."""
        def int_get_ad_users_or_groups(self, page:int, maxpagesize: int, filter:list="", group_only: bool="") ->list:
            if filter != "" and (group_only == True or group_only == False):
                print("1")
                filter_url = urllib.parse.quote(json.dumps(filter,separators=(', ', ':')))
                url_filter = f"?filter={filter_url}&group_only={group_only}&page={page}&size={maxpagesize}"
            elif filter == "" and (group_only == True or group_only == False):
                print("2")
                url_filter = f"?group_only={group_only}&page={page}&size={maxpagesize}"
            elif filter != "" and not (group_only == True or group_only == False):
                print("3")
                filter_url = urllib.parse.quote(json.dumps(filter,separators=(', ', ':')))
                url_filter = f"?filter={filter_url}&page={page}&size={maxpagesize}"
            else:
                print("4")
                url_filter = f"?page={page}&size={maxpagesize}"
            response = requests.get(f'{self.url}/rest/external/v1/ad-users-or-groups{url_filter}', verify=False, headers=self.access_token)
            if response.status_code == 400:
                error_message = (response.json())["error_message"]
                raise Exception(f"Error {response.status_code}: {error_message}")
            elif response.status_code != 200:
                raise Exception(f"Error {response.status_code}: {response.reason}")
            else:
                try:
                    response.raise_for_status()
                except requests.exceptions.RequestException as e:
                    raise "Error: " + str(e)
                else:
                    return response
        if maxpagesize > 1000:
            maxpagesize = 1000
        page = 1
        response = int_get_ad_users_or_groups(self,page = page, maxpagesize= maxpagesize,filter = filter, group_only = group_only)
        results = response.json()
        while 'HAS_MORE_RECORDS' in response.headers:
            page += 1
            response = int_get_ad_users_or_groups(self,page = page, maxpagesize= maxpagesize,filter = filter, group_only = group_only)
            results += response.json()
        return results

    def get_ad_users_or_group(self, id) -> dict:
        """Get information related to AD User or Group.

        Requires id of the user object
        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/external/v1/ad-users-or-groups/{id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_datastores(self, vcenter_id : str, host_or_cluster_id:str ) -> list:
        """Lists all the datastoress from the vCenter for the given host or cluster.

        Requires host_or_cluster_id and vcenter_id
        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/external/v1/datastores?host_or_cluster_id={host_or_cluster_id}&vcenter_id={vcenter_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_datastore_paths(self, vcenter_id : str, datastore_id:str ) -> list:
        """Lists all the folder paths within a Datastore from vCenter.

        Requires datastore_id and vcenter_id
        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/external/v1/datastore-paths?datastore_id={datastore_id}&vcenter_id={vcenter_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_network_labels(self, vcenter_id : str, host_or_cluster_id:str, network_type:str = "" ) -> list:
        """Retrieves all network labels on the given host or cluster.

        Requires host_or_cluster_id, vcenter_id and optionally a network type.
        Valid options for network_type are: NETWORK, OPAQUE_NETWORK, DISTRUBUTED_VIRTUAL_PORT_GROUP
        Available for Horizon 8 2006 and later."""
        if network_type == "":
            response = requests.get(f'{self.url}/rest/external/v1/network-labels?host_or_cluster_id={host_or_cluster_id}&vcenter_id={vcenter_id}', verify=False,  headers=self.access_token)
        elif network_type == "NETWORK" or network_type == "OPAQUE_NETWORK" or network_type == "DISTRUBUTED_VIRTUAL_PORT_GROUP":
            response = requests.get(f'{self.url}/rest/external/v1/network-labels?host_or_cluster_id={host_or_cluster_id}&network_type={network_type}&vcenter_id={vcenter_id}', verify=False,  headers=self.access_token)
        else:
            raise(f"{network_type} is not a valid network type try NETWORK, OPAQUE_NETWORK or DISTRUBUTED_VIRTUAL_PORT_GROUP")
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_resource_pools(self, vcenter_id : str, host_or_cluster_id:str) -> list:
        """Lists all the resource pools from the vCenter for the given host or cluster.

        Requires host_or_cluster_id and vcenter_id.
        Available for Horizon 8 2006 and later."""

        response = requests.get(f'{self.url}/rest/external/v1/resource-pools?host_or_cluster_id={host_or_cluster_id}&vcenter_id={vcenter_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_vm_folders(self, vcenter_id : str, datacenter_id:str) -> list:
        """Lists all the VM folders from the vCenter for the given datacenter.

        Requires datacenter_id and vcenter_id.
        Available for Horizon 8 2006 and later."""

        response = requests.get(f'{self.url}/rest/external/v1/vm-folders?datacenter_id={datacenter_id}&vcenter_id={vcenter_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_network_interface_cards(self, vcenter_id : str, base_snapshot_id:str = "", base_vm_id:str = "",vm_template_id:str = ""  ) -> list:
        """Returns a list of network interface cards (NICs) suitable for configuration on a desktop pool/farm.

        Requires vcenter_id and either vm_template_id or (base_vm_id and base_snapshot_id).
        Available for Horizon 8 2006 and later."""
        if base_snapshot_id != "" and base_vm_id != "" and vm_template_id != "":
            raise("When VM template is specified, base VM and snapshot cannot be specified.")
        elif base_snapshot_id != "" and base_vm_id != "" and vm_template_id == "":
            response = requests.get(f'{self.url}/rest/external/v1/network-interface-cards?base_snapshot_id={base_snapshot_id}&base_vm_id={base_vm_id}&vcenter_id={vcenter_id}', verify=False,  headers=self.access_token)
        elif base_snapshot_id == "" and base_vm_id == "" and vm_template_id != "":
            response = requests.get(f'{self.url}/rest/external/v1/network-interface-cards?vcenter_id={vcenter_id}&vm_template_id={vm_template_id}', verify=False,  headers=self.access_token)
        else:
            raise("Either VM template or (base VM with snapshot) are required for fetching network interface cards.")
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()