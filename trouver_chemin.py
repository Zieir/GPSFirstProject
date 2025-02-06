import math
from Dijkstra import *

def trouver_chemin(G,src,dest):
    x=dest
    t=[x]
    while x!= src:
        for i in range(len(G)):
            if existe_arc_Dij(G,i,x):
                x=i
                t.append(x)
                break
    return t[::-1]

#print(trouver_chemin(Graphe,0,4))