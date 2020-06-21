import json

import requests

def getToken():
    api_url = 'http://47.96.181.17:9090/rest/toController'
    header = {'Content-Type':'application/json'}

    payload = {
        "userName":"J201903070064",
        "password":"362387359"
    }

    reps = requests.post(api_url,json=payload,headers=header)
    token = json.loads(reps.text)['uploadFile']
    return token


if __name__ == '__main__':
    token = getToken()
    print(token)