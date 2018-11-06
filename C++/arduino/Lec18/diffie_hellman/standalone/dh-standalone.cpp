/*
	Includes the code for the basic Diffie-Hellman key exchange protocol.
	Current version works for 16-bit primes only.
*/
#include <iostream>
#include <stdint.h>

using namespace std;
/*
	Compute and return (a to the power of b) mod m.
 	Assumes 1 <= m < 2^16 (i.e. that m fits in a uint16_t).
	Example: powMod(2, 5, 13) should return 6.
*/
uint32_t powMod(uint32_t a, uint32_t b, uint32_t m) {
	// multiply a by itself b times, keeping the intermediate
	// values mod m each step

	// question: if x,y are uint32_t, but each are < 2^16,
	// is (x*y) % m avoiding overflow?
	// YES: x*y < 2^32, so the multiplication does not overflow

	/*
		result = 1
		for b steps
			result = (result*a) mod m
		return result
	*/

	a = a%m;
	uint32_t result = 1 % m; // even initialize to be mod m
	for (uint32_t i = 0; i < b; i++) {
		result = (result*a) % m;
	}
	return result;
}

/*
	Check if powMod(a, b, m) == result
*/
void onePowModTest(uint32_t a, uint32_t b, uint32_t m,
									 uint32_t expected) {
	uint32_t calculated = powMod(a, b, m);
	if (calculated != expected) {
		cout << ("error in powMod test") << endl;
		cout << ("expected: ");
		cout << (expected) << endl;
		cout << ("got: ");
		cout << (calculated) << endl;
	}
}

void testPowMod() {
	cout << ("starting tests") << endl;
	// run powMod through a series of tests
	onePowModTest(1, 1, 20, 1); //1^1 mod 20 == 1
	onePowModTest(5, 7, 37, 18);
	onePowModTest(5, 27, 37, 31);
	onePowModTest(3, 0, 18, 1);
	onePowModTest(2, 5, 13, 6);
	onePowModTest(1, 0, 1, 0);
	onePowModTest(123456, 123, 17, 8);
	cout << ("tests done!") << endl;
}


int main() {
	testPowMod();


	// begin chat, make sure to encrypt!


	return 0;
}
