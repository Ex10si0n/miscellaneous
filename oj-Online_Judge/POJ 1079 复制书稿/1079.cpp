/*
POJ - 1079 复制书稿  ：要求被分到书稿的最大页数抄写员的页数最小
多组数据，注意init  因为给出的书稿是有序的 所以可以用来二分答案求
答案要求的最值
*/
#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

#define N 505

int T,m,k,a[N],ans;
long long tot,l,r,mid,cnt;

void init(){
	memset(a,0,sizeof(a));
	tot=0;
}

bool ok(){
	int dd=0;cnt=0;
	for(int i=0;i<m;i++){
		if(dd+a[i+1]<mid){
			dd+=a[i+1];
			continue;
		}
		else{
			dd=a[i+1];
			cnt++;
		}
	}
	if(cnt+1>k) return 0;
	return 1;
}

int main(){
	freopen("/Users/Ex10si0n/Desktop/data.in","r",stdin);
	cin>>T;
	while(T--){
		init();
		cin>>m>>k;//m 页数        k 人数
		for(int i=1;i<=m;i++){cin>>a[i];tot+=a[i];}
		l=1,r=tot;
		while(l<=r){
			mid=(l+r)>>1;
			cout<<l<<" "<<mid<<" "<<r<<endl;
			if(ok()) ans=mid,r=mid-1;
			else l=mid+1;

		}
		int dd=0;
		for(int i=0;i<m;i++){
			if(dd+a[i+1]<ans){
				cout<<a[i+1]<<" ";
				dd+=a[i+1];
				continue;
			}
			else{
				dd=a[i+1];
				cout<<"/ "<<a[i+1]<<" ";
			}
		}
		cout<<endl;
	



	}
	return 0;
}