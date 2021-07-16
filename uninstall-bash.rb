File.write("/data/data/com.termux/files/usr/etc/bash.bashrc", File.open("/data/data/com.termux/files/usr/etc/bash.bashrc",&:read).gsub("python3 ~/termuxloginpass/login.py", " "))
File.write("/data/data/com.termux/files/usr/etc/bash.bashrc", File.open("/data/data/com.termux/files/usr/etc/bash.bashrc",&:read).gsub("sudo python3 ~/termuxloginpass/login.py", " "))
File.write("/data/data/com.termux/files/usr/etc/bash.bashrc", File.open("/data/data/com.termux/files/usr/etc/bash.bashrc",&:read).gsub("python3 ~/termuxloginpass/login-style.py", " "))
