# ABOUT VLCVIDEO

## Install VLCVIDEO
On a brand new pi, you will have to :
- git clone the Templates repo : git clone https://github.com/IuNoWat/Templates.git
- create a video_env on Desktop : python -m venv /home/pi/Desktop/video_env
- install vlc/python bindings : /home/pi/Desktop/video_env/bin/pip install python-vlc
- IF YOU WANT TO USE THE AUDIO JACK OUTPUT : Connect something on the jack, and enable it via sudo raspi-config
- download the video on Desktop
- copy the vlcvideo you need (normal, loop or button) on Desktop and rename it to video.py
- open it and change the url of the video
- create autostart.sh : nano autostar.sh
- add the following line : /home/pi/Desktop/video_env/bin/python /home/pi/Desktop/video.py 
- copy autostart.sh on Desktop
- go to /etc/xdg/autostart : cd /etc/xdg/autostart
- create a .desktop file : sudo nano video.desktop
- add following lines :
    - #!/usr/bin/env xdg-open
    - [Desktop Entry]
    - Name=Video
    - Exec=bash /home/pi/Desktop/autostart.sh
    - Type=Application
    - Terminal=true
- reboot pi

## Close VLCVIDEO
On reboot, the video is launched. If you want the video to loop, it can be hard to stop the loop after it launched. You can stop it with a keyboard, using Ctrl+Alt+T to open a command line, and then kill it with htop. Yiu also can minimize the videoplayer using the Alt+Space shortcut.

