/* ===================================================
# Exercise 5: Counting Lights
# ===================================================
# Name: Ryan Sandoval
# ID: 1529017
# Course: CMPUT 274, FALL 2018
*/

#include <Arduino.h>


/* LED Init */

// Note, order is from Most significant bit to
// least Significant bit. i.e. ledPins[0] is MSB
const int ledPins[5] = {13, 12, 11, 10, 9};
const int incrementBtn = 6;
const int decrementBtn = 7;
const int numLeds = 5;
int *ledStates;

void setup()
{
    init();
    Serial.begin(9600);

    // LED
    for (int i = 0; i < 5; i++)
    {
        pinMode(ledPins[i], OUTPUT);
    }

    // Btns
    pinMode(incrementBtn, INPUT_PULLUP);
    pinMode(decrementBtn, INPUT_PULLUP);
}

/**
 * Converts an integer into its binary representation
 * Param:
 *  (int) i - Integer to convert
 * Returns an array pointer of size numLeds
 * Array goes from MSB to LSB
 */
int* intToBinary(int integer)
{
    static int binary[numLeds];
    int index = numLeds - 1;
    int remain;

    while (integer != 0 && index >= 0)
    {
        remain = integer % 2;
        integer = integer / 2;
        binary[index] = remain;
        index--;
    }

    // Fill the rest with zeroes
    while (index >= 0 )
    {
        binary[index] = 0;
        index--;
    }

    return binary;
}

/**
 * Gets the number to change count (in main) based on the 
 * button pressed
 * Return:
 *  - integer to change count by: 1 or -1
 *  - Also returns 0 if nothing is pressed
 */
int getCountChange()
{
    if (digitalRead(incrementBtn) == LOW)
    {
        return 1;
    }
    else if (digitalRead(decrementBtn) == LOW)
    {
        return -1;
    }
    else
    {
        return 0;
    }
}

/**
 * Updates Leds based on ledStates array
 */
void updateLeds()
{
    for (int i = 0; i < numLeds; i++)
    {
        digitalWrite(ledPins[i], ledStates[i]);
    }
}

/**
 * Checks if count is less than 0 or greater
 * than 2^(numLeds) - 1
 * 
 * Return:
 *  - 0 if it's greater than 2^(numLeds) - 2
 *  - 2^(numLeds) - 1 if < 0
 */
int correctOverflow(int count)
{
    if (count < 0)
    {
        return (2 << numLeds - 1) - 1;
    }
    else if (count > (2 << numLeds - 1) - 1)
    {
        return 0;
    }
    else
    {
        return count;  // No changes
    }
}

int main()
{
    /* Initialization */
    setup();
    bool buttonHeld = false;
    int count = 0;
    int countChange;

    ledStates = intToBinary(count);
    updateLeds();

    while (true)
    {
        countChange = getCountChange();  // 0 if no button pressed

        if (!buttonHeld && countChange != 0)  // Value change if button not held
        {
            buttonHeld = true;
            count += countChange;

            // Uncomment to print count after push
            // Serial.println(count);

            count = correctOverflow(count);

            // Update States and LED
            ledStates = intToBinary(count);
            updateLeds();
        }
        else if (countChange == 0 && buttonHeld)
        {
            // Button no longer held
            buttonHeld = false;
        }

        // Delay for button bounce
        delay(50);
    }

    return 0;
}
