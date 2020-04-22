#include <iostream>
#include <cmath>
using namespace std;

int n,k,a[25],ans;

bool isp(int x){
	for(int i=2;i<=sqrt(x);i++)
		if(x%i==0) return 0;
	return 1;
}

void dfs(int dep,int sum,int pos){
	if(dep==k){
		if(isp(sum)) ans++;
		return ;
	}
	for(int i=pos;i<=n;i++) dfs(dep+1,sum+a[i],i+1);//可以剪掉自己和自己前面重复的数字
}

int main(){
	cin>>n>>k;
	for(int i=1;i<=n;i++) cin>>a[i];
	dfs(0,0,1);
	cout<<ans<<endl;
	return 0;
}