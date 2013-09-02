import os
import threading
import re

class MqttManagement(object):
	execShell = "{0} 2>&1"
	NEW_CONNECTION_PATTERN = r'\d+: New client connected from (\d+\.\d+\.\d+\.\d+) as (\S+) .*'
	DISCONNECT_PATTERN_1 = r'\d+: Socket read error on client (\S+), disconnecting.*'
	DISCONNECT_PATTERN_2 = r'\d+: Client (\S+) has exceeded timeout, disconnecting.*'
	START_PATTERN = r'\d+: (Opening ipv6 listen socket on port 1883.)'

	ERROR_PATTERN = r'\d+: (Error): Address already in use'

	"""docstring for MqttMangement"""
	def __init__(self, mosquittoPath):
		self.__runStatus = False;
		if(mosquittoPath == None):
			raise Exception("mosquitto path can not be none")

		self.execShell = self.execShell.format(mosquittoPath)

	""" 
	the callback function when a new 
	client connect to the mosquitto 
	broker
	"""
	def onConnect(self, name, ip):
		pass

	""" 
	the callback function when a new 
	client disconnect to the mosquitto 
	broker
	"""
	def onDisconnect(self, name):
		pass

	def onCmdRun(self):
		pass

	"""
	start run the mosquitto broker on
	the host
	"""
	def run(self):
		print "in Run func" + str(hasattr(self,"mThread"))
		if not hasattr(self,"mThread"):
			self.mThread = threading.Thread(target=self.getStrFromCmd)
			self.mThread.start()

	def getStrFromCmd(self):
		print self.execShell
		strFromCmd = os.popen(self.execShell)
		self.__runStatus = True
		info = strFromCmd.readline()
		while info:
			print info
			info_tmp = info
			match = re.match(self.START_PATTERN, info_tmp)
			if match:
				self.onCmdRun()
				info = strFromCmd.readline()
				continue

			match = re.match(self.NEW_CONNECTION_PATTERN, info_tmp)
			if match:
				ipAndName = match.groups()
				self.onConnect(ipAndName[0], ipAndName[1])
				info = strFromCmd.readline()
				continue

			match = re.match(self.DISCONNECT_PATTERN_1, info_tmp)
			if match:
				name = match.groups()
				self.onDisconnect(name[0])
				info = strFromCmd.readline()
				continue

			match = re.match(self.DISCONNECT_PATTERN_2, info_tmp)
			if match:
				name = match.groups()
				self.onDisconnect(name[0])
				info = strFromCmd.readline()
				continue

			match = re.match(self.ERROR_PATTERN, info_tmp)
			if match:
				self.__runStatus = False
			
			info = strFromCmd.readline()



	def getMosquittoisRunning(self):
			return self.__runStatus