from Files import *
import math

def defiler_Dij(F):
    F.sort()
    return F.pop(0)

def graphe_Dij(n):
    return [[math.inf]*n for i in range(n)]
def taille_graphe_Dij(G):
    return(len(G))
def new_arc_Dij(G,i,j,dist):
    G[i][j]=dist
def existe_arc_Dij(G,i,j):
    return G[i][j]<math.inf
def afficher_graphe_Dij(G):
    print(G)
   
def Dijkstra(G,src):
    dist =[math.inf]*len(G)
    dist[src]=0
    pre= [None]*len(G)
    F=nouvelle_file()
    F=enfiler(F,src)
    while not file_vide(F):
        u=defiler_Dij(F) 
        for j in range(len(G)):
            if G[u][j]<math.inf and dist[j]>dist[u]+G[u][j] :
                pre[j]= u
                dist[j]= dist[u]+G[u][j]
                F=enfiler(F,j)
    return (pre,dist)

def Dijkstra_Aux(G,src):
    t=Dijkstra(G,src)
    H=graphe_Dij(len(G)+1)
    for i in range(len(G)):
        if t[0][i]!=None:
            new_arc_Dij(H,t[0][i],i,t[1][i])
    H[src][src]=0
    return H


            
            

    """H=graphe_Dij(len(G))
    H[src][src]=0
    for i in range(len(pre)):
        if i!=src:
            H[i][pre[i]]=dist[i]
    return H"""
"""                
Graphe=graphe_Dij(5)
Graphe[0][2]=10
Graphe[0][3]=35
Graphe[1][2]=15
Graphe[1][3]=20
Graphe[1][4]=22
Graphe[2][0]=10
Graphe[2][1]=15
Graphe[2][3]=18
Graphe[3][0]=35
Graphe[3][1]=20
Graphe[3][2]=18
Graphe[4][1]=22

print(Dijkstra_Aux(Graphe,0))"""