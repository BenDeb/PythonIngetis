#!/usr/bin/python3

infos = {}
while 1:
    name = input('Votre nom?\n')
    age = input('Votre age?\n')
    taille = input('Votre taille en cm?\n')
    infos[name] = (age, taille)
    quitter = input('quitter? y/n \n')
    if quitter[0].lower() == 'y':
        break
 
def consultation(name_in_dic):
    return '{0} : {1}'.format(name_in_dic, infos.get(name_in_dic))

print(consultation('ben'))

    