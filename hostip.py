#!/usr/bin/env python
#coding:utf8
import json
import hostid
import zabmaster

API = zabmaster.zabbixtools()

#HostIDinfo=hostid.host_get()
#print HostIDinfo

def get_hostip(hostIDinfo):
    data = json.dumps({
        "jsonrpc": "2.0",
        "method": "hostinterface.get",
        "params": {
            "output": "extend",
            "hostids": hostIDinfo
                },
        "auth": API.authID,
        "id": 1})
    res = API.get_data(data)['result']
    for  r in res:
        print "InterFaceID: %s HostIP: %s " %(r['interfaceid'],r['ip']) 
def main():
    HostInputID = str(raw_input("Please input a hostid:"))
    AllRESULT = get_hostip(HostInputID)
if __name__ == "__main__":
    main()
