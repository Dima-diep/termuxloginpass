# termuxloginpass

OS system = Termux

It's termux-locker

Until using, change default login and password

Also, until installation, run

$ chmod +x * && bash install-requirements.sh

for installing requirements and check your current shell

For change login, edit chlogin.py and run it

$ python3 chlogin.py

For change password, in the first time, edit chpass.py and run it

$ python3 chpass.py

(For later changes, if you used addition.sh, run chmod +w ~/termuxloginpass/* and run commands above)

(If you used addition-root.sh, run:

$ sudo bash unadd.sh

$ sudo nano ~/termuxloginpass/login.py (chpass.py)

$ sudo python3 ~/termuxloginpass/chlogin.py (chpass.py)

After changing and running, run your addition again)

Run install-bash.sh if you use bash

$ bash install-bash.sh

Run install-zsh.sh if you use zsh

$ bash install-zsh.sh

Analogically you can uninstall it

$ chmod +x * && bash uninstall-bash.sh (or uninstall-zsh.sh)

If you want additional protect, run

[WARNING! YOU NEED ROOT FOR IT!!!]

$ bash addition-root.sh
$ python3 additional-bash.py (or additional-zsh.py)

Without root, run (but it isn t very good)

$ addition.sh

For uninstall, run

$ python3 uninstall-bash.py (uninstall-zsh.py)
