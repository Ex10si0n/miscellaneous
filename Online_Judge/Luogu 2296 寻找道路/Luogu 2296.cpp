/*
NOIP 2014 d2t2 寻找道路，题目中给出的条件是满足一条最短路上所有出边指向的点都与终点连接
我的思路是：存反向图，拓扑入度为0的点，然后剪掉它所在的路径 然后最短路求最短距离
*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>

using namespace std;

#define N 10005
queue<int>q,t;
vector<int>G[N];
int indg[N],n,m,x,y,s,t;
void addedge(int a,int b){G[b].push_back(a),indg[a]++;}//存反向图
void topo(){
	for(int i=1;i<=n;i++) if(i!=s && indg[i]==0) t.push(i);
	while(!t.empty()){
		int tt=t.front();
		t.pop();
		for(int i=0;i<G[tt].size();i++){//筛选出度
			
			
		}
	}
}

int main(){
	cin>>n>>m;
	for(int i=1;i<=m;i++){cin>>x>>y,addedge(x,y);}
	cin>>s>>t;


	return 0;
}