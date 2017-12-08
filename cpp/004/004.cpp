#include <iostream>

using namespace std;

bool isPalindromeNumber(int num) {
  string normal = to_string(num);
  string reverse = "";
  for(char c : normal) {
    reverse = c + reverse;
  }
  return normal == reverse;
}

int largestPalindrome() {
  int largest = 0;

  for(int a = 100; a < 1000; a++) {
    for(int b = a; b < 1000; b++) {
      int c = a * b;
      largest = (c > largest && isPalindromeNumber(c)) ? c : largest;
    }
  }

  return largest;
}

int main() {
  cout << largestPalindrome() << endl;
  return 0;
}