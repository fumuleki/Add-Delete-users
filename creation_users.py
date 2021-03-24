#!/usr/bin/python3

import os 
import subprocess
import sys
import getpass

def add_user():
    username = input("Enter Username : ")
    passwd = getpass.getpass()

    try:
        subprocess.run(['useradd', '-p', password, username ])
    except subprocess.error:
        return False
        sys.exit(1)

add_user()
