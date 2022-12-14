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
            sys.exit("I Don't support the distro that you use. If you do run this command with --force")
        else :
            warning_msg = f"This tool wasn't build for the distro that your running. Shit might be weird. Good luck"
            warnings.warn(warning_msg, Warning)

    print("Downloading additional dependencies")

    command = "mkdir -pv /tmp/encore/pkgs"
    os.system(command)
    
    #  for downloads use the unix curl with os.system
    
    # file settings
    mode  = 400

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
            home = f"/usr/local/bin{files}"
            copy_file(src, dst)

    os.symlink("/opt/encore/encrypt", "/usr/local/bin/encrypt")
    os.symlink("/opt/encore/encore", "/usr/local/bin/encore")
    os.system("chmod +x /usr/local/bin/*")

    # Cheking for the encrypt script first
    exists = os.path.exists("/usr/local/bin/encrypt")

    if exists == True:
        write_log("secret sauce intact")
    else :
        print("Falling back to the unpatched encrypt script")
        sys.exit("Not Implemented")

    if os.path.exists("/opt/encore/encore") == False:
        sys.exit("Encrypt file was not downloaded or imported")

    os.system("encore initialize")
    

    #Done checking and installing dependencies from pkg anagers
    # installing pip stuff 
        



#!https://raw.githubusercontent.com/fastsitephp/fastsitephp/master/scripts/shell/bash/encrypt.sh    

arguments = int(len(sys.argv))

if arguments == 2: 
    keyword = str(sys.argv[1])
else :
    keyword = "magic"

if keyword == "install":
    install("none")
