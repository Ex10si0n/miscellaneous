#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

int n;

struct stu{
	int ans;
	char name[50];
	int qm;
	int bj;
	char a;
	char b;
	int lw;
}s[105];

int main(){
	freopen("data.in","r",stdin);
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>s[i].name>>s[i].qm>>s[i].bj>>s[i].a>>s[i].b>>s[i].lw;
		if(s[i].qm>80 && s[i].lw) s[i].ans+=8000;
		if(s[i].qm>85 && s[i].bj>80) s[i].ans+=4000;
		if(s[i].qm>90) s[i].ans+=2000;
		if(s[i].qm>85 && s[i].b=='Y') s[i].ans+=1000;
		if(s[i].bj>80 && s[i].a=='Y') s[i].ans+=850;
	}
	int r=-1,flag=1;
	long long sum=0;
	for(int i=1;i<=n;i++){
		if(s[i].ans>r){
			flag=i;
			r=s[i].ans;
		}
		sum+=s[i].ans;
	}
	cout<<s[flag].name<<endl;
	cout<<r<<endl;
	cout<<sum<<endl;
	return 0;
}