import sys
import random
import time

import pygame

#from tools import *

#CONSTANTS
FPS=30
DIR="/home/pi/Desktop/"
SCREEN_SIZE=(1600, 900)
FULLSCREEN=True
#Define DEBUG
try :
    if sys.argv[1]=="debug" :
        DEBUG=True
except IndexError :
    DEBUG=False

#Animation CONSTANTS

#STYLE
WHITE=pygame.Color("White")
BLACK=pygame.Color("Black")
GREEN=pygame.Color("Green")
RED=pygame.Color("Red")
COLOR_BG=pygame.Color(0,0,0,255)
COLOR_HL=pygame.Color(255,255,255,255)
pygame.font.init()
debug_font=pygame.font.Font('freesansbold.ttf',16)

#ASSETS LOAD

#ENGINE

class Anim() : #Use this class as base for animations, see below with the Pop example
    def __init__(self,max_frame) :
        self.max_frame=max_frame
        self.current_frame=0
        self.method=print
        self.finished=False
    def anim(self) :
        self.method(self.current_frame)
        self.current_frame=self.current_frame+1
        if self.current_frame==self.max_frame :
            self.finished=True

class Pop(Anim) : # The Pop anim will play the moove method each frame until the max frame is reached
    def moove(self,current_frame) :
        self.img.set_alpha(255-current_frame*16)
        center_blit(SCREEN,self.img,(self.pos[0],self.pos[1]-current_frame*3))
    def __init__(self,max_frame,img,pos) :
        Anim.__init__(self,max_frame)
        self.img=img
        self.pos=pos
        self.method=self.moove
    def anim(self) :
        print(self.current_frame)
        Anim.anim(self)

#SPECIFIC ENGINE

#MAINLOOP PREPARATION
ANIMATIONS=[]

#MAINLOOP

on=True
SCREEN = pygame.display.set_mode(SCREEN_SIZE,pygame.FULLSCREEN)
CLOCK = pygame.time.Clock()

while on :
    #Cleaning of Screen
    SCREEN.fill(COLOR_BG)

    #Event handling
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            on = False
        if keys[pygame.K_ESCAPE] : # ECHAP : Quitter
            on=False

    #Animation handling
    for i,animation in enumerate(ANIMATIONS) :
        animation.anim()
        if animation.finished :
            ANIMATIONS.pop(i)

    #Show DEBUG
    if DEBUG :
        fps = str(round(CLOCK.get_fps(),1))
        txt = "DEBUG MODE | FPS : "+fps
        to_blit=debug_font.render(txt,1,WHITE,COLOR_BG)
        SCREEN.blit(to_blit,(0,0))

    #End of loop
    pygame.display.update()
    CLOCK.tick(FPS) 