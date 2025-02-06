def direction(ch1,ch2):
    vecteur=(ch2[0]-ch1[0],ch2[1]-ch1[1])
   # print(vecteur)
    if vecteur[0]==0:
        if vecteur[1]>0:
            return "à gauche"
        else: return "à droite"
    elif vecteur[1]==0:
        if vecteur[0]>0:
            return "tout droit"
        else: return "Derrière"#Cas impossible
    elif vecteur[1]>0:
        if (vecteur[0] >0 and vecteur[1]/vecteur[0]>1) or vecteur[0]<0:  
            return "à gauche"
        elif abs(vecteur[1]/vecteur[0])<2:
            return "tout droit"
    elif vecteur[1]<0:
        if vecteur[0]<0 or (vecteur[0]>0 and vecteur[1]/vecteur[0]<-1):
            return "à droite"
        elif abs(vecteur[1]/vecteur[0])<2:
            return "tout droit"
    
    #elif 
    """else:
        if vecteur[1]/vecteur[0]<0.5 and vecteur[1]/vecteur[0]>0:
            return "tout droit"
        elif vecteur[1]>0: return "à gauche"
        else: return " à droite"  """      