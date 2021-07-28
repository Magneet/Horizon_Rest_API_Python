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

    def get_desktop_pool_installed_applications(self, desktop_pool_id: str) -> list:
        """Lists the installed applications on the given desktop pool.

        Requires id of a desktop pool
        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/desktop-pools/{desktop_pool_id}/installed-applications', verify=False,  headers=self.access_token)
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

    def get_farm_installed_applications(self, farm_id:str) -> list:
        """Lists the installed applications on the given farm.

        Requires id of a RDS Farm
        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/farms/{farm_id}/installed-applications', verify=False,  headers=self.access_token)
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

    def new_farm(self,farm_data:dict):
        """Creates a farm.

        Requires farm_data as a dict
        Available for Horizon 8 2103 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(farm_data)
        response = requests.post(f'{self.url}/rest/inventory/v1/farms', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code == 401:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code == 403:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code == 409:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 201:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status_code

    def update_farm(self,farm_data : dict, farm_id : str):
        """Updates a farm.

        Requires farm_data as a dict
        Available for Horizon 8 2103 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(farm_data)
        response = requests.put(f'{self.url}rest/inventory/v1/farms/{farm_id}', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code == 401:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code == 403:
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

    def delete_farm(self, farm_id:str) -> list:
        """Deletes a farm.

        Requires id of a RDS Farm
        Available for Horizon 8 2103 and later."""
        response = requests.delete(f'{self.url}/rest/inventory/v1/farms/{farm_id}', verify=False,  headers=self.access_token)
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

    def check_farm_name_availability(self,farm_name: str)-> dict:
        """Checks if the given name is available for farm creation.

        Requires the name of the RDS farm to test as string
        Available for Horizon 8 2103 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["name"] = farm_name
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/inventory/v1/farms/action/check-name-availability', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 409:
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

        def int_get_machines(self, page:int, maxpagesize: int, filter:dict="") ->list:
            if filter != "":
                filter_url = urllib.parse.quote(json.dumps(filter,separators=(', ', ':')))
                add_filter = f"{filter_url}"
                response = requests.get(f'{self.url}/rest/inventory/v1/machines?filter={add_filter}&page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
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
        response = requests.delete(f'{self.url}/rest/inventory/v1/machines/{machine_id}', verify=False,  headers=headers, data=json_data)
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
        response = requests.delete(f'{self.url}/rest/inventory/v1/machines', verify=False,  headers=headers, data=json_data)
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
        response = requests.post(f'{self.url}/rest/inventory/v1/machines/action/enter-maintenance', verify=False,  headers=headers, data=json_data)
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
        response = requests.post(f'{self.url}/rest/inventory/v1/machines/action/exit-maintenance', verify=False,  headers=headers, data=json_data)
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
        response = requests.post(f'{self.url}/rest/inventory/v1/machines/action/rebuild', verify=False,  headers=headers, data=json_data)
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
        response = requests.post(f'{self.url}/rest/inventory/v1/machines/action/recover', verify=False,  headers=headers, data=json_data)
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
        response = requests.post(f'{self.url}/rest/inventory/v1/machines/action/reset', verify=False,  headers=headers, data=json_data)
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
        response = requests.post(f'{self.url}/rest/inventory/v1/machines/action/restart', verify=False,  headers=headers, data=json_data)
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

    def check_machine_name_availability(self,machine_name: str)-> dict:
        """Checks if the given name is available for machine creation.

        Requires the name of the application to test as string
        Available for Horizon 8 2103 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["name"] = machine_name
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/inventory/v1/machines/action/check-name-availability', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 409:
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

    def get_sessions(self, filter:dict="", maxpagesize:int=100) -> list:
        """Lists the Session information in the environment.

        Will default to 1000 results with a pagesize of 100, max pagesize is 1000.
        Available for Horizon 8 2006 and later, filtering available since Horizon 2103."""

        def int_get_sessions(self, page:int, maxpagesize: int, filter:dict="") ->list:
            if filter !="":
                filter_url = urllib.parse.quote(json.dumps(filter,separators=(', ', ':')))
                add_filter = f"{filter_url}"
                response = requests.get(f'{self.url}/rest/inventory/v1/sessions?filter={add_filter}&page={page}&size={maxpagesize}', verify=False,  headers=self.access_token)
            else:
                response = requests.get(f'{self.url}/rest/inventory/v1/sessions?page={page}&size={maxpagesize}', verify=False,  headers=self.access_token)

            # response = requests.get(f'{self.url}/rest/inventory/v1/sessions?page={page}&size={maxpagesize}', verify=False,  headers=self.access_token)
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
        response = int_get_sessions(self,page = page, maxpagesize= maxpagesize, filter= filter)
        results = response.json()
        while 'HAS_MORE_RECORDS' in response.headers:
            page += 1
            response = int_get_sessions(self,page = page, maxpagesize= maxpagesize, filter= filter)
            results += response.json()
        return results

    def get_session(self, session_id: str) -> dict:
        """Gets the Session information.

        Requires session_id
        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/sessions/{session_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def disconnect_sessions(self, session_ids: list):
        """Disconnects user sessions.

        Requires list of session ids
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(session_ids)
        response = requests.post(f'{self.url}/rest/inventory/v1/sessions/action/disconnect', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def logoff_sessions(self, session_ids: list, forced_logoff:bool=False):
        """Logs user sessions off.

        Requires list of session ids optional to set forced to True to force a log off (defaults to False)
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(session_ids)
        response = requests.post(f'{self.url}/rest/inventory/v1/sessions/action/logoff?forced={forced_logoff}', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def reset_session_machines(self, session_ids: list):
        """Resets machine of user sessions. The machine must be managed by Virtual Center and the session cannot be an application or an RDS desktop session.

        Requires list of session ids
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(session_ids)
        response = requests.post(f'{self.url}/rest/inventory/v1/sessions/action/reset', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def restart_session_machines(self, session_ids: list):
        """Restarts machine of user sessions. The machine must be managed by Virtual Center and the session cannot be an application or an RDS desktop session.

        Requires list of session ids
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(session_ids)
        response = requests.post(f'{self.url}/rest/inventory/v1/sessions/action/reset', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def send_message_sessions(self, session_ids: list, message:str, message_type:str="INFO"):
        """Sends the message to user sessions

        Requires list of session ids, message type (INFO,WARNING,ERROR) and a message
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data={}
        data["message"] = message
        data["message_type"] = message_type
        data["session_ids"] = session_ids
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/inventory/v1/sessions/action/send-message', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_messages"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
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
                if "error_messages" in response.json():
                    error_message = (response.json())["error_messages"]
                else:
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
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
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
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
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
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status_code

    def get_application_icons(self, application_pool_id: str) -> list:
        """Lists the application icons for the given application pool.

        Requires Application_pool_id
        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/application-icons?application_pool_id={application_pool_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def get_application_icon(self, application_icon_id: str) -> dict:
        """Gets application icon

        Requires application_icon_id
        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/application-icons/{application_icon_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def new_application_icon(self,data : str,height : str,width : str) -> dict:
        """Creates an application icon.

        Requires data, width and height as string
        Data needs to be Base64 encoded binary data of the image
        Available for Horizon 8 2103 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        raw_data={}
        raw_data["data"] = data
        raw_data["height"] = height
        raw_data["width"] = width
        json_data = json.dumps(raw_data)
        response = requests.post(f'{self.url}/rest/inventory/v1/application-icons', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
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
                return response.json()

    def set_application_pool_icon(self,application_pool_id : str, icon_id : str):
        """Associates a custom icon to the application pool.

        Requires application_pool_id and asicon_id as string
        Available for Horizon 8 2103 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data={}
        data["icon_id"] = icon_id
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/inventory/v1/application-pools/{application_pool_id}/action/add-custom-icon', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 401:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status_code

    def delete_application_pool_icon(self,application_pool_id : str):
        """Removes the associated custom icon from the application pool.

        Requires application_pool_id as string
        Available for Horizon 8 2103 and later."""
        response = requests.post(f'{self.url}/rest/inventory/v1/application-pools/{application_pool_id}/action/remove-custom-icon', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 401:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status_code

    def remove_machines(self, desktop_pool_id:str,machine_ids: list):
        """Removes machines from the given manual desktop pool.

        Requires list of machine_ids and desktop_pool_id to remove them from
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(machine_ids)
        response = requests.post(f'{self.url}/rest/inventory/v1/desktop-pools/{desktop_pool_id}/action/remove-machines', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def add_machines(self, desktop_pool_id:str,machine_ids: list):
        """Adds machines to the given manual desktop pool.

        Requires list of machine_ids and desktop_pool_id to add them to
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(machine_ids)
        response = requests.post(f'{self.url}/rest/inventory/v1/desktop-pools/{desktop_pool_id}/action/add-machines', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def add_machines_by_name(self, desktop_pool_id:str, machine_data: list):
        """Adds machines to the given manual desktop pool.

        Requires requires desktop_pool_id and list of of dicts where each dict has name and user_id.
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(machine_data)
        response = requests.post(f'{self.url}/rest/inventory/v1/desktop-pools/{desktop_pool_id}/action/add-machines-by-name', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def assign_user_to_machine(self, machine_id:str, user_ids: list):
        """Assigns the specified users to the machine.

        Requires machine_id of the machine and list of user_ids.
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(user_ids)
        response = requests.post(f'{self.url}/rest/inventory/v1/machines/{machine_id}/action/assign-users', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def unassign_user_to_machine(self, machine_id:str, user_ids: list):
        """Unassigns the specified users to the machine.

        Requires machine_id of the machine and list of user_ids.
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(user_ids)
        response = requests.post(f'{self.url}/rest/inventory/v1/machines/{machine_id}/action/unassign-users', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_global_desktop_entitlement(self, global_desktop_entitlement_id:str) -> dict:
        """Gets the Global Desktop Entitlement in the environment.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/global-desktop-entitlements/{global_desktop_entitlement_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def get_global_desktop_entitlements(self, maxpagesize:int=100, filter:dict="") -> list:
        """Lists the Global Application Entitlements in the environment.

        For information on filtering see https://vdc-download.vmware.com/vmwb-repository/dcr-public/f92cce4b-9762-4ed0-acbd-f1d0591bd739/235dc19c-dabd-43f2-8d38-8a7a333e914e/HorizonServerRESTPaginationAndFilterGuide.doc
        Available for Horizon 8 2006 and later."""

        def int_get_global_desktop_entitlements(self, page:int, maxpagesize: int, filter:list="") ->list:
            if filter != "":
                add_filter = urllib.parse.quote(json.dumps(filter,separators=(', ', ':')))
                response = requests.get(f'{self.url}/rest/inventory/v1/global-desktop-entitlements?filter={add_filter}&page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            else:
                response = requests.get(f'{self.url}/rest/inventory/v1/global-desktop-entitlements?page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            if response.status_code == 400:
                if "error_messages" in response.json():
                    error_message = (response.json())["error_messages"]
                else:
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
        response = int_get_global_desktop_entitlements(self,page = page, maxpagesize= maxpagesize,filter = filter)
        results = response.json()
        while 'HAS_MORE_RECORDS' in response.headers:
            page += 1
            response = int_get_global_desktop_entitlements(self,page = page, maxpagesize= maxpagesize, filter = filter)
            results += response.json()
        return results

    def add_global_desktop_entitlement(self, global_desktop_entitlement_data: dict):
        """Creates a Global Desktop Entitlement.

        Requires global_desktop_entitlement_data as a dict
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(global_desktop_entitlement_data)
        response = requests.post(f'{self.url}/rest/inventory/v1/global-desktop-entitlements', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 201:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def get_global_desktop_entitlement_compatible_desktop_pools(self, global_desktop_entitlement_id:str) -> list:
        """Lists Local Application Pools which are compatible with Global Application Entitlement.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/global-desktop-entitlements/{global_desktop_entitlement_id}/compatible-local-desktop-pools', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def add_global_desktop_entitlement_local_desktop_pools(self, global_desktop_entitlement_id:str, desktop_pool_ids: list):
        """Adds a local desktop pool to a GLobal desktop Entitlement

        Requires global_desktop_entitlement_id as a string and desktop_pool_ids as a list
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(desktop_pool_ids)
        response = requests.post(f'{self.url}/rest/inventory/v1/global-desktop-entitlements/{global_desktop_entitlement_id}/local-desktop-pools', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_global_desktop_entitlement_local_desktop_pools(self, global_desktop_entitlement_id:str) -> list:
        """Lists Local Desktop Pools which are assigned to Global Desktop Entitlement.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/global-desktop-entitlements/{global_desktop_entitlement_id}/local-desktop-pools', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def remove_global_desktop_entitlement_local_desktop_pools(self, global_desktop_entitlement_id:str, desktop_pool_ids: list):
        """Removes Local Desktop Pools from Global Desktop Entitlement.

        Requires global_desktop_entitlement_id as a string and desktop_pool_ids as a list
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(desktop_pool_ids)
        response = requests.delete(f'{self.url}/rest/inventory/v1/global-desktop-entitlements/{global_desktop_entitlement_id}/local-desktop-pools', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_global_application_entitlement(self, global_application_entitlement_id:str) -> dict:
        """Gets the Global Application Entitlement in the environment.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/global-application-entitlements/{global_application_entitlement_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def get_global_application_entitlements(self, maxpagesize:int=100, filter:dict="") -> list:
        """Lists the Global Application Entitlements in the environment.

        For information on filtering see https://vdc-download.vmware.com/vmwb-repository/dcr-public/f92cce4b-9762-4ed0-acbd-f1d0591bd739/235dc19c-dabd-43f2-8d38-8a7a333e914e/HorizonServerRESTPaginationAndFilterGuide.doc
        Available for Horizon 8 2006 and later."""

        def int_get_global_application_entitlements(self, page:int, maxpagesize: int, filter:list="") ->list:
            if filter != "":
                add_filter = urllib.parse.quote(json.dumps(filter,separators=(', ', ':')))
                response = requests.get(f'{self.url}/rest/inventory/v1/global-application-entitlements?filter={add_filter}&page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            else:
                response = requests.get(f'{self.url}/rest/inventory/v1/global-application-entitlements?page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            if response.status_code == 400:
                if "error_messages" in response.json():
                    error_message = (response.json())["error_messages"]
                else:
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
        response = int_get_global_application_entitlements(self,page = page, maxpagesize= maxpagesize,filter = filter)
        results = response.json()
        while 'HAS_MORE_RECORDS' in response.headers:
            page += 1
            response = int_get_global_application_entitlements(self,page = page, maxpagesize= maxpagesize, filter = filter)
            results += response.json()
        return results

    def get_global_application_entitlement_compatible_application_pools(self, global_application_entitlement_id:str) -> list:
        """Lists Local Application Pools which are compatible with Global Application Entitlement.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/global-application-entitlements/{global_application_entitlement_id}/compatible-local-application-pools', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def add_global_application_entitlement_local_Application_pools(self, global_application_entitlement_id:str, application_pool_ids: list):
        """Adds a local Application pool to a GLobal Application Entitlement

        Requires global_application_entitlement_id as a string and application_pool_ids as a list
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(application_pool_ids)
        response = requests.post(f'{self.url}/rest/inventory/v1/global-application-entitlements/{global_application_entitlement_id}/local-application-pools', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_global_application_entitlement_local_Application_pools(self, global_application_entitlement_id:str) -> list:
        """Lists Local Application Pools which are assigned to Global Application Entitlement.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/global-application-entitlements/{global_application_entitlement_id}/local-application-pools', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def remove_global_application_entitlement_local_Application_pools(self, global_application_entitlement_id:str, application_pool_ids: list):
        """Removes Local Application Pools from Global Application Entitlement.

        Requires global_application_entitlement_id as a string and application_pool_ids as a list
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(application_pool_ids)
        response = requests.delete(f'{self.url}/rest/inventory/v1/global-application-entitlements/{global_application_entitlement_id}/local-application-pools', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def desktop_pool_push_image(self, desktop_pool_id:str, start_time:str, add_virtual_tpm:bool=False, im_stream_id:str="",im_tag_id:str="",logoff_policy:str="WAIT_FOR_LOGOFF",parent_vm_id:str="",snapshot_id:str="", stop_on_first_error:bool=True):
        """Schedule/reschedule a request to update the image in an instant clone desktop pool

        Requires start_time in epoch, desktop_pool_id as string and either im_stream_id and im_tag_id OR parent_vm_id and snapshit_id as string.
        Optional: stop_on_first_error as bool, add_virtual_tpm as bool, logoff_policy as string with these options: FORCE_LOGOFF or WAIT_FOR_LOGOFF
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        if add_virtual_tpm !=False:
            data["add_virtual_tpm"] = add_virtual_tpm
        if im_stream_id != "" and im_tag_id !="":
            data["im_stream_id"] = im_stream_id
            data["im_tag_id"] = im_tag_id
        data["logoff_policy"] = logoff_policy
        if parent_vm_id != "" and snapshot_id !="":
            data["parent_vm_id"] = parent_vm_id
            data["snapshot_id"] = snapshot_id
        data["start_time"]= start_time
        data["stop_on_first_error"] = stop_on_first_error
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/inventory/v1/desktop-pools/{desktop_pool_id}/action/schedule-push-image', verify=False,  headers=headers, data = json_data)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 403:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def cancel_desktop_pool_push_image(self, desktop_pool_id:str):
        """Lists Local Application Pools which are assigned to Global Application Entitlement.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/desktop-pools/{desktop_pool_id}/action/cancel-scheduled-push-image', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 403:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def get_rds_servers(self, maxpagesize:int=100, filter:dict="") -> list:
        """Lists the RDS Servers in the environment.

        For information on filtering see https://vdc-download.vmware.com/vmwb-repository/dcr-public/f92cce4b-9762-4ed0-acbd-f1d0591bd739/235dc19c-dabd-43f2-8d38-8a7a333e914e/HorizonServerRESTPaginationAndFilterGuide.doc
        Available for Horizon 8 2012 and later."""

        def int_get_rds_servers(self, page:int, maxpagesize: int, filter:list="") ->list:
            if filter != "":
                add_filter = urllib.parse.quote(json.dumps(filter,separators=(', ', ':')))
                response = requests.get(f'{self.url}/rest/inventory/v1/rds-servers?filter={add_filter}&page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            else:
                response = requests.get(f'{self.url}/rest/inventory/v1/rds-servers?page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            if response.status_code == 400:
                if "error_messages" in response.json():
                    error_message = (response.json())["error_messages"]
                else:
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
        response = int_get_rds_servers(self,page = page, maxpagesize= maxpagesize,filter = filter)
        results = response.json()
        while 'HAS_MORE_RECORDS' in response.headers:
            page += 1
            response = int_get_rds_servers(self,page = page, maxpagesize= maxpagesize, filter = filter)
            results += response.json()
        return results

    def get_rds_server(self, rds_server_id:str) -> dict:
        """Gets the RDS Server information.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/rds-servers/{rds_server_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def delete_rds_server(self, rds_server_id:str) -> dict:
        """Deletes the RDS Server.

        Available for Horizon 8 2012 and later."""
        response = requests.delete(f'{self.url}/rest/inventory/v1/rds-servers/{rds_server_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 403:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def recover_rds_servers(self, rds_server_ids:list) -> list:
        """Recovers the specified RDS Servers.

        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = rds_server_ids
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/inventory/v1/rds-servers/action/recover', verify=False,  headers=headers, data = json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def update_rds_server(self, rds_server_id:str, max_sessions_count_configured:int,max_sessions_type_configured:str, enabled:bool=True):
        """Schedule/reschedule a request to update the image in an instant clone desktop pool

        Requires the rds_server_id as string, enabled as booleanm max_sessions_count_configured as int and max_sessions_type_configured as string
        enabled defaults to True, the options for max_sessions_type_configured are: UNLIMITED, LIMITED, UNCONFIGURED
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["enabled"] = enabled
        data["max_sessions_count_configured"] = max_sessions_count_configured
        data["max_sessions_type_configured"] = max_sessions_type_configured
        json_data = json.dumps(data)
        response = requests.put(f'{self.url}/rest/inventory/v1/rds-servers/{rds_server_id}', verify=False,  headers=headers, data = json_data)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 403:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def add_rds_server(self,description: str, dns_name: str, operating_system: str, farm_id: str):
        """Registers the RDS Server.

        Requires description, dns_name, operating_system and farm_id as string
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["description"] = description
        data["dns_name"] = dns_name
        data["farm_id"] = farm_id
        data["operating_system"] = operating_system
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/inventory/v1/rds-servers/action/register', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 409:
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

    def check_rds_server_name_availability(self,machine_name: str)-> dict:
        """Checks if the given prefix is available for RDS Server creation.

        Requires the name of the RDS Server to test as string
        Available for Horizon 8 2103 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["name"] = machine_name
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/inventory/v1/rds-servers/action/check-name-availability', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 409:
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

    def get_physical_machines(self, maxpagesize:int=100, filter:dict="") -> list:
        """Lists the Physical Machines in the environment.

        For information on filtering see https://vdc-download.vmware.com/vmwb-repository/dcr-public/f92cce4b-9762-4ed0-acbd-f1d0591bd739/235dc19c-dabd-43f2-8d38-8a7a333e914e/HorizonServerRESTPaginationAndFilterGuide.doc
        Available for Horizon 8 2012 and later."""

        def int_get_physical_machines(self, page:int, maxpagesize: int, filter:list="") ->list:
            if filter != "":
                add_filter = urllib.parse.quote(json.dumps(filter,separators=(', ', ':')))
                response = requests.get(f'{self.url}/rest/inventory/v1/physical-machines?filter={add_filter}&page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            else:
                response = requests.get(f'{self.url}/rest/inventory/v1/physical-machines?page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            if response.status_code == 400:
                if "error_messages" in response.json():
                    error_message = (response.json())["error_messages"]
                else:
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
                    return response
        if maxpagesize > 1000:
            maxpagesize = 1000
        page = 1
        response = int_get_physical_machines(self,page = page, maxpagesize= maxpagesize,filter = filter)
        results = response.json()
        while 'HAS_MORE_RECORDS' in response.headers:
            page += 1
            response = int_get_physical_machines(self,page = page, maxpagesize= maxpagesize, filter = filter)
            results += response.json()
        return results

    def get_physical_machine(self, physical_machine_id:str) -> dict:
        """Gets the Physical Machine information.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/physical-machines/{physical_machine_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def delete_physical_machine(self, physical_machine_id:str):
        """Deletes the Physical Machine.

        Available for Horizon 8 2012 and later."""
        response = requests.delete(f'{self.url}/rest/inventory/v1/physical-machines/{physical_machine_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 403:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def add_physical_machine(self,description: str, dns_name: str, operating_system: str):
        """Registers the Physical Machine.

        Requires ad_domain_id, username and password in plain text.
        Available for Horizon 7.11 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["description"] = description
        data["dns_name"] = dns_name
        data["operating_system"] = operating_system
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/inventory/v1/physical-machines/action/register', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 409:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def get_desktop_pool_tasks(self, desktop_pool_id:str) -> list:
        """Lists the tasks on the desktop pool.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/desktop-pools/{desktop_pool_id}/tasks', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def get_desktop_pool_task(self, desktop_pool_id:str, task_id:str) -> dict:
        """Gets the task information on the desktop pool.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/inventory/v1/desktop-pools/{desktop_pool_id}/tasks/{task_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def cancel_desktop_pool_task(self, desktop_pool_id:str, task_id:str) -> dict:
        """Cancels the instant clone desktop pool push image task.

        Available for Horizon 8 2012 and later."""
        response = requests.post(f'{self.url}/rest/inventory/v1/desktop-pools/{desktop_pool_id}/tasks/{task_id}/action/cancel', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def check_application_name_availability(self,application_name: str)-> dict:
        """Checks if the given name is available for application pool creation.

        Requires the name of the application to test as string
        Available for Horizon 8 2103 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["name"] = application_name
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/inventory/v1/application-pools/action/check-name-availability', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 409:
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

    def check_desktop_pool_name_availability(self,desktop_pool_name: str)-> dict:
        """Checks if the given name is available for desktop pool creation.

        Requires the name of the desktop pool to test as string
        Available for Horizon 8 2103 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["name"] = desktop_pool_name
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/inventory/v1/desktop-pools/action/check-name-availability', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 409:
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

    def check_farm_name_availability(self,farm_name: str)-> dict:
        """Checks if the given name is available for farm creation.

        Requires the name of the farm to test as string
        Available for Horizon 8 2103 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["name"] = farm_name
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/inventory/v1/farms/action/check-name-availability', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 409:
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

    def get_desktop_pool_metrics(self, desktop_pool_ids:list) -> list:
        """Lists metrics of desktop pools (except RDS desktop pools).

        Available for Horizon 8 2012 and later."""
        urlstring='&ids='.join(desktop_pool_ids)
        response = requests.get(f'{self.url}/rest/monitor/v1/desktop-pools/metrics?ids={urlstring}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
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
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
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

    def get_local_access_groups(self) -> list:
        """Lists all local access groups.

        Available for Horizon 8 2103 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/local-access-groups', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_local_access_group(self,local_access_group_id: str) -> dict:
        """Retrieves a local access group.

        Requires the id of an local access group as string
        Available for Horizon 8 2103 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/local-access-groups/{local_access_group_id}', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_im_assets(self,im_version_id : str) ->list:
        """Lists image management assets.

        Requires im_version_id  as string
        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/im-assets?im_version_id={im_version_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_im_asset(self,im_asset_id : str) ->dict:
        """Gets image management asset.

        Requires im_version_id  as string
        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/im-assets/{im_asset_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_im_streams(self) -> list:
        """Lists image management streams.

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/im-streams', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_im_stream(self, im_stream_id : str) -> dict:
        """Gets image management stream.

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/im-streams/{im_stream_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_im_tags(self, im_stream_id : str) -> list:
        """Lists image management tags.

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/im-tags?im_stream_id={im_stream_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_im_tag(self, im_tag_id : str) -> dict:
        """Gets image management stream.

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/im-tags/{im_tag_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_im_versions(self, im_stream_id : str) -> list:
        """Lists image management versions.

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/im-versions?im_stream_id={im_stream_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_im_version(self, im_version_id : str) -> dict:
        """Gets image management version.

        Available for Horizon 7.12 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/im-versions/{im_version_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def new_im_asset(self,im_stream_id : str,im_version_id : str, clone_type:str,image_type : str,status : str,vcenter_id : str, 
        additional_details_1:str = "", additional_details_2:str = "", additional_details_3:str = "", base_snapshot_id : str = "", base_vm_id : str = "", vm_template_id: str = "" ):
        """Creates image management asset.

        Requires all as string:
            im_stream_id
            im_version_id
            clone_type : either FULL_CLONE or INSTANT_CLONE
            image_type : RDSH_APPS, RDSH_DESKTOP or VDI_DESKTOP"
            status : AVAILABLE, DEPLOYING_VM, DEPLOYMENT_DONE, DELETED, DISABLED, FAILED, REPLICATING, RETRY_PENDING or SPECIALIZING_VM
            vcenter_id
            Choice between:
                base_snapshot_id and base_vm_id
                OR
                vm_template_id
            Optional:
                additional_details_1
                additional_details_2
                additional_details_3
        Available for Horizon 7.12 and later."""
        valid_image_type = [ "RDSH_APPS", "RDSH_DESKTOP", "VDI_DESKTOP" ]
        valid_status = [ "AVAILABLE", "DEPLOYING_VM", "DEPLOYMENT_DONE", "DELETED", "DISABLED", "FAILED", "REPLICATING", "RETRY_PENDING", "SPECIALIZING_VM" ]
        valid_clone_type = [ "FULL_CLONE", "INSTANT_CLONE" ]
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        additional_details = {}
        additional_details["additionalProp1"] = additional_details_1
        additional_details["additionalProp2"] = additional_details_2
        additional_details["additionalProp3"] = additional_details_3
        data["additional_details"] = additional_details
        if vm_template_id != "" and (base_vm_id != "" or base_snapshot_id != ""):
            raise Exception("Error: either vm_template_id or base_vm_id and base_snapshot_id is required")
        elif vm_template_id == "" and (base_vm_id == "" or base_snapshot_id == ""):
            raise Exception("Error: Both base_vm_id and base_snapshot_id are required")
        elif vm_template_id == "" and (base_vm_id != "" and base_snapshot_id != ""):
            data["base_snapshot_id"] = base_snapshot_id
            data["base_vm_id"] = base_vm_id
        if clone_type in valid_clone_type:
            data["clone_type"] = clone_type
        else:
            raise Exception(f"Error: please provide a valid clone_type from these options: {valid_clone_type}")
        data["im_stream_id"] = im_stream_id
        data["im_version_id"] = im_version_id
        if image_type in valid_image_type:
            data["image_type"] = image_type
        else:
            raise Exception(f"Error: please provide a valid image_type from these options: {valid_image_type}")
        if status in valid_status:
            data["status"] = status
        else:
            raise Exception(f"Error: please provide a valid status from these options: {valid_status}")
        data["vcenter_id"] = vcenter_id
        if vm_template_id != "":
            data["vm_template_id"] = vm_template_id
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/config/v1/im-assets', verify=False,  headers=headers, data=json_data)
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

    def update_im_asset(self,im_asset_id : str, clone_type:str,image_type : str,status : str, additional_details_1:str = "", additional_details_2:str = "", additional_details_3:str = ""):
        """Updates image management asset.

        Requires:
            im_assit_id as string
            clone_type : either FULL_CLONE or INSTANT_CLONE
            image_type : RDSH_APPS, RDSH_DESKTOP or VDI_DESKTOP"
            status : AVAILABLE, DEPLOYING_VM, DEPLOYMENT_DONE, DELETED, DISABLED, FAILED, REPLICATING, RETRY_PENDING or SPECIALIZING_VM
            vcenter_id
            Optional:
                additional_details_1
                additional_details_2
                additional_details_3
        Available for Horizon 7.12 and later."""
        valid_image_type = [ "RDSH_APPS", "RDSH_DESKTOP", "VDI_DESKTOP" ]
        valid_status = [ "AVAILABLE", "DEPLOYING_VM", "DEPLOYMENT_DONE", "DELETED", "DISABLED", "FAILED", "REPLICATING", "RETRY_PENDING", "SPECIALIZING_VM" ]
        valid_clone_type = [ "FULL_CLONE", "INSTANT_CLONE" ]
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        additional_details = {}
        additional_details["additionalProp1"] = additional_details_1
        additional_details["additionalProp2"] = additional_details_2
        additional_details["additionalProp3"] = additional_details_3
        data["additional_details"] = additional_details
        if clone_type in valid_clone_type:
            data["clone_type"] = clone_type
        else:
            raise Exception(f"Error: please provide a valid clone_type from these options: {valid_clone_type}")
        if image_type in valid_image_type:
            data["image_type"] = image_type
        else:
            raise Exception(f"Error: please provide a valid image_type from these options: {valid_image_type}")
        if status in valid_status:
            data["status"] = status
        else:
            raise Exception(f"Error: please provide a valid status from these options: {valid_status}")
        json_data = json.dumps(data)
        response = requests.put(f'{self.url}/rest/config/v1/im-assets/{im_asset_id}', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 409:
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

    def delete_im_asset(self, im_asset_id : str):
        """Deletes image management asset.

        Available for Horizon 7.12 and later."""
        response = requests.delete(f'{self.url}/rest/config/v1/im-assets/{im_asset_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def new_im_tag(self,name : str,im_stream_id : str,im_version_id : str, additional_details_1:str = "", additional_details_2:str = "", additional_details_3:str = ""):
        """Creates image management tag.

        Requires all as string:
            im_stream_id
            im_version_id
            name
            Optional:
                additional_details_1
                additional_details_2
                additional_details_3
        Available for Horizon 7.12 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        additional_details = {}
        additional_details["additionalProp1"] = additional_details_1
        additional_details["additionalProp2"] = additional_details_2
        additional_details["additionalProp3"] = additional_details_3
        data["im_stream_id"] = im_stream_id
        data["im_version_id"] = im_version_id
        data["name"] = name
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/config/v1/im-tags', verify=False,  headers=headers, data=json_data)
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

    def update_im_tag(self,name : str,im_tag_id : str,im_version_id : str, additional_details_1:str = "", additional_details_2:str = "", additional_details_3:str = ""):
        """Updates image management tag.

        Requires all as string:
            im_tag_id
            im_version_id
            name
            Optional:
                additional_details_1
                additional_details_2
                additional_details_3
        Available for Horizon 7.12 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        additional_details = {}
        additional_details["additionalProp1"] = additional_details_1
        additional_details["additionalProp2"] = additional_details_2
        additional_details["additionalProp3"] = additional_details_3
        data["im_version_id"] = im_version_id
        data["name"] = name
        json_data = json.dumps(data)
        response = requests.put(f'{self.url}/rest/config/v1/im-tags/{im_tag_id}', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 409:
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

    def delete_im_tag(self, im_tag_id : str):
        """Deletes image management tag.

        Available for Horizon 7.12 and later."""
        response = requests.delete(f'{self.url}/rest/config/v1/im-tags/{im_tag_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def new_im_stream(self,description : str,name : str, operating_system:str,publisher : str,source : str,status : str, 
        additional_details_1:str = "", additional_details_2:str = "", additional_details_3:str = ""):
        """Creates image management stream.

        Requires all as string:
            description
            name
            operating_system :  UNKNOWN, WINDOWS_XP, WINDOWS_VISTA, WINDOWS_7, WINDOWS_8, WINDOWS_10, WINDOWS_SERVER_2003,
                                WINDOWS_SERVER_2008, WINDOWS_SERVER_2008_R2, WINDOWS_SERVER_2012, WINDOWS_SERVER_2012_R2,
                                WINDOWS_SERVER_2016_OR_ABOVE, LINUX_OTHER, LINUX_SERVER_OTHER, LINUX_UBUNTU, LINUX_RHEL, LINUX_SUSE, LINUX_CENTOS
            status : AVAILABLE, DELETED, DISABLED, FAILED, IN_PROGRESS, PARTIALLY_AVAILABLE, PENDING
            publisher
            source : MARKET_PLACE, UPLOADED, COPIED_FROM_STREAM, COPIED_FROM_VERSION
            Optional:
                additional_details_1
                additional_details_2
                additional_details_3
        Available for Horizon 7.12 and later."""
        valid_operating_system =    [ "UNKNOWN", "WINDOWS_XP", "WINDOWS_VISTA", "WINDOWS_7", "WINDOWS_8", "WINDOWS_10", "WINDOWS_SERVER_2003", 
                                    "WINDOWS_SERVER_2008", "WINDOWS_SERVER_2008_R2", "WINDOWS_SERVER_2012", "WINDOWS_SERVER_2012_R2", "WINDOWS_SERVER_2016_OR_ABOVE", 
                                    "LINUX_OTHER", "LINUX_SERVER_OTHER", "LINUX_UBUNTU", "LINUX_RHEL", "LINUX_SUSE", "LINUX_CENTOS" ]
        valid_status = [ "AVAILABLE", "DELETED", "DISABLED", "FAILED", "IN_PROGRESS", "PARTIALLY_AVAILABLE", "PENDING" ]
        valid_source = [ "MARKET_PLACE", "UPLOADED", "COPIED_FROM_STREAM", "COPIED_FROM_VERSION" ]
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        additional_details = {}
        additional_details["additionalProp1"] = additional_details_1
        additional_details["additionalProp2"] = additional_details_2
        additional_details["additionalProp3"] = additional_details_3
        data["description"] = description
        data["name"] = name
        if operating_system in valid_operating_system:
            data["operating_system"] = operating_system
        else:
            raise Exception(f"Error: please provide a valid operating_system from these options: {valid_operating_system}")
        data["publisher"] = publisher
        if source in valid_source:
            data["source"] = source
        else:
            raise Exception(f"Error: please provide a valid source from these options: {valid_source}")
        if status in valid_status:
            data["status"] = status
        else:
            raise Exception(f"Error: please provide a valid status from these options: {valid_status}")
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/config/v1/im-streams', verify=False,  headers=headers, data=json_data)
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

    def update_im_stream(self,im_stream_id : str, description : str,name : str, operating_system:str,publisher : str,source : str,status : str, 
        additional_details_1:str = "", additional_details_2:str = "", additional_details_3:str = ""):
        """Updates image management stream.

        Requires all as string:
            description
            name
            operating_system :  UNKNOWN, WINDOWS_XP, WINDOWS_VISTA, WINDOWS_7, WINDOWS_8, WINDOWS_10, WINDOWS_SERVER_2003,
                                WINDOWS_SERVER_2008, WINDOWS_SERVER_2008_R2, WINDOWS_SERVER_2012, WINDOWS_SERVER_2012_R2,
                                WINDOWS_SERVER_2016_OR_ABOVE, LINUX_OTHER, LINUX_SERVER_OTHER, LINUX_UBUNTU, LINUX_RHEL, LINUX_SUSE, LINUX_CENTOS
            status : AVAILABLE, DELETED, DISABLED, FAILED, IN_PROGRESS, PARTIALLY_AVAILABLE, PENDING
            publisher
            source : MARKET_PLACE, UPLOADED, COPIED_FROM_STREAM, COPIED_FROM_VERSION
            Optional:
                additional_details_1
                additional_details_2
                additional_details_3
        Available for Horizon 7.12 and later."""
        valid_operating_system =    [ "UNKNOWN", "WINDOWS_XP", "WINDOWS_VISTA", "WINDOWS_7", "WINDOWS_8", "WINDOWS_10", "WINDOWS_SERVER_2003", 
                                    "WINDOWS_SERVER_2008", "WINDOWS_SERVER_2008_R2", "WINDOWS_SERVER_2012", "WINDOWS_SERVER_2012_R2", "WINDOWS_SERVER_2016_OR_ABOVE", 
                                    "LINUX_OTHER", "LINUX_SERVER_OTHER", "LINUX_UBUNTU", "LINUX_RHEL", "LINUX_SUSE", "LINUX_CENTOS" ]
        valid_status = [ "AVAILABLE", "DELETED", "DISABLED", "FAILED", "IN_PROGRESS", "PARTIALLY_AVAILABLE", "PENDING" ]
        valid_source = [ "MARKET_PLACE", "UPLOADED", "COPIED_FROM_STREAM", "COPIED_FROM_VERSION" ]
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        additional_details = {}
        additional_details["additionalProp1"] = additional_details_1
        additional_details["additionalProp2"] = additional_details_2
        additional_details["additionalProp3"] = additional_details_3
        data["description"] = description
        data["name"] = name
        if operating_system in valid_operating_system:
            data["operating_system"] = operating_system
        else:
            raise Exception(f"Error: please provide a valid operating_system from these options: {valid_operating_system}")
        data["publisher"] = publisher
        if source in valid_source:
            data["source"] = source
        else:
            raise Exception(f"Error: please provide a valid source from these options: {valid_source}")
        if status in valid_status:
            data["status"] = status
        else:
            raise Exception(f"Error: please provide a valid status from these options: {valid_status}")
        json_data = json.dumps(data)
        response = requests.put(f'{self.url}/rest/config/v1/im-streams/{im_stream_id}', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 409:
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

    def delete_im_stream(self, im_stream_id : str):
        """Deletes image management stream.

        Available for Horizon 7.12 and later."""
        response = requests.delete(f'{self.url}/rest/config/v1/im-streams/{im_stream_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def new_im_version(self,description : str,name : str, im_stream_id : str,status : str, additional_details_1:str = "", additional_details_2:str = "", additional_details_3:str = ""):
        """Creates image management version.

        Requires all as string:
            description
            name
            im_stream_id
            status : AVAILABLE, DEPLOYING_VM, DEPLOYMENT_DONE, DELETED, DISABLED, FAILED, PARTIALLY_AVAILABLE, PUBLISHING, REPLICATING
            Optional:
                additional_details_1
                additional_details_2
                additional_details_3
        Available for Horizon 7.12 and later."""
        valid_status = [ "AVAILABLE", "DEPLOYING_VM", "DEPLOYMENT_DONE", "DELETED", "DISABLED", "FAILED", "PARTIALLY_AVAILABLE", "PUBLISHING", "REPLICATING" ]
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        additional_details = {}
        additional_details["additionalProp1"] = additional_details_1
        additional_details["additionalProp2"] = additional_details_2
        additional_details["additionalProp3"] = additional_details_3
        data["description"] = description
        data["im_stream_id"] = im_stream_id
        data["name"] = name
        if status in valid_status:
            data["status"] = status
        else:
            raise Exception(f"Error: please provide a valid status from these options: {valid_status}")
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/config/v1/im-versions', verify=False,  headers=headers, data=json_data)
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

    def update_im_version(self,description : str,name : str, im_version_id : str,status : str, additional_details_1:str = "", additional_details_2:str = "", additional_details_3:str = ""):
        """Updates] image management version.

        Requires all as string:
            description
            name
            im_stream_id
            status : AVAILABLE, DEPLOYING_VM, DEPLOYMENT_DONE, DELETED, DISABLED, FAILED, PARTIALLY_AVAILABLE, PUBLISHING, REPLICATING
            Optional:
                additional_details_1
                additional_details_2
                additional_details_3
        Available for Horizon 7.12 and later."""
        valid_status = [ "AVAILABLE", "DEPLOYING_VM", "DEPLOYMENT_DONE", "DELETED", "DISABLED", "FAILED", "PARTIALLY_AVAILABLE", "PUBLISHING", "REPLICATING" ]
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        additional_details = {}
        additional_details["additionalProp1"] = additional_details_1
        additional_details["additionalProp2"] = additional_details_2
        additional_details["additionalProp3"] = additional_details_3
        data["description"] = description
        data["name"] = name
        if status in valid_status:
            data["status"] = status
        else:
            raise Exception(f"Error: please provide a valid status from these options: {valid_status}")
        json_data = json.dumps(data)
        response = requests.put(f'{self.url}/rest/config/v1/im-versions/{im_version_id}', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 409:
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

    def delete_im_version(self, im_version_id : str):
        """Deletes image management version.

        Available for Horizon 7.12 and later."""
        response = requests.delete(f'{self.url}/rest/config/v1/im-versions/{im_version_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_federation_access_groups(self) -> list:
        """Lists all federation access groups.

        Available for Horizon 8 2106 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/federation-access-groups', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_federation_access_group(self,id) -> dict:
        """Retrieves a federation access group.

        Requires the id of an Instant Clone Admin account to be provided as id
        Available for Horizon 8 2106 and later."""
        response = requests.get(f'{self.url}/rest/config/v1/federation-access-groups/{id}', verify=False,  headers=self.access_token)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def new_federation_access_group(self, name: str, description: str):
        """Creates federation access group.

        Requires name and description as string
        Available for Horizon 8 2106 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {"name": name, "description": description,}
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/config/v1/federation-access-groups', verify=False,  headers=headers, data=json_data)
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

    def delete_federation_access_group(self,id: str):
        """Deletes a federation access group.

        Requires id of a federation access group
        Available for Horizon 8 2106 and later."""
        response = requests.delete(f'{self.url}/rest/config/v1/federation-access-groups/{id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status_code

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

    def get_ad_domains_v3(self) -> list:
        """Lists information related to AD Domains of the environment.

        Available for Horizon 8 2106 and later."""
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
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
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
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
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
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
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
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
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
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
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
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
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
                filter_url = urllib.parse.quote(json.dumps(filter,separators=(', ', ':')))
                url_filter = f"?filter={filter_url}&group_only={group_only}&page={page}&size={maxpagesize}"
            elif filter == "" and (group_only == True or group_only == False):
                url_filter = f"?group_only={group_only}&page={page}&size={maxpagesize}"
            elif filter != "" and not (group_only == True or group_only == False):
                filter_url = urllib.parse.quote(json.dumps(filter,separators=(', ', ':')))
                url_filter = f"?filter={filter_url}&page={page}&size={maxpagesize}"
            else:
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
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
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
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_datastore_clusters(self, vcenter_id : str, host_or_cluster_id:str ) -> list:
        """Lists all the datastore clusters from the vCenter for the given host or cluster.

        Requires host_or_cluster_id and vcenter_id
        Available for Horizon 8 2103 and later."""
        response = requests.get(f'{self.url}/rest/external/v1/datastore-clusters?host_or_cluster_id={host_or_cluster_id}&vcenter_id={vcenter_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
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
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
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
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
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
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
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
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
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
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_virtual_machines(self, vcenter_id:str) -> list:
        """Lists all the VMs from a vCenter.

        Requires datacenter_id and vcenter_id.
        Available for Horizon 8 2006 and later."""

        response = requests.get(f'{self.url}/rest/external/v1/virtual-machines?vcenter_id={vcenter_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def compute_datastore_requirement(self,desktop_or_farm_id: str, user_assignment : str, vcenter_id : str, pool_size : int, source : str, type : str, base_snapshot_id: str="",base_vm_id: str="", use_separate_replica_and_os_disk : bool=False, use_vsan : bool = False, vm_template_id : str = "") -> list:
        """Creates Instant Clone Domain Account

        Requirements:
        base_snapshot_id : str - Required when source is INSTANT_CLONE
        base_vm_id : string - Required when source is INSTANT_CLONE
        desktop_or_farm_id: string
        pool_size : int32
        source : string - Required to be either FULL_CLONE or INSTANT_CLONE
        type : string - Required to be DESKTOP_POOL or FARM
        use_separate_replica_and_os_disk : boolean - Ignored for FULL_CLONE or when vSAN is used, defaults to False
        use_vsan : boolean - defaults to False
        user_assignment : string - Required to be DEDICATED or FLOATING
        vcenter_id : string
        vm_template_id : string - Required when source is FULL_CLONE

        Available for Horizon 8 2103 and later."""
        if source !="FULL_CLONE" and source !="INSTANT_CLONE":
            raise Exception(f"Error: source has to be either FULL_CLONE or INSTANT_CLONE")
        if type !="DESKTOP_POOL" and type !="FARM":
            raise Exception(f"Error: type has to be either DESKTOP_POOL or FARM")
        if user_assignment !="DEDICATED" and user_assignment !="FLOATING":
            raise Exception(f"Error: user_assignment has to be either DEDICATED or FLOATING")
        if source == "FULL_CLONE" and vm_template_id == "":
            raise Exception(f"Error: When type is FULL_CLONE vm_template_id is required ")
        if source == "INSTANT_CLONE" and (base_vm_id == "" or base_snapshot_id == ""):
            raise Exception(f"Error: When type is INSTANT_CLONE both base_vm_id and base_snapshot_id are required ")
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        if source == "INSTANT_CLONE":
            data["base_snapshot_id"] = base_snapshot_id
            data["base_vm_id"] = base_vm_id
        data["id"] = desktop_or_farm_id
        data["pool_size"] = pool_size
        data["source"] = source
        data["type"] = type
        data["use_separate_replica_and_os_disk"] = use_separate_replica_and_os_disk
        data["use_vsan"] = use_vsan
        data["user_assignment"] = user_assignment
        data["vcenter_id"] = vcenter_id
        if type == "FULL_CLONE":
            data["vm_template_id"] = vm_template_id
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/external/v1/datastores/action/compute-requirements', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 409:
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

    def new_auxiliary_account(self, domain_id: str, username: str, password: str):
        """Add auxiliary accounts to the untrusted domain

        Requires domain_id, username and password as string
        Available for Horizon 8 2106 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["auxiliary_accounts"] = []
        auxiliary_account = {}
        auxiliary_account["password"] = password
        auxiliary_account["username"] = username
        (data["auxiliary_accounts"]).append(auxiliary_account)
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/external/v1/ad-domains/{domain_id}/action/add-auxiliary-accounts', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 409:
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

    def delete_auxiliary_account(self, domain_id: str, auxiliary_account_ids: list):
        """deletes auxiliary accounts from the untrusted domain

        Requires domain_id as string and auxiliary_account_ids as a list
        Available for Horizon 8 2106 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["auxiliary_account_ids"] = auxiliary_account_ids
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/external/v1/ad-domains/{domain_id}/action/delete-auxiliary-accounts', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 409:
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

    def update_auxiliary_account(self, auxiliary_account_id: str, password : str):
        """updates auxiliary accounts of the untrusted domain

        Requires auxiliary_account_id and password as string
        Available for Horizon 8 2106 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["auxiliary_accounts"] = []
        auxiliary_account = {}
        auxiliary_account["id"] = auxiliary_account_id
        auxiliary_account["password"] = password
        (data["auxiliary_accounts"]).append(auxiliary_account)
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/external/v1/ad-domains/action/update-auxiliary-accounts', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 409:
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

    def get_audit_events(self, filter:dict="", maxpagesize:int=100) -> list:
        """Lists the audit events.

        Requires nothing
        Available for Horizon 8 2106 and later."""

        def int_get_audit_events(self, page:int, maxpagesize: int, filter:dict="") ->list:
            if filter !="":
                filter_url = urllib.parse.quote(json.dumps(filter,separators=(', ', ':')))
                add_filter = f"{filter_url}"
                response = requests.get(f'{self.url}/rest/external/v1/audit-events?filter={add_filter}&page={page}&size={maxpagesize}', verify=False,  headers=self.access_token)
            else:
                response = requests.get(f'{self.url}/rest/external/v1/audit-events?page={page}&size={maxpagesize}', verify=False,  headers=self.access_token)

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
        response = int_get_audit_events(self,page = page, maxpagesize= maxpagesize, filter= filter)
        results = response.json()
        while 'HAS_MORE_RECORDS' in response.headers:
            page += 1
            response = int_get_audit_events(self,page = page, maxpagesize= maxpagesize, filter= filter)
            results += response.json()
        return results

class Entitlements:
    def __init__(self, url: str, access_token: dict):
        """Default object for the Entitlements class for the entitlement of resources."""
        self.url = url
        self.access_token = access_token

    def get_application_pools_entitlements(self, maxpagesize:int=100, filter:dict="") -> list:
        """Lists the entitlements for Application Pools in the environment.

        Allows for filtering, either application_pool id can be used to filter on id key and or ad_user_or_group_ids can be filtered on.
        Available for Horizon 8 2006 and later."""

        def int_get_application_pools(self, page:int, maxpagesize: int, filter:dict="") ->list:
            if filter != "":
                filter_url = urllib.parse.quote(json.dumps(filter,separators=(', ', ':')))
                add_filter = f"?filter={filter_url}"
                response = requests.get(f'{self.url}/rest/entitlements/v1/application-pools{add_filter}&page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            else:
                response = requests.get(f'{self.url}/rest/entitlements/v1/application-pools?page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
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

    def  get_application_pool_entitlement(self, application_pool_id:str) -> list:
        """Returns the IDs of users or groups entitled to a given application pool

        Requires applictaion_pool_id
        Available for Horizon 8 2006 and later."""

        response = requests.get(f'{self.url}/rest/entitlements/v1/application-pools/{application_pool_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def new_application_pools_entitlements(self,application_pool_data:dict):
        """Creates an application pool.

        Requires application_pool_data as a dict
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(application_pool_data)
        response = requests.post(f'{self.url}/rest/entitlements/v1/application-pools', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status_code

    def delete_application_pools_entitlements(self,application_pool_data:dict):
        """Creates an application pool.

        Requires application_pool_data as a dict
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(application_pool_data)
        response = requests.delete(f'{self.url}/rest/entitlements/v1/application-pools', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status_code

    def get_desktop_pools_entitlements(self, maxpagesize:int=100, filter:dict="") -> list:
        """Lists the entitlements for desktop Pools in the environment.

        Allows for filtering, either desktop_pool id can be used to filter on id key and or ad_user_or_group_ids can be filtered on.
        Available for Horizon 8 2006 and later."""
        def int_get_desktop_pools(self, page:int, maxpagesize: int, filter:dict="") ->list:
            if filter != "":
                filter_url = urllib.parse.quote(json.dumps(filter,separators=(', ', ':')))
                add_filter = f"?filter={filter_url}"
                response = requests.get(f'{self.url}/rest/entitlements/v1/desktop-pools{add_filter}&page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            else:
                response = requests.get(f'{self.url}/rest/entitlements/v1/desktop-pools?page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
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
        response = int_get_desktop_pools(self,page = page, maxpagesize= maxpagesize,filter = filter)
        results = response.json()
        while 'HAS_MORE_RECORDS' in response.headers:
            page += 1
            response = int_get_desktop_pools(self,page = page, maxpagesize= maxpagesize, filter = filter)
            results += response.json()
        return results

    def  get_desktop_pool_entitlement(self, desktop_pool_id:str) -> list:
        """Returns the IDs of users or groups entitled to a given desktop pool

        Requires desktop_pool_id
        Available for Horizon 8 2006 and later."""
        response = requests.get(f'{self.url}/rest/entitlements/v1/desktop-pools/{desktop_pool_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def new_desktop_pools_entitlements(self,desktop_pools_data:list):
        """Create the bulk entitlements for a set of desktop pools.

        Requires desktop_pools_data as a list
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(desktop_pools_data)
        response = requests.post(f'{self.url}/rest/entitlements/v1/desktop-pools', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status_code

    def delete_desktop_pools_entitlements(self,desktop_pools_data:list):
        """Delete the bulk entitlements for a set of desktop pools.

        Requires desktop_pools_data as a list.
        Available for Horizon 8 2006 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(desktop_pools_data)
        response = requests.delete(f'{self.url}/rest/entitlements/v1/desktop-pools', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.status_code

    def get_global_desktop_entitlement(self, global_desktop_entitlement_id:str) -> dict:
        """Gets the user or group entitlements for a Global Desktop Entitlement.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/entitlements/v1/global-desktop-entitlements/{global_desktop_entitlement_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def get_global_desktop_entitlements(self, maxpagesize:int=100, filter:dict="") -> list:
        """Lists the user or group entitlements for Global Desktop Entitlements in the environment.

        For information on filtering see https://vdc-download.vmware.com/vmwb-repository/dcr-public/f92cce4b-9762-4ed0-acbd-f1d0591bd739/235dc19c-dabd-43f2-8d38-8a7a333e914e/HorizonServerRESTPaginationAndFilterGuide.doc
        Available for Horizon 8 2012 and later."""

        def int_get_global_desktop_entitlements(self, page:int, maxpagesize: int, filter:list="") ->list:
            if filter != "":
                add_filter = urllib.parse.quote(json.dumps(filter,separators=(', ', ':')))
                response = requests.get(f'{self.url}/rest/entitlements/v1/global-desktop-entitlements?filter={add_filter}&page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            else:
                response = requests.get(f'{self.url}/rest/entitlements/v1/global-desktop-entitlements?page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            if response.status_code == 400:
                if "error_messages" in response.json():
                    error_message = (response.json())["error_messages"]
                else:
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
        response = int_get_global_desktop_entitlements(self,page = page, maxpagesize= maxpagesize,filter = filter)
        results = response.json()
        while 'HAS_MORE_RECORDS' in response.headers:
            page += 1
            response = int_get_global_desktop_entitlements(self,page = page, maxpagesize= maxpagesize, filter = filter)
            results += response.json()
        return results

    def new_global_desktop_entitlement(self, global_desktop_entitlement_data: list):
        """Create the bulk entitlements for a set of Global Desktop Entitlements.

        Requires global_desktop_entitlement_data as a dict
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(global_desktop_entitlement_data)
        response = requests.post(f'{self.url}/rest/entitlements/v1/global-desktop-entitlements', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def delete_global_desktop_entitlement(self, global_desktop_entitlement_data: list):
        """Delete the bulk entitlements for a set of Global Desktop Entitlements.

        Requires global_desktop_entitlement_data as a dict
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(global_desktop_entitlement_data)
        response = requests.delete(f'{self.url}/rest/entitlements/v1/global-desktop-entitlements', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def get_global_application_entitlement(self, global_application_entitlement_id:str) -> dict:
        """Gets the user or group entitlements for a Global Application Entitlement.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/entitlements/v1/global-application-entitlements/{global_application_entitlement_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def get_global_application_entitlements(self, maxpagesize:int=100, filter:dict="") -> list:
        """Lists the user or group entitlements for Global Application Entitlements in the environment.

        For information on filtering see https://vdc-download.vmware.com/vmwb-repository/dcr-public/f92cce4b-9762-4ed0-acbd-f1d0591bd739/235dc19c-dabd-43f2-8d38-8a7a333e914e/HorizonServerRESTPaginationAndFilterGuide.doc
        Available for Horizon 8 2012 and later."""

        def int_get_global_application_entitlements(self, page:int, maxpagesize: int, filter:list="") ->list:
            if filter != "":
                add_filter = urllib.parse.quote(json.dumps(filter,separators=(', ', ':')))
                response = requests.get(f'{self.url}/rest/entitlements/v1/global-application-entitlements?filter={add_filter}&page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            else:
                response = requests.get(f'{self.url}/rest/entitlements/v1/global-application-entitlements?page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            if response.status_code == 400:
                if "error_messages" in response.json():
                    error_message = (response.json())["error_messages"]
                else:
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
        response = int_get_global_application_entitlements(self,page = page, maxpagesize= maxpagesize,filter = filter)
        results = response.json()
        while 'HAS_MORE_RECORDS' in response.headers:
            page += 1
            response = int_get_global_application_entitlements(self,page = page, maxpagesize= maxpagesize, filter = filter)
            results += response.json()
        return results

    def new_global_application_entitlement(self, global_application_entitlement_data: list):
        """Create the bulk entitlements for a set of Global Application Entitlements

        Requires global_application_entitlement_data as a dict
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(global_application_entitlement_data)
        response = requests.post(f'{self.url}/rest/entitlements/v1/global-application-entitlements', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def delete_global_application_entitlement(self, global_application_entitlement_data: list):
        """Delete the bulk entitlements for a set of Global Application Entitlements

        Requires global_application_entitlement_data as a dict
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        json_data = json.dumps(global_application_entitlement_data)
        response = requests.delete(f'{self.url}/rest/entitlements/v1/global-application-entitlements', verify=False,  headers=headers, data=json_data)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {response}")
        elif response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

class Federation:
    def __init__(self, url: str, access_token: dict):
        """Default object for the pools class where all Desktop Pool Actions will be performed."""
        self.url = url
        self.access_token = access_token

    def get_cloud_pod_federation(self) -> dict:
        """Retrieves the pod federation details.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/federation/v1/cpa', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def get_home_sites(self, maxpagesize:int=100, filter:dict="") -> list:
        """Lists all the home sites in the pod federation.

        For information on filtering see https://vdc-download.vmware.com/vmwb-repository/dcr-public/f92cce4b-9762-4ed0-acbd-f1d0591bd739/235dc19c-dabd-43f2-8d38-8a7a333e914e/HorizonServerRESTPaginationAndFilterGuide.doc
        Available for Horizon 8 2012 and later."""

        def int_Get_home_sites(self, page:int, maxpagesize: int, filter:list="") ->list:
            if filter != "":
                add_filter = urllib.parse.quote(json.dumps(filter,separators=(', ', ':')))
                response = requests.get(f'{self.url}/rest/federation/v1/home-sites?filter={add_filter}&page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            else:
                response = requests.get(f'{self.url}/rest/federation/v1/home-sites?page={page}&size={maxpagesize}', verify=False, headers=self.access_token)
            if response.status_code == 400:
                if "error_messages" in response.json():
                    error_message = (response.json())["error_messages"]
                else:
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
        response = int_Get_home_sites(self,page = page, maxpagesize= maxpagesize,filter = filter)
        results = response.json()
        while 'HAS_MORE_RECORDS' in response.headers:
            page += 1
            response = int_Get_home_sites(self,page = page, maxpagesize= maxpagesize, filter = filter)
            results += response.json()
        return results

    def get_sites(self) -> list:
        """Lists all the sites in the pod federation.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/federation/v1/sites', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def get_site(self, site_id:str) -> dict:
        """Retrives a given site.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/federation/v1/sites/{site_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def update_cloud_pod_federation(self, name:str):
        """Updates a Pod Federation

        Requires a new name of the cpa as a string
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["name"] = name
        json_data = json.dumps(data)
        response = requests.put(f'{self.url}/rest/federation/v1/cpa', verify=False,  headers=headers, data = json_data)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 403:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def get_home_site(self, home_site_id:str) -> dict:
        """Retrieves a given home site in the pod federation.

        Requires a home_site_id as a string
        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/federation/v1/home-sites/1/{home_site_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def new_site(self, name:str, description:str):
        """creates a site.

        Requires the name and description as strings
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["description"] = description
        data["name"] = name
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/federation/v1/sites', verify=False,  headers=headers, data = json_data)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 403:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 201:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def update_site(self,site_id:str  ,name:str, description:str):
        """Updates a site.

        Requires site_id, the name and description as strings
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["description"] = description
        data["name"] = name
        json_data = json.dumps(data)
        response = requests.put(f'{self.url}/rest/federation/v1/sites/{site_id}', verify=False,  headers=headers, data = json_data)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 403:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def delete_site(self, site_id:str):
        """Retrives a given site.

        Available for Horizon 8 2012 and later."""
        response = requests.delete(f'{self.url}/rest/federation/v1/sites/{site_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 403:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_pods(self) -> list:
        """Lists all the pods in the pod federation.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/federation/v1/pods', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def get_pod(self, pod_id:str) -> dict:
        """Retrieves a given pod from the pod federation.

        Requires pod_id as a string
        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/federation/v1/pods/{pod_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def update_pod(self,pod_id:str, description:str, site_id:str ,name:str, cloud_managed:bool=""):
        """Updates the given pod in the pod federation.

        Requires pod_id, site_id, the name and description as strings, cloud_managed needs to be a bool
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        if cloud_managed != "":
            data["cloud_managed"] = cloud_managed
        if description!="":
            data["description"] = description
        data["name"] = name
        data["site_id"] = site_id
        json_data = json.dumps(data)
        response = requests.put(f'{self.url}/rest/federation/v1/pods/{pod_id}', verify=False,  headers=headers, data = json_data)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 403:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def get_pod_endpoints(self, pod_id:str) -> list:
        """Lists all the pod endpoints for the given pod.

        Requires pod_id as a string
        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/federation/v1/pods/{pod_id}/endpoints', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def get_pod_endpoint(self, pod_id:str, endpoint_id:str) -> dict:
        """Lists all the pod endpoints for the given pod.

        Requires pod_id and endpoint_id as a string
        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/federation/v1/pods/{pod_id}/endpoints/{endpoint_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def get_tasks(self) -> list:
        """Lists all the CPA tasks in the pod federation.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/federation/v1/cpa/tasks', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def get_task(self, task_id:str) -> dict:
        """Retrieves the information for a given task.

        Available for Horizon 8 2012 and later."""
        response = requests.get(f'{self.url}/rest/federation/v1/cpa/tasks/{task_id}', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def eject_pod(self, pod_id:str) :
        """Removes a pod from Cloud Pod Federation.

        Requires pod_id as a string
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["pod_id"] = pod_id
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/federation/v1/cpa/action/eject', verify=False,  headers=headers, data = json_data)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 403:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)

    def join_cpa(self, remote_pod_address:str, username:str, password:str) -> dict:
        """ Join Cloud Pod Federation.

        Requires remote_pod_address (fqdn), username (domain\\username) and password as str
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["password"] = password
        data["remote_pod_address"] = remote_pod_address
        data["username"] = username
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/federation/v1/cpa/action/join', verify=False,  headers=headers, data = json_data)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def unjoin_cpa(self) -> dict:
        """Unjoin from Cloud Pod Federation.

        Available for Horizon 8 2012 and later."""
        response = requests.post(f'{self.url}/rest/federation/v1/cpa/action/unjoin', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def initialize_cpa(self) -> dict:
        """Initialize Cloud Pod Federation.

        Available for Horizon 8 2012 and later."""
        response = requests.post(f'{self.url}/rest/federation/v1/cpa/action/initialize', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def uninitialize_cpa(self) -> dict:
        """Initialize Cloud Pod Federation.

        Available for Horizon 8 2012 and later."""
        response = requests.post(f'{self.url}/rest/federation/v1/cpa/action/uninitialize', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def unjoin_cpa(self) -> dict:
        """Initialize Cloud Pod Federation.

        Available for Horizon 8 2012 and later."""
        response = requests.post(f'{self.url}/rest/federation/v1/cpa/action/unjoin', verify=False,  headers=self.access_token)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
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

    def new_home_site(self, ad_user_or_group_id:str, global_application_entitlement_id:str, global_desktop_entitlement_id:str, site_id:str) -> list:
        """Creates the given home site in the pod federation.

        Requires ad_user_or_group_id, global_application_entitlement_id, global_desktop_entitlement_id, site_id as strings
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["ad_user_or_group_id"] = ad_user_or_group_id
        data["global_application_entitlement_id"] = global_application_entitlement_id
        data["global_desktop_entitlement_id"] = global_desktop_entitlement_id
        data["site_id"] = ad_user_or_group_id
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/federation/v1/home-sites', verify=False,  headers=headers, data = json_data)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 403:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def delete_home_sites(self, homesite_ids:list) -> list:
        """Creates the given home site in the pod federation.

        Requires ad_user_or_group_id, global_application_entitlement_id, global_desktop_entitlement_id, site_id as strings
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        data["homesite_ids"] = homesite_ids
        json_data = json.dumps(data)
        response = requests.delete(f'{self.url}/rest/federation/v1/home-sites', verify=False,  headers=headers, data = json_data)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 403:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()

    def get_user_home_site(self, user_id:str, global_application_entitlement_id:str="", global_desktop_entitlement_id:str="") -> list:
        """Creates the given home site in the pod federation.

        Requires global_application_entitlement_id, global_desktop_entitlement_id, user_id as strings
        Available for Horizon 8 2012 and later."""
        headers = self.access_token
        headers["Content-Type"] = 'application/json'
        data = {}
        if global_application_entitlement_id !="":
            data["global_application_entitlement_id"] = global_application_entitlement_id
        if global_desktop_entitlement_id !="":
            data["global_desktop_entitlement_id"] = global_desktop_entitlement_id
        data["user_id"] = user_id
        json_data = json.dumps(data)
        response = requests.post(f'{self.url}/rest/federation/v1/home-sites', verify=False,  headers=headers, data = json_data)
        if response.status_code == 400:
            if "error_messages" in response.json():
                error_message = (response.json())["error_messages"]
            else:
                error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        if response.status_code == 404:
            error_message = (response.json())["error_message"]
            raise Exception(f"Error {response.status_code}: {error_message}")
        elif response.status_code == 403:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        elif response.status_code != 204:
            raise Exception(f"Error {response.status_code}: {response.reason}")
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise "Error: " + str(e)
            else:
                return response.json()