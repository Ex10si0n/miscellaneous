/*
rqnoj 73 24点
如果能凑出24输出yes，否则no：input A 2 3 4  output yes
深搜题，见代码
*/
#include <iostream>
#include <cstring>
using namespace std;

string c;
int a[5];
bool vis[5];

bool dfs(int dep,double amount){
	if(dep==4){
		if(23.999999<amount&&amount<24.000001) return 1;
		else return 0;
	}
	for(int i=1;i<=4;i++){
		if(!vis[i]){
			vis[i]=1;
			if(dfs(dep+1,amount+a[i])) return 1;
			if(dfs(dep+1,amount-a[i])) return 1;
			if(dfs(dep+1,a[i]-amount)) return 1;
			if(amount!=0 && dfs(dep+1,amount*a[i])) return 1;
			if(amount!=0 && dfs(dep+1,amount/a[i])) return 1;
			if(amount!=0 && dfs(dep+1,a[i]/amount)) return 1;
			vis[i]=0;
		}
	}
	return 0;
}

int main(){
	for(int i=1;i<=4;i++){
		cin>>c;
		if(c[0]=='A'){a[i]=1;continue;}
		if(c[0]=='J'){a[i]=11;continue;}
		if(c[0]=='Q'){a[i]=12;continue;}
		if(c[0]=='K'){a[i]=13;continue;}
		if(c[0]=='1' && c[1]=='0'){a[i]=10;continue;}
		a[i]=c[0]-'0';
	}
	//debug: for(int i=1;i<=4;i++) cout<<a[i]<<" ";
	if(dfs(0,0)) cout<<"yes"<<endl;
	else cout<<"no"<<endl;
	return 0;
}