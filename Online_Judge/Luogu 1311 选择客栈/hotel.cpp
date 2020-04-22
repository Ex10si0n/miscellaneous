#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

#define N 200005

int n,k,p,ans;
struct hotel{
	int c,p;
}h[N];

int main(){
	//freopen("/Users/Ex10si0n/Desktop/LN-2333/hotel/data1.in","r",stdin);
	//freopen("hotel.in","r",stdin);
	//freopen("hotel.out","w",stdout);
	scanf("%d%d%d",&n,&k,&p);
	for(int i=1;i<=n;i++) scanf("%d%d",&h[i].c,&h[i].p);
	for(int i=0;i<k;i++){
		for(int j=1;j<=n;j++){
			if(h[j].c==i){
				int m=h[j].p;
				for(int q=j+1;q<=n;q++){
					if(h[q].p<m) m=h[q].p;
					if(h[q].c==i && m<=p){
						ans++;
						//cout<<j<<" "<<q<<endl;
					}
				}
			}
		}
	}
	if(n==1){cout<<0<<endl;return 0;}
	cout<<ans<<endl;
	return 0;
}