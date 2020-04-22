#include <iostream>
using namespace std;
#define N 100005

bool vis[N];
int a[N],s[N],n,t[N],m,ans,pre,tt,aa;

struct home{
	int s,a;
}h[100010];

void debug(){for(int i=1;i<=n;i++) cout<<t[i]<<" "; cout<<endl;}

int main(){
	freopen("/Users/Ex10si0n/Desktop/Code Repo/Luogu 2672 推销员/data.in","r",stdin);
	cin>>n;
	for(int i=1;i<=n;i++) cin>>h[i].s;
	for(int i=1;i<=n;i++) cin>>h[i].a;
	m=-1;
	for(int i=1;i<=n;i++){
		t[i]=h[i].a+h[i].s*2;
		if(t[i]>m) m=t[i],pre=i;
	}
	vis[pre]=1;
	ans=m;
	cout<<ans<<endl;
	m=-1;

	for(int j=2;j<=n;j++){
	//cout<<"ppp"<<pre<<endl;
	
		m=-1;
		int dd=0;
		for(int i=1; i<=n; i++){
			if(vis[i]) continue;
			if(i<pre){
				t[i]=h[i].a+h[pre].s*2;
				aa=ans+h[i].a;
				if(aa>m) m=t[i],tt=i,dd=1;
			}
			else{
				t[i]=h[i].a+h[i].s*2;
				aa=ans-h[pre].s*2+h[i].a+h[i].s*2;
				if(aa>m) m=t[i],tt=i,dd=2;
			}
		}
		//debug();
		vis[tt]=1;

		//debug();
		if(dd==1) ans=ans+h[tt].a;
		if(dd==2) ans=ans-h[pre].s*2+h[tt].a+h[tt].s*2;
		pre=tt;

		cout<<ans<<endl;
		
	}


	return 0;
}