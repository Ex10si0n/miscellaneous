#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;
#define N 20005

struct Edge{
	int u,v,next;
}edge[N];
int head[N],tot;
void addedge(int u,int v){
	tot++;
	edge[tot].u=u;
	edge[tot].v=v;
	edge[tot].next=head[u];
	head[u]=tot;
}
int first[N],occur[2*N],depth[2*N];
int m=0;

int T,n,a,b,u,v;
void dfs(int u,int dep){
	occur[++m]=u;
	depth[m]=dep;
	if(!first[u]) first[u]=m;
	for(int i=head[u];i;i=edge[i].next){
		dfs(edge[i].v,dep+1);
		occur[++m]=u;
		depth[m]=dep;
	}
}

void init(){
	tot=0,m=0,u=0,v=0;
	memset(head,0,sizeof(head));
	memset(first,0,sizeof(first));
	int in[N]={0};
	cin>>n;
	for(int i=1;i<n;i++){
		cin>>u>>v;
		addedge(u,v);
		in[v]=1;
	}
	for(int i=1;i<=n;i++){
		if(!in[i]){
			dfs(i,1);
			break;
		}
	}
	cin>>a>>b;
}

int main(){
	cin>>T;
	while(T--){
		init();
		// for(int i=1;i<=2*n-1;i++)cout<<occur[i]<<endl;
		int l=first[a],r=first[b];
		int t;
		if(l>r) t=l,l=r,r=t;
		int m=N,f;
		for(int i=l;i<=r;i++)
			if(depth[i]<=m) m=depth[i],f=i;
		cout<<occur[f]<<endl;
	}
	return 0;
}
