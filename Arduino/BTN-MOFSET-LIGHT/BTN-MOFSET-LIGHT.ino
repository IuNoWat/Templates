
// PINS
int mofset = 9 ;
int btn = 10;
int val;



void setup() {
  pinMode(mofset, OUTPUT);
  pinMode(btn, INPUT_PULLUP);  
  Serial.begin(9600);
}

void loop() {
  val = digitalRead(btn);
  Serial.println(val);
  if(val){
    digitalWrite(mofset,HIGH);
  } else {
    digitalWrite(mofset,LOW);
  }
}
