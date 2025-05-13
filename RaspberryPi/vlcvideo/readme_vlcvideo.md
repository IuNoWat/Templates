# How to use vlcvideo

On a brand new pi, you will have to :
- git clone the Templates repo : git clone https://github.com/IuNoWat/Templates.git
- create a video_env on Desktop : python -m venv /home/pi/Desktop/video_env
- install vlc/python bindings : /home/pi/Desktop/video_env/pip install python-vlc
- download the video on Desktop
- copy vlcvideo_loop.py on Desktop and rename it video.py
- open it and change the name of the video
- copy autostart.sh on Desktop
- go to /etc/xdg/autostart : cd /etc/xdg/autostart
- create a .desktop file : sudo nano video.desktop
- add following lines :
#!/usr/bin/env xdg-open
[Desktop Entry]
Name=Video
Exec=bash /home/pi/Desktop/autostart.sh
Type=Application
Terminal=true
- reboot pi


