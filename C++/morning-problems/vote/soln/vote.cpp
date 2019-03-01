#include <iostream>

using namespace std;

int main() {
  int n = 0;
  int vote[1001];
  int tally[1001] = {0};

  // keep reading until we see 0
  while (true) {
    cin >> vote[n];
    if (vote[n] == 0) {
      break;
    }
    ++n;
  }

  // now n == # votes and vote[i] is the i'th vote
  // for 0 <= i <= n-1
  for(int i = 0; i < n + 1; i++)
  {
    tally[vote[i]] += 1;
  }
  // solve the problem and print the answer

  int max = 0;
  int winner;
  bool tie = false;
  
  for (int i = 1; i < 1001; i++)
  {
    if (max == tally[i])
    {
      tie = true;
    }
    else if (tally[i] > max)
    {
      max = tally[i];
      winner = i;
      tie = false;
    }
  }

  if (tie)
  {
    cout << "tie" << endl;
  }
  else
  {
    cout << winner << endl;
  }

  return 0;
}
