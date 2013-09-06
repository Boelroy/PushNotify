import mosquitto
from datetime import *
from UserUtil import UserUtil
import threading
from mqttmanage import MqttManagement
from models import CachedNotification
from models import Users

def singleton(cls, *args, **kw):   
    instances = {}   
    def _singleton():   
        if cls not in instances:   
            instances[cls] = cls(*args, **kw)   
        return instances[cls]   
    return _singleton

@singleton
class Notify(object):
	mqtt_port = 1883
	mqtt_host = "127.0.0.1"

	NOTIFY_TYPE_ALL = 0
	NOTIFY_TYPE_SINGLE = 1

	def __init__(self):
		self.mqtt = mosquitto.Mosquitto('bowen')
		self.mqtt.on_message = self.on_message
		self.isConnect = False

		#start the mosquitto broker
		self.mqttBroker = MqttManagement(mosquittoPath="/usr/sbin/mosquitto")
		self.mqttBroker.onDisconnect = self.onDisconnect
		self.mqttBroker.onConnect = self.onConnect

		self.mqttBroker.onCmdRun = self.onCmdRun

		self.userUtil = UserUtil()
		self.mqttBroker.run()
		pass

	def notify(self, topic, msg, type):
		try:
			self.__notify(topic, msg)
		except Exception, e:
			self.mqtt.connect(hostname=self.mqtt_host, port=self.mqtt_port)

		self.mqtt.subscribe('tokudo/12', 0)
		if type == self.NOTIFY_TYPE_SINGLE:
			self.cacheMsg(msg, type, topic)
		elif type == self.NOTIFY_TYPE_ALL:
			self.cacheMsg(msg, type, None)

	def __notify(self, topic, msg):
		self.mqtt.publish(topic, str(msg),1)

	def onConnect(self, ip, name):
		print "Connecting " + name
		if self.userUtil.isInUsers(name):

			self.userUtil.changeUser(name=name,
						onlineStatus=True,
						ip=ip,
						lastonLineTime=datetime.now())
			userList = self.userUtil.getUsers(name)
			if hasattr(userList,"msgUser"):
				msgList = userList.msgUser.all()
				if msgList:
					self.__notify(name,msgList[0].note)
					self.deleteMsg(name)
		else:

			self.userUtil.addUser(name=name,
					onlineStatus=True,
					ip=ip,
					lastonLineTime=datetime.now())

	def onDisconnect(self,name):
		if self.userUtil.isInUsers(name):

			self.userUtil.changeUser(name=name,
					onlineStatus=False,
					lastonLineTime=datetime.now())

		else :
			raise Exception("Unkown Users disconnect from the server")

	def onCmdRun(self):
		self.mqtt.connect(hostname=self.mqtt_host, port=self.mqtt_port)

		def loop():
			rc = 0
			while rc == 0:
				rc = self.mqtt.loop()

		mThread = threading.Thread(target=loop)
		mThread.start()

	def on_message(self, mosq, obj, msg):
		print msg.payload
		self.deleteMsg(msg.payload)

	def cacheMsg(self, msg, type, name=None):
		if type == self.NOTIFY_TYPE_ALL:
			users = Users.objects.all()
			for user in users:
				newCachedMsg = CachedNotification(msgUser=user, notifiUsername=user.name, note=msg)
				newCachedMsg.save()
		elif type == self.NOTIFY_TYPE_SINGLE:
			newCachedMsg = CachedNotification(msgUser=user, notifiUsername=name, note=msg)
			newCachedMsg.save()

	def deleteMsg(self, name):
		try:
			cacheMsgs = CachedNotification.objects.filter(notifiUsername = name)
			for cacheMsg in cacheMsgs:
				message = CachedNotification.objects.get(id=cacheMsg.id)
				message.delete()

		except Exception, e:
			pass