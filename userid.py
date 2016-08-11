#!/usr/bin/env python
#coding:utf8
import json
import zabmaster
API = zabmaster.zabbixtools()
def get_usergroupid():
    data = json.dumps({
        "jsonrpc": "2.0",
        "method": "user.get",
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
#    print res
    if res != []:
        for r in res:
            print "+++++++++++++++++++++++++++++++++++++++++++"
            print "userName: %s userID: %s " %(r['surname'],r['userid'])
        
#x = get_hostgroupid()
#print x
get_usergroupid()
