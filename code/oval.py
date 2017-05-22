import pygame
import math
import sys
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("drawing oval")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()

    screen.fill((0,0,200))
    #draw the oval
    color=255,0,255
    position=100,150,400,100
    
    width=8
    start_angle1=math.radians(0)
    end_angle1=math.radians(180)
    start_angle2=math.radians(180)
    end_angle2=math.radians(360)
    pygame.draw.arc(screen,color,position,start_angle1,end_angle1,width)
    pygame.draw.arc(screen,color,position,start_angle2,end_angle2,width)

    pygame.display.update()
    
