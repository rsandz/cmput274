#include <algorithm> // contains sort()
#include <iostream>

using namespace std;

int main() {
    // read in the input
    int n;
    cin >> n;

    // create the array A to hold n integers
    int A[n];

    // read in the values of A
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }

    // now read in the second array!
    int m;
    cin >> m;

    int B[m];
    for (int i = 0; i < m; i++)
    {
        cin >> B[i];
    }

    // solve the problem
    sort(A, A + n);
    sort(B, B + m);
    int lastIndex = 0;
    
    for (int i = 0; i < m; i++)
    {
        if (A[lastIndex] == B[i])
        {
            lastIndex++;
        }
    }

    // output the result 
    if (lastIndex == n)
    {
        cout << "Yes" << endl;
    }
    else
    {
        cout << "No" << endl;
    }

    return 0;
}