# #!/usr/bin/env python
# func sample, coast creation
# seems to work only with very small ratio values, around 1.001 - 1.010
 
import math
from random import random as rnd
import pygame
from pygame.locals import *
 
def fractal(screen,x0,x1,y0,y1,sp,s):
    l = math.sqrt((x1-x0)*(x1-x0)+(y1-y0)*(y1-y0))
    if l<2 or sp>=9:
        pygame.draw.line(screen,(255,255,255),(x0,y0/3+50),(x1,y1/3+50))
        return
    r = rnd()+rnd()+rnd()-2
    x2 = (x0+x1)/2 + s*(y1-y0)*r
    y2 = (y0+y1)/2 + s*(x0+x1)*r
    sp = sp + 1
    fractal(screen,x0,x2,y0,y2,sp,s)
    fractal(screen,x2,x1,y2,y1,sp,s)
 
s=0
while s<1 or s>2:
    s = float(input("ratio 1 to 2\n"))
s = (s-1)/10 + 1
s = math.sqrt(s*s-1)
x0 = 100
x1 = 412
y0 = 0
y1 = 0
 
pygame.init()
screen =pygame.display.set_mode((500,500))
fractal(screen,x0,x1,y0,y1,1,s)
pygame.draw.line(screen, (255,255,255), (100, 50), (412, 50))
pygame.display.flip()
 
while (pygame.event.wait().type != KEYDOWN):
    pass
