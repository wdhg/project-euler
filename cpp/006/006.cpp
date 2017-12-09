#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

const int UP_TO = 100;

int main() {
  int sumOfSquares = 0;
  int squareOfSums = 0;

  for(int i = 1; i <= UP_TO; i++) {
    sumOfSquares += pow(i, 2);
    squareOfSums += i;
  }

  printf("%f0", pow(squareOfSums, 2) - sumOfSquares);
  cout << endl;
  return 0;
}