import requests

from 接口自动化.day2.uploadFile.getToken import getToken

api_url = 'http://47.96.181.17:9090/rest/ac01CrmController'
token = getToken()
header = {'X-AUTH-TOKEN':token,'Content-Type':'application/json'}

payload = {
    "aac003": "张四",
    "aac004": "1",
    "aac011": "21",
    "aac030": "15222456845",
    "aac01u": "88002255",
    "crm003": "1",
    "crm004": "1",
    "crm00a": "2018-11-11",
    "crm00b": "aaaaaa",
    "crm00c": "2019-02-28",
    "crm00d": "bbbbbb"
}

reps = requests.post(api_url,json=payload,headers=header)
print(reps.text)
