/*
二分mid作为最多能组成的牌的数目，接下来就是判断。我们可以看成将牌全部摆在桌子上，然后拿
Joker补全空隙，但是需要注意的是，这个是贪心思想，需要证明正确性，因为要求每套牌只能拿一
个Joker代替，x是这些扑克牌最大套数，m是Joker数量，m可以局限最大套数，因为每一套必须小
于等于m，所以用 min(m,x) 来限制套数，如果用m将扑克牌搭出了x套的条件满足，则必然可以证
明贪心的正确性。
*/
#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int n,m,a[60],l,r,mid,ans;

bool ok(int x){
	int k=min(m,x);//k为需要的Joker数量，并且每套最多1个Joker。
	for(int i=1;i<=n;i++){
		if(a[i]<x) k-=(x-a[i]);//Joker数量减去对于第i个牌要想搭成x套牌需要的Joker数
		if(k<0) return 0;
	}
	return 1;
}

int main(){
	cin>>n>>m;
	for(int i=1;i<=n;i++) cin>>a[i];
	int l=1;r=600000000;
	while(l<=r){
		mid=(l+r)>>1;
		if(ok(mid)) ans=mid,l=mid+1;//第一次写的l=mid 结果二分跑炸了
		else r=mid-1;
	}
	cout<<ans<<endl;
	return 0;
}