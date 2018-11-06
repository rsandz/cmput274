// the LED is attached to this digital output pin
int ledPin = 13;
// the pushbutton is attached to this digital input pin
int buttonPin = 9;
// the value read by the pin .
int buttonValue ;
void setup () {
// set ledPin to OUTPUT
pinMode ( ledPin , OUTPUT );
// set buttonPin to INPUT and turn on internal pull up resistor
pinMode ( buttonPin , INPUT );
digitalWrite ( buttonPin , HIGH ) ;
}
void loop () {
// read the pushbutton state and set the light to be the same value
buttonValue = digitalRead ( buttonPin ) ;
digitalWrite ( ledPin , buttonValue );
}

