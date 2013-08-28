# Create your views here.
from notify import Notify
from django.http import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response

def main(request):
	c = RequestContext(request,{"main_page":"start/start.htm"})
	return render_to_response('index.htm', c)


def notification(request):
	response = HttpResponse()

	notifymessage = request.GET['notifymessage']

	no = Notify()
	no.notify(notifymessage)

	return response;

def start(request):
	c = RequestContext(request,{})
	renderTemplate = "start/start.htm"
	return render_to_response(renderTemplate, c)