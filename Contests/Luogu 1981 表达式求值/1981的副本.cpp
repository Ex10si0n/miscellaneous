#include <iostream>
using namespace std;

string exp;

int main(){
	cin>>exp;
	for(int i=0;i<exp.size();i++) cout<<exp[i];
	int flag=0;
	for(int i=0;i<exp.size();i++){
		if(exp[i]=='+'){
			flag=i+1;
			for(int j=flag;j<=i;j++)cout<<exp[i];
			cout<<" ";
		}
		
	}

	return 0;
}