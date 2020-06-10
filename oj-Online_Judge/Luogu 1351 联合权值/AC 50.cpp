#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <cmath>

#define N 2000005
#define mod 10007

using namespace std;


int n,tot,c[N],ans;

int sum,a[N];

vector<int>G[N];

void addedge(int x,int y){
	G[x].push_back(y);	
}

int main(){
	cin>>n;
	for(int i=1;i<=n-1;i++){
		int a,b;
		cin>>a>>b;
		addedge(a,b);
		addedge(b,a);
	}
	for(int i=1;i<=n;i++) cin>>c[i];
	
	for(int i=1;i<=n;i++){
		int son[N],pp=0;
		memset(son,0,sizeof(son));
		sum=0;
		for(int j=0;j<G[i].size();j++){
			son[++pp]=c[G[i][j]];
			sum+=c[G[i][j]];
			sum%=mod;
		}
		int max1,max2;
		max1=son[pp];
		max2=son[pp-1];
		for(int j=0;j<G[i].size();j++){
			a[i]+=c[G[i][j]]*(sum-c[G[i][j]]);
		}
		ans=max(ans,max1*max2);
	}
	int ans2=0;
	for(int i=1;i<=n;i++){
		ans2+=a[i];
		ans2%=mod;
	}
	cout<<ans<<" "<<ans2<<endl;
	return 0;
}
