#include <iostream>
#include <queue>
#define INF 0x7ffffff
#define in_map newx>=1 && newx<=r && newy>=1 && newy<=c
using namespace std;

int newx,newy,h,r,c,ans=-1;
int a[105][105],f[105][105];

int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};


int dp(int x,int y){
	if(f[x][y]) return f[x][y];
	int t=0;
	for(int i=0;i<=3;i++){
		newx=x+dx[i];
		newy=y+dy[i];
		if(in_map && a[newx][newy]<a[x][y]){
			t=max(t,dp(newx,newy));
		}
	}
	f[x][y]=t+1;
	return f[x][y];
}

int main(){
	cin>>r>>c;
	for(int i=1;i<=r;i++)
		for(int j=1;j<=c;j++)
			cin>>a[i][j];
	for(int i=1;i<=r;i++){
		for(int j=1;j<=c;j++)
			ans=max(ans,dp(i,j));
	}
	cout<<ans<<endl;
	return 0;
}