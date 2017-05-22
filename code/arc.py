import pygame
import math
import sys
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("draw arcs")
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()

    screen.fill((0,0,200))

    #draw arc
    color=255,0,255
    width=8
    position=200,150,200,200#(position),wedth,height-->rectangle
    start_angle=math.radians(0)
    end_angle=math.radians(180)

    pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
    pygame.display.update()
