#include <Arduino.h> // for uint32_t and friends
#include "powmod.h"

/*
	Compute and return (a to the power of b) mod m.
 	Assumes 1 <= m < 2^16 (i.e. that m fits in a uint16_t).
	Example: powMod(2, 5, 13) should return 6.
*/
uint32_t powModSlow(uint32_t a, uint32_t b, uint32_t m) {
	// multiply a by itself b times, keeping the intermediate
	// values mod m each step

	a = a%m;
	uint32_t result = 1 % m; // even initialize to be mod m
	for (uint32_t i = 0; i < b; i++) {
		if (i%10000 == 0) {
			Serial.print("Iteration: ");
			Serial.println(i);
		}
		result = (result*a) % m;
	}
	return result;
}

/*
	Compute and return (a to the power of b) mod m.
 	Assumes 1 <= m < 2^16 (i.e. that m fits in a uint16_t).
	Example: powMod(2, 5, 13) should return 6.
*/
uint32_t powModFastOld(uint32_t a, uint32_t b, uint32_t m) {
	// compute ap[0] = a
	// ap[1] = ap[0]*ap[0]
	// ...
	// ap[i] = ap[i-1]*ap[i-1] (all mod m) for i >= 1

	uint32_t ap[32];
	ap[0] = a % m;
	for (int i = 1; i < 32; i++) {
		// no overflow if m < 2^16, as the product is at most 32 bits
		// replace this with your multplication routine that you worked out on the worksheet
		ap[i] = (ap[i-1]*ap[i-1]) % m;
	}
	// now ap[i] = a^(2^i) mod m (here ^ means exponentiation)

	// now look at the binary expansion of b to determine which
	// ap[i] values to multiply together
	// eg: a^13 = a^(2^3) * a^(2^2) * a^(2^0)
	//          = ap[3]   * ap[2]   * ap[0]

	uint32_t result = 1 % m;
	for (int i = 0; i < 32; i++) {
		// if the i'th bit of b is 1
		// shifting moves the i'th bit to position 0, then & 1 isolates this bit
		if (((b>>i)&1) == 1) {
			// no overflow if m < 2^16, as the product is at most 32 bits
			// replace this with your multplication routine that you worked out on the worksheet
			result = (result*ap[i]) % m;
		}
	}

	return result;
}


/*
	Compute and return (a to the power of b) mod m.
 	Assumes 1 <= m < 2^16 (i.e. that m fits in a uint16_t).
	Example: powMod(2, 5, 13) should return 6.
*/
uint32_t powModFast(uint32_t a, uint32_t b, uint32_t m) {
	// compute ap[0] = a
	// ap[1] = ap[0]*ap[0]
	// ...
	// ap[i] = ap[i-1]*ap[i-1] (all mod m) for i >= 1

	uint32_t result = 1%m;
	uint32_t sqrVal = a%m; //stores a^{2^i} values, initially 2^{2^0}
	uint32_t newB = b;

	// LOOP INVARIANT: statements that hold throughout a loop
	//                 with the goal of being convinced the loop works
	// statements: just before iteration i,
	//               result = a^{binary number represented the first i bits of b}
	//               sqrVal = a^{2^i}
	//               newB = b >> i
	while (newB > 0) {
		if (newB&1) { // evalutates to true iff i'th bit of b is 1
			result = (result*sqrVal)%m;
		}
		sqrVal = (sqrVal*sqrVal) % m;
		newB = (newB>>1);
	}

	// upon termination: newB == 0
	// so b >> i is 0
	// so result a^{binary number represented the first i bits of b} = a^b, DONE!

	// # iterations ~ log_2 b ~ # of bits to write b
	// running time = O(log b)
	// NOTATION: we write O(some function) to express how the running times
	//           grows as a function of the input

	return result;
}



/*
	Check if powMod(a, b, m) == result
*/
void onePowModFastTest(uint32_t a, uint32_t b, uint32_t m,
									 uint32_t expected) {
	uint32_t calculated = powModFast(a, b, m);
	if (calculated != expected) {
		Serial.println("error in powMod test");
		Serial.print("expected: ");
		Serial.println(expected);
		Serial.print("got: ");
		Serial.println(calculated);
	}
}

void testPowModFast() {
	Serial.println("starting tests");
	// run powMod through a series of tests
	onePowModFastTest(1, 1, 20, 1); //1^1 mod 20 == 1
	onePowModFastTest(5, 7, 37, 18);
	onePowModFastTest(5, 27, 37, 31);
	onePowModFastTest(3, 0, 18, 1);
	onePowModFastTest(2, 5, 13, 6);
	onePowModFastTest(1, 0, 1, 0);
	onePowModFastTest(123456, 123, 17, 8);

	Serial.println("Now starting big test");
	uint32_t start = micros();
	onePowModFastTest(123, 2000000010ul, 17, 16);
	uint32_t end = micros();
	Serial.print("Microseconds for big test: ");
	Serial.println(end-start);

	Serial.println("Another big test");
	onePowModFastTest(123456789, 123456789, 61234, 51817);

	Serial.println("With a big modulus (< 2^31)");
	onePowModFastTest(123456789, 123456789, 2147483647, 1720786551);


	Serial.println("tests done!");
}
