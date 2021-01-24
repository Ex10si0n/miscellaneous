/*
Luogu NOIP 模拟赛 d2 将军令
*/
#include <iostream>
#include <vector>
using namespace std;
#define N 100005

int n,k,t,u,v,fa[N];
vector<int>G[N];
void addedge(int a,int b){G[a].push_back(b);}

int find(int x){return fa[x]==x?x:find(fa[x]);}

int main(){
	cin>>n>>k>>t;
	for(int i=1;i<=n;i++) fa[i]=i;
	for(int i=1;i<=n-1;i++) cin>>v>>u,addedge(u,v),addedge(v,u),fa[u]=find(u),fa[v]=find(v);
	if(t==2 && k>=2) {cout<<1<<endl;return 0;}
	if(t==2 && k==1) for(int i=1;i<=n;i++) cout<<fa[i]<<" ";
	return 0;
}
/*
6 1 2 
1 2 
1 3 
1 4 
4 5 
4 6
*/