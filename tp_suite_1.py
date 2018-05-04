import sys
import numpy as np
from math import sqrt

nombres = [int(nb) for nb in sys.argv[1:]]

def calcul_ecart_type(nombres):
    var = []
    avg = np.average(nombres)
    for i in nombres:
        var.append((i-avg)**2)
    somme_var = sum(var)
    return sqrt(somme_var/len(nombres))


def calcul_ecart_type_np(nombres):
    return np.std(nombres)
    
print(calcul_ecart_type(nombres))

print(calcul_ecart_type_np(nombres))


exit()





def calcul_moyenne_np(nombres):
    return np.average(nombres)

def calcul_moyenne_manuel(nombres):
    len_nombres = len(nombres)
    somme = 0
    for i in nombres:
        somme += i
    return somme/len_nombres

def calcul_mediane_np(nombres):
    return np.median(nombres)





print(calcul_moyenne_np(nombres))
print(calcul_mediane_np(nombres))
print(calcul_ecart_type_np(nombres))

