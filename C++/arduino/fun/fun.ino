// LED for wave
int led1 = 13;
int led2 = 12;
int led3 = 11;
int led4 = 10;

// Wave Delay
int waveDelay = 50;

void blink(int led) {
  // Turns an LED on, waits then LED off
  digitalWrite(led, HIGH);
  delay(waveDelay);
  digitalWrite(led, LOW);
  delay(waveDelay);
}

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
}

void loop() {
  blink(led1);
  blink(led2);
  blink(led3);
  blink(led4);
  blink(led3);
  blink(led2);
}



