import json, requests, ssl

class Connection:
    def hv_connect(username, password, domain, url):
        headers = {
            'accept': '*/*',
            'Content-Type': 'application/json',
        }

        data = {"domain": domain, "password": password, "username": username}
        json_data = json.dumps(data)

        response = requests.post(f'{url}/rest/login', verify=False, headers=headers, data=json_data)
        data = response.json()

        access_token = {
            'accept': '*/*',
            'Authorization': 'Bearer ' + data['access_token']
        }
        return access_token

    def hv_disconnect(url, access_token):
        requests.post(f'{url}/rest/logout', verify=False, headers=access_token)

class Pools:
    def list_hvpools(url,access_token):
        response = requests.get(f'{url}/rest/inventory/v1/desktop-pools', verify=False,  headers=access_token)
        return response.json()



