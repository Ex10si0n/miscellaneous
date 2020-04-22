#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<queue>
#define N 10010
using namespace std;

struct node{
  int v,nxt;
}e[200010];

int head[N],num;

void add(int u,int v){
  e[num].v=v;
  e[num].nxt=head[u];
  head[u]=num++;
}

int que[N*10],top,dist[N],vis[N];

bool fk[N];

void spfa(int s,int t){
  memset(vis,0,sizeof(vis));
  memset(dist,0x3f,sizeof(dist));
  que[0]=s;
  dist[s]=0;
  top=1;
  for(int i=0;i<top;i++){
    int u=que[i];
    vis[u]=0;
    for(int j=head[u];j!=-1;j=e[j].nxt){
      int v=e[j].v;
      if(fk[v])continue;
      if(dist[v]>dist[u]+1){
    dist[v]=dist[u]+1;
    if(!vis[v]){
      vis[v]=1;
      que[top++]=v;
    }
      }
    }
  }
}

int main(){
  memset(head,-1,sizeof(head));
  int n,m,a,b,s,t;
  cin>>n>>m;

  while(m--){
    scanf("%d%d",&a,&b);
    add(b,a);
  }

  cin>>s>>t;
  
  spfa(t,s);
  
  for(int i=1;i<=n;i++){
    if(dist[i]==dist[0]){
      for(int j=head[i];j!=-1;j=e[j].nxt){
        fk[e[j].v]=1;
      }
    }
  }
  
  spfa(t,s);
  
  if(dist[s]==dist[0])cout<<-1;
  
  else cout<<dist[s];
  
  return 0; 
}