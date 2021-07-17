#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

with open("/data/data/com.termux/files/usr/etc/zshrc", "r") as f:
    raw = f.read().lower().replace("python3 login.py", " ")
    file = open("/data/data/com.termux/files/usr/etc/zshrc", "w")
    file.write(raw)
    file.close()
    f.close()
with open("/data/data/com.termux/files/usr/etc/zshrc", "r") as f:
    raw = f.read().lower().replace("sudo python3 login.py", " ")
    file = open("/data/data/com.termux/files/usr/etc/zshrc", "w")
    file.write(raw)
    file.close()
    f.close()
with open("/data/data/com.termux/files/usr/etc/zshrc", "r") as f:
    raw = f.read().lower().replace("python3 login-style.py", " ")
    file = open("/data/data/com.termux/files/usr/etc/zshrc", "w")
    file.write(raw)
    file.close()
    f.close()
