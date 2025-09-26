
#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_TFTLCD.h> // Hardware-specific library

#define LCD_CS A3 // Chip Select goes to Analog 3
#define LCD_CD A2 // Command/Data goes to Analog 2
#define LCD_WR A1 // LCD Write goes to Analog 1
#define LCD_RD A0 // LCD Read goes to Analog 0

#define LCD_RESET A4 // Can alternately just connect to Arduino's reset pin

// Assign human-readable names to some common 16-bit color values:
#define	BLACK   0x0000
#define	BLUE    0x001F
#define	RED     0xF800
#define	GREEN   0x07E0
#define CYAN    0x07FF
#define MAGENTA 0xF81F
#define YELLOW  0xFFE0
#define WHITE   0xFFFF

Adafruit_TFTLCD tft(LCD_CS, LCD_CD, LCD_WR, LCD_RD, LCD_RESET);

void setup() {
  Serial.begin(9600);
  Serial.println(F("Test Program for TFT LCD screen"));

  #ifdef USE_ADAFRUIT_SHIELD_PINOUT
  Serial.println(F("Using Adafruit 2.8\" TFT Arduino Shield Pinout"));
  #else
  Serial.println(F("Using Adafruit 2.8\" TFT Breakout Board Pinout"));
  #endif

  tft.reset();

  //Check the type of the screen's driver

  uint16_t identifier = tft.readID();

  if(identifier == 0x9325) {
    Serial.println(F("Found ILI9325 LCD driver"));
  } else if(identifier == 0x9328) {
    Serial.println(F("Found ILI9328 LCD driver"));
  } else if(identifier == 0x7575) {
    Serial.println(F("Found HX8347G LCD driver"));
  } else if(identifier == 0x9341) {
    Serial.println(F("Found ILI9341 LCD driver"));
  } else if(identifier == 0x8357) {
    Serial.println(F("Found HX8357D LCD driver"));
  } else {
    Serial.print(F("Unknown LCD driver chip: "));
    return;
  }

  tft.begin(identifier);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  tft.fillScreen(BLACK);
  delay(500);
  tft.fillScreen(RED);
  delay(500);
  tft.fillScreen(GREEN);
  delay(500);
  tft.fillScreen(BLUE);
  delay(500);
}
