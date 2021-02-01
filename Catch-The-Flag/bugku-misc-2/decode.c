#include <stdio.h>

int getint() {
	int ch = getchar(), ans = 0;
	while(ch<'0' || ch>'9') ch = getchar();
	while('0'<=ch&&ch<='9') ans=ans*10+ch-'0', ch = getchar();
	return ans;
}

int main() {
	while(1) {
		int x = getint();
		printf("%c", x);
	}
	return 0;
}
