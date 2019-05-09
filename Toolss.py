import os

def menu():

    print(""" 
.########..#######...#######..##........######...######.
....##....##.....##.##.....##.##.......##....##.##....##
....##....##.....##.##.....##.##.......##.......##......
....##....##.....##.##.....##.##........######...######.
....##....##.....##.##.....##.##.............##.......##
....##....##.....##.##.....##.##.......##....##.##....##
....##.....#######...#######..########..######...######.
========================================
Created By daLoAttack
Ver: 2.0
----
ONLY FOR TERMUX!
----
==========================================
00. Turn your Android into Hacking Machine.
------------------------------------------
1. Install Nmap 
2. Install Hydra
3. Install SQLMap
4. Install Metasploit
5. Install ngrok

------------------------------------------
99. Exit
==========================================
""")

loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "00":
        print("================================")
        print("This will install: nmap, hydra, sqlmap, metasploit, ngrok, with one click.")
        print("----------------")
        hm = input("[?] Do you want to continue? (y/n): ")
        print("================================")
        if hm == "y":
            print("========================================================")
            print("[+] Please put down you android and go to the toilet...")
            print("Because this will take a long time.")
            print("========================================================")
            os.system("pkg update")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y python2")
            os.system("pkg install -y wget")
            os.sysetm("pkg install -y nmap")
            os.system("plg install -y hydra ")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg install wget")
            os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
            os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
            os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
            os.system("cd /data/data/com.termux/files/home && bundle install")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("clear")
            print("========================================")
            print("[+] everything successfully installed :)")
            print("[+] Happy Hacking <3")
            print("========================================")
        else:
            rmenu = input("[?] Back to Menu? (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    if what == "1":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y nmap")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] nmap installed successfully :)")
        print("[+] Type 'nmap' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "2":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y hydra")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] hydra installed successfully :)")
        print("[+] Type 'hydra' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "3":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] SQLMap installed successfully :)")
        print("[+] Go to sqlmap folder and type 'python2 sqlmap.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "4":
        os.system("pkg install -y wget")
        os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
        os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
        os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
        os.system("cd /data/data/com.termux/files/home && bundle install")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Metasploit installed successfully :)")
        print("[+] Type 'msfconsole' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "5":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] ngrok installed successfully :)")
        print("[+] Go to ngrok folder and type './ngrok http 80' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            print("====================================")
            print("[+] routersploit installed successfully :)")
            print("[+] Go to routersploit folder and type 'python2 rsf.py' to start.")
            print("====================================")
            rmenu = input("[?] Back to Menu? (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    elif what == "99":
        print("Bye.")
        break
