# _*_coding:utf-8_*_
# Author:xupan


SESSION_ID='__session__id__'
EXPIRERS = 300   #超时时间

############# 使用 类型 #############
SESSION_ENGINE="session_code.CacheSession"
# SESSION_ENGINE="session_code.REdisSession"


################# Redis 的接口 #################
REDISHOST='192.xxx.xx.xx'
REDISPORT=6379