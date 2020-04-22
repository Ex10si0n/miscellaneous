#include <iostream>
using namespace std;
#define N 100005

bool vis[N];
int a[N],s[N],t[N];
int n,work,m,pre,ppre,sum,di;

struct home{
	int s,a;
}h[100010];

int main(){
	freopen("/Users/Ex10si0n/Desktop/Code Repo/Luogu 2672 推销员/data.in","r",stdin);
	cin>>n;
	for(int i=1;i<=n;i++) cin>>h[i].s;
	for(int i=1;i<=n;i++) cin>>h[i].a;
	
	for(int x=1;x<=n;x++){
		m=-1;
		if(x==1){
			for(int i=1;i<=n;i++){
				t[i]=h[i].a+2*h[i].s;
				if(t[i]>=m) pre=i,m=t[i];
			}
			sum=m;
			vis[pre]=1;
			cout<<sum<<endl;
			continue;
		}
		ppre=pre;
		m=-1;
		for(int i=1;i<=n;i++){
			if(i<ppre){
				t[i]=h[i].a+2*h[ppre].s;
				if(t[i]>m) pre=i,m=t[i];
			}
			if(i>ppre){
				t[i]=h[i].a+2*h[i].s;
				if(t[i]>m) pre=i,m=t[i];
			}
		}
		cout<<m<<endl;
	}
	return 0;
}

/*
if(di) {sum+=h[pre].a;vis[pre]=1;}
		else {sum=sum+h[pre].a+2*h[pre].s-2*h[ppre].s;vis[pre]=1;}
		cout<<sum<<endl;
		for(int i=1;i<=n;i++) cout<<vis[i]<<" ";
				cout<<endl;
*/