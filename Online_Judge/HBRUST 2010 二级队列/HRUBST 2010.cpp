/*
if(a[j]>a[i] && dp[j]=max{dp[1]...dp[i]})
dp[i]=dp[j]+1;
*/
#include <iostream>
#include <cstring>
using namespace std;
int n,a[1005],dp[1005];
int main(){
	while(cin>>n){
		for(int i=1;i<=n;i++) cin>>a[i];
		memset(dp,0,sizeof(dp));
		dp[1]=1;
		for(int i=2;i<=n;i++){
			int max=-1;
			for(int j=1;j<i;j++)
				if(dp[j]>max && a[j]>=a[i]) max=dp[j];
			dp[i]=max+1;
		}
		/*for(int i=1;i<=n;i++) cout<<dp[i]<<" ";
		cout<<endl;*/
		cout<<n-dp[n]<<endl;
	}
	return 0;
}