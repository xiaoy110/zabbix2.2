#!/usr/bin/env python
#coding:utf8
import json
import zabmaster
API = zabmaster.zabbixtools()
def get_hostgroupid():
    data = json.dumps({
        "jsonrpc": "2.0",
        "method": "hostgroup.get",
        "params": {
            "output": "extend"
#            "filter": {
#                    "name": [
#                            "Zabbix servers",
#                             "Linux servers"
#            ]
#        }
    },
    "auth": API.user_login(),
    "id": 5
        })
    res = API.get_data(data)['result']
    if res != []:
        for r in res:
            print "+++++++++++++++++++++++++++++++++++++++++++"
            print "GroupName: %s GroupID: %s " %(r['name'],r['groupid'])
        
get_hostgroupid()
#print x
