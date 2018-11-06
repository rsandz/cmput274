/*# ---------------------------------------------------
# Name : Imtisal Ahmad
# ID: 1495401
# CMPUT 274 , Fall 2018
#
# Exercise 5:Counting Lights 
# ---------------------------------------------------*/
#include <Arduino.h>

//the variables for each button
//increment button 
const int Button0Pin = 6;  
//decrement button         
const int Button1Pin = 7;  


//assign low voltages to each bulb 
//assign the variables for each LED

int LEDPins[5] = {9,10,11,12,13};
int LEDstates[5] = {LOW,LOW,LOW,LOW,LOW};





void setup() {
    init();
    int i =0;
    int m =0;
    Serial.begin(9600);
    //assign the variables for each LED
    while(i < 5) {
     digitalWrite(LEDPins[i], LEDstates[i]);
    i = i + 1;
    }
    // config LED pins to be a digital OUTPUT
    while(m<5){
        pinMode(LEDPins[m] , OUTPUT);
        m ++;

    }
    
    
    // configue the button pins to be a digital INPUT
    // turn on the internal pull-up resistors
    pinMode(Button0Pin, INPUT);
    digitalWrite(Button0Pin, HIGH);
    pinMode(Button1Pin, INPUT);
    digitalWrite(Button1Pin, HIGH);

}
void increasestates(){
    //This function checks if the increment button is pushed then assigns the LED states to the LEDstates array 
    int k;
    for (k = 0;k<5;k++){
         //checks if LED is off then turns it on 
        if (LEDstates[k] ==LOW){
            LEDstates[k]=HIGH;
            break; 

            }
        else{
            //otherwise turns the LED off
            LEDstates[k]=LOW;
                
            }


        }

    
}
void decreasestates(){
    //This function checks if the decrement button is pushed then assigns the LED states to the LEDstates array 

    
    int k;
    for (k = 0;k<5;k++){
        //checks if LED is on then turns it off 
        if (LEDstates[k] ==HIGH){
             LEDstates[k]=LOW;
            break; 

            }
        else{
            //otherwise turns it on
            LEDstates[k]=HIGH;
                
            }
        }
    
}
void apply(){
    //This function takes all the changes to LED states made from the increasestates and decrease states functions and displays the output 
    int r;
    for (r = 0; r<5;r++){
        // assigns the pins the states passed on from the main functions 
        digitalWrite(LEDPins[r], LEDstates[r]);
    }
    
}


int main() {
    setup(); // our first act should be to initialize everything
    //check if button is being pushed 
    int Push = 0;
    int Pushno = 0;

    while (true) {
        if (digitalRead(Button0Pin) == LOW)
        {
            Serial.println("Button pressed");
        }
        // increment Pushcount
        if (( digitalRead(Button0Pin) == LOW ) && (Push !=5)){
            //push - 2 only counts 1 push even if its pressed down for a long time 
            Push = 2;
        }
        if (Push == 2){
            //sets the states of the lights 
            increasestates();
            //digitally displays the states of the LEDs on the arduino 
            apply();
            Push = 5;
            }
        //Decrement Pushcount  
        if (( digitalRead(Button1Pin)== LOW) && (Pushno !=5)){
            //Pushno = 2 bascially only counts it as 1 push 
            Pushno = 2;
        }
        if (Pushno == 2) {
            //sets the states of the decreasing lights 
            decreasestates();
            //digitally dispplays the states of the LEDs on the arduino 
            apply();
            //By setting Pushno to 5 I am basically letting the game run over again 
            Pushno = 5;
        }
        if((Push == 5)&&( digitalRead(Button0Pin) == HIGH)){
            Push = 0;
        }
         if((Pushno == 5)&&( digitalRead(Button0Pin) == HIGH )){
            Pushno = 0;
        }

        for (int i = 0; i <5 ; i++)
        {
            Serial.print(LEDstates[i]);
        }
            Serial.println();

        // wait 50 ms for any button bounce to die out
        delay(50);
    }

return 0;  
}     
        




    


