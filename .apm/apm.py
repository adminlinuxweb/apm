import os
from datetime import datetime
import pyttsx3
import calendar
from pathlib import Path
import subprocess
from getpass import getpass

#speech engine
apm_speech_engine = pyttsx3.init()
username = input("login as:\t")
password = getpass()

if password == "apmkeypairpass":
        while True:

                apm_shell = input(username + "@apm$\t")
                
                if apm_shell == "version":
                        version_dec = 0.1
                        print ("APM version ", version_dec)

                elif apm_shell == "python":
                        pycmd = "python"
                        os.system(pycmd)
                        
                elif apm_shell == "wsl":
                        pycmdw = "bash"
                        os.system(pycmdw)

                elif apm_shell == "os-release":
                        pycmdor = "wmic os get name"
                        os.system(pycmdor)
                
                elif apm_shell == "options":
                        apmoptions_intro = "APM options:"
                        print(apmoptions_intro)

                elif apm_shell == "time":
                        time = datetime.now()
                        current_time = time.strftime("%H:%M:%S")
                        print("Current Time =", current_time)
                        apm_speech_engine.say(current_time)
                        apm_speech_engine.runAndWait()
                        

                elif apm_shell == "apm -intro":
                        intro = "Welcome to APM, a package manager for any os!"
                        print(intro)
                        apm_speech_engine.say(intro)
                        apm_speech_engine.runAndWait()
                        

                elif apm_shell == "pwd":
                        pwd = os.getcwd()
                        print(pwd)

                elif apm_shell == "cal":
                        yy = 2021
                        mm = 8
                        print(calendar.month(yy,mm))

                elif apm_shell == "install":
                        print("We are still working on the install command!")
                        print("We applogize for your inconvinience🙏")

                elif apm_shell == "ls":
                        cmd = 'dir'
                        os.system(cmd)

                elif apm_shell == "dir":
                        cmd = 'dir'
                        os.system(cmd)


                elif apm_shell == "clear":
                        os.system("CLS")

                elif apm_shell == "cls":
                        os.system("CLS")

                elif apm_shell == "uname -a":
                        uname_a = ("APM Shell localhost kernel version 0.1 based on Linux")
                        print(uname_a)

                elif apm_shell == "echo $SHELL":
                        shell_dir = "bin/apmshell"
                        print(shell_dir)

                elif apm_shell == "rm":
                        file = input("Which file do you want to delete?:\t")
                        location = input("Enter the location of the file you want to delete:\t")
                        path = os.path.join(location, file)
                        os.remove(path)
                        print(file + " has been successfully deleted!")
                elif apm_shell == "cd":
                        cd_name = input("Which directry do you want to go to?:\t")
                        os.chdir(cd_name)

                elif apm_shell == "cd /":
                        drive_name = input("Which drive to you want to switch to?:\t")
                        os.chdir(drive_name)

                elif apm_shell == "pip":
                        cnd = "pip"
                        os.system(cnd)

                else:
                        password = getpass()

                        if password == "apmkeypairpass":
                                os.system(apm_shell)
                        else:
                                db = "wrong password"
                                print(db)

        
else:
        print("incorrect username or password, or both may be")
