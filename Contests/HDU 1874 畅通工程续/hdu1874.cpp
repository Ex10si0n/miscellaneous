#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <queue>

#define INF 2139062143
#define N 205
using namespace std;

int a,b,s,t,x;
int map[N][N],dis[N],vis[N];
queue<int>q;

void addedge(int a,int b,int c){
	map[a][b]=c;
}

void SPFA(){
	q.push(s);
	vis[s]=1;
	dis[s]=0;
	while(!q.empty()){
		x=q.front();
		q.pop();
		for(int i=0;i<a;i++){
			if(map[x][i]!=-1 && dis[x]+map[x][i]<dis[i]){
				dis[i]=dis[x]+map[x][i];
				if(!vis[i]){
					vis[i]=1;
					q.push(i);
				}
			}
		}
		vis[x]=0;
	}
}

int main(){
	while(scanf("%d%d",&a,&b)!=EOF){
		memset(map,-1,sizeof(map));
		memset(dis,127,sizeof(dis));
		memset(vis,0,sizeof(vis));
		for(int i=1;i<=b;i++){
			int x,y,z;
			cin>>x>>y>>z;
			addedge(x,y,z);
			addedge(y,x,z);
		}
		cin>>s>>t;
		SPFA();
		if(dis[t]<INF) cout<<dis[t]<<endl;
		else cout<<-1<<endl;
	}
	return 0;
}