import pygame
import random
#import time
import sys
from pygame.locals import *
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("random line")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()

    screen.fill((0,0,200))
    color=random.randint(0,255),random.randint(0,255),random.randint(0,255)
    width=1
    for i in range(0,1000):
        #time.sleep(1)
        pygame.draw.line(screen,color,(random.randint(0,600),random.randint(0,500)),(random.randint(0,600),random.randint(0,500)),width)
        i=i-1
        

    pygame.display.update()
