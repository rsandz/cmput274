#include <iostream>

using namespace std;

int main() {
    // here is a template to help get you started
    // declare some variables
    int m, n, stored, cap;
    int count = 0;

    // read in the first line of input
    cin >> m >> n;

    // now solve the problem and output the result!
    for (int i = 0; i < n; i++)
    {
        cin >> stored >> cap;
        if ((stored + m) <= cap)
        {
            count++;
        }
    }

    cout << count << endl;

    return 0;
}
