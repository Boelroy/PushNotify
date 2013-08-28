# Create your views here.
from django.http import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from notification.models import Users

def getUser(request):
	if not 'type' in request.GET:
		users = Users.objects.all()
		title = "All Users"
	elif request.GET['type'] == 'online':
		users = Users.objects.filter(onlineStatus=True)
		title = "Online Users"
	elif request.GET['type'] == 'offline':
	 	users = Users.objects.filter(onlineStatus=False)
	else:
		pass

	renderDic = {}
	renderDic['users'] = users
	renderDic['title'] = title
	print users[1].onlineStatus
	c = RequestContext(request,renderDic)

	return render_to_response('users/users.htm', c)
