#include <iostream>
#include <stack>
using namespace std;

struct words{
	char p;
	char word[1005];
}w[10005];

string s;

int main(){
	getline(cin,s);
	int pos=0,num=0,q,i=0;
	while(i<=s.length()){
		if(s[i]==']' || s[i]=='['){
			++num;q=0;pos=i;
			w[num].p=s[i];
			for(int j=pos+1;j<=s.length();j++)
				if(s[j]==']' || s[j]=='['){i=j;break;}
			for(int j=pos+1;j<=i;j++){
				w[num].word[++q]=s[j];
			}
		}
		i++;
	}
	for(int i=1;i<=num;i++){
		cout<<w[i].p<<endl;
		for(int i=1;i<=w[])
	}
	return 0;
}