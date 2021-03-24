# Add-Delete-users
Il s'agit d'un script qui va automatiser des taches de créations utilisateurs.
Parceque créer un utilisateur via la ligne de commande sous Linux est une tâche fastidieuse. Chaque fois que quelqu'un rejoint votre organisation et que vous devez taper une longue commande Linux plutôt que de le faire, vous pouvez créer un script python qui peut vous demander le nom d'utilisateur et le mot de passe et créer cet utilisateur pour vous.

# Exemples:

 - Input : 
 - Enter Username : Cedrick
 - Password: ****

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
       
       
       
Supprimer un utilisateur de votre système ou serveur via un script python est une tâche très simple. Il vous suffit de passer le nom d'utilisateur de l'utilisateur et le script supprimera les détails et tous les fichiers de cet utilisateur.Ce script python utilise la commande userdel Linux pour supprimer l'utilisateur.Vous pouvez directement utiliser la commande userdel si vous vous souvenez de la commande mais si vous ne le faites pas alors le script facilite la suppression de l'utilisateur.

Input:
     - Enter Username: Cedra

Output:
     - User successfully deleted 

Avant d'exécuter le script, nous montrerons l'utilisateur que nous voulons supprimer.
grace la commande cat / etc / paswd listera tous les utilisateurs de votre système ou serveur. Cedra est l'utilisateur que nous allons supprimer

Le code Python ci-dessous est le script que nous utiliserons pour notre objectif.

#!/usr/bin/python3

- import os
- import subprocess
- import sys
- import getpass

 - def delete_user():
 
    - username = input("Enter Username : ")

   - try:
    
       -output = subprocess.run(['userdel', username])
       
         -  if output.returncode == 0:
          
            - print("User successfully deleted with given credentials")

    - except subprocess.error:
    
       -return False
       
   - sys.exit(1)

delete_user()

# python3 delete_users.py

Après avoir exécuté le script, il vous demandera le nom d'utilisateur que nous voulons supprimer et après avoir entré le nom, le même utilisateur sera supprimé du système.
Après, si nous vérifions en tapant cat / etc / passwd, nous pouvons voir que l'utilisateur «Cedra» n'est plus sur cette liste. Nous avons donc supprimé avec succès notre utilisateur.
