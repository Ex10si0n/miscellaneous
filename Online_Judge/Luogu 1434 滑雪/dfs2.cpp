#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
struct minx{//结构体定义
    int xx,yy;
    int number;
}f[105*105];
int cmp(const minx &a,const minx &b){//结构体快排
    return a.number<b.number;
}
int a[105][105];//第一个输入，第二个赋值
int b[105][105];
int n,m;
int dfs(int x,int y){//dfs大法好
    b[x][y]++;
    if(a[x-1][y]<a[x][y]&&x-1>0){
        if(b[x-1][y]!=0){
            b[x][y]=fmax(b[x][y],b[x-1][y]+1);
        }else{
            dfs(x-1,y);
        }
    }if(a[x+1][y]<a[x][y]&&x+1<=n){
        if(b[x+1][y]!=0){
            b[x][y]=fmax(b[x][y],b[x+1][y]+1);
        }else{
            dfs(x+1,y);
        }
    }if(a[x][y+1]<a[x][y]&&y+1<=m){
        if(b[x][y+1]!=0){
            b[x][y]=fmax(b[x][y],b[x][y+1]+1);
        }else{
            dfs(x,y+1);
        }
    }if(a[x][y-1]<a[x][y]&&y-1>0){
        if(b[x][y-1]!=0){
            b[x][y]=fmax(b[x][y],b[x][y-1]+1);
        }else{
            dfs(x,y-1);
        }
    }
}
int main(){
    scanf("%d%d",&n,&m);
    int t=1;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            scanf("%d",&a[i][j]);
            f[t].xx=i;
            f[t].yy=j;
            f[t].number=a[i][j];
            t++;
        }
    }
    //读入之后，快排入x,y，然后从最小开始dfs吧
    sort(f+1,f+n*m+1,cmp);
    for(int i=1;i<=n*m;i++){
            dfs(f[i].xx,f[i].yy);
    }
    int maxn=-1;//找最大
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            if(b[i][j]>maxn){
                maxn=b[i][j];
            }
        }
    }
    printf("%d",maxn);
    return 0;
}