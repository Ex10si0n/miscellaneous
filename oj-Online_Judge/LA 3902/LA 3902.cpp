#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>

#define N 1005

using namespace std;

vector<int>G[N],n[N];
int T,n,s,k;

void addedge(int x,int y){
	G[x].push_back(y);
}

void dfs(int dep){

}

int main(){
	freopen("/Users/Ex10si0n/Desktop/Code Repo/LA 3902/data.in","r",stdin);
	cin>>T;
	while(T--){
		memset(map,0,sizeof(map));
		cin>>n;
		cin>>s>>k;
		for(int i=1;i<=n-1;i++){
			int a,b;
			cin>>a>>b;
			addedge(a,b);
			addedge(b,a);
		}
		





	}

	
	return 0;
}