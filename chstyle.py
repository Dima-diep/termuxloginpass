#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
print("Old style (print this: \"a = \"kali\"\"):")
a = input()
print("New style:")

with open("/data/data/com.termux/files/home/termuxloginpass/login-style.py", r) as f:
    raw = f.read().lower().replace("a = \"kali\"", "a = \"arch\""
    file = open("/data/data/com.termux/files/home/termuxloginpass/login-style.py", w)
    file.write(raw)
    file.close()
    f.close()
