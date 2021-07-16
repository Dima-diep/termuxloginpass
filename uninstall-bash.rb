File.write("/data/data/com.termux/files/usr/etc/bash.bashrc", File.open("/data/data/com.termux/files/usr/etc/bash.bashrc",&:read).gsub("python3 login.py", " "))
