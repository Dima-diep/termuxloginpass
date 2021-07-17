# termuxloginpass

OS system = Termux

It's termux-locker

Until using, change default login and password

Also, until installation, run

$ chmod +x * && bash install-requirements.sh

for installing requirements and check your current shell

For change login, edit chlogin.rb and run it

$ ruby chlogin.rb

For change password, in the first time, edit chpass.rb and run it

$ ruby chpass.rb

(For later changes, if you used addition.sh, run chmod +w ~/termuxloginpass/* and run commands above)

(If you used addition-root.sh, run:

$ sudo bash unadd.sh

$ sudo nano ~/termuxloginpass/login.rb (chpass.rb)

$ sudo ruby ~/termuxloginpass/chlogin.rb (chpass.rb)

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
$ ruby addition-bash.rb (or addition-zsh.rb)

Without root, run (but it isn t very good)

$ addition.sh

For uninstall, run

$ ruby uninstall-bash.rb (uninstall-zsh.rb)
