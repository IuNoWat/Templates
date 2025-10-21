import rpi_ws281x as rpi
import time

strip = rpi.PixelStrip(22,18)

strip.begin()

while True :
    for i in range(0,22) :
        for j in range(0,22) :
            strip.setPixelColor(j,rpi.Color(0,0,0))
        strip.setPixelColor(i,rpi.Color(255,255,255))
        strip.show()
        time.sleep(0.5)