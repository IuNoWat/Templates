
//CONSTANTS
bool debug = true;

int FPS = 30;
int millis_of_frame = 1000 / FPS;
float current_fps;

// PINS

//ENGINE
#include "RunningAverage.h"
long current_time;
long elapsed_time;
long old_time = 0;
int time_to_wait;
RunningAverage avg_wait(FPS*3);


void setup() {
  
  Serial.begin(9600);
  
}

void loop() {

  

  tic();
}

void tic(){

  current_time = millis();
  elapsed_time = current_time - old_time;
  time_to_wait = millis_of_frame - elapsed_time;

  if(debug){
    avg_wait.addValue(time_to_wait);
    Serial.println(avg_wait.getAverage());
  }

  if(time_to_wait>0){
    delay(time_to_wait);
  }

  old_time = current_time;
}
