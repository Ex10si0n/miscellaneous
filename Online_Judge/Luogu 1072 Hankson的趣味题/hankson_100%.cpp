#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#define N 1000005

using namespace std;

int n,a0,a1,b0,b1,numa0,numa1,numb0,numb1;
int aa0[N][2],aa1[N][2],bb0[N][2],bb1[N][2];//fac表

void factorb1(){
	numb1=0;
	for(int i=2;i*i<=b1;i++){
		if(b1%i==0){
			bb1[++numb1][0]=i;
			bb1[numb1][1]=0;
			do{
				bb1[numb1][1]++;
				b1/=i;
			}while(b1%i==0);
		}
	}
	if(b1>1){
		bb1[++numb1][0]=b1;
		bb1[numb1][1]=1;
	}
}

void factorb0(){
	numb0=0;
	for(int i=2;i*i<=b0;i++){
		if(b0%i==0){
			bb0[++numb0][0]=i;
			bb0[numb0][1]=0;
			do{
				bb0[numb0][1]++;
				b0/=i;
			}while(b0%i==0);
		}
	}
	if(b0>1){
		bb0[++numb0][0]=b0;
		bb0[numb0][1]=1;
	}
}

void factora1(){
	numa1=0;
	for(int i=2;i*i<=a1;i++){
		if(a1%i==0){
			aa1[++numa1][0]=i;
			aa1[numa1][1]=0;
			do{
				aa1[numa1][1]++;
				a1/=i;
			}while(a1%i==0);
		}
	}
	if(a1>1){
		aa1[++numa1][0]=a1;
		aa1[numa1][1]=1;
	}
}

void factora0(){
	numa0=0;
	for(int i=2;i*i<=a0;i++){
		if(a0%i==0){
			aa0[++numa0][0]=i;
			aa0[numa0][1]=0;
			do{
				aa0[numa0][1]++;
				a0/=i;
			}while(a0%i==0);
		}
	}
	if(a0>1){
		aa0[++numa0][0]=a0;
		aa0[numa0][1]=1;
	}
}
//反正没有码长限制 可劲霍霍...

int main(){
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>a0>>a1>>b0>>b1;
		factora1();
		factora0();
		factorb1();
		factorb0();
		for(int i=1;i<=numa0;i++){
			cout<<aa0[i][0]<<" ";
		}



	}
	
	return 0;
}