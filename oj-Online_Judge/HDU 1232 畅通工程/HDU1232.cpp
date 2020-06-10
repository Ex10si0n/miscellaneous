#include <iostream>
#include <cstdio>
using namespace std;

#define N 1005

int n,m,a,b,aa,bb,ans,fa[N];

int find(int x){return x==fa[x]?x:fa[x]=find(fa[x]);}
void union_(int i,int j){aa=find(i);bb=find(j);fa[aa]=bb;}

int main(){
	while(1){
		scanf("%d",&n);
		if(n==0) break;
		for(int i=1;i<=n;i++) fa[i]=i;
		ans=0;
		scanf("%d",&m);
		for(int i=1;i<=m;i++){
			scanf("%d%d",&a,&b);
			union_(a,b);
		}
		for(int i=1;i<=n;i++)
			if(find(1)!=find(i)) ans++,union_(1,i);
		cout<<ans<<endl;
	}
	return 0;
}