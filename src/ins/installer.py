#!/usr/bin/env python36
# -*- encoding: UTF-8 -*-

# Installer python file to install, update or uninstall fsociety3

import os
import sys

def clearScr():
    os.system('clear')

clearScr()

print('''
███████╗███████╗ ██████╗  ██████╗██╗███████╗████████╗██╗   ██╗██████╗ 
██╔════╝██╔════╝██╔═══██╗██╔════╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝╚════██╗
█████╗  ███████╗██║   ██║██║     ██║█████╗     ██║    ╚████╔╝  █████╔╝
██╔══╝  ╚════██║██║   ██║██║     ██║██╔══╝     ██║     ╚██╔╝   ╚═══██╗
██║     ███████║╚██████╔╝╚██████╗██║███████╗   ██║      ██║   ██████╔╝
╚═╝     ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚══════╝   ╚═╝      ╚═╝   ╚═════╝ 
         python3 build - version: 1.3 - Last update: 1/4/20                                                    
            
             }---{Made by CRO-THEHACKER & Manisso}---{
        }---{https://github.com/CRO-THEHACKER/fsociety3}---{
            
        |---------------------[Main Options]---------------|
        |    1) Install   FSociety3                        |
        |    2) Update    FSociety3                        |
        |    3) Uninstall FSociety3                        |
        |------------------------[MISC.]-------------------|
        |    4) Need help? Do this option...               |
        |--------------------------------------------------|
''')

opt = input('FSOCIETY$: ')
while True:    
    if opt == '1':
        os.system('sudo bash install.sh')
        sys.exit(1)
    elif opt == '2':
        os.system('sudo bash update.sh')
        print("FSOCIETY3: STAT_CODE=DONE")
        sys.exit(1)
    elif opt == '3':
        os.system('sudo bash uninstall.sh')
        print("FSOCIETY3: STAT_CODE=DONE")
        sys.exit(1)
    elif opt == '4':
        print(""" 
        
        Join the discord and go to the #py3s-fs for help
        
        https://discord.gg/BaBpuPn
        
        """)
        sys.exit(1)
    else:
        pass
