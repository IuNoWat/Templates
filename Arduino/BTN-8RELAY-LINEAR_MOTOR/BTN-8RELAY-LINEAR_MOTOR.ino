
// PINS
int motor_1 = 46 ;
int motor_1 = 46 ;
int motor_1 = 46 ;
int motor_1 = 46 ;
int motor_1 = 46 ;
int motor_1 = 46 ;
int motor_1 = 46 ;
int motor_1 = 46 ;



int dir1 = 8 ;
int dir2 = 9 ;
int btn1 = 6;
int btn2 = 7;
int btn3 = 5;
int val1;
int val2;
int val3;


void setup() {
  pinMode(dir1, OUTPUT);
  pinMode(dir2, OUTPUT);
  pinMode(btn1, INPUT_PULLUP);
  pinMode(btn2, INPUT_PULLUP);
  pinMode(btn3, INPUT_PULLUP);  
  Serial.begin(9600);
}

void loop() {
  val1 = digitalRead(btn1);
  val2 = digitalRead(btn2);
  val3 = digitalRead(btn3);

  Serial.println("--");
  Serial.println(val1);
  Serial.println(val2);

  digitalWrite(dir1,LOW);
  digitalWrite(dir2,LOW);

  if(val1){
    digitalWrite(dir1,HIGH);
  } else {
    digitalWrite(dir1,LOW);
  }
  
  if(val2){
    digitalWrite(dir2,HIGH);
  } else {
    digitalWrite(dir2,LOW);
  }

}
