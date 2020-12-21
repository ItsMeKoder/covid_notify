import argparse
import platform
from case import cases,deaths,recovered,active,confirmed
import pyttsx3
from notifypy import Notify
from googletrans import *
import gtts
from playsound import playsound


LANGUAGE=''

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument(dest='LANGUAGE', metavar='LANGUAGE', type=str, nargs='+',
                    help='an integer for the accumulator')

args = parser.parse_args()
LANGUAGE=args.LANGUAGE[0][:2]
print(LANGUAGE)


print("Default Language is",LANGUAGE)



appname="Covid Cases in Haryana"
iconfile = './icon.png'


c="In Haryana,"+" people died are "+str(deaths)+". Active cases are "+str(active)+". Patients recovered are "+str(recovered)+". Total cases confirmed are "+str(confirmed)
print("Original text is : ",c)


c_platform=platform.system()

if c_platform == 'Linux':
   import notify2
   notify2.init(appname)
   notification = notify2.Notification(appname, cases)
   notification.show()

else:
   notification = Notify(default_notification_title="Covid 19 Cases in Haryana", default_application_name="Covid-19 Cases", default_notification_icon="./icon.png", default_notification_audio="./sound.wav")
   notification.icon='./icon.png'
   notification.message = c
   notification.send()


translator = Translator()
result = translator.translate(c,dest=LANGUAGE[:2])
print("Translated test is :  ",result.text)

tts = gtts.gTTS(result.text, lang=LANGUAGE[:2])
tts.save("main.mp3")
playsound("main.mp3")


