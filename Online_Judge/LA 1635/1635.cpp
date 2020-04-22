#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#define N 100005
using namespace std;

int line[N],n,m,cnt,fac[100005][2],a[100005],c[100005],num;

void factor(){
	for(int i=2;i*i<=m;i++){
		if(m%i==0){
			fac[++num][0]=i;
			fac[num][1]=0;
			do{
				fac[num][1]++;
				m/=i;
			}while(m%i==0);
		}
	}
	if(m>1){
		fac[++num][0]=m;
		fac[num][1]=1;
	}
}

bool check(int n,int i){
	int x=n-i;
	int y=i;
	for(int i=1;i<=num;i++){
		int p=fac[i][0];
		while(x%p==0){
			x/=p;
			c[i]++;
		}
		while(y%p==0){
			y/=p;
			c[i]--;
		}
	}
	for(int i=1;i<=num;i++){
		if(c[i]<fac[i][1])
			return 0;
		return 1;
	}
}

int main(){
	while(cin>>n>>m){
		num=cnt=0;
		factor();
		memset(c,0,sizeof(0));
		for(int i=1;i<n-1;i++){
			if(check(n,i))
				a[cnt++]=i+1;
		}
		cout<<cnt<<endl;
		for(int i=0;i<cnt;i++){
			cout<<a[i]<<" ";
		}
		
	}
	return 0;
}



/*

comb[0][0]=comb[1][0]=comb[1][1]=1;
for(int i=1;i<=k;i++) comb[i][0]=1;
for(int i=2;i<=k;i++){
	for(int j=1;j<=i;j++){
		comb[i][j]=((comb[i-1][j-1]%10007)+(comb[i-1][j]%10007))%10007;
	}
}


void work(){
	line[0]=line[1]=1;
	for(int x=1;x<=n;x++){
		line[x]=line[x-1]*(n-x+1)/x;
	}
}


*/