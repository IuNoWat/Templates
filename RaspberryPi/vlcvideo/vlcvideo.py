import vlc

instance = vlc.Instance('--input-repeat=-1','--mouse-hide-timeout=0')
player = instance.media_player_new()
player.toggle_fullscreen()

vid = vlc.Media("/home/pi/Desktop/robot_nul.mp4")

player.set_media(vid)

playing=True

while playing :
    player.play()
    if player.get_state() == vlc.State.Ended :
        exit()


