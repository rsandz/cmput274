#include <iostream>

using namespace std;

int main() {
  
  int sum, a, b, c, d;
  cin >> a >> b >> c >> d;
  
  // Let's use Arrays, since they're Fun!
  int barcode[4] = {a, b, c, d};
  sum = 0;
  for (int i = 0; i < 4; i++)
  {
    sum += (i + 1) * barcode[i];
  }

  if (sum % 5 == 0)
  {
    cout << "yes" << endl;
  }
  else
  {
    cout << "no" << endl;
  }
  return 0;
}
