import platform
from main import cases

appname="Covid Cases in Haryana"
iconfile = './favicon.png'

c_platform=platform.system()

if c_platform == 'Linux':
   import notify2
   notify2.init(appname)
   notification = notify2.Notification(appname, cases)
   notification.show()
elif c_platform == 'Darwin':
   import pync
   pync.notify(cases,title=appname)
