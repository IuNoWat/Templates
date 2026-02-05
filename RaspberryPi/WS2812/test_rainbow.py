import rpi_ws281x as rpi
import time

range_led = 45
frame = 0.02


strip_1 = rpi.PixelStrip(range_led,12,channel=0)
strip_1.begin()

offset = 0

third = int(range_led/3)

def rainbow() :
    global offset
    colors=[0]*range_led

    for j in range(0,range_led) :
        meh=j+offset
        if meh>range_led :
            meh-=range_led
        if meh < range_led/2 :
            colors[j]=(int(255*(meh/range_led)),0,0)
        else :
            colors[j]=(int(255*(1-meh/range_led)),0,0)

    offset+=1
    if offset==range_led :
        offset=0
    
    for i,entry in enumerate(colors) :
        strip_1.setPixelColor(i,rpi.Color(entry[0],colors[i+third if i+third<range_led else i+third-range_led][0],colors[i+third*2 if i+third*2<range_led else i+third*2-range_led][0]))
    
    strip_1.show()
    time.sleep(frame)


while True :
    rainbow()
    print("done")