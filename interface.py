import pygame as py
py.init()
import webbrowser

class Button:
	def __init__(self,text,width,height,pos):
		self.pressed = False

		self.top_rect = py.Rect(pos,(width,height))
		self.top_color = '#ACB1B0'
		
		self.bottom_rect = py.Rect(pos,(width,height))
		self.bottom_color = '#ACB1B0'

		self.text_surf = gui_font.render(text,True,'#E7E9E8')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def draw(self):
		py.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		py.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse_pos = py.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D3D9F9'
			if py.mouse.get_pressed()[0]:
				self.pressed = True
			else:
				if self.pressed == True:
					self.pressed = False
		else:
			self.top_color = '#ACB1B0'



class onoff(py.sprite.Sprite):
	def __init__(self, img, scale, x, y):
		super(onoff, self).__init__()

		self.image = img
		self.scale = scale
		self.image = py.transform.scale(self.image, self.scale)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.clicked = False

	def update_image(self, img):
		self.image = py.transform.scale(img, self.scale)

	def draw(self, screen):
		action = False
		pos = py.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if py.mouse.get_pressed()[0] and not self.clicked:
				action = True
				self.clicked = True


			if not py.mouse.get_pressed()[0]:
				self.clicked = False

		screen.blit(self.image, self.rect)
		return action


gui_font = py.font.Font(None,30)
width, height = 900,750
screen = py.display.set_mode((width,height))
img = py.image.load('pics/Icon.png')
py.display.set_icon(img)
py.display.set_caption('Navigateur')
map = py.image.load('pics/carte.png')
map = py.transform.scale(map,(width,height))

green=py.image.load('pics/check.png')
red=py.image.load('pics/delete.png')
here=py.image.load('pics/user.png') 

carte=py.image.load('pics/carte_oversimplified.png')
carte=py.transform.scale(carte,(width,height))

Vp_V=py.transform.scale(py.image.load('pics/Vp_Velo.png'),(width,height))
Vp_A=py.transform.scale(py.image.load('pics/Vp_Aix.png'),(width,height))
Vp_L=py.transform.scale(py.image.load('pics/Vp_Lumy.png'),(width,height))
Vp_C=py.transform.scale(py.image.load('pics/Vp_Cal.png'),(width,height))
A_Vel=py.transform.scale(py.image.load('pics/Aix_Velo.png'),(width,height))
A_lu=py.transform.scale(py.image.load('pics/Aix_lumy.png'),(width,height))
A_cal=py.transform.scale(py.image.load('pics/Aix_cal.png'),(width,height))
Vel_lu=py.transform.scale(py.image.load('pics/Vel_lumy.png'),(width,height))
Vel_Cal=py.transform.scale(py.image.load('pics/Velo_cal.png'),(width,height))
Lu_C=py.transform.scale(py.image.load('pics/lumy_cal.png'),(width,height))








run =True

Start =  Button("Naviguer",170,70,(width*0.4,450))
Tourisme =  Button("Présentation",170,70,(width*0.4,540))
Quit= Button("Quitter",170,70,(width*0.4,630))
passe=onoff(green,(24,24),200,200)
VieuxPort=onoff(red,(24,24),266,237)
Luminy=onoff(red,(24,24),647,549)
Velodrome=onoff(red,(24,24),799,355)
Aix=onoff(red,(24,24),550,54)
Calanques=onoff(red,(24,24),388,577)


draw1=draw2=draw3=draw4=draw5=passe1=passe2=passe3=passe4=passe5=False



Villes=["Vieux Port","Luminy", "Velodrome", "Aix", "Calanques"]
Coordonnées=[(266,237),(647,549),(799,355),(550,54),(388,577)]

from Graphes import *
from Dijkstra import *
from trouver_chemin import *
from Directions import *
from Chemins import *

Graphe=graphe_Dij(5)
new_arc_Dij(Graphe,0,1,30)
new_arc_Dij(Graphe,1,0,30)
new_arc_Dij(Graphe,0,2,10)
new_arc_Dij(Graphe,0,3,35)
new_arc_Dij(Graphe,1,2,15)
new_arc_Dij(Graphe,1,3,40)
new_arc_Dij(Graphe,1,4,5)
new_arc_Dij(Graphe,2,0,10)
new_arc_Dij(Graphe,2,1,15)
new_arc_Dij(Graphe,2,3,18)
new_arc_Dij(Graphe,3,0,35)
new_arc_Dij(Graphe,3,1,40)
new_arc_Dij(Graphe,3,2,18)
new_arc_Dij(Graphe,4,1,5)


















