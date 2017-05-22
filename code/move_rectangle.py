import pygame
import random
import sys
import time
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("change color")
pos_x=0
pos_y=0
vel_x=1
vel_y=1


while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()

    screen.fill((0,0,200))

   

    #move the rectangle
   
    
    if pos_x==500 and pos_y!=400:
        pos_y+=vel_y
        if pos_x==500:
            color=random.randint(0,255),random.randint(0,255),random.randint(0,255)
        #time.sleep(2)
    elif pos_y==400 and pos_x!=0:
        pos_x-=vel_x
        if pos_y==400:
            color=random.randint(0,255),random.randint(0,255),random.randint(0,255)
        #time.sleep(2)
    elif pos_x==0 and pos_y!=0:
        pos_y-=vel_y
        if pos_x==0:
            color=random.randint(0,255),random.randint(0,255),random.randint(0,255)
        #time.sleep(2)
    elif pos_y==0 and pos_x!=500:
        pos_x+=vel_x
        if pos_y==0:
            color=random.randint(0,255),random.randint(0,255),random.randint(0,255)
        #time.sleep(2)
        
   


    #draw the rectangle
    
    width=0
    position=pos_x,pos_y,100,100
    pygame.draw.rect(screen,color,position,width)


    pygame.display.update()
    
        
