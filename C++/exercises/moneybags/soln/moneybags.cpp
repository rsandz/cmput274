/*
===========================
| Exercise 7 - Money Bags |
===========================
Name: Ryan Sandoval
Id: 1529017
Course: CMPUT 274, Fall 2018
*/

#include <iostream>
#include <algorithm>

using namespace std;

/**
 * Populates an array in place with input from
 * cin based on amount. 
 * @param array arr Array to populate
 * @param int amount Number of inputs to take
 */
void populate_array(int arr[], int amount)
{
    for (int i = 0; i < amount; i++)
    {
        cin >> arr[i];
    }
}

int main()
{
    // Init
    int num_aplicants = 0;
    int net_worth_arr[100000];
    int threshold = 1;
    int valid_applicants = 0;

    // Get the Inputs and preprocess them
    cin >> num_aplicants;

    populate_array(net_worth_arr, num_aplicants);
    sort(net_worth_arr, net_worth_arr + num_aplicants);
    reverse(net_worth_arr, net_worth_arr + num_aplicants);

    // Get the best N a.k.a Threshold
    while (true)
    {
        valid_applicants = 0;

        for (int i = 0; i < num_aplicants; i++)
        {
            if (net_worth_arr[i] >= threshold)
            {
                valid_applicants++;
            }
            else
            {
                break;
            }
        }

        if (valid_applicants < threshold)
        {
            // Last threshold correct so `--` it
            threshold--;
            break;
        }

        threshold++;
    }

    // Output and done
    cout << threshold << endl;

    return 0;
}
