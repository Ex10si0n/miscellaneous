#include<cstdio>
#include<cstring>
#define maxn 200001
using namespace std;
int find(int x);
bool uni(int x,int y);
int pre[maxn],father[maxn],t[maxn],n,ans=0x7fffffff,temp;
int main()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&t[i]);
        father[i]=pre[i]=i;
    }
    for(int i=1;i<=n;i++)
        if(!uni(i,t[i]))
        {
            temp=1;
            for(int j=t[i];j!=i;j=pre[j])
                temp++;
            ans=temp<ans? temp:ans;
        }
    printf("%d\n",ans);
    return 0;
}
int find(int x)
{
    int pos=x,i=x,temp;
    while(father[pos]!=pos)
        pos=father[pos];
    while(father[i]!=pos)
    {
        temp=father[i];
        father[i]=pos;
        i=temp;
    }
    return pos;
}
bool uni(int x,int y)
{
    int rx=find(x),ry=find(y);
    if(rx==ry)
        return false;
    else
    {
        pre[x]=y;    //pre[]是不压缩的并查集数组
        father[x]=ry;    //father[]是路径压缩的并查集数组
        return true;
    }
}