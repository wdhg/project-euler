#include <iostream>
#include <vector>

using namespace std;

vector<int> evenFibUpTo(int max) {
  vector<int> sequence;
  int a = 1, b = 2;

  while(a < max) {
    if(a % 2 == 0) {
      sequence.insert(sequence.end(), a);
    }
    b = a + b;
    a = b - a;
  }

  return sequence;
}

int sum(vector<int> numbers) {
  int total = 0;
  for(int num : numbers) {
    total += num;
  }
  return total;
}

int main() {
  vector<int> numbers = evenFibUpTo(4000000);
  cout << sum(numbers) << endl;
  return 0;
}