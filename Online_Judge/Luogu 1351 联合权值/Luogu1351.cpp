#include <cstdio>
#include <iostream>
#include <vector>
#define N 2000005
#define mod 10007

using namespace std;


int n,tot,c[N];


/*struct graph{
	int in,out,v;
}g[N];

vector<int>G[N];

*/

vector<int>G[N];

void addedge(int x,int y){
	G[x].push_back(y);	
}

int sum;

int main(){
	cin>>n;
	for(int i=1;i<=n-1;i++){
		int a,b;
		cin>>a>>b;
		addedge(a,b);
		addedge(b,a);
	}
	for(int i=1;i<=n;i++) cin>>c[i];
	
	for(int i=1;i<=n;i++){
		for(vector<int>::iterator it=G[i].begin;it!=G[i].end;it++){
			cout<<
		}
		
		
		
		
	} 
		
	
	
	return 0;
}
