/*
审题：“也就是说我们要按照订单的先后顺序依次为每份订单分配教室。如果在分配的过程中遇到一份订
单无法完全满足，则需要停止教室的分配，通知当前申请人修改订单” 这句话是二分判断的依据，为了
保证操作次数尽可能的少，引进了一个比较强的东西[it]用来维护一段区间内的订单数目。
*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
#define N 1000005
using namespace std;
int n,m,rr[N],d[N],x[N],y[N],seg[N],mid,ans,it;//伪大佬的写法 seg(ement)维护一段天数
bool ok(){
	memset(seg,0,sizeof(seg));it=0;
	for(int i=1;i<=mid;i++){seg[x[i]]+=d[i];seg[y[i]+1]-=d[i];}//用[x,y+1]这段区间的前缀和来更改此时的it
	for(int i=1;i<=n;i++){it+=seg[i];if(it>rr[i]) return 0;}
	return 1;
}
int main(){
	scanf("%d%d",&n,&m);
	for(int i=1;i<=n;i++) scanf("%d",&rr[i]);
	for(int i=1;i<=m;i++) scanf("%d%d%d",&d[i],&x[i],&y[i]);
	int l=1,r=m;//二分判断第mid个订单可不可以
	while(l<=r){
		mid=(l+r)>>1;
		if(ok()) l=mid+1;
		else ans=mid,r=mid-1;
	}
	if(ans==0){//ans没有被更改，即所有ok()均return 1
		cout<<0<<endl;
		return 0;
	}
	cout<<-1<<endl;
	cout<<ans<<endl;
	return 0;
}
