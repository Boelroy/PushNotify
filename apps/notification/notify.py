import mosquitto
from datetime import *
from models import Users
from mqttmanage import MqttManagement

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
	def __init__(self):
		self.mqtt = mosquitto.Mosquitto('bowen')
		self.isConnect = False

		#start the mosquitto broker
		self.mqttBroker = MqttManagement("/usr/local/sbin/mosquitto")
		self.mqttBroker.onDisconnect = self.onDisconnect
		self.mqttBroker.onConnect = self.onConnect
		self.mqttBroker.run()
		pass

	def notify(self, msg):
		self.mqtt.connect(host=self.mqtt_host, port=self.mqtt_port)
		self.mqtt.publish('tokudo/123',str(msg))


	def onConnect(self, ip, name):
		print "Connecting"
		newUser = Users.objects.filter(name = name)
		if len(newUser) == 1:
			newUser[0].onlineStatus = True
			newUser[0].ip = ip
			newUser[0].save()
		elif len(newUser) == 0:
			user = Users(name=name, 
							ip=ip, 
							onlineStatus = True, 
							lastonLineTime=datetime.now())
			user.save()
		else:
			raise Exception("Error date Two Clients have the same name")

	def onDisconnect(self,name):
		print name + " is disconnecting"
		disConUser = Users.objects.filter(name = name)
		if len(disConUser) == 1:
			disConUser[0].onlineStatus = False
			disConUser[0].lastonLineTime = datetime.now()
			disConUser[0].save()
		elif len(disConUser) == 0:
			raise Exception("Unkown Users disconnect from the server")
		else :
			raise Exception("Error date Two Clients have the same name")
