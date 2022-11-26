#!/usr/bin/env python3
import sys
import os
import shutil
import subprocess
from functions import *



installer_version="P1.25"


def install(keyword):
    # not implemented yet 
    action = "NI"

    if action !="force":
        # checking ubuntu
        apt = "/usr/bin/apt"
        if os.path.exists(apt) == True:
            os_install = "ubuntu"
        
        cent = "/usr/bin/yum"
        if os.path.exists(cent) == True:
            os_install = "centos"

        arch = "/usr/bin/pacman"
        if os.path.exists(arch) == True:
            os_install = "arch"

    pkg_list = "make jq bison libtool automake autoconf flex unzip python3 xxd"

    if os_install == "ubuntu":
        command = f"apt-get install {pkg_list} -y"
        os.system(command)

    elif os_install == "arch":
        command = f"pacman -Sy {pkg_list} --confirm"
        os.system(command)

    elif os_install == "centos":
        command = f"yum install {pkg_list} -y"
        os.system(command)

    else :

        if keyword != "force":
            sys.exit("I Don't support the distro that you use. If YOU do run this command with --force")
        else :
            exit_msg = f"This tool wasn't build for the distro that your running. Shit might be weird. Good luck"
            sys.exit(exit_msg)
    
    print("Extracting and placing files")
    
    hit_list = ["/opt/encore", "/etc/encore", "/var/encore", "/var/log/encore" ]

    for path in hit_list:
        
        make_folder(path)
    
    # After the folder trees have been created the log can be initialized for the first time
    start_log()

    if os.path.exists("/opt/encore/encore") == False:
        hit_list = ["conf.py", "encore", "functions.py", "install.py", "encrypt"]

        for files in hit_list:

            src = f"./{files}"
            dst = f"/opt/encore/{files}"
            copy_file(src, dst)

    if os.path.exists("/usr/local/bin/encrypt") == False:
        os.symlink("/opt/encore/encrypt", "/usr/local/bin/encrypt")
    
    if os.path.exists("/usr/local/bin/encore") == False:
        os.symlink("/opt/encore/encore", "/usr/local/bin/encore")

    if os.path.exists("/etc/encore/config") == False:
        os.symlink("/opt/encore/conf.py", "/etc/encore/config")
    
    os.system("chmod +x /usr/local/bin/encrypt")
    os.system("chmod +x /usr/local/bin/encore")

    # Cheking for the encrypt script first
    exists = os.path.exists("/usr/local/bin/encrypt")

    if exists == True:
        write_log("secret sauce intact")
    else :
        print("Falling back to the unpatched encrypt script")
        sys.exit("Not Implemented")

    if os.path.exists("/opt/encore/encore") == False:
        sys.exit("Encrypt file was not downloaded or imported")


    print("Installation finished ! Running first time initialization")
    os.system("encore initialize")
    


#!https://raw.githubusercontent.com/fastsitephp/fastsitephp/master/scripts/shell/bash/encrypt.sh    

arguments = int(len(sys.argv))

if arguments == 2: 
    keyword = str(sys.argv[1])
else :
    keyword = "magic"

if keyword == "install":
    install("none")
