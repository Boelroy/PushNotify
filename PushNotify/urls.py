from django.conf.urls import patterns, include, url
import settings
import notification
import users
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^notifyCenter$', 'notification.views.main', name='main'),
	url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_URL},name='static'),
    url(r'^notify$','notification.views.notification', name='notification'),
    url(r'^start$','notification.views.start', name='start'),

    url(r'^users$','users.views.getUser',name='getuser'),
    # Examples:
    # url(r'^$', 'PushNotify.views.home', name='home'),
    # url(r'^PushNotify/', include('PushNotify.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
