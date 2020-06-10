/*
用并查集省掉了建图的麻烦，然后在筛的时候先选一级公路，如果不能选，选二级公路，但是前提是
都不能大于k，判断正确性是有的。
*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

struct edge{int a,b,c1,c2;}e[200005];

int n,m,k,l,r,ans,fa[10005];

int find(int x){
	if(fa[x]==x) return x;
	return fa[x]=find(fa[x]);
}

bool ok(int x){//判断最大花费为当前mid时能不能全部连通
	for(int i=1;i<=n;i++) fa[i]=i;//注意fa归零
	int cnt=0;
	for(int i=1;i<=m;i++){//先筛一遍c1
		if(e[i].c1>x) continue;
		int p=find(e[i].a);
		int q=find(e[i].b);
		if(p!=q) fa[p]=q,cnt++;
	}
	if(cnt<k) return 0;//cnt>k时必然不是最优，因为可以选更便宜的了为什么选贵的
	for(int i=1;i<=m;i++){
		if(e[i].c2>x) continue;
		int p=find(e[i].a);
		int q=find(e[i].b);
		if(p!=q) fa[p]=q,cnt++;
	}
	if(cnt!=n-1) return 0;//没有把所有点都连上
	return 1;
}

int main(){
	cin>>n>>k>>m;
	for(int i=1;i<m;i++) cin>>e[i].a>>e[i].b>>e[i].c1>>e[i].c2;
	l=1;r=30000;
	while(l<=r){
		int mid=(l+r)>>1;
		if(ok(mid)) ans=mid,r=mid-1;
		else l=mid+1;
	}
	cout<<ans<<endl;
	return 0;
}
/* data.in
10 4 20
3 9 6 3
1 3 4 1
5 3 10 2
8 9 8 7
6 8 8 3
7 1 3 2
4 9 9 5
10 8 9 1
2 6 9 1
6 7 9 8
2 6 2 1
3 8 9 5
3 2 9 6
1 6 10 3
5 6 3 1
2 7 6 1
7 8 6 2
10 9 2 1
7 1 10 2
*/