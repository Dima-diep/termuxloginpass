#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
import signal

signal.signal(signal.SIGTSTP, signal.SIG_IGN)

# login have to be as a single word in " "
login = "oldlogin"
print("Login:")
a = input()

if a == login:
    os.system("python3 ~/termuxloginpass/pass.py")
elif a != login:
    print("Login incorrect")
    os.system("python3 ~/termuxloginpass/login.py")
