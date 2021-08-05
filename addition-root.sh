#!/bin/bash
apt install tsu root-repo -y
sudo chown root ~/termuxloginpass/chlogin.py
sudo chown root ~/termuxloginpass/chpass.py
sudo chown root ~/termuxloginpass/login.py
sudo chown root ~/termuxloginpass/pass.py
sudo chmod 500 ~/termuxloginpass/chlogin.py
sudo chmod 500 ~/termuxloginpass/chpass.py
sudo chmod 500 ~/termuxloginpass/login.py
sudo chmod 500 ~/termuxloginpass/pass.py
sudo chattr +i ~/termuxloginpass/chlogin.py
sudo chattr +i ~/termuxloginpass/chpass.py
sudo chattr +i ~/termuxloginpass/login.py
sudo chattr +i ~/termuxloginpass/pass.py
sudo chown root ~/termuxloginpass
sudo chmod 500 ~/termuxloginpass
sudo chattr +i ~/termuxloginpass
