
# Journal Général

# 2025_06_03 - Premiers Pas
Premiers test sur arduino, beaucoup plus stable et intuitifs que dans mes souvenirs.

J'ai fait un premier petit code, qui me permet de contrôler la position d'une lumière sur un ring led à partir d'un potentiomètre.

Tuto Analog : https://docs.arduino.cc/built-in-examples/basics/AnalogReadSerial/
Tuto RingLed NeoPixel : https://medium.com/@elonskolnik/arduino-uno-tutorial-neopixel-ring-setup-9fafc099c89a

## 2025_07_16

I was having issues with working on a Raspberry Pi with VS Code throught SSH. Sometimes, the Pi would freeze and force me to hard reboot it.
This tutorial says it's VS Code fault, installing pluggins on server side that occasionnally max the CPU capacity of low power devices, such as my Pi : https://medium.com/good-robot/use-visual-studio-code-remote-ssh-sftp-without-crashing-your-server-a1dc2ef0936d
I desactivated all the pluggin, and it work much better now.

# Dependencies and Tutorials

## Arduino

## Godot

## RaspberryPi

### Buzzer Passif

The passive buzzer pilot is based on pigpiod : https://abyz.me.uk/rpi/pigpio/pigpiod.html

### Video_Player_v1

The video player is based on pyvidplayer2 : https://github.com/anrayliu/pyvidplayer2
The test program have very low performance on raspi 3b : around 3 fps
I'm switching to python-vlc in Video_v2

#### TO DO
- [ ] Test the test program on a Raspberry Pi 4B 4G

### Video_v2

Since pyvidplayer2 shows huge performances issues ont Raspi 3, I tried another approach, based on this video : https://www.youtube.com/watch?v=Y3SJ8qLqQA8
The code video_vlc.py works really well on a Raspi 3, but I can't manage to launch it through systemd. I get this error : vlcpulse audio output error: PulseAudio server connection failure: Connection refused

#### TO DO
- [ ] Debug launching video_vlc.py through systemd

