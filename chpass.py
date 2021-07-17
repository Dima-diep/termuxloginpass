#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

print("Old password:")
a = input()
print("New password:")
b = input()

with open("/data/data/com.termux/files/home/termuxloginpass/pass.py", r) as f:
    raw = f.read().lower().replace(a, b)
    file = open("/data/data/com.termux/files/home/termuxloginpass/pass.py", w)
    file.write(raw)
    file.close()
    f.close()
