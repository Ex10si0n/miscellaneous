#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

int n,a,b,c,e;
double dis[10][10],m=-1.0,ans=0,t,pi=acos(-1),s[10];
bool vis[10],f;

struct dot{double x,y,m,r;}d[10];

void dfs(int dep,double s){
	f=0;
	if(dep==n){if(s>ans) ans=s;return ;}
	for(int i=1;i<=n;i++){
		if(!vis[i]){
			vis[i]=1;
			m=d[i].m;
			for(int j=1;j<=n;j++){
				if(vis[j]&&j!=i){
					if(dis[i][j]-d[j].r<0){f=1;break;}
					if(dis[i][j]-d[j].r<m){
						m=dis[i][j]-d[j].r;
					}
				}
			}
			if(f==0) d[i].r=m;
			if(f==0) dfs(dep+1,s+pi*m*m);
			else if(f==1) dfs(dep+1,s);
			vis[i]=0;
		}
	}
	return ;
}

int main(){
	cin>>n;
	cin>>a>>b>>c>>e;
	int size=(abs(e-a)*abs(c-b));
	for(int i=1;i<=n;i++) cin>>d[i].x>>d[i].y;
	for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
			dis[i][j]=sqrt((d[i].x-d[j].x)*(d[i].x-d[j].x)+(d[i].y-d[j].y)*(d[i].y-d[j].y));
	for(int i=1;i<=n;i++){
		if(fabs(d[i].x-a)>m) d[i].m=fabs(d[i].x-a),m=d[i].m;
		if(fabs(d[i].x-c)>m) d[i].m=fabs(d[i].x-c),m=d[i].m;
		if(fabs(d[i].y-b)>m) d[i].m=fabs(d[i].x-b),m=d[i].m;
		if(fabs(d[i].y-e)>m) d[i].m=fabs(d[i].x-e),m=d[i].m;
	}
	dfs(1,0);
	cout<<size-ans<<endl;


	return 0;
}