#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;
#define N 10005
#define able abs(x[i]-x[j])+abs(y[i]-y[j])<=t[i]-t[j]
int ans,n,m,x[N],y[N],t[N],dp[N];
int main(){
	cin>>n>>m;
	cin>>t[1]>>x[1]>>y[1];
	dp[1]=1;
	for(int i=2;i<=m;i++){
		cin>>t[i]>>x[i]>>y[i];
		dp[i]=1;
		for(int j=1;j<=i-1;j++)
			if(able) dp[i]=max(dp[i],dp[j]+1);
		ans=max(ans,dp[i]);
	}	
	cout<<ans<<endl;
	return 0;
}
