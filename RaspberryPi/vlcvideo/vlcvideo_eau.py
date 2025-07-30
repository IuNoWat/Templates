import vlc
#import keyboard
import os
import gpiozero

btn=gpiozero.Button("BOARD12")

instance = vlc.Instance('--input-repeat=-1','--mouse-hide-timeout=0')
player = instance.media_player_new()
player.toggle_fullscreen()

vid_1 = vlc.Media("/home/pi/Desktop/robot_nul.mp4")
vid_2 = vlc.Media("/home/pi/Desktop/robot_nul.mp4")

current_vid=0

player.set_media(vid_1)

playing=True

def stop() :
    global playing
    playing=False
    player.stop()

def toggle_vid(arg) :
    print(arg)
    global current_vid
    if current_vid==0 :
        current_vid=1
        player.set_media(vid_2)
        player.play()
    else :
        current_vid=0
        player.set_media(vid_1)
        player.play()


#keyboard.add_hotkey("Esc",lambda:stop())
#
#keyboard.add_hotkey("enter",lambda:toggle_vid())
btn.when_pressed=toggle_vid

while playing :
    if player.get_state() == vlc.State.Ended and playing :
        player.set_media(vid)
    
    #player.play()
