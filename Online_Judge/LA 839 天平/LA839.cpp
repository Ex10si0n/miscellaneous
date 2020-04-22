#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int T;
bool ok;

int work(){
	int w1,d1,w2,d2;
	cin>>w1>>d1>>w2>>d2;
	if(w1==0) w1=work();
	if(w2==0) w2=work();
	if(w1*d1!=w2*d2) ok=0;
	return w1+w2;
}

int main(){
	cin>>T;
	while(T--){
		ok=1;
		work();
		if(ok)cout<<"YES"<<endl<<endl;
		else cout<<"NO"<<endl<<endl;
	}
	return 0;
}