while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run =False

    screen.fill((0,0,0))
    screen.blit(map,(0,0))
    Start.draw()
    Tourisme.draw()
    Quit.draw()
    py.display.update()
    if Quit.pressed: run=False;break
    elif Start.pressed:
        screen.fill((0,0,0))
        screen.blit(carte,(0,0))
        py.display.update()
        break
    if Tourisme.pressed:
        webbrowser.open('https://www.canva.com/design/DAFRNP5lJqQ/bvfwmEH8Urk7mTQm5cRt7A/view?utm_content=DAFRNP5lJqQ&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink')
        
    
    
    
    
t=[]
while run:
    for event in py.event.get():
        if event.type==py.QUIT:
            run =False
    if Start.pressed:
        """CoordonnéesVP=py.mouse.get_pos()
        print(CoordonnéesVP)"""
        if VieuxPort.draw(screen):
            draw1=not draw1
            if draw1:
                VieuxPort.update_image(here)
                passe1=True
            else:
                VieuxPort.update_image(red)
        elif Luminy.draw(screen):
            draw2=not draw2
            if draw2:
                Luminy.update_image(here)
                passe2=True
            else:
                Luminy.update_image(red)   
        elif Velodrome.draw(screen):
            draw3=not draw3
            if draw3: 
                Velodrome.update_image(here)
                passe3=True
            else: 
                Velodrome.update_image(red)
        elif Aix.draw(screen):
            draw4=not draw4
            if draw4:
                Aix.update_image(here)
                passe4=True
            else: 
                Aix.update_image(red)
        elif Calanques.draw(screen):
            draw5=not draw5
            if draw5:
                Calanques.update_image(here)
                passe5=True
            else: 
                Calanques.update_image(red)
        py.display.update()
                
        
        
        #if not (passe1 or passe2 or passe3 or passe4 or passe5):screen.blit(carte,(0,0))
        if passe1:
            t.append((266,237))
            passe1=False
        elif passe2:
            t.append((647,549))
            passe2=False
        elif passe3:
            t.append((799,355))
            passe3=False
        elif passe4:
            t.append((550,54))
            passe4=False
        elif passe5:
            t.append((388,577))
            passe5=False
        #if len(t)==2:print(t)
        if len(t)==2:
            src=dest=""
            for i in range(len(Graphe)):
                if Coordonnées[i]==t[0]:
                    src=Villes[i]
                    srcindex=i
                elif Coordonnées[i]==t[1]:
                    dest=Villes[i]
                    destindex=i 
                elif src!="" and dest!="":
                    print(f"Vous voulez aller de {src} à {dest}")
                    
                    H=Dijkstra_Aux(Graphe,srcindex)
                    Path=trouver_chemin(H,srcindex,destindex)
                    print(Path)
                    
                    if Path[0]==0:
                        if Path[len(Path)-1]==1:
                            screen.blit(Vp_L,(0,0))
                        elif Path[len(Path)-1]==2:
                            screen.blit(Vp_V,(0,0))
                        elif Path[len(Path)-1]==3:
                            screen.blit(Vp_A,(0,0))
                        elif Path[len(Path)-1]==4:
                            screen.blit(Vp_C,(0,0))
                    if Path[0]==1:
                        if Path[len(Path)-1]==0:
                            screen.blit(Vp_L,(0,0))
                        elif Path[len(Path)-1]==2:
                            screen.blit(Vel_lu,(0,0))
                        elif Path[len(Path)-1]==3:
                            screen.blit(A_lu,(0,0))
                        elif Path[len(Path)-1]==4:
                            screen.blit(Lu_C,(0,0))
                    if Path[0]==2:
                        if Path[len(Path)-1]==1:
                            screen.blit(Vel_lu,(0,0))
                        elif Path[len(Path)-1]==0:
                            screen.blit(Vp_V,(0,0))
                        elif Path[len(Path)-1]==3:
                            screen.blit(A_Vel,(0,0))
                        elif Path[len(Path)-1]==4:
                            screen.blit(Vel_Cal,(0,0))
                    if Path[0]==3:
                        if Path[len(Path)-1]==1:
                            screen.blit(A_lu,(0,0))
                        elif Path[len(Path)-1]==2:
                            screen.blit(A_Vel,(0,0))
                        elif Path[len(Path)-1]==0:
                            screen.blit(Vp_A,(0,0))
                        elif Path[len(Path)-1]==4:
                            screen.blit(A_cal,(0,0))
                    if Path[0]==4:
                        if Path[len(Path)-1]==1:
                            screen.blit(Lu_C,(0,0))
                        elif Path[len(Path)-1]==2:
                            screen.blit(Vel_Cal,(0,0))
                        elif Path[len(Path)-1]==3:
                            screen.blit(A_cal,(0,0))
                        elif Path[len(Path)-1]==0:
                            screen.blit(Vp_C,(0,0))
                    
                    for j in range(1,len(Path)):
                        print(f"Allez {direction(Coordonnées[Path[j-1]],Coordonnées[Path[j]])} de {Villes[Path[j-1]]} vers {Villes[Path[j]]}")
                    Path=[]                
            t=[]

            
            
            
                
        

        
        
