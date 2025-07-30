import vlc
import keyboard

instance = vlc.Instance('--input-repeat=-1','--mouse-hide-timeout=0')
player = instance.media_player_new()
player.toggle_fullscreen()

vid = vlc.Media("/home/vaisseau/Desktop/robot_nul.mp4")

player.set_media(vid)

keyboard.add_hotkey("Esc",lambda:exit())

while True :
    if player.get_state() == vlc.State.Ended :
        player.set_media(vid)
    player.play()



