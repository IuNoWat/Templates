import sys
import random
import time

import pygame
pygame.init()

from tools import *

#CONSTANTS
FPS=30
DIR="C:/Users/lorenzo.jacques/Desktop/Templates/RaspberryPi/Pygame/framework/"
SCREEN_SIZE=(1920, 1080)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
FULLSCREEN=True

#Define DEBUG
try :
    if sys.argv[1]=="debug" :
        DEBUG=True
except IndexError :
    DEBUG=False

# STYLE
WHITE=pygame.Color("White")
BLACK=pygame.Color("Black")
GREEN=pygame.Color("Green")
RED=pygame.Color("Red")
COLOR_BG=pygame.Color(22,13,34,255)
COLOR_HL=pygame.Color(255,255,255,255)

# ENGINE

#Default
default_img = pygame.image.load(DIR+"default_img.png").convert_alpha()

#Classes
class Animation() :
    def __init__(self,update,max_frames=60) :
        self.max_frames=max_frames
        self.update=update

class Object(pygame.sprite.Sprite) :

    #How to create an animation
    def idle_loop_method(self):
        SCREEN.blit(self.image,self.pos)

    idle_loop = Animation(idle_loop_method,60)

    #Here is a list ofall the available animations
    animations_list = {
        "idle_loop":idle_loop
    }

    def __init__(self,img=default_img,pos=(0,0)) :
        pygame.sprite.Sprite.__init__(self)
        #ANIM
        self.current_frame=0
        self.animation = self.idle_loop
        self.loop=True #loop can be true, or reference an entry in self.animations_list, meaning the next animation
        #Attributes
        self.image=img
        self.pos=pos
        self.rect=(pos[0],pos[1],120,120)
    def update(self) :
        self.animation.update(self)
        self.current_frame+=1
        if self.current_frame>=self.animation.max_frames :
            if self.loop==True :
                self.current_frame=0
            else :
                self.animation = self.animations_list[self.loop]

#Preparing the mainloop

CLOCK = pygame.time.Clock()
on = True
delta_time = 0

BACKGROUND = pygame.sprite.Group()
MAIN = pygame.sprite.Group()
FX = pygame.sprite.Group()

test = Object()
test.add(MAIN)

#MAINLOOP
while on :
    #Cleaning of Screen
    SCREEN.fill(BLACK)

    #Event handling
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            on = False

        if keys[pygame.K_ESCAPE] : # ECHAP : Quitter
            on=False

    #Here go your code

    BACKGROUND.update()

    MAIN.update()

    FX.update()

    #Show DEBUG
    if DEBUG :
        #Show FPS
        fps = str(round(CLOCK.get_fps(),1))
        txt = f"DEBUG MODE | FPS : {fps} | GOOD : {GOOD} | ARDUINO : {arduino_values} | VICTORY_TIMER : {VICTORY_TIMER} | VICTORY_ANIM_TIMER : {VICTORY_ANIM_TIMER}"
        to_blit=debug_font.render(txt,1,WHITE,COLOR_BG)
        SCREEN.blit(to_blit,(0,0))

    #End of loop
    pygame.display.update()
    delta_time = CLOCK.tick(FPS) 




