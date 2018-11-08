/*
	Includes the code for the basic Diffie-Hellman key exchange protocol.
	Current version works for 16-bit primes only.
*/

#include <Arduino.h> // angle brackets, from the system
#include "powmod.h"  // look in the local directory first

void setup() {
	init();
	Serial.begin(9600);
}

uint32_t diffieHellman() {
	const uint32_t p = 19211;
	const uint32_t g = 6;

	// TODO: get a random number
	// step 1 of setup procedure
	uint32_t myPrivateKey = 123;

	// step 2 of setup procedure
	uint32_t myPublicKey = powModFast(g, myPrivateKey, p);

	// TODO: print the public key to the screen
	// step 3 of setup procedure

	// TODO: type in the other Arduino's public key
	// step 4 of setup procedure
	uint32_t otherPublicKey = 456; // should read from serial mon

	// step 5 of setup procedure
	uint32_t sharedSecretKey = powModFast(otherPublicKey, myPrivateKey, p);

	return sharedSecretKey;
}

int main() {
	setup();

	testPowModFast();

	// uint32_t sharedKey = diffieHellman();

	// begin chat, make sure to encrypt!

	Serial.end();

	return 0;
}
