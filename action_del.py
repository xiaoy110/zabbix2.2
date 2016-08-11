#!/usr/bin/env python
#-*-coding:utf8-*-
import json
import sys
import zabmaster
API = zabmaster.zabbixtools()

action_id = sys.argv[1]
def action_del():
    data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "action.delete",
                "params": [
                "36"
                ],
                "auth": API.authID,
                "id": action_id
            })
    res = API.get_data(data)
#    print res
#    print res['result']["actionids"][0]
#    print res['error']['data']
    if "result" in res:
#          print "+++++++++++++++++++++++++++++++++++++++++++++"
          if int(res['result']["actionids"][0]) == action_id:
               print "success"
    else:
        print  "error message: %s " %(res['error']['data'])
action_del()
#print x
#hostname = str(raw_input("Please input your hostname(not Visible name):"))
