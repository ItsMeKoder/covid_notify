import argparse
import platform
from case import cases,deaths,recovered,active,confirmed
import pyttsx3
from notifypy import notify as Notify
from googletrans import *
import gtts
from playsound import playsound
import config
def notify():
    """
    Notify the Cases etc.
    """
    print("Default Language is",config.Language)



    appname="Covid Cases in Haryana"

    c="In Haryana,"+" people died are "+str(deaths)+". Active cases are "+str(active)+". Patients recovered are "+str(recovered)+". Total cases confirmed are "+str(confirmed)
    print("Original text is : ",c)


    c_platform=platform.system()

    if c_platform == 'Linux':
        import notify2
        notify2.init(appname)
        notification = notify2.Notification(appname, cases)
        notification.show()

    else:
#        notification = Notify(default_notification_title="Covid 19 Cases in Haryana", default_application_name="Covid-19 Cases", default_notification_icon="./icon.png", default_notification_audio="./sound.wav")
        notification=Notify
        notification.icon='./icon.png'
        notification.message = c
        #notification.send()


    translator = Translator()
    print(config.Language[:2])
    result = translator.translate(c,dest=config.Language[:2])
    print("Translated test is :  ",result.text)

    tts = gtts.gTTS(result.text, lang=config.Language[:2])
    tts.save("main.mp3")
    playsound("main.mp3")


