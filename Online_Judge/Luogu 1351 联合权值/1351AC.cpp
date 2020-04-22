#include<cstdio>
#include<vector>
using namespace std;
vector<int>G[200002];
int n,d[200002],ans=0,Max=0;
bool b[200002];
void addedge(int from,int to){
    G[from].push_back(to);
    G[to].push_back(from);
}
void dfs(int u,int fa,int fasfa){
    b[u]=true;
    if(fasfa) ans=(ans+d[u]*d[fasfa]%10007)%10007;
    int sum=0,no1=0,no2=0;
    for(int i=0;i<G[u].size();++i)
    if(!b[G[u][i]]){
        if(d[G[u][i]]>no1)no2=no1,no1=d[G[u][i]];else
        if(d[G[u][i]]>no2)no2=d[G[u][i]];
        ans=(ans+d[G[u][i]]*sum%10007)%10007;
        sum=(sum+d[G[u][i]])%10007;
    }
    if(no1*no2>Max)Max=no1*no2;
    if(d[u]*d[fasfa]>Max)Max=d[u]*d[fasfa];
    for(int i=0;i<G[u].size();++i)
    if(!b[G[u][i]]){
        b[G[u][i]]=true;
        dfs(G[u][i],u,fa);
    }
}
int main(){
    scanf("%d",&n);
    for(int i=1;i<n;++i){
        int x,y;
        scanf("%d%d",&x,&y);
        addedge(x,y);
    }
    for(int i=1;i<=n;++i)scanf("%d",&d[i]);
    dfs(1,0,0);
    printf("%d %d\n",Max,ans*2%10007);
    return 0;
}