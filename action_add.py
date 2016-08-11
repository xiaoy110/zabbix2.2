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

    
#alert_get()
action_name = sys.argv[1]
hostid = sys.argv[2]
userid = sys.argv[3]
def create_action():
    data = json.dumps({
    "jsonrpc": "2.0",
    "method": "action.create",
    "params": {
        "name": action_name, # this is a variable
        "eventsource": 0,
        "evaltype": 0,
        "status": 0,
        "esc_period": 120,
        "def_shortdata": "{TRIGGER.STATUS}: {TRIGGER.NAME}",
        "def_longdata": "Trigger:{TRIGGER.NAME}\nTrigger: {TRIGGER.STATUS}\nLast value: {ITEM.LASTVALUE}\nTrigger URL: {TRIGGER.URL}\nitem values:\n1. {ITEM.NAME1} ({HOST.NAME1}:{ITEM.KEY1}): {ITEM.VALUE1}}\nOriginal event ID: {EVENT.ID}",
        "recovery_msg": "1",
        "r_shortdata": "{TRIGGER.STATUS}: {TRIGGER.NAME}",
        "r_longdata": "Trigger:{TRIGGER.NAME}\nTrigger: {TRIGGER.STATUS}\nLast value: {ITEM.LASTVALUE}\nTrigger URL: {TRIGGER.URL}\nitem values:\n1. {ITEM.NAME1} ({HOST.NAME1}:{ITEM.KEY1}): {ITEM.VALUE1}}\nOriginal event ID: {EVENT.ID}",
        "conditions": [
            {
                "conditiontype": 16,
                "operator": 7,
                "value": ""
            },
            {
                "conditiontype": 5,
                "operator": 0,
                "value": "1"
            },
            {
                "conditiontype": 1,
                "operator": 0,
                "value": hostid #use host_getid.py to get the host ID
            }
        ],
        "operations": [
            {
                "operationtype": 0,
                "esc_period": 0,
                "esc_step_from": 1,
                "esc_step_to": 1,
                "evaltype": 0,
                "opmessage_usr": [
                    {
                        "userid": userid # this is useris variable
                    }
                ],
                "opmessage": {
                    "default_msg": 1,
                    "mediatypeid": "1"
                }
            }
        ]
    },
    "auth": API.authID,
    "id": 1
    })
    res = API.get_data(data)
    print res
create_action()
#alert_get ()

