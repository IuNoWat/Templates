import vlc
import keyboard
import os
import pigpio

#CONSTANTS
os.system("sudo pigpiod") #pigpoid needs to be launched
PIN=18
PI=pigpio.pi()

#INIT
PI.set_mode(PIN,pigpio.INPUT)

instance = vlc.Instance('--input-repeat=-1','--mouse-hide-timeout=0')
player = instance.media_player_new()
player.toggle_fullscreen()

vid_1 = vlc.Media("/home/pi/Desktop/robot_nul.mp4")
vid_2 = vlc.Media("/home/pi/Desktop/robot_nul_nb.mp4")

current_vid=0

player.set_media(vid_1)

playing=True

def stop() :
    global playing
    playing=False
    player.stop()

def toggle_vid(args,args1,args2) :
    print("COUCOU")
    global current_vid
    if current_vid==0 :
        current_vid=1
        player.set_media(vid_2)
        player.play()
    else :
        current_vid=0
        player.set_media(vid_1)
        player.play()


keyboard.add_hotkey("Esc",lambda:stop())

keyboard.add_hotkey("enter",lambda:toggle_vid())
PI.callback(PIN,pigpio.RISING_EDGE,toggle_vid)

while playing :
    if player.get_state() == vlc.State.Ended and playing :
        player.set_media(vid)
    
    player.play()
