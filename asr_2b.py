#!/usr/bin/python3

import sys
from asr_2a import limite_fichiers as lim

try:
    limite = int(sys.argv[1])
except (IndexError, ValueError):
    print("La limite n'a pas été précisée ou n'est pas un entier!")
    exit()

def check_homes(limite):
    """ Fonction qui détermine si le home d'un utilisateur contient plus de fichiers que la limite 
    définie 
    -1 si + de fichiers que la limite
    0 si - de fichiers"""

    with open('/etc/passwd') as data:
        # On crée un dictionnaire qui contient comme clé le username et en valeur le répertoire /home
        # La compréhension de liste sert juste à split chaque ligne du /etc/passwd avec le caractère ':'
        # On définit les uids à vérifier(entre 1000 et 1010 inclus)
        utilisateur = {l[0]:l[-2].strip() for l in [i.split(':') for i in data] if int(l[2]) >= 1000 and int(l[2]) <= 1010}

    # On créé le dictionnaire que l'on va retourner : clé -> username; valeur -> -1 ou 0 (selon que la limite ait été dépassée ou pas)
    home_checks = {user:lim(user_home, limite) for user, user_home in utilisateur.items()}

    return home_checks



print(check_homes(limite))
                                


