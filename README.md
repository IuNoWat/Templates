
# Journal Général

## 2025_07_30

I'm changing how the video players on raspi are handled. To projects will coexist :
- pyvideo will use pyvidplayer2 and pygame to add interaction
- vlcvideo will use python-vlc to add basic loop-playing video

The old files have been put in old

pyvidplayer2 is not efficient enough, even on a raspi4. For now, python-vlc prove to be the best alternative, pyvideo will not be used for now

## 2025_07_16

I was having issues with working on a Raspberry Pi with VS Code throught SSH. Sometimes, the Pi would freeze and force me to hard reboot it.
This tutorial says it's VS Code fault, installing pluggins on server side that occasionnally max the CPU capacity of low power devices, such as my Pi : https://medium.com/good-robot/use-visual-studio-code-remote-ssh-sftp-without-crashing-your-server-a1dc2ef0936d
I desactivated all the pluggin, and it work much better now.

# 2025_06_03 - Premiers Pas
Premiers test sur arduino, beaucoup plus stable et intuitifs que dans mes souvenirs.

J'ai fait un premier petit code, qui me permet de contrôler la position d'une lumière sur un ring led à partir d'un potentiomètre.

Tuto Analog : https://docs.arduino.cc/built-in-examples/basics/AnalogReadSerial/
Tuto RingLed NeoPixel : https://medium.com/@elonskolnik/arduino-uno-tutorial-neopixel-ring-setup-9fafc099c89a

# Dependencies and Tutorials

## Using Systemd

Very good explanation here : https://wiki.archlinux.org/title/Systemd/User

It seem like systemd --user shouldl be preferd in all cases.

## Using the GPIO on Raspberry

Since Bookworm, RPi.GPIO as been deprecated and we have to migrate to gpiozero :
To install it on a virtalenv, one must install :
 - pip install gpiozero
 - pip install lgpio
 - pip install rpi-lgpio

## Arduino

### FPS_example

Example of the implementation of a FPS handler on arduino. The tic() method make the arduino wait the appropriate time to achieve the aimed FPS with the delay() method.

### SCREEN_OPEN412

This examples work with this specific model of screen shield for arduino : https://www.lextronic.fr/ecran-graphique-tactile-arduino-open412-40425.html
It's based on this very good tutorial : https://ouilogique.com/2-4-in_TFT_Touch_screen/
As it says, you need to install 3 libraries in the arduino IDE (usually in "Documents/Arduino/libraries/ : 
- git clone https://github.com/adafruit/Adafruit-GFX-Library.git
- git clone https://github.com/adafruit/TFTLCD-Library.git
- git clone https://github.com/adafruit/Adafruit_TouchScreen.git

## Godot

## RaspberryPi

### SerialCom

Example of communication through serial port between a raspi and an arduino.
It uses pyserial on the py, install it with pip install pyserial

It's doesn't work at all. fck this

### Ecran LCD Rond
This example work with this specific model of lcd round screen : https://www.lextronic.fr/afficheur-lcd-rond-128--78057.html
There is in the folder a user manual that describe the installation process :
- Activate SPI interface via sudo raspi-config
- pip install Pillow
- pip install numpy
- sudo apt-get install libopenjp2-7
- wget https://www.joy-it.net/files/files/Produkte/SBC-LCD1.28R/SBCLCD128R-RPi.zip
- unzip SBC-LCD128R-RPi.zi
- Do the connexions as statted in the manual, and the example SBC-LCD128R.py should work

### Autostart on Raspberry
- Create the file autostart.sh in Desktop and enter the bash command launching your app : /home/pi/Desktop/my_env_env/bin/python /home/pi/Desktop/my_app
- Go in /etc/xdg/autostart
- Create a .desktop file : sudo nano my_app.desktop
- Enter the following lines :
#!/usr/bin/env xdg-open
[Desktop Entry]
Name=my_app 
Exec=bash /home/pi/Desktop/autostart.sh
Type=Application
Terminal=true

### WS2812

Installing everything proved to be a bit hard and confusing. I ended up using directly the rpi-ws281x library : https://pypi.org/project/rpi-ws281x/
Via : pip install rpi-ws281x

The library must be used with sudo access :(

The library also use the PWM output of the pi, disallowing the use of the audio jack. Audio can stil be sent through HDMI or Bluethoot

To do so, create a file named asound.conf in /etc/ :
cd /etc/
sudo nano asound.conf

There, you can define the default audio output :
defaults.pcm.card 2
defaults.ctl.card 2

To check the audio output of the raspberry, use the command : aplay-l

### Buzzer Passif

The passive buzzer pilot is based on pigpiod : https://abyz.me.uk/rpi/pigpio/pigpiod.html

There is also a pilot based on gpiozero, buzzer_zero.py

Remember, a buzzer can only be controlled via a PWM-friendly GPIO.
On Raspberry 4, there are two PWM channel :
- PWM0_0 available on GPIO 12, 18 or 52. (meaning GPIO12, GPIO18, etc)
- PWM0_1 available on GPIO 13, 19, 45 or 53

### pyvideo

The video player is based on pyvidplayer2 : https://github.com/anrayliu/pyvidplayer2
The test program have very low performance on raspi 3b : around 3 fps
I'm switching to python-vlc in vlcvideo

#### TO DO
- [x] Test the test program on a Raspberry Pi 4B 4G
    - This programm run at 16 fps on raspi4 4G. So i'm separating the project in two : pyvideo to use pyvidplayer2 and vlcvideo to use python-vlc. The rest is saved in old.
- [ ] Find a way to have better performances

### vlcvideo

Since pyvidplayer2 shows huge performances issues ont Raspi 3, I tried another approach, based on this video : https://www.youtube.com/watch?v=Y3SJ8qLqQA8

- vlcvideo.py allows you to play a video in fullscreen one time
- vlcvideo_loop.py allows you to play a video in fullscreen and loop on it
- a readme file explain how to use this folder

#### TO DO
- [x] Debug launching video_vlc.py through systemd
- [x] Finish vlcvideo_interact.py

