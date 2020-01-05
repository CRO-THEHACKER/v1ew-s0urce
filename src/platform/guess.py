#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

# guess os for fsociety3 from the command line fast start..

import os
from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
    # linux
    os.system('python3 /usr/share/doc/fsociety3/src/platform/NORMAL/fsociety3.py')
elif _platform == "darwin":
    # MAC OS X
    os.system('python3 /usr/share/doc/fsociety3/src/platform/NORMAL/fsociety3.py')
elif _platform == "/data/data/com.termux/files/usr" or _platform == "termux":
    # Termux / Android
    os.system('python3 /usr/share/doc/fsociety3/src/platform/MOBIL/MOBIL-fs3.py')
else:
    print("[!]  Could not find OS; try running: python3 /usr/share/doc/fsociety3/src/platform/NORMAL/fsociety3.py")