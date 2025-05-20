#!/usr/bin/python
#coding: utf-8

import time

import pygame
pygame.mixer.init(48000, -16, 1, 4096)
pygame.font.init()
from pyvidplayer2 import Video

class Player() :
    def __init__(self,fps=30,tactile=False) :
        #Pygame core
        self.on=True
        self.Screen=False
        self.Clock=pygame.time.Clock()

        #core
        self.fps=fps
        self.playing=False
        self.video_path=""
        self.video=False
        self.show_debug=True
        self.tactile=tactile

        #Style
        self.bg_color=pygame.Color("Black")
        self.debug_font=pygame.font.Font(size=40)

    def start(self) :
        while self.on :
            #CLEANUP
            #self.Screen.fill(self.bg_color)
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
            if self.video.draw(self.Screen,(0,0),force_draw=False) :
                #DEBUG
                if self.show_debug :
                    text_debug = self.debug_font.render(f"FPS : {int(self.Clock.get_fps())}", False, (0,0,0))
                    self.Screen.blit(text_debug,(0,0))
                pygame.display.update()

            #END OF LOOP
            #pygame.display.flip()
            self.Clock.tick(self.fps)            
    def load_video(self,path) :
        self.video_path=path
        self.video=Video(path)
        self.Screen=pygame.display.set_mode(self.video.current_size)
        pygame.display.set_caption(self.video.name)
        



if __name__=="__main__" :

    default_vid_path="/home/vaisseau/Desktop/robot_nul.mp4"

    player=Player()

    player.load_video(default_vid_path)
                       
    player.start()

