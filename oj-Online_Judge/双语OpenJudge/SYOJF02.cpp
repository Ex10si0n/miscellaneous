#include <iostream>
using namespace std;
int n,m,a[105][105];
int main(){
	cin>>n>>m;
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
			cin>>a[i][j];
	for(int j=1;j<=m;j++){
		for(int i=1;i<=n;i++)
			cout<<a[i][j]<<" ";
		cout<<endl;
	}
	return 0;
}