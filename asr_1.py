#!/usr/bin/python3.6
import sys
import os

# Vérification présence de l'argument répertoire
try:
    repertoire = sys.argv[1]
# Si pas d'argument (IndexError) ou argument invalide (FNFError)
except (IndexError, FileNotFoundError):
    print("Le répertoire n'existe pas ou n'est pas précisé!")
    rep_courant = input('Utiliser le répertoire courant? y/n ')
    if rep_courant.lower().startswith('y'):
        repertoire = os.getcwd()
    else:
        exit()


def changer_permissions(repertoire):
    for racine, reps, fichiers in os.walk(repertoire):
        print(racine)
        for fichier in fichiers:
            # Si le fichier finit par ".txt"
            if fichier.endswith('.txt'):
                chemin = os.path.join(racine, fichier)
                print("Changement permission sur {}".format(fichier))
                print(os.path.getsize(chemin))
                os.chmod(chemin, 0o744)


changer_permissions(repertoire)
