// This example code show how to use a buzzer.
// 

void setup() {
  // put your setup code here, to run once:
  pinMode(11, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  //tone (11, 600); // allume le buzzer actif arduino
  //delay(500);
  //tone(11, 900); // allume le buzzer actif arduino
  //delay(500);
  noTone(11);  // désactiver le buzzer actif arduino
  delay(500);
  for(int i=0;i<100;i++){
    tone(11,i*10);
    delay(300);
  }
}
