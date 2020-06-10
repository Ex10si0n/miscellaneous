#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn = 1005;
vector<int>f[maxn],depth[maxn];
int fa[maxn],vis[maxn],flag[maxn];
int n,s,k;
void build(int rt,int d)
{
    vis[rt] = 1;
    int len = f[rt].size();
    if(len==1 && d>k)depth[d].push_back(rt);
    for(int i = 0;i<len;++i)
    {
        int u = f[rt][i];
        if(vis[u])continue;
        fa[u] = rt;
        build(u,d+1);
    }
}
void dfs(int rt,int d)
{
    vis[rt] = 1;
    int len = f[rt].size();
    if(len==1 && d<=k){flag[rt]=1;return;}
    for(int i = 0;i<len;++i)
    {
        int u = f[rt][i];
        if(!vis[u])dfs(u,d+1);
    }
}
int main()
{
//    freopen("in.txt","r",stdin);
    int T;scanf("%d",&T);
    while(T--)
    {
        memset(f,0,sizeof(f));
        memset(vis,0,sizeof(vis));
        memset(flag,0,sizeof(flag));
        memset(depth,0,sizeof(depth));
        scanf("%d%d%d",&n,&s,&k);
        for(int i = 1;i<n;++i)
        {
            int u,v;scanf("%d%d",&u,&v);
            f[u].push_back(v);
            f[v].push_back(u);
        }
        build(s,0);
        int ans = 0;
        for(int i = n;i>k;--i)
        {
            int len = depth[i].size();
            for(int j = 0;j<len;++j)
            {
                int u = depth[i][j];
                if(flag[u])continue;
                memset(vis,0,sizeof(vis));
                for(int i = 0;i<k;++i)u = fa[u];
                dfs(u,0);
                ans++;
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}