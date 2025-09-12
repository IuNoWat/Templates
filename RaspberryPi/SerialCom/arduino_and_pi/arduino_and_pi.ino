String serial_msg;

String get_serial_input() {
  serial_msg = Serial.readStringUntil("#");
  serial_msg.remove(serial_msg.length()-1);
  return serial_msg;
}

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop() {
  String msg = get_serial_input();
  if(msg!="#"){
    Serial.print(msg+"#");
  }
  
}
