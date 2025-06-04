#include <Adafruit_NeoPixel.h>

#define LED_PIN 6
#define LED_COUNT 16

Adafruit_NeoPixel ring(LED_COUNT,LED_PIN);

void setup() {
  ring.begin();           
  ring.show();            
  ring.setBrightness(50);
}

void loop() {
  for(int j = 0; j<16;j++){
    for(int i = 0; i<16;i++){
      ring.setPixelColor(i,0,0,0,0);
    }
    ring.setPixelColor(j,255,255,255,0);
    ring.show();
    delay(1000);
  }

}
