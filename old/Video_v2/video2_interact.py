import vlc

import pygame
pygame.font.init()
flags = pygame.FULLSCREEN | pygame.NOFRAME | pygame.SRCALPHA
Screen=pygame.display.set_mode((1920,1080),flags)
Clock=pygame.time.Clock()
debug_font=pygame.font.Font(size=40)
instance = vlc.Instance()
player = instance.media_player_new()
#player.toggle_fullscreen()

vid = vlc.Media("/home/vaisseau/Desktop/robot_nul.mp4")

player.set_media(vid)
Screen.fill((0,0,0,0))
fond=pygame.Surface((100,100),pygame.SRCALPHA)
fond.fill((0,0,0,0))
while True :
    

    Screen.blit(fond,(0,0))
    text_debug = debug_font.render(f"FPS : {int(Clock.get_fps())}", False, (255,255,255,255))
    Screen.blit(text_debug,(0,0))
    pygame.display.flip()
    Clock.tick(30)

    player.play()



