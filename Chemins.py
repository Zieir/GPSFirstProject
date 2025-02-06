import pygame as py
from interface import height, width

def chemin(t):
    if t[0]==0 and t[len(t)]==2:
        return py.transform.scale(py.image.load('Vp_Velo.png'),(width,height))