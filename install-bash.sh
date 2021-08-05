#!/bin/bash
echo "python3 ~/termuxloginpass/login.py" > /data/data/com.termux/files/usr/etc/login
echo "python3 ~/termuxloginpass/login-style.py" >> /data/data/com.termux/files/usr/etc/login
mkdir ~/.linuxcolor
mv kalilinux ~/.linuxcolor
mv debian ~/.linuxcolor
mv Ubuntu ~/.linuxcolor
mv archlinux ~/.linuxcolor
