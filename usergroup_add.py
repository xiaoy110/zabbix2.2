#!/usr/bin/env python
#coding:utf8
import json,sys
import zabmaster
#import hostid,hostip,groupid,tempid
#import usergroupid
API = zabmaster.zabbixtools()
#usergroupid.get_usergroupid()
#tempid.get_temid()
#hostid.host_get()
#groupid.get_hostgroupid()
#CreateHostName = str(raw_input("Please input your will create HostName:"))
#CreateHostIp = str(raw_input("Please input your HostIP:"))
#GroupID = str(raw_input("Please input your GroupID:"))
#TMPID = str(raw_input("Please input your templateid:"))
#hostip.get_hostip(CreateHostName)

usergroupname = sys.argv[1]
def usergroup_add ():
    data = json.dumps({
    "jsonrpc": "2.0",
    "method": "usergroup.create",
    "params": {
        "name": usergroupname, # this is variable
        "rights": {
            "permission": 0,
            "id": "2"
        },
    },
    "auth": API.authID,
    "id": 1
    })
    res = API.get_data(data)
    print res
usergroup_add()
#alert_get ()

