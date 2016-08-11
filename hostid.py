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
def host_get():
    data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "host.get",
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
    if res != []:
        for r in res:
            print "+++++++++++++++++++++++++++++++++++++++++++++"
            if r["status"] == "0":
               print "Online %s HostID: %s" %(r["host"],r['hostid'])
            else:
               print  "offline %s HostID: %s " %(r['host'],r['hostid'])
    else:
        return  "Not found host information on your Zabbix Server"
host_get()
#print x
#hostname = str(raw_input("Please input your hostname(not Visible name):"))
