#include<iostream>
#include<cstdio>
#define fo(i,j,k) for(i=j;i<=k;i++) 
using namespace std;
int a[200001],ru[200001],n,ans=1e8;
int main()
{
    int i,j,k,tmp;
    scanf("%d",&n);
    fo(i,1,n)
    {
        scanf("%d",&a[i]);
        ru[a[i]]++;
    }
    fo(i,1,n)
      if(!ru[i])
      {
        ru[i]=-1;
        for(j=a[i];--ru[j]==0;j=a[j])
          ru[j]=-1;    //排除不成环的点 
      }
    fo(i,1,n)   //跑一编回路并统计长度 
      if(ru[i]!=-1)
      {
        tmp=0;
        for(j=i;j!=i || !tmp;j=a[j])
          tmp++,ru[j]=-1;   //跑过的点标记 
        ans=min(ans,tmp); 
      }
    printf("%d\n",ans); 
    return 0;
}