#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-
#
# =========================================================
# .________     /\  ________________                __    
# |   ____/    / / /   __   \______ \ _____ _______|  | __
# |____  \    / /  \____    /|    |  \\__  \\_  __ \  |/ /
# /       \  / /      /    / |    `   \/ __ \|  | \/    < 
#/______  / / /      /____/ /_______  (____  /__|  |__|_ \
#       \/  \/                      \/     \/           \/
#  - Made with <3 by the FiveNineDark Team  

import os, sys, time, pycurl
from io import BytesIO 
from alive_progress import alive_bar, bouncing_spinner_factory

PROGRAM_VERSION = '1.0'
b_obj = BytesIO() 
c = pycurl.Curl()
c.setopt(pycurl.USERAGENT, 'Mozilla/5.0 (Windows; U; Windows NT 6.1; it; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)')
c.setopt(c.URL, 'https://fiveninedark.com/api/git/config/config.php')
c.setopt(c.WRITEDATA, b_obj)
c.perform()
c.close() 
body = b_obj.getvalue()
response = body.decode('utf8')
CURRENT_CONFIG = body.decode('utf8')

### MAIN PROGRAM ###
def check_version():
    if response == '1.0':
        #Good to update
        time.sleep(1.5)
        pass
    else:
        print('[*] Current version is {} and the installed program version is {}... Please update to {}'.format(CURRENT_CONFIG, PROGRAM_VERSION, CURRENT_CONFIG))
        UPDATE = 'False'
        sys.exit(1)

def main_update():
    if response == '1.0':
        time.sleep(1)
        os.system('git clone --depth=2 https://github.com/5-9Dark/v1ew-s0urce > /dev/null 2>&1 &')
        print("[✔] Updated to version {}!".format(CURRENT_CONFIG))
    else:
        print("[✔] Program is already on version: {}".format(CURRENT_CONFIG))
        sys.exit(1)
    
### INSTALL HANDLER ###
try:
    message = bouncing_spinner_factory('Working...', 20, left_chars='Please wait.', hiding=False)
    with alive_bar(2, spinner=message) as bar:
        bar(check_version())
        bar(main_update())
    print("[✔] Program Finished!")
except KeyboardInterrupt:
    print('\n\n[!] No exit')
    pass
### END OF PROGRAM ###
