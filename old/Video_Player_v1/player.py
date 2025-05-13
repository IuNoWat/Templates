#!/usr/bin/python
#coding: utf-8

import time

from threading import Thread
import pygame
pygame.mixer.init(48000, -16, 1, 4096)
pygame.font.init()
from pyvidplayer import Video

class Player() :
    def __init__(self,screen_size=(1920,1080),bg_color=pygame.Color("Black"),fps=30) :
        #Pygame core
        self.on=True
        self.screen_size=screen_size
        self.Screen=pygame.display.set_mode(self.screen_size)
        self.Clock=pygame.time.Clock()

        #core
        self.fps=fps
        self.playing=False
        self.video_path=""
        self.video=False
        self.show_debug=True

        #Style
        self.bg_color=bg_color
        self.debug_font=pygame.font.Font(size=40)

    def start(self) :
        self.playing=True
        while self.on :
            #CLEANUP
            self.Screen.fill(self.bg_color)
            #do the ting

            #EVENT HANDLING
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()

                #Commands always on
                if event.type == pygame.QUIT:
                    self.on=False
                if keys[pygame.K_p] :
                    self.on=False
                if keys[pygame.K_w] :
                    self.show_debug = True
                if keys[pygame.K_x] :
                    self.show_debug = False

            #UPDATE OF VIDEO
            if self.playing :
                if self.video!=False :
                    self.video.draw(self.Screen,(0,0))
                    print(self.video.active)

            #DEBUG
            if self.show_debug :
                text_debug = self.debug_font.render(f"FPS : {int(self.Clock.get_fps())}", False, (0,0,0))
                self.Screen.blit(text_debug,(0,0))

            #END OF LOOP
            pygame.display.flip()
            self.Clock.tick(self.fps)            
    def load_video(self,path) :
        self.video_path=path
        self.video=Video(path)
        self.video.set_size(self.screen_size)



if __name__=="__main__" :

    default_vid_path="/home/pi/Desktop/robot_nul.mp4"

    player=Player()

    player.load_video(default_vid_path)
                       
    player.start()
