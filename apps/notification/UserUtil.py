from models import Users

"""the singleton func"""
def singleton(cls, *args, **kw):   
    instances = {}   
    def _singleton():   
        if cls not in instances:   
            instances[cls] = cls(*args, **kw)   
        return instances[cls]   
    return _singleton

@singleton
class UserUtil(object):
	"""the User Helper class to 
		to help Manage the User Entity
	"""
	def __init__(self):
		pass
	

	def addUser(self,name,lastonLineTime,onlineStatus,ip):
		existUser = Users.objects.filter(name=name)
		if len(existUser) != 0:
			raise Exception("the Users is already exits")

		newUser = Users(name=name, 
						ip=ip, 
						onlineStatus = True, 
						lastonLineTime=lastonLineTime)

		newUser.save()

	def changeUser(self, name, **changeDic):
		existUser = self.getUsers(name)
		changeDic = dict(changeDic)
		print changeDic
		if existUser:
			for attribute, value in changeDic.iteritems():
				setattr(existUser, attribute, value)

			existUser.save()

	def isInUsers(self, name):
		try:
			existUser = Users.objects.get(name=name)
			return True
		except Exception, e:
			return False

	def getUsers(self, name):
		try:
			existUser = Users.objects.get(name=name)
			return existUser
		except Exception, e:
			return None
