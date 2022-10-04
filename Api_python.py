


import requests
import requests.auth
#from requests.auth import HTTPBasicAuth

    
def get_token():

    url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
    #auth = HTTPBasicAuth ("devnetuser", "Cisco123!")
    auth = requests.auth.HTTPBasicAuth ("devnetuser", "Cisco123!")
    headers = {"Content-Type":"application/json"}

    api_result = requests.post(url=url, auth=auth, headers=headers, verify=False)
    token=api_result.json()["Token"]
    api_result.raise_for_status()
    return token


def get_devices():
    
    url="https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"
    headers = {
        "Content-Type":"application/json",
        "X-Auth-Token":get_token()
    }

    api_result = requests.get(url=url, headers=headers, verify=False)
    devices = api_result.json() ["response"]
    api_result.raise_for_status
    return devices




    


