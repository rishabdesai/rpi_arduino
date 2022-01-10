void setup() {
  Serial.begin(115200);  //
  while(!Serial){}  //optional for Auduino UNO boards

}

void loop() {
 Serial.println("hello from Arduino UNO");
 delay(1000);
  
}
