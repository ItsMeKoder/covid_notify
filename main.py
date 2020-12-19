
import platform
from case import cases,deaths,recovered,active,confirmed
import pyttsx3
from notifypy import Notify



appname="Covid Cases in Haryana"
iconfile = './icon.png'

c="In Haryana,"+" people died are "+str(deaths)+". Active cases are "+str(active)+". Patients recovered are "+str(recovered)+". Total cases confirmed are "+str(confirmed)
print(c)


c_platform=platform.system()

if c_platform == 'Linux':
   import notify2
   notify2.init(appname)
   notification = notify2.Notification(appname, cases)
   notification.show()

else:
   notification = Notify(default_notification_title="Function Message", default_application_name="Covid-19 Cases", default_notification_icon="./icon.png", default_notification_audio="./sound.wav")
   notification.icon='./icon.png'
   notification.message = c
   notification.send()



engine = pyttsx3.init()
engine.setProperty('rate', 215)
engine.say(c)
engine.runAndWait()
