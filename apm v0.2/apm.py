import os
from datetime import datetime
import pyttsx3
import calendar
from pathlib import Path
import subprocess
from getpass import getpass
import socket
from sudo import run_as_sudo
import gc
import requests, json , sys
import ifcfg

#speech engine

def engine_talk(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


username = input("login as:\t")
password = getpass()

if password == "@apmpass123$":
        while True:
                hostname = socket.gethostname()
                apm_shell = input(username + "@" + hostname + "$ ")
                        
                if apm_shell == "version":
                        version_dec =" 0.2 "
                        version_release_state = "(beta)"
                        print ("APM version " +  version_dec + version_release_state)
                                        
                elif "hello" in apm_shell:
                        output = "hi, how can I help you today?"
                        print(output)

                elif apm_shell == "age":
                        current_year = input("Please enter the present year:\t")
                        birth_year = input("Please enter birth year:\t")
                        age = int(current_year) - int(birth_year)
                        print("Your age is", age)

                elif apm_shell == "python":
                        pycmd = "python"
                        os.system(pycmd)
                                
                elif apm_shell == "wsl":
                        pycmdw = "bash"
                        os.system(pycmdw)

                elif apm_shell == "os-release":
                        pycmdor = "wmic os get name"
                        os.system(pycmdor)
                        
                elif "os-architecture" in apm_shell:
                        nxcmd = "wmic os get osarchitecture"
                        os.system(nxcmd)

                elif apm_shell == "options":
                        apmoptions_intro = "APM options:"
                        print(apmoptions_intro)

                elif apm_shell == "time":
                        time = datetime.now().strftime('%I:%M %p')
                        engine_talk('The current time is' +time)
                                

                elif apm_shell == "apm -intro":
                        intro = "Welcome to APM, a package manager for any os!"
                        print(intro)
                        engine_talk(intro)
                                

                elif apm_shell == "pwd":
                        pwd = os.getcwd()
                        print(pwd)

                elif apm_shell == "cal":
                        yy = 2021
                        mm = 9
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

                elif apm_shell == "clean":
                        os.system("CLS")

                elif apm_shell == "uname -a":
                        hostname = socket.gethostname()
                        uname_a = ("APM Shell " + hostname  + " kernel version 0.2 (beta) based on Linux")
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
                        
                #version 0.2 command:
                elif "giveip" in apm_shell:
                        hostname = socket.gethostname()
                        ip_address = socket.gethostbyname(hostname)
                        print(f"Hostname: {hostname}")
                        print(f"IP Address: {ip_address}")

                elif "which" in apm_shell:
                        print("The command '" + apm_shell + " is using the which function which is available in the latest version 0.2")

                elif "sudo" in apm_shell:
                        password = getpass()
                        if password == "@apmpass123$":
                                print("The command " + apm_shell +  " is using sudo function which is available in the latest version 0.2")
                        else:
                                print("sudo: wrong password")

                elif "ifcfg" in apm_shell:
                        print(ifcfg.interfaces())

                elif "pfr" in  apm_shell:
                        rf = "<pfr> -rf to run a file"
                        df = "<pfr> -df to delete a file"
                        
                #python file runner commands
                elif "pfr -rf" in apm_shell:
                        runfile = apm_shell.replace("pfr -rf", "python")
                        os.system(runfile)

                #exit command
                elif "exit" in apm_shell:
                        sys.exit()

                        #in all versions

                else:
                        password = getpass()
                        if password == "@apmpass123$":
                                os.system(apm_shell)
                        else:
                                db = "wrong password"
                                print(db)

                
        else:
                print("incorrect username or password, or both may be")
