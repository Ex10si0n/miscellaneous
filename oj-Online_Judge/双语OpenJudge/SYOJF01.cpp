#include <iostream>
using namespace std;
int n,a,cnt;
void count(){
	int t=a/70;
	cnt+=(t+1);
	if(a%70==0) cnt--;
}
int main(){
	cin>>n;
	for(int i=1;i<=n;i++){cin>>a;count();}
	cout<<(double)cnt*0.1<<endl;
	return 0;
}