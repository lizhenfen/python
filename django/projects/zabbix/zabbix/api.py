#!/usr/bin/env python
# coding:utf-8
import json
import requests

headers = {"Content-Type":"application/json"}

def auth_login(url,user,passwd):
  auth_request = json.dumps({
     "jsonrpc": "2.0",
     "method": "user.login",
     "params": {
         "user": "%s"% user,
         "password": "%s"% passwd,
     },  
     "id": 1,
  })
  auth_response = requests.post(url,data=auth_request,headers=headers)
  return json.loads(auth_response.text)['result']

if __name__ == "__main__":
  zabbix_url = "http://192.168.27.253/zabbix"
  zabbix_api = "/api_jsonrpc.php"
  request_url = zabbix_url + zabbix_api
  auth_id = auth_login(request_url,'Admin','zabbix')
  print auth_id

