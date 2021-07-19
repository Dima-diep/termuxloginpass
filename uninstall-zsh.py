#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os

with open("/data/data/com.termux/files/usr/etc/zshrc", "r") as f:
    raw = f.read().lower().replace("python3 ~/termuxlogin/login.py", " ")
    file = open("/data/data/com.termux/files/usr/etc/zshrc", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/data/data/com.termux/files/usr/etc/zshrc", "r") as f:
    raw = f.read().lower().replace("sudo python3 ~/termuxlogin/login.py", " ")
    file = open("/data/data/com.termux/files/usr/etc/zshrc", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/data/data/com.termux/files/usr/etc/zshrc", "r") as f:
    raw = f.read().lower().replace("python3 ~/termuxlogin/login-style.py", " ")
    file = open("/data/data/com.termux/files/usr/etc/zshrc", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/data/data/com.termux/files/usr/etc/zshrc", "r") as f:
    raw = f.read().lower().replace("chmod +x * && bash exit.sh", " ")
    file = open("/data/data/com.termux/files/usr/etc/zshrc", "w")
    file.write(raw)
    file.close()
    f.close()

os.system("bash ~/termuxloginpass/unadd.sh && cd ~ && rm -rf ~/.linuxcolor ~/termuxloginpass")
