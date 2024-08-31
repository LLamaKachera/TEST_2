#include <iostream>
using namespace std;

int main() {
    long long m, j;
    cin >> m >> j;

    long long s = m - j;
    long long t = (s + 1) * j;
    long long r = m * (m + 1) / 2;

    cout << r - t << endl;

    return 0;
}
