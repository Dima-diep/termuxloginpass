#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os

# login have to be as a single word in " "
login = "oldlogin"
print("Login:")
a = input()

if a == login:
    os.system("python3 ~/TermPass/pass.py")
elif a != login:
    print("Login incorrect")
    os.system("python3 ~/TermPass/login.py")
