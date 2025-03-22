# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:52:42 2022

@author: pc
"""

from file import *
from graphe import * 
from Djikstra import *
"""
on veut essayer d'implementer un graph tels que ce graph a pour noeud/ sommet des villes 
"""
# pourquoi on laisse tous comme il était et juste on cree un tableau de ville 
dic={}
##dic["A"]=(9,6)
##dic["B"]=(990,7)
def direction(ch1,ch2):
    vecteur=(ch2[0]-ch1[0],ch2[1]-ch1[1])
    print(vecteur)
    if vecteur[0]==0:
        if vecteur[1]>0:
            return "gauche"
        else: return "droite"
    elif vecteur[1]==0:
        if vecteur[0]>0:
            return "Tout droit"
        else: return "gauche"
    else:
        if abs(vecteur[1]/vecteur[0])<2:
            return "tout droit"
        elif vecteur[1]>0: return "gauche"
        else: return "droite"        
       
print(direction(dic["A"],dic["B"]))


villes=['vieux-port','castellane','joliette','prado','stade']
def indice_ville(laville,villes):
    n=len(villes)
    for i in range(n):
        if villes[i].upper()==laville.upper():
            return i
    return -1 

def nom_ville(indice,villes):
    n=len(villes)
    return(villes[indice])
print('\n\n')       
print(indice_ville('Prado',villes))   
print(nom_ville(1,villes))


def calculer_chemin(P, s, t):
    Djikstra(P, s)
    n = len(P)
    v = t
    x=0
    print(v)
    while v != s:
       for u in range(n):
          if P[u][v] == 1: # il y a un arc en arri`ere
              x = u # faire un pas en arri`ere
              print(u)
              break
          v=x

G=nouveau_graph(5)
ajouter_arc(G, 0, 1,1)
ajouter_arc(G, 0, 4,2)
ajouter_arc(G, 0, 2,3)
ajouter_arc(G, 1, 4,9)
ajouter_arc(G, 2, 4,5)
ajouter_arc(G, 2, 3,1)
ajouter_arc(G, 4, 3,2)
print(G)
print('CHEMIN :  --->\n')
#c=[]
#calculer_chemin_bon_sens(G, 0, 3,c)
print('LE CHEMIN POUR ALLER AU PRADO A PARTIR DU VIEUX PORT :--->')
c=[]
calculer_chemin_bon_sens(G, 0, 3,c)
print('VIEUX-PORT-->')
print(c)
for i in range(len(c)):
    print(nom_ville(c[i],villes))
