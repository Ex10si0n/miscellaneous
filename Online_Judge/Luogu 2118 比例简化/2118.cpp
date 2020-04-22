#include <iostream>
#include <cmath>
using namespace std;
double a,b,bili,t=99999;
int l;
int xx,yy;
int main(){
	cin>>a>>b>>l;
	double s;
	s=a/b;
	for(int i=1;i<=l;i++){
		for(int j=1;j<=l;j++){
			bili=(double)i/j;
			if(bili>=s){
				double gg=fabs(bili-s);
				if(t>gg){
					t=gg;
					xx=i;
					yy=j;
				}
			}		
		}
	}
	cout<<xx<<" "<<yy<<endl;
	return 0;
}