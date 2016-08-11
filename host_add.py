#!/usr/bin/env python
#coding:utf8
import json,sys, zabmaster
import hostid,hostip,groupid,tempid
API = zabmaster.zabbixtools()
CreateHostName = sys.argv[1]
CreateHostIp = sys.argv[2]
GroupID = sys.argv[3]
TMPID = sys.argv[4]
#hostip.get_hostip(CreateHostName)

def create_host():
    data = json.dumps({
        "jsonrpc": "2.0",
        "method": "host.create",
        "params": {
            "host": CreateHostName,
            "interfaces": [
                {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": CreateHostIp,
                "dns": "",
                "port": "10050"
                }
                ],
        "groups": [
            {
                "groupid": GroupID
            }
        ],
        "templates": [
            {
                "templateid": TMPID
            }
        ]
#        "inventory": {
#            "macaddress_a": "01234",
#            "macaddress_b": "56768"
#        }
    },
    "auth": API.authID,
    "id": 6
    })
    res = API.get_data(data)['result']
    print res
create_host()
