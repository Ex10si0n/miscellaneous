#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;
#define in_map newx>=1&&newx<=n&&newy>=1&&newy<=m

int n,m,newx,newy,vis[105][105],ans;
char map[105][105];
int dx[10]={1,1,1,0,0,-1,-1,-1};
int dy[10]={0,1,-1,1,-1,-1,0,1};

queue<int>qx,qy;

void bfs(int x,int y){
	qx.push(x);
	qy.push(y);
	while(!qx.empty()){
		int xx=qx.front(); qx.pop();
		int yy=qy.front(); qy.pop();
		for(int i=0;i<8;i++){
			newx=xx+dx[i];
			newy=yy+dy[i];
			if(in_map && map[newx][newy]=='W' && !vis[newx][newy]){
				vis[newx][newy]=1;
				map[newx][newy]='.';
				qx.push(newx);
				qy.push(newy);
			}
		}
	}
}

int main(){
	cin>>n>>m;
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
			cin>>map[i][j];
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++){
			if(map[i][j]=='W'){
				bfs(i,j);
				ans++;			
			}
		}
	cout<<ans<<endl;

	return 0;
}