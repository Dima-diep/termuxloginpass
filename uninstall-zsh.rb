File.write("/data/data/com.termux/files/usr/etc/zshrc", File.open("/data/data/com.termux/files/usr/etc/zshrc",&:read).gsub("python3 ~/termuxloginpass/login.py", " "))
File.write("/data/data/com.termux/files/usr/etc/zshrc", File.open("/data/data/com.termux/files/usr/etc/zshrc",&:read).gsub("sudo python3 ~/termuxloginpass/login.py", " "))
File.write("/data/data/com.termux/files/usr/etc/zshrc", File.open("/data/data/com.termux/files/usr/etc/zshrc",&:read).gsub("python3 ~/termuxloginpass/login-style.py", " "))
