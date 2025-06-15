#include <Servo.h>

Servo myservo;

void setup() {
  // put your setup code here, to run once:
  myservo.attach(9);
  myservo.write(93);
}

void loop() {
  // put your main code here, to run repeatedly:
  //myservo.write(93);
  //delay(200);
  //myservo.write(93-4);
  //delay(200);
  //myservo.write(93+4);
  //delay(200);
}
