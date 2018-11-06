// the external LED is attached to this pin .
// onboard LED is attached to pin 13 ,
int ledPin = 13;

// slider of potentiometer attached to this analog input
int analogInPin = 0;

// length of a dot
int dotTime = 300;

// even though we are not using it yet , make sure the
// pushbutton is set up correctly
// the pushbutton is attached to this digital input pin
int buttonPin = 9;

// the value read from the pushbutton
int buttonValue ;

// On or Off for signal
boolean active = true;

// we take the code for sending dot and dash and put them
// into two methods
void sendDot () {
  // a dot is one unit long
  digitalWrite(ledPin, HIGH);
  delay(dotTime);
  digitalWrite(ledPin, LOW);
  delay(dotTime);
}
void sendDash () {
  // a dash is 3 dots long
  digitalWrite ( ledPin , HIGH );
  delay (3 * dotTime );
  // an inter - element gap is one dot
  digitalWrite ( ledPin , LOW );
  delay ( dotTime );
}
void sendShortGap () {
  // we assume that we are preceeded by an inter - element gap .
  // so that we have 3 dots of gap
  delay (2 * dotTime );
}
void sendMediumGap () {
  // Assume preceeded by inter - element gap
  // Only need 6 dots of gap
  delay(6 * dotTime);
}
void setup () {
  // configure ledPin to be a digital output
  pinMode ( ledPin , OUTPUT );
  // set buttonPin to INPUT and
  // turn on internal pull up resistor
  pinMode ( buttonPin , INPUT );
  digitalWrite ( buttonPin , HIGH ) ;
}
void loop () {
  
  if (active) {
    // Send S
    sendDot();
    sendDot();
    sendDot();
    sendShortGap();
    // send out an O: - - -
    sendDash () ;
    sendDash () ;
    sendDash () ;
    sendShortGap () ;
    // Send S
    sendDot();
    sendDot();
    sendDot();
    sendMediumGap();
  }
  
  // Get new dotTime
  dotTime = analogRead(analogInPin);
}
