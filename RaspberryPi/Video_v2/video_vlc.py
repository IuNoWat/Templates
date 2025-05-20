import vlc

instance = vlc.Instance()
player = instance.media_player_new()

vid = vlc.Media("/home/vaisseau/Desktop/robot_nul.mp4")

player.set_media(vid)
player.play()

