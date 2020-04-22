#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;


int n;
double x[15],y[15],dis[15][15],ans=99999999.9,now;
bool vis[15];

void dfs(int pos,int dep){
	if(now>ans) return;
	if(dep==n){ans=now;return;}
	vis[pos]=1;
	for(int i=1;i<=n;i++){
		if(!vis[i]){
			now+=dis[pos][i];
			dfs(i,dep+1);
			now-=dis[pos][i];
		}
	}
	vis[pos]=0;
}

int main(){
	cin>>n;
	for(int i=1;i<=n;i++) cin>>x[i]>>y[i];
	x[0]=y[0]=0;
	for(int i=0;i<=n;i++)
		for(int j=0;j<=n;j++)
			dis[i][j]=sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]));
	dfs(0,0);
	printf("%.2lf\n",ans);
	return 0;
}