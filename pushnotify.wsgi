import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(root_path)))
sys.path.insert(0, os.path.abspath(os.path.join(root_path, 'app')))
sys.path.append(os.path.abspath(os.path.join(root_path, 'PushNotify')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'PushNotify.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
