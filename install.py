import os, time, subprocess, sys
from sys import stdout


def Command_exe(msg,cmd):
    i = "[STATUS] Processing"
    stdout.write(" " + msg + " %s" % i)
    stdout.flush()
    if subprocess.call(cmd +' >/dev/null 2>&1', shell=True)==0:
        i = "Complete [WARNING] "
    else:
        i = "Error [WARNING] "
    stdout.write("\r" + msg +"[STATUS] %s" % i)

def start():
    if os.getuid() != 0:
        print("[ERROR] Install must be run as root.")
        print("Login as root (sudo) or try sudo python3 install.py")
        exit()
    print(" ==  BabySploit Installation  ==")
    input("Press ENTER To Start Installation")
    with open("/etc/apt/sources.list", "r") as myfile:
        data = myfile.read().replace('\n', "")
        if "http://http.kali.org/kali" not in data:
            print(Command_exe("["+time.strftime('%H:%M:%S')+"] Adding Repo To Sources...                  ",'apt-add-repository "deb http://http.kali.org/kali kali-rolling main non-free contrib"')) 
        else:
            pass
    print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing Required Dependencies...        ",'apt-get install exploitdb netcat nmap php7.0 perl -y'))
    print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing Virtual Environment...          ",'pip3 install virtualenv'))
    print("Complete!")
    print("Please start virtualenv and run pip3 install -r requirements.txt!")

start()
