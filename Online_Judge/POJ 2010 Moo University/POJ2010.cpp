#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int n,c,f;

struct cow{
	int s;
	int v;
}a[100005];

bool cmp_of_mark(cow a,cow b) {return a.s>b.s;}
//bool cmp_of_money()

int main(){
	cin>>n>>c>>f;
	for(int i=1;i<=c;i++){
		cin>>a[i].s>>a[i].v;
	}
	sort(a+1,a+1+c,cmp_of_mark);





	return 0;
}