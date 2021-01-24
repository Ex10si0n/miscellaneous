#include <iostream>
#include <cstdio>
#define N 105
#define mod 1000007
using namespace std;
int n,m,a[N],f[N][N];
int main(){
	cin>>n>>m;
	for(int i=1;i<=n;i++) cin>>a[i];
	for(int i=0;i<=m;i++) f[i][0]=1;
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
			for(int k=0;k<=a[i];k++)
				if(j-k>=0)
					f[i][j]=(f[i][j]+f[i-1][j-k])%mod;
	cout<<f[n][m]<<endl;
	return 0;
}