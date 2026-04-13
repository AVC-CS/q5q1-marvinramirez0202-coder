#include <iostream>
using namespace std;

int main()
{
    int n;
    char letters[6] = {'A', 'B', 'C', 'D', 'E', 'F'};

    // TODO: ask user for input
    cout << "Enter number: ";
    cin >> n;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < i + 1; j++){
            cout << letters[j] << " ";
        }
        cout << endl;
    }
    // TODO: outer loop for each row
    
        // TODO: inner loop to print letters for this row

            // TODO: print the letter for this column

        // TODO: print newline after each row


    return 0;
}
