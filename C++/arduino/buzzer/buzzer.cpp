#include <Arduino.h>

int speakerPin = 9;
int controlPin = 0;

void setup () {
    pinMode ( speakerPin , OUTPUT ) ;
}
/*
play a tone with period given in microseconds for a duration
given in milliseconds
*/
void playTone (int period , int duration ) {
    // elapsed time in microseconds , the long is needed to get
    // a big enough range .
    long elapsedTime = 0;
    // note we are making a slight error here if period is not even
    int halfPeriod = period / 2;
    while ( elapsedTime < duration * 1000L ) {
        // generate a square wave of the given period . Half the
        // period is on , the other half is off .
        digitalWrite ( speakerPin , HIGH );
        delayMicroseconds ( halfPeriod ) ;
        digitalWrite ( speakerPin , LOW ) ;
        delayMicroseconds ( halfPeriod ) ;
        // count the time we just consumed for one cycle of the tone
        elapsedTime = elapsedTime + period ;
    }
}
void loop () {
    int period;
    int newPeriod;
    period = analogRead ( controlPin );
    newPeriod = map(period, 0, 1023, 100, 10000);
    playTone ( newPeriod , 500);
}