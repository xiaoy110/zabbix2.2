#!/usr/bin/env python
#coding:utf8
import zabmaster
import json

API = zabmaster.zabbixtools()

def get_temid():
    data = json.dumps({
        "jsonrpc": "2.0",
        "method": "template.get",
        "params": {
            "output": "extend"
        },
        "auth": API.user_login(),
        "id": 3
    })
    res = API.get_data(data)['result']
    for r in res:
        print "TempLateName %s TemplateID %s"  %(r['name'],r['templateid'])
get_temid()
