#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
import getpass
#password have to be as a single word in " "
passwd = "oldpass"
a = getpass.getpass("Password: ")

if a == passwd:
    os.system("kill -9 python3")
elif a != passwd:
    print("Password incorrect")
    os.system("python3 ~/termuxloginpass/login.py")
