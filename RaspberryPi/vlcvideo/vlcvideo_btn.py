import vlc
import gpiozero

btn=gpiozero.Button("BOARD12")

instance = vlc.Instance('--input-repeat=-1','--mouse-hide-timeout=0')
player = instance.media_player_new()
#player.toggle_fullscreen()

vids = [
    vlc.Media("/home/pi/Desktop/robot_nul.mp4"),
    vlc.Media("/home/pi/Desktop/robot_nul_nb.mp4")
    #Add here more video if you want
]


def toggle_vid(arg) :
    print(arg)
    global current_vid
    current_vid+=1
    if current_vid==len(vids) :
        current_vid=0
    player.set_media(vids[current_vid])
    player.play()


btn.when_pressed=toggle_vid

current_vid=0
player.set_media(vids[current_vid])
player.play()

playing=True

while playing :

    if player.get_state() == vlc.State.Ended and playing :
        player.set_media(vids[current_vid])
        player.play()

    
    
