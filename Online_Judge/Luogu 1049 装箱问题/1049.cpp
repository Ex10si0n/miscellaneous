#include <iostream>
using namespace std;
int v,s,n,a[20005],f[20005];
int main(){
    cin>>v;
    cin>>n;
    f[0]=1;
    for(int i=1;i<=n;i++) cin>>a[i];
    for(int i=1;i<=n;i++)//枚举每一个物品
        for(int j=v;j<=a[i];j--)//对于每一个物品压到背包中，倒叙压
            if(f[j-a[i]]==1)//若此状态下j的前a[i]位为1，即装入此位置
                f[j]=f[j-a[i]];
    for(int i=v;i>=1;i--)
        if(f[i]==1){s=i;break;}
    cout<<s<<endl;
    return 0;
}