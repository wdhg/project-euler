#include <iostream>

using namespace std;

bool isDivisableUpTo(int x, int upTo) {
  if(upTo < 1) {
    return false;
  }
  for(int i = 2; i <= upTo; i++) {
    if(x % i != 0) {
      return false;
    }
  }
  return true;
}

int smallestMultiple(int upTo) {
  int i = 1;
  while(!isDivisableUpTo(i, upTo)) {
    i++;
  }
  return i;
}

int main() {
  cout << smallestMultiple(20) << endl;
  return 0;
}