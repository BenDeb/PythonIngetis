#!/usr/bin/python3.6
import sys
import os

if __name__ == '__main__':

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
    try:
        limite = int(sys.argv[2])
    except (IndexError, ValueError):
        print("La limite n'a pas été précisée ou n'est pas un entier!")
        exit()

def limite_fichiers(repertoire, limite):
    #print('Nombre de fichiers : {}'.format(len([fichier for racine, reps, fichiers in os.walk(repertoire) for fichier in fichiers])))
    if limite < len([fichier for racine, reps, fichiers in os.walk(repertoire) for fichier in fichiers]):
        return -1
    return 0

