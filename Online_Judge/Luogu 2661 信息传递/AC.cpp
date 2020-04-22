#include <iostream>
using namespace std;

int a[200005],ru[200005],tmp,n,ans=99999999;

int main(){
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		scanf("%d",&a[i]);
		ru[a[i]]++;
	}
	for(int i=1;i<=n;i++){
		if(!ru[i]){
			ru[i]=-1;
			for(int j=a[i];--ru[j]==0;j=a[j]){
				ru[j]=-1;
			}
		}
	}
	for(int i=1;i<=n;i++){
		if(ru[i]!=-1){
			tmp=0;
			for(int j=i;j!=i||!tmp;j=a[j]){
				tmp++;
				ru[j]=-1;
			}
			ans=min(ans,tmp);
		}
	}
	printf("%d\n",ans); 
	return 0;
}