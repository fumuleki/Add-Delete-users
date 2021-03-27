# Creation-User

Il s'agit d'un script qui permet d'automatiser certaines taches sur la création des utilisateurs dans un serveur ou système.
Parceque créer un utilisateur via la ligne de commande sous Linux est une tâche fastidieuse. Chaque fois que quelqu'un rejoint votre entreprise et que vous devez taper une longue commande Linux plutôt que de le faire, vous pouvez créer un script python qui peut automatiser la tache, il vous demande d'entrée le nom d'utilisateur et le mot de passe et créer cet utilisateur pour vous.

# Exemples:

 - Input : 
 - Enter Username : Cedrick
 - Password: ****
 - confirm password: ****

# Ci-dessous le code Python

#!/usr/bin/python3
# importation de la bibliothèque

  - import os
  - import subprocess
  - import sys
  - import getpass
  
# ajouter une fonction utilisateur
    - def add_user():

# Demandez l'entrée
    - username = input("Enter Username : ")
    - passwd = getpass.getpass()
    - confirm_password = getpass.getpass(prompt="To confirm, re-enter password: ")
# exécution de la commande useradd à l'aide du module
    try:
        subprocess.run(['useradd', '-p', password, username ])
    except subprocess.error:
        return False
        sys.exit(1)

add_user()

# python3 add_users.py

Après avoir créé avec succès les utilisateurs, utilisez cette commande pour obtenir les détails de nouvelles utilisateurs

       - cat /etc/passwd
       
       
       
