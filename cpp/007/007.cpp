#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(int num) {
  if(num <= 1) {
    return false;
  } else if(num % 2 == 0) {
    return false;
  }
  for(int i = 3; i <= pow(num, 0.5); i += 2) {
    if(num % i == 0) {
      return false;
    }
  }
  return true;
}

int getPrime(int pos) {
  int primeCount = 1, n = 1;
  while(primeCount < pos) {
    n++;
    if(isPrime(n)) {
      primeCount++;
    }
  }
  return n;
}

int main() {
  cout << getPrime(10001) << endl;

  return 0;
}