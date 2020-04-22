#include <iostream>
#include <cstdio>
using namespace std;


int n,a[10],sum=0;
int hash_[100005][10],p;
bool able;

void dfs(int dep){
	for(int i=1;i<=n;i++){
		a[dep]=i; sum+=i;
		if(sum>n){
			sum-=a[i];
			break;
		}
		if(sum==n){
			able=0;
			++p;
			for(int i=1;i<=dep;i++){
				hash_[p][a[i]]++;
			}
			for(int i=1;i<p;i++){
				for(int j=1;j<=8;j++){
					if(hash_[i][j]!=hash_[p][j]){able=1;break;}
				}
			}
			if(able){
				cout<<a[1];
				for(int j=2;j<=dep;j++) cout<<"+"<<a[j];
				cout<<endl;
				sum-=i;
				return ;
			}else{
				p--;
				return ;
			}
		}
		dfs(dep+1);
		sum-=i;
	}
}

int main(){
	cin>>n;
	dfs(1);


	return 0;
}