#!/usr/bin/python3

import os
import subprocess
import sys
import getpass

def delete_user():
    username = input("Enter Username : ")

    try:
        output = subprocess.run(['userdel', username])
        if output.returncode == 0:
            print("User successfully deleted with given credentials")

    except subprocess.error:
        return False
    sys.exit(1)

delete_user()
