import signal

from main import cases
import notify2

appname="Covid Cases in India"
iconfile = './favicon.png'



notify2.init(appname)
notification = notify2.Notification(appname, cases)
notification.show()