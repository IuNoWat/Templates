
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

## Arduino

## Godot

## RaspberryPi

### Buzzer Passif

The passive buzzer pilot is based on pigpiod : https://abyz.me.uk/rpi/pigpio/pigpiod.html

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

