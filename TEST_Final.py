from Dijkstra import *

Graphe=graphe_Dij(5)
new_arc_Dij(Graphe,0,2,10)
new_arc_Dij(Graphe,0,3,35)
new_arc_Dij(Graphe,1,2,15)
new_arc_Dij(Graphe,1,3,20)
new_arc_Dij(Graphe,1,4,22)
new_arc_Dij(Graphe,2,0,10)
new_arc_Dij(Graphe,2,1,15)
new_arc_Dij(Graphe,2,3,18)
new_arc_Dij(Graphe,3,0,35)
new_arc_Dij(Graphe,3,1,20)
new_arc_Dij(Graphe,3,2,18)
new_arc_Dij(Graphe,4,1,22)

from interface import *

Villes=["Vieux Port","Luminy", "Velodrome", "Aix", "Calanques"]
Coordonnées=[(266,237),(647,549),(799,355),(550,54),(388,577)]
src=dest=""

for i in range(len(Graphe)):
    if Coordonnées[i]==t[0]:
        src=Villes[i]
    elif Coordonnées[i]==t[1]:
        dest=Villes[i]  
    elif src!="" and dest!="":
        break
    
print(src)
print(dest)
    
#H=Dijkstra(Graphe,t[])
