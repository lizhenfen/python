#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import os
import requests
import json
from zabbix import api
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
headers = {"Content-Type":"application/json"}
zabbix_url = "http://192.168.27.253/zabbix"
zabbix_api = "/api_jsonrpc.php"
request_url = zabbix_url + zabbix_api

auth_id = api.auth_login(request_url,'Admin','zabbix')

host_get = json.dumps({
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": [
            "hostid",
            "host"
        ],
        "selectInterfaces": [
            "interfaceid",
            "ip"
        ]
    },
    "id": 1,
    "auth": "%s" % auth_id
})

data = requests.post(request_url,data=host_get,headers=headers)
print data.text
