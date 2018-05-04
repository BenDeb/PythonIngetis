#!/usr/bin/python3


def file_to_dict(my_file):

    with open(my_file) as f:
        montagnes = f.readlines()

    montagnes_liste = [x.split(' ;') for x in montagnes]

    sommet = {}

    for coordonnees in montagnes_liste:
        sommet[coordonnees[0]] = (coordonnees[1], coordonnees[2])

    return sommet
    






