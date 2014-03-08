#PushNotify
***
基于[mosquitto](http://mosquitto.org/)的Android推送的二次封装。Android的demo可以在[tukodu](https://github.com/tokudu/AndroidPushNotificationsDemo)中修改。
###Feature
***
* 添加了用户管理
* mosquitto的命令行监控
* (TODO)离线消息缓存
###How to using
* 运行环境Mac/*nix
* 装有[moquitto](http://mosquitto.org/)
* 安装[Django](https://www.djangoproject.com/)
* 将apps/notification/mqttmanager.py中端口改为你需要的端口
```python
execShell = "{0} -p 1884 2>&1"
```
* 将[Android](https://github.com/tokudu/AndroidPushNotificationsDemo)客户端的ip和端口改为你的端口和ip
###TODO
* 独立出mosquitto管理模块，针对客户端数量开启活关闭服务
* 离线缓存