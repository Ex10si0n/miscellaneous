#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;
long long b,p,k;
long long qpow(int a,int n){
	if(n==0) return 1;
	long long r=1;
	long long t=a;
	while(n){
		if(n&1) r = (r%k * t%k) % k;
		t = (t%k * t%k) % k;
		n >>= 1;
	}
	return r%k;
}
int main(){
	cin>>b>>p>>k;
	printf("%lld^%lld mod %lld=",b,p,k);
	cout<<qpow(b,p)<<endl;
	return 0;
}