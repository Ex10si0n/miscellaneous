/*
NOIp - 2014 联合权值
2017/10/29
*/
#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;
#define N 2005
#define mod 10007

int n,w[N],tot,head[N],nextt[N*2],to[N*2],sum;
int max1,max2,ans1,ans2;

void addedge(int a,int b){
	to[++tot]=b;  
	nextt[tot]=head[a];
	head[a]=tot;
}

int main(){
	scanf("%d",&n);

	for(int i=1;i<=n-1;i++){
		int x,y;
		scanf("%d%d",&x,&y);
		addedge(x,y);
		addedge(y,x);
	}

	for(int i=1;i<=n;i++){
		scanf("%d",&w[i]);
	}

	for(int i=1;i<=n;i++){
		max1=max2=-1; //max1 max2 最大 次大
		sum=0;
		for(int j=head[i];j;j=nextt[j]){
			int temp=w[to[j]];
			sum+=temp;//sum所有儿子的联合权值之和
			sum%=mod;
			if(temp>max1){
				max2=max1;
				max1=temp;
			}
			else if(temp>max2)
				max2=temp;
		}
		ans2=max(ans2,max1*max2);
		for(int j=head[i];j;j=nextt[j]){
			ans1+=(w[to[j]]*(sum-w[to[j]]))%mod;
			ans1%=mod;
		}
	}

	ans1=(ans1+mod)%mod;
	cout<<ans2<<" "<<ans1<<endl;
	return 0;
}


/*

Sample Input
5
1 2
2 3
3 4
4 5
1 5 2 3 10

Sample Output
20 74

*/