#include <iostream>

using namespace std;

int main() {
  int n, diff, total;
  int array[1000];

  // read in the input
  cin >> n;
  
  for (int i = 0; i < n; i++)
  {
    cin >> array[i];
  }
  // now compute and print the answer
  total = 0;
  for (int i = 0; i < (n - 1); i++)
  {

    diff = array[i+1] - array[i];
    if (diff > 0)
    {
      total += diff;
    }
  }

  cout << total << endl;

  return 0;
}
