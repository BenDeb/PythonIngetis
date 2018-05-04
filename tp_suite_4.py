#!/usr/bin/python3

import sys
import os

# Usage : ./tp_suite_4.py 'fichier.ext' 'repertoire'

# A faire :
# - ajouter possibilité de créer de plusieurs fichiers en même temps
# - améliorer gestion des erreurs
# - mieux gérer les fichiers avec des noms contenant plusieurs '.'

fichier_a_creer = sys.argv[1]
repertoire = sys.argv[2]

def decoupage_fichier(fichier_a_creer):
    # Fonction qui découpe simplement le fichier en deux : le nom et l'extension
    # Si pas d'extension, on quitte le script
    if '.' not in fichier_a_creer:
        raise Exception("Le fichier n'a pas d'extension!")

    nom_fichier = fichier_a_creer.split('.')[0]
    extension_fichier = fichier_a_creer.rsplit('.', 1)[-1]
    return nom_fichier, extension_fichier
        
nom_fichier, extension = decoupage_fichier(fichier_a_creer)


#On créé une liste de tous les fichiers dans le répertoire spécifié
#On prend soin de remplacer '-v' par un '.' pour pouvoir ensuite splitter plus facilement
#Cela nous permet de bien isoler le nom du fichier, la version et l'extension
fichiers_decoupes = [fichier.replace('-v', '.').split('.') for fichier in os.listdir(repertoire)]


def get_last_file(nom_fichier, extension, fichiers_decoupes):

    # On met la liste des fichiers du répertoires dans 'fichiers'
    fichiers = os.listdir(repertoire)
    # On set la version par défaut à 001
    default_version = '001'
    # Le fichier par défaut aura le nom, v001 et l'extension
    default_fichier = '{0}-v{1}.{2}'.format(nom_fichier, default_version, extension)
    # Si on ne trouve pas le fichier par défaut dans les fichiers, cela signifie qu'il n'existe pas
    # On retourne donc default_fichier pour qu'il soit créé plus tard
    if default_fichier not in fichiers:
        return default_fichier
    
    # Si le fichier existe, on créé une liste vide qui va contenir une liste des versions du fichier
    versions = []
    # On utilise fichiers_decoupes pour isoler la version
    for fichier in fichiers_decoupes:
        # Si le nom du fichier et l'extension correspondent, on regarde la version et on la place dans la liste versions
        if nom_fichier == fichier[0] and extension == fichier[-1]:
            version = int(fichier[1])
            versions.append(version)
    # On regarde la version maximum dans la liste grâce à max
    # La nouvelle version sera la version maximale + 1      
    nouvelle_version = str(max(versions)+1).zfill(3)
    
    # On créé nouveau_fichier
    nouveau_fichier = '{0}-v{1}.{2}'.format(nom_fichier, nouvelle_version, extension)
    return nouveau_fichier




#Création du nouveau fichier : on part sur un fichier vide (d'où le pass)
nouveau_fichier = get_last_file(nom_fichier, extension, fichiers_decoupes)
with open(nouveau_fichier, "w"): pass
        
          
        


