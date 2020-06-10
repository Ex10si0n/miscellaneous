#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;
#define pi acos(-1)

int pai[10];
int n,a,b,c,e;
double dis[10][10],m=0.0,ans=0.0,t;
bool vis[10],f,gg;
struct dot{double x,y,m,r;}d[10];

double min_(double a,double b){return a+0.0000001>b+0.0000001 ? b : a;}

void search(){
	double ss=0.0;
	for(int i=1;i<=n;i++){
		m=9999999.9999;gg=0;
		for(int j=1;j<i;j++){
			if(dis[pai[i]][pai[j]]-d[pai[j]].r<m && dis[pai[i]][pai[j]]-d[pai[j]].r>0.000001) m=dis[pai[i]][pai[j]]-d[pai[j]].r;
			if(dis[pai[i]][pai[j]]-d[pai[j]].r<0.000001) gg=1;
		}
		if(!gg) d[pai[i]].r=min_(d[pai[i]].m,m);
		if(!gg) ss+=(d[pai[i]].r*d[pai[i]].r*pi);
	}
	if(ss>ans) ans=ss;
}

void qp(int l){
	if(l==n+1){search();return ;}
	for(int i=1;i<=n;i++){
		if(!vis[i]){
			vis[i]=1;
			pai[l]=i;
			qp(l+1);
			vis[i]=0;
		}
	}
}

int main(){	
	cin>>n;
	cin>>a>>b>>c>>e;
	int size=(abs(a-c)*abs(b-e));
	for(int i=1;i<=n;i++) cin>>d[i].x>>d[i].y;
	for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
			dis[i][j]=sqrt((d[i].x-d[j].x)*(d[i].x-d[j].x)+(d[i].y-d[j].y)*(d[i].y-d[j].y));
	for(int i=1;i<=n;i++){
		m=9999999.9;
		if(fabs(d[i].x-a)<m) {m=fabs(d[i].x-a);d[i].m=m;}
		if(fabs(d[i].x-c)<m) {m=fabs(d[i].x-c);d[i].m=m;}
		if(fabs(d[i].y-b)<m) {m=fabs(d[i].y-b);d[i].m=m;}
		if(fabs(d[i].y-e)<m) {m=fabs(d[i].y-e);d[i].m=m;}
	}
	qp(1);
	cout<<size<<" "<<ans<<endl;
	cout<<(int)(size-ans+0.5)<<endl;
	return 0;
}
