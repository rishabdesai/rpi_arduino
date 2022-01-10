int cnt=0;

void setup() {
  Serial.begin(115200);
    
  while(!Serial){}  

}

void loop() {
  if(Serial.available() > 0) {
  String msg = Serial.readStringUntil('\n');
  msg = msg +" " +String(cnt);
  cnt++;
  Serial.print(msg);
    }
 }
