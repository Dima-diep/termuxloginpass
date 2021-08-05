#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os

with open("/data/data/com.termux/files/usr/bin/login", "r") as f:
    raw = f.read().lower().replace("python3 ~/termuxloginpass/login.py", " ")
    file = open("/data/data/com.termux/files/usr/bin/login", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/data/data/com.termux/files/usr/bin/login", "r") as f:
    raw = f.read().lower().replace("sudo python3 ~/termuxloginpass/login.py", " ")
    file = open("/data/data/com.termux/files/usr/bin/login", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/data/data/com.termux/files/usr/bin/login", "r") as f:
    raw = f.read().lower().replace("python3 ~/termuxloginpass/login-style.py", " ")
    file = open("/data/data/com.termux/files/usr/bin/login", "w")
    file.write(raw)
    file.close()
    f.close()

os.system("bash ~/termuxloginpass/unadd.sh && cd ~ && rm -rf ~/.linuxcolor ~/termuxloginpass")
