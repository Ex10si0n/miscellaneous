/*
NOIp - 2014 联合权值
2017/10/29

*/
#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;
#define N 2005

int n,x,y,start,map[N][N],pre[N];//pre存前驱
bool t[N];

struct tree{
	int sum;
	queue<int>son;
}p[N];

void addedge(int a,int b){
	//if(t[a]==0) t[b]=1; else t[b]=0;
	p[a].son.push(b);
	pre[b]++;
}

int main(){
	scanf("%d",&n);
	for(int i=1;i<=n-1;i++){
		scanf("%d%d",&x,&y);
		addedge(x,y);
	}
	for(int i=1;i<=n;i++){
		scanf("%d",p[i].sum);
		if(pre[i]==0){
			start=i;
		}
	}





	return 0;
}


/*

Sample Input
5
1 2
2 3
3 4
4 5
1 5 2 3 10

Sample Output
20 74

*/