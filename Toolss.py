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
Created By AnonHacker
Channel: youtube.com/kalinuxx
Facebook: facebook.com/kalinuxtutorials
Ver: 1.0
----
ONLY FOR TERMUX!
----
========================================
1. Install Nmap
2. Install Hydra
3. Install SQLMap
4. Install Metasploit
5. Install ngrok
6. Install Kali Nethunter
7. Install angryFuzzer
8. Install Red_Hawk
9. Install Weeman
10. Install IPGeoLocation
--------
11. Update
99. Exit
========================================
""")

loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "1":
        os.system("cd $HOME")
        os.system("pkg update")
        os.system("pkg install -y nmap")
        os.system("cd $HOME")
        print("====================================")
        print("[+] nmap installed successfully :)")
        print("[+] Type 'nmap' to start.")
        print("====================================")
        break
    elif what == "2":
        os.system("cd $HOME")
        os.system("pkg update")
        os.system("pkg install -y hydra")
        os.system("cd $HOME")
        print("====================================")
        print("[+] hydra installed successfully :)")
        print("[+] Type 'hydra' to start.")
        print("====================================")
        break
    elif what == "3":
        os.system("cd $HOME")
        os.system("pkg update")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("git clone https://github.com/sqlmapproject/sqlmap.git")
        os.system("cd $HOME")
        print("====================================")
        print("[+] SQLMap installed successfully :)")
        print("[+] Go to sqlmap folder and type 'python2 sqlmap.py' to start.")
        print("====================================")
        break
    elif what == "4":
        os.system("cd $HOME")
        os.system("wget https://Auxilus.github.io/metasploit.sh")
        os.system("bash metasploit.sh")
        os.system("cd $HOME")
        os.system("cd metasploit-framework")
        os.system("gem install bundle --pre")
        os.system("bundle config build.nokogiri --use-system-libraries")
        os.system("bundle install")
        os.system("cd $HOME")
        print("====================================")
        print("[+] Metasploit installed successfully :)")
        print("[+] Type 'msfconsole' to start.")
        print("====================================")
        break
    elif what == "5":
        os.system("cd $HOME")
        os.system("pkg update")
        os.system("pkg install -y git")
        os.system("cd $HOME")
        os.system("git clone https://github.com/themastersunil/ngrok.git")
        os.system("cd $HOME")
        print("====================================")
        print("[+] ngrok installed successfully :)")
        print("[+] Go to ngrok folder and type './ngrok http 80' to start.")
        print("====================================")
        break
    elif what == "6":
        os.system("cd $HOME")
        os.system("pkg update")
        os.system("cd $HOME")
        os.system("git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
        os.system("cd Nethunter-In-Termux")
        os.system("chmod +x kalinethunter")
        os.system("cd $HOME")
        print("====================================")
        print("[+] Nethunter installed successfully :)")
        print("[+] Go to Nethunter-In-Termux folder and type './kalinethunter' to start.")
        print("====================================")
        break
    elif what == "7":
        os.system("cd $HOME")
        os.system("pkg update")
        os.system("pkg install -y git")
        os.system("cd $HOME")
        os.system("pkg install -y python2")
        os.system("git clone https://github.com/ihebski/angryFuzzer.git")
        os.system("cd angryFuzzer")
        os.system("pip2 install -r requirements.txt")
        os.system("pip2 install requests")
        os.system("cd $HOME")
        print("====================================")
        print("[+] angryFuzzer installed successfully :)")
        print("[+] Go to angryFuzzer folder and type 'python2 angryFuzzer.py' to start.")
        print("====================================")
        break
    elif what == "8":
        os.system("cd $HOME")
        os.system("pkg update")
        os.system("pkg install -y git")
        os.system("pkg install -t php")
        os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")
        os.system("cd $HOME")
        print("====================================")
        print("[+] RED_HAWK installed successfully :)")
        print("[+] Go to RED_HAWK folder and type 'php rhawk.php' to start.")
        print("====================================")
        break
    elif what == "9":
        os.system("cd $HOME")
        os.system("pkg update")
        os.system("pkg install -y python2")
        os.system("pkg install -y git")
        os.system("cd $HOME")
        os.system("git clone https://github.com/evait-security/weeman.git")
        os.system("cd weeman")
        os.system("chmod +x weeman.py")
        os.system("cd $HOME")
        print("====================================")
        print("[+] weeman installed successfully :)")
        print("[+] Go to weeman folder and type 'python2 weeman.py' to start.")
        print("====================================")
        break
    elif what == "10":
        os.system("cd $HOME")
        os.system("pkg update")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd $HOME")
        os.system("git clone https://github.com/maldevel/IPGeoLocation.git")
        os.system("cd IPGeoLocation")
        os.system("pip3 install -r requirements.txt")
        os.system("cd $HOME")
        print("====================================")
        print("[+] IPGeoLocation installed successfully :)")
        print("[+] Go to IPGeoLocation folder and type 'python ipgeolocation.py' to start.")
        print("====================================")
        break
    elif what == "11":
         os.system("cd $HOME")
         os.system("rm Toolss.py")
         os.system("git clone https://github.com/AnonHackerr/toolss.git")
         print("====================================")
         print("[+] Toolss Updated successfully :)")
         print("====================================")
         break
    elif what == "99":
        print("Bye.")
        break