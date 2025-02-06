"""
*********************************************************************
                  MACHINE ABSTRAITE GRAPHES 
*********************************************************************
"""
#---------------------------------------------------------------
def nouveau_graph(n):
    matrice=[[0]*n for i in range(n)]
    return matrice        
     
#---------------------------------------------------------------           
def taille_graphe(G):
    return len(G)
   
#---------------------------------------------------------------
def ajouter_arc(G,i,j,valeur):
    if len(G)!=0 :
        G[i][j]=valeur
    else: return ('GRAPHE VIDE !')   

#---------------------------------------------------------------
def existe_arc(G,i,j):
    if len(G)==0:
        return(False)
    else:
        if G[i][j]!=0 :return True
        else: return(False)

#---------------------------------------------------------------
def afficher_graphe(G):
    print(G)

#---------------------------------------------------------------
         
         
from Files import *    
         
def nouv_graphe(n):
    return [[0]*n for i in range(n)]
def taille_graphe(G):
    return len(G)
def ajouter_arc(G,i,j):
    G[i][j]=1
def existe_arc(G,i,j):
    return G[i][j]==1
def afficher_graphe(G):
    print(G)
   


def parcours_largeur(G, s):
    f = nouvelle_file()
    enfiler(f, s)
    t = [s]
    while not file_vide(f):
        x = defiler(f)
        for i in range(len(G)):
            if G[x][i] == 1 and i not in t:
                enfiler(f, i)
                t.append(i)
    return(t)

