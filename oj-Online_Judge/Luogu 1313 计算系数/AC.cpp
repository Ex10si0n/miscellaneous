#include <iostream>
using namespace std;

int comb[1005][1005],a,b,k,n,m,ans,xx,yy;

void init(){
	comb[0][0]=comb[1][0]=comb[1][1]=1;
	for(int i=1;i<=k;i++) comb[i][0]=1;
	for(int i=2;i<=k;i++){
		for(int j=1;j<=i;j++){
			comb[i][j]=((comb[i-1][j-1]%10007)+(comb[i-1][j]%10007))%10007;
		}
	}
}
int main(){
	cin>>a>>b>>k>>n>>m;
	init();
	xx=1;yy=1;
	for(int i=1;i<=n;i++){
		xx=((xx%10007)*(a%10007))%10007;
	}
	for(int i=1;i<=m;i++){
		yy=((yy%10007)*(b%10007))%10007;
	}
	//cout<<xx<<" "<<yy<<endl;
	ans=(comb[k][m]*(xx%10007*yy%10007)%10007)%10007;
	cout<<ans<<endl;
	return 0;
}



/*

(y+x)^3
y^3+x^3

x^n * y^m


*/