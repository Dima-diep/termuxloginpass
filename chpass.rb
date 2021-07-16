File.write("/data/data/com.termux/files/home/TermPass/pass.py", File.open("/data/data/com.termux/files/home/TermPass/pass.py",&:read).gsub("newpass", "oldpass"))
