# zabbix2.2
## zabbix api使用说明
### 添加删除主机
 ***
- host_add.py  添加主机
- host_del.py  删除主机
- hostid.py 获取主机HostID
- hostgroup_add.py 添加主机组
- hostgroup_del.py 删除主机组
- hostgroup_get.py 获取主机组
- user_add.py    添加用户
- user_del.py    删除用户
- user_getid.py  获取用户id
- usergroup_add       添加用户组
- usergroup_del	    删除用户组
- usergroup_getid.py  获取组id
- action_add.py    添加动作
- action_del.py    删除动作
- action_getid.py  获取动作id
- zabmaster.py 获取token

### 添加流程
- 创建主机组1 --- 添加主机到主机组1
- 如果加入报警
- 创建用户组 --- 添加用户 ---- 创建动作指定主机报警收取邮件的用户组或用户


### 删除流程
- 删除 动作 --- 删除主机 ----删除主机组 --- 删除用户 ---删除用户组


