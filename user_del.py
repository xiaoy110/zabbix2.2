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
host_id == sys.argv[1]
def user_delete():
    data = json.dumps({
    "jsonrpc": "2.0",
    "method": "user.delete",
    "params": [
       username 
    ],
    "auth": API.authID,
    "id": 1
    })
    res = API.get_data(data)
    print res
    if "result" in res:
#          print "+++++++++++++++++++++++++++++++++++++++++++++"
          if int(res['result']["userids"][0]) == 14:
               print "success"
    else:
        print  "error message: %s " %(res['error']['data'])
user_delete()

#alert_get ()

