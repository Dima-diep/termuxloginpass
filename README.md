# termuxloginpass

OS system = Termux

It's termux-locker

## How to install

Until using, change default login and password by:
```
$ python3 chlogin.py
$ python3 chpass.py
```
Also, until installation, run
```
$ chmod 777 * && bash install-requirements.sh
```
for installing requirements.

## How change your login/pass

For change login, run ***chlogin.py***
```
$ python3 chlogin.py
```
For change password, in the first time, run ***chpass.py***
```
$ python3 chpass.py
```
(For later changes, if you used addition.sh, run `chmod 777 ~/termuxloginpass/*` and run commands above)

(If you used ***addition-root.sh***, run:
```
$ sudo bash unadd.sh

$ sudo nano ~/termuxloginpass/login.py (chpass.py)

$ sudo python3 ~/termuxloginpass/chlogin.py (chpass.py)
```
After changing and running, run your addition again)

## Installation

Run ***install.sh*** if you use bash
```
$ bash install.sh
```
Analogically you can uninstall it
```
$ chmod 777 * && bash uninstall.sh
```
## Additional protect

***WARNING! YOU NEED ROOT FOR IT!***
If you want additional protect, run
```
$ bash addition-root.sh
```
### Without root, run (but it isn t very good)
```
$ addition.sh
```
## How uninstall?

For uninstall, run
```
$ python3 uninstall.py
```
