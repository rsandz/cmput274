/*
Blink for testing LEDS
*/
#include <Arduino.h>
int toBlink[] = {13, 12, 11, 10,9};
int numLeds = 5;

void setup()
{
    init();
    for (int i = 0; i < numLeds; i++)
    {
        pinMode(toBlink[i], OUTPUT);
    }
}

int main()
{
    setup();
    for (int i = 0; i < numLeds; i++)
    {
        digitalWrite(toBlink[i], HIGH);
        delay(100);
        digitalWrite(toBlink[i], LOW);
    }

    return 0;
}