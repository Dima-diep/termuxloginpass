#!/bin/bash
echo "#!/bin/bash" > /data/data/com.termux/files/usr/bin/login
echo "python3 ~/termuxloginpass/login.py" >> /data/data/com.termux/files/usr/bin/login
echo "python3 ~/termuxloginpass/login-style.py" >> /data/data/com.termux/files/usr/bin/login
mkdir ~/.linuxcolor
mv kalilinux ~/.linuxcolor
mv debian ~/.linuxcolor
mv Ubuntu ~/.linuxcolor
mv archlinux ~/.linuxcolor
