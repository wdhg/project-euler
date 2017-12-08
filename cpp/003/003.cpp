#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(int num) {
  if(num % 2 == 0) {
    return false;
  }
  for(int i = 3; i < pow(num, 0.5); i += 2) {
    if(num % i == 0) {
      return false;
    }
  }
  return true;
}

int largestPrimeFactor(long num) {
  int largest = 1;
  if(num % 2 == 0) {
    largest = 2;
  }
  for(int i = 3; i < pow(num, 0.5); i += 2) {
    if(num % i == 0 && isPrime(i)) {
      largest = i;
    }
  }
  return largest;
}

int main() {
  cout << largestPrimeFactor(600851475143L) << endl;
  return 0;
}