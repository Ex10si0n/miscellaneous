#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#define N 1005
using namespace std;

char bin;
int n,e,a,b,c,T;
int depth[N],dis[N],p[N][20];
bool vis[N];

struct EDGE{
	int to,v;
}edge[N];

vector<EDGE>G[N];
EDGE t;
void addedge(){
	t.to=b;t.v=c;G[a].push_back(t);
	t.to=a;t.v=c;G[b].push_back(t);
}

void dfs(int x){
	vis[x]=1;
	for(int i=1;i<=15;i++){
		if(depth[x]<(1<<i)) break;
		p[x][i]=p[p[x][i-1]][i-1];
	}
	for(int i=0;i<G[x].size();i++){
		if(!vis[G[x][i].to]){
			depth[G[x][i].to]=depth[x]+1;
			dis[G[x][i].to]=dis[x]+G[x][i].v;
			p[G[x][i].to][0]=x;
			dfs(G[x][i].to);
		}
	}
}

int lca(int x,int y){
	if(depth[x]<depth[y]) swap(x,y);
	int t=depth[x]-depth[y];
	for(int i=0;i<=15;i++)
		if(t&(1<<i)) x=p[x][i];
	for(int i=15;i>=0;i--)
		if(p[x][i]!=p[y][i])
			x=p[x][i],y=p[x][i];
	if(x==y) return x;
	return p[x][0];
}

int main(){
	cin>>n>>T;
	for(int i=1;i<=n-1;i++){
		cin>>a>>b>>c;
		addedge();
	}
	dfs(1);
	while(T--){
		int x,y;
		cin>>x>>y;
		int root=lca(x,y);
		cout<<dis[x]+dis[y]-2*dis[root]<<endl;
	}
	return 0;
}
/*
6 1
1 2 5
2 3 6
1 4 2
4 5 3
4 6 7
*/