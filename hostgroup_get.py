#!/usr/bin/env python
#-*-coding:utf8-*-
import json
import urllib2
from urllib2 import URLError
import sys
import os
import time
import zabmaster
API = zabmaster.zabbixtools()
def hostgroup_get():
    data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "hostgroup.get",
                "params": {
                    "output":["hostid",
                               "name",
                               "status",
                               "host"]
                    },
                "auth": API.authID,
                "id": 1
            })
    res = API.get_data(data)['result']
    print res
    if res != []:
        for r in res:
            print "+++++++++++++++++++++++++++++++++++++++++++++"
            print "Online %s HostID: %s" %(r["name"],r['groupid'])
    else:
        return  "Not found host information on your Zabbix Server"
hostgroup_get()
#print x
#hostname = str(raw_input("Please input your hostname(not Visible name):"))
