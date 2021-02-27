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
#  - Made with <3 by the FiveNineDark Dev team  


import os
import sys
import random
import time

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'
    # BG
    LIGHTGREY_BG ='\033[47m'
    DARKGREY_BG = '\033[90m'
    RED_BG = '\033[41m'
    BLACK_TEXT = '\033[40m'

color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]
random.shuffle(color_random)

def clearScr():
    os.system('clear')

####################

def qm_1():
  clearScr()
def qm_2():
  clearScr()
def qm_3():
  clearScr()
def main_menu():
  clearScr()
  
####################
clearScr()
start_menu = """
        ___,___,_______,____
        |  :::|///./||'||    \\ 
        |  :::|//.//|| || H)  |
        |  :::|/.///|!!!|     |              V1EW S0URCE 
        |   _______________   |         Made with <3 by 5/9Dark
        |  |""" + color.RED_BG + """:::::::::::::::""" + color.END + """|  |
        |  |""" + color.LIGHTGREY_BG + """_______________""" + color.END + """|  |
        |  |""" + color.LIGHTGREY_BG + """_______________""" + color.END + """|  |
        |  |""" + color.LIGHTGREY_BG + """_______________""" + color.END + """|  |   
        |  |""" + color.LIGHTGREY_BG + """_______________""" + color.END + """|  |  - Visit us at FiveNineDark.com
        ||_|""" + color.LIGHTGREY_BG + """    SKYLIT     """ + color.END + """||_|  - Join us on Discord[.gg/BaBpuPn]
        |__|_______________|__|
              CODENAME: SKYLIT

  """ + color.DARKGREY_BG + """[================================================================]""" + color.END + """          


      """ + color.LIGHTGREY_BG +  color.RED + """[ Quick Menu ]""" + color.END + """
  
      [ 1. Create Payloads ]   
      
      [ 2. Web Exploit Menu ] 

      [ 3. Automated Network Scans ]


  """ + color.DARKGREY_BG + """[================================================================]""" + color.END + """
      
      """ + color.LIGHTGREY_BG +  color.RED + """[ Main Menu ]""" + color.END + """

      [ 4. View all ]\n\n
  Type """ + color.NOTICE + """EXIT""" + color.END + """ to end the program!

"""

def main_menu():
  clearScr()
  main_menuScr = """
        ___,___,_______,____
        |  :::|///./||'||    \\ 
        |  :::|//.//|| || H)  |             """ + color.RED + color.LIGHTGREY_BG + """[ MAIN MENU ]""" + color.END + """
        |  :::|/.///|!!!|     |              V1EW S0URCE 
        |   _______________   |         Made with <3 by 5/9Dark
        |  |""" + color.RED_BG + """:::::::::::::::""" + color.END + """|  |
        |  |""" + color.LIGHTGREY_BG + """_______________""" + color.END + """|  |
        |  |""" + color.LIGHTGREY_BG + """_______________""" + color.END + """|  | 
        |  |""" + color.LIGHTGREY_BG + """_______________""" + color.END + """|  |   
        |  |""" + color.LIGHTGREY_BG + """_______________""" + color.END + """|  |  - Visit us at FiveNineDark.com
        ||_|""" + color.LIGHTGREY_BG + """    SKYLIT     """ + color.END + """||_|
        |__|_______________|__|
              CODENAME: SKYLIT

      Type 'menu' to display menu options.  
      * Type 'help' to get started - More on the menu 'help {menu-number}'.

  """ + color.DARKGREY_BG + """[================================================================]""" + color.END
  print(main_menuScr)
  
  while True:
    menu_opt = input("Project-SKYLIT$> "S)
    if menu_opt == "help":
      print(help_screen)
    elif menu_opt == "menu":
      
    elif menu_opt == "":
      #

# main 
clearScr()
print(start_menu)

sel_term = input("Command: ")

if sel_term == "1":
  qm_1()
elif sel_term == "2":
  qm_2()
elif sel_term == "3":
  qm_3()
elif sel_term == "4":
  main_menu()
