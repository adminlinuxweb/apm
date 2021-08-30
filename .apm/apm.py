import os
from datetime import datetime
import pyttsx3
import calendar

#speech engine
apm_speech_engine = pyttsx3.init()

while True:
    apm_shell = input("apm$\t")
    
    if apm_shell == "version":
            version_dec = 0.1
            print ("APM version ", version_dec)
    
    elif apm_shell == "options":
            apmoptions_intro = "APM options:"
            print(apmoptions_intro)

    elif apm_shell == "time":
            time = datetime.now()
            current_time = time.strftime("%H:%M:%S")
            print("Current Time =", current_time)
            apm_speech_engine.say(current_time)
            apm_speech_engine.runAndWait()
            

    elif apm_shell == "apm":
            intro = "Welcome to APM, a package manager for any os!"
            print(intro)
            apm_speech_engine.say(intro)
            apm_speech_engine.runAndWait()
            

    elif apm_shell == "pwd":
            pwd = os.getcwd()
            print(pwd)

    elif apm_shell == "calender":
            yy = 2021
            mm = 8
            print(calendar.month(yy,mm))

    elif apm_shell == "install":
            print("We are still working on the install command!")
            print("We applogize for your inconvinience🙏")
    else:
        print("command =", apm_shell)
        print("Sorry, the command you have entered is not found!")
        apm_speech_engine.say("Sorry, the command you have entered is not found!")
        apm_speech_engine.runAndWait()