import pyshorteners
import sys
import time
import requests


def animate(text) :
    for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.001)


def is_valid(url):
    try :
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def is_exit():
    user = input("\033[0;32m~ enter \033[0;31m0 \033[0;32mto exit \n~\033[0;32m else press anthing to continue ")
    if user in ( 0,"0",'0'):
        return False
    else:
        return True

# logo
logo = """
\033[0;32m██      ██ ███    ██ ██   ██     ███████ ██   ██  ██████  ██████  ████████ ███    ██ ███████ ██████  
██      ██ ████   ██ ██  ██      ██      ██   ██ ██    ██ ██   ██    ██    ████   ██ ██      ██   ██ 
██      ██ ██ ██  ██ █████       ███████ ███████ ██    ██ ██████     ██    ██ ██  ██ █████   ██████  
██      ██ ██  ██ ██ ██  ██           ██ ██   ██ ██    ██ ██   ██    ██    ██  ██ ██ ██      ██   ██ 
███████ ██ ██   ████ ██   ██     ███████ ██   ██  ██████  ██   ██    ██    ██   ████ ███████ ██   ██
░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒ ▒ ▒▒ ▓   ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ 
░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░░ ░▒ ▒    ░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░   ░▒ ░ ▒░    ░    ░ ░░   ░ ▒░ ░ ░  ░  ░▒ 
  ░ ░    ▒ ░   ░   ░ ░ ░ ░░     ░  ░  ░   ░  ░░ ░░ ░ ░ ▒    ░░   ░   ░         ░   ░ ░    ░     ░░ 
    ░  ░ ░           ░ ░  ░            ░   ░  ░  ░    ░ ░     ░                       ░    ░  ░   ░     

\033[0;31m***************************  

\033[1;33mAUTHOR : SH4RK00
social : https://github.com/SH4RK00  

\033[0;31m***************************
"""
#text
text="""
\033[0;32m[+] working on it ~
[+] wait a second ~
"""
#warn
warn ='''
\033[0;31m[-]something went to wrong :[
[-]check the link is valid or not
[-]check properly installed requirements.txt
'''


animate(logo)

#link shortner main
terminate = True
while terminate:

    url = input("\033[0;32mEnter your link :\033[0;34m")

    if is_valid(url):
        animate(text)
        time.sleep(1)
        s = pyshorteners.Shortener()
        provide = s.tinyurl.short(url)
        print(f"\033[0;32myour shorten link is :\033[1;33m{provide}")
        time.sleep(1)
        print("\n")
        terminate = is_exit()
        print("\n")

    else:
        animate(warn)
        time.sleep(1)
        print("\n")
        terminate = is_exit()
        print("\n")
