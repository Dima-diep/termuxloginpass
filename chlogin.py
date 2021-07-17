#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

with open("/data/data/com.termux/files/home/termuxloginpass/login.py", "r") as f:
    raw = f.read().lower().replace("oldlogin", "newlogin")
    file = open("/data/data/com.termux/files/home/termuxloginpass/login.py", "w")
    file.write(raw)
    file.close()
    f.close()
