/*
	Using the analog pin to generate a random bit.
*/

#include <Arduino.h>

// an analog pin will "float" if nothing is attached
// this can be used as a source of randomness
const int random_pin = A0;

void setup() {
	init();
	Serial.begin(9600);
}

uint16_t getRandomU16() {
	uint16_t num = 0;
	
	num = (analogRead( random_pin ) &1);
	
	Serial.print( num, BIN );

	return num;
}


int main() {
    setup();

    Serial.print( "Random bit generation using analog pin A0\n" );
    while (true) {
        uint16_t privateKey = getRandomU16();
        delay(1000);
    }
    
    Serial.end();

    return 0;
}
