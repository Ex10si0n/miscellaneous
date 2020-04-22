#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <cstdlib>
using namespace std;

#define N 100005
#define INF 2139062143
int n,m,s,t,in[N],dis[N];
bool vis[N];
vector<int>G[N];
queue<int>p,q;

void addedge(int i,int j){G[i].push_back(j);}

void SPFA(){
	dis[t]=0;
	vis[t]=1;
	q.push(t);
	while(!q.empty()){
		int x=q.front();
		q.pop();
		for(int i=0;i<G[x].size();i++){
			int next=G[x][i];
			if(dis[x]+1<dis[next] && dis[next]!=INF+1){
				dis[next]=dis[x]+1;
				if(!vis[next]){
					q.push(next);
					vis[next]=1;
				}
			}
		}
		vis[x]=0;
	}
}

int main(){
	//freopen("/Users/Ex10si0n/Desktop/tmp/data.in","r",stdin);
	cin>>n>>m;
	for(int i=1;i<=m;i++){
		int a,b;
		cin>>a>>b;
		addedge(b,a);//反向存图
		in[a]++;
	}
	cin>>s>>t;
	memset(dis,127,sizeof(dis));
	
	for(int i=1;i<=n;i++) if(in[i]==0 && i!=t) p.push(i);
	
	while(!p.empty()){
		int x=p.front();
		dis[x]=INF;
		p.pop();
		for(int i=0;i<G[x].size();i++){
			int next=G[x][i];
			if(in[next]==0) p.push(next);
			else dis[next]=INF+1;
		}
	}
	
	for(int i=1;i<=n;i++) vis[i]=0;
	SPFA();
	if(dis[s]>=INF){
		cout<<-1<<endl;
	}else
		cout<<dis[s]<<endl;
	return 0;
}