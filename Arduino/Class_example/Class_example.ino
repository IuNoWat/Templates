
// PINS
uint8_t motor_1_up = 8 ;
uint8_t motor_1_down = 9 ;
int btn1 = 6;
int btn2 = 7;
int btn3 = 5;
int val1;
int val2;
int val3;

class LinearMotor{
  private :
    uint8_t pin_up;
    uint8_t pin_down;
    int pas = 666;
    int chill_time = pas * 4;
    bool busy = false;
    bool chill = false;
    bool current_dir = false;
    unsigned long previousMillis = millis();
  
  public :
    LinearMotor(uint8_t pin_up,uint8_t pin_down); // Constructeur
    void up();
    void down();
    void update();
};

LinearMotor::LinearMotor(uint8_t pin1, uint8_t pin2){
  pin_up = pin1;
  pin_down = pin2;
  pinMode(pin_up, OUTPUT);
  pinMode(pin_down, OUTPUT);
}

void LinearMotor::up(){
  if(busy){
    Serial.println("Motor busy");
  } else if(chill) {
    Serial.println("Motor chillin'");
  } else {
    busy = true;
    chill = true;
    current_dir = true;
    previousMillis = millis();
  }
}

void LinearMotor::down(){
  if(busy){
    Serial.println("Motor busy");
  } else if(chill) {
    Serial.println("Motor chillin'");
  } else {
    busy = true;
    chill = true;
    current_dir = false;
    previousMillis = millis();
  }
}

void LinearMotor::update(){
  digitalWrite(pin_up,LOW);
  digitalWrite(pin_down,LOW);
  unsigned long currentMillis = millis();

  if(busy) {
    if(current_dir){
      digitalWrite(pin_up,HIGH);
    } else {
      digitalWrite(pin_up,LOW);
    }
    
    if(current_dir==false){
      digitalWrite(pin_down,HIGH);
    } else {
      digitalWrite(pin_down,LOW);
    }
    
    if(currentMillis-previousMillis >= pas){
      busy = false;
    }
  }
  
  if(currentMillis-previousMillis >= chill_time){
     chill = false;
  }
  
}

LinearMotor test(motor_1_up,motor_1_down);

void setup() {
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

  if(val1==false){
    test.up();
  }

  if(val2==false){
    test.down();
  }

  test.update();



}
