#include <iostream>
#include <cmath>

using namespace std;

int n = 0;
float potenz;

int main(){
    while (n <=10) {
        potenz = pow(2.0, n);
        cout << "2 hoch " << n << " ist: " << potenz << endl;
        n++;
    }
    return 0;
}