#include <iostream>
using namespace std;

int a0,a1,b0,b1,n,cnt,g;

int gcd(int m,int n){
	int r,t;
	if(m<n)	t=m,m=n,n=t;
	while(n!=0) r=m%n,m=n,n=r;
	return m;
}

int lcm(int m,int n,int r){
	int t;
	t=m*n/r;
	return t;
}


int main(){
	cin>>n;
	for(int i=1;i<=n;i++){
		cnt=0;
		cin>>a0>>a1>>b0>>b1;
		for(int x=1;x<=b1;x++){
			g=gcd(x,b0);
			if(gcd(x,a0)==a1 && lcm(x,b0,g)==b1) cnt++;
		}
		cout<<cnt<<endl;

	}



	return 0;
}
