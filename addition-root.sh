#!/bin/bash
apt install tsu root-repo -y
sudo chown root ~/termloginpass/chlogin.py
sudo chown root ~/termloginpass/chpass.py
sudo chown root ~/termloginpass/login.py
sudo chown root ~/termloginpass/pass.py
sudo chmod 500 ~/termloginpass/chlogin.py
sudo chmod 500 ~/termloginpass/chpass.py
sudo chmod 500 ~/termloginpass/login.py
sudo chmod 500 ~/termloginpass/pass.py
sudo chattr +i ~/termloginpass/chlogin.py
sudo chattr +i ~/termloginpass/chpass.py
sudo chattr +i ~/termloginpass/login.py
sudo chattr +i ~/termloginpass/pass.py
sudo chown root ~/termloginpass
sudo chmod 500 ~/termloginpass
sudo chattr +i ~/termloginpass
