#include <iostream>
using namespace std;

int num, sum, x[20], ans[100][20];

void drawMap() {
  for (int j = 1; j <= num *2 + 1; j++) {
    if (j % 2 == 1) {
      for (int i = 1; i <= num * 2 + 1; i++) {
        if (i % 2 == 1) {
          cout << "+";
        }
        else {
          cout << "---";
        }
      }
    }
    else {
      for (int i = 1; i <= num * 2 + 1; i++) {
        if (i % 2 == 1) {
          cout << "|";
        }
        else if (i / 2 == ans[sum][j/2]) {
          cout << " x ";
        }else {
          cout << "   ";
        }
      }
    }
    cout << endl;
  }
}

bool place(int k) {
  for (int j = 1; j < k; j++)
    if (abs(x[k] - x[j]) == abs(k - j) || x[j] == x[k])
      return false;
    return true;
}

void backTrack(int t) {
  if (t > num) {
    sum ++;
    if (sum <= 5) {
      for (int m = 1; m <= num; m++) {
        ans[sum][m] = x[m];
      }
      cout << endl <<  "Solution No." << sum << " found." << endl;
      drawMap();
    }
  }
  else for (int i = 1; i <= num; i++) {
      x[t] = i;
      if (place(t))
        backTrack(t + 1);
  }
}

int main(int argc, char** argv) {
  cout << "Input Size N of the Chart: (int) N = " ;
  cin >> num;
  backTrack(1);
  cout << "All " << sum << " Answer(s) found." << endl;
}
