File.write("/data/data/com.termux/files/usr/etc/zshrc", File.open("/data/data/com.termux/files/usr/etc/zshrc",&:read).gsub("python3 login.py", "sudo python3 login.py"))
