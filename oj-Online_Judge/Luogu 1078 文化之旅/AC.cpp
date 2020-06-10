#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <queue>
#define N 105
#define INF 9999999
using namespace std;

int n,k,m,s,t;
int c[N],map[N][N],a[N][N],dis[N],vis[N];
queue<int>q;

int main(){
	cin>>n>>k>>m>>s>>t;
	for(int i=1;i<=n;i++) cin>>c[i];
	for(int i=1;i<=k;i++){
		for(int j=1;j<=k;j++){
			cin>>a[i][j];//a i j 代表第i个文化排斥第j个文化
		}
	}
	for(int i=1;i<=m;i++){
		int x,y,v;
		cin>>x>>y>>v;
		map[x][y]=map[y][x]=v;
		if(a[c[x]][c[y]]==1) map[y][x]=INF;
		if(a[c[y]][c[x]]==1) map[x][y]=INF;
	}


	for(int i=1;i<=n;i++) dis[i]=9999999;

	vis[s]=1;
	dis[s]=0;
	q.push(s);

	while(!q.empty()){
		int x=q.front();
		q.pop();
		for(int i=1;i<=n;i++){
			if(map[x][i]!=0 && dis[x]+map[x][i]<dis[i]){
				dis[i]=dis[x]+map[x][i];
				if(!vis[i]){
					vis[i]=1;
					q.push(i);
				}
			}
		}
		vis[x]=0;
	}


	if(dis[t]!=INF)	cout<<dis[t]<<endl;
	else cout<<-1<<endl;

	return 0;
}