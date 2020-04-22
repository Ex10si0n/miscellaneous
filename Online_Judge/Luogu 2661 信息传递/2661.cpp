#include <iostream>
#include <queue>
#define N 200005
using namespace std;

int p,indg[N],n;

struct Edge{
	int from,to;
}edge[N];


void addedge(int x,int y){
	edge[++p].from=x;
	edge[p].to=y;
	indg[y]++;
}

queue<int>q;

void topo(){
	while(!q.empty()){
		int u=q.front();
		q.pop();
		for(int i=1;i<=p;i++){
			 if(indg[i]==0){
				q.push(i);
				indg[edge[i].to]--;
				edge[i].from=edge[i].to=0;
			}
		}
	}
}

void bfs(){
	
}

int main(){
	cin>>n;
	for(int i=1;i<=n;i++){
		int t;
		cin>>t;
		addedge(i,t);
	}
	for(int i=1;i<=n;i++){
		if(indg[i]==0){
			q.push(i);
			indg[edge[i].to]--;
			edge[i].from=edge[i].to=0; //delete
			topo();
		}
	}


	return 0;
}