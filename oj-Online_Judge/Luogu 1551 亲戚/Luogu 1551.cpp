#include <iostream>
using namespace std;
#define N 5005
int n,m,p,a,b,fa[N];

int find(int x){return fa[x]==x?x:fa[x]=find(fa[x]);}

int main(){
	cin>>n>>m>>p;
	for(int i=1;i<=n;i++) fa[i]=i;
	for(int i=1;i<=m;i++){
		cin>>a>>b;
		int aa=find(a),bb=find(b);
		if(aa!=bb) fa[aa]=bb;
	}
	for(int i=1;i<=p;i++){
		cin>>a>>b;
		if(find(a)==find(b))cout<<"Yes"<<endl;
		else cout<<"No"<<endl;
	}
	return 0;
}