#include <iostream>
#include <cstdio>
#include <cstring>
#include <termios.h>
#include <unistd.h>

#define size_x 
#define size_y 

using namespace std;

int map[105][105];
int s;
int dx[8]={0,-1,-1,-1,0,1,1,1};
int dy[8]={-1,-1,0,1,1,1,0,-1};

int getc() {
	struct termios oldt,newt;
	int ch;
	tcgetattr( STDIN_FILENO, &oldt );
	newt = oldt;
	newt.c_lflag &= ~( ICANON | ECHO );
	tcsetattr( STDIN_FILENO, TCSANOW, &newt );
	ch = getchar();
	tcsetattr( STDIN_FILENO, TCSANOW, &oldt );
	return ch;
}

void p(){
	for(int i=0;i<=s;i++){
		for(int j=0;j<=s;j++){
			if(map[i][j]==0) cout<<"  ";
			else printf("%-2d",map[i][j]);
		}
		cout<<endl;
	}
}

void init(){
	cout<<"================================Game Of Life===================================="<<endl;
	cout<<"|       Developed by @Ex10si0n      ----          Build Version 1.0            |"<<endl;
	cout<<"|  How to play ?  Visit https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life  |"<<endl;
	cout<<"================================================================================"<<endl;
	cout<<endl;
	cout<<"Please enter the size of the playground (default size is 25): ";
	cin>>s;
	system("clear");
	for(int i=0;i<=s;i++){
		map[0][i]=i;
		map[i][0]=i;
	}
	p();
	cout<<"Please enter the plot (x,y) of cell (input 0 means start): ";
	while(1){
		int x,y;
		cin>>x;
		if(x==0) return;
		cin>>y;
		map[x][y]=1;
		system("clear");
		p();
		cout<<"Please enter the plot (x,y) of cell (input 0 means start): ";
	}
	for(int i=0;i<=s;i++){
			map[0][i]=0;
			map[i][0]=0;
	}
}

void go(){
	int cnt=0;
	for(int i=1;i<=s;i++){
		for(int j=1;j<=s;j++){
			cnt=0;
			for(int k=0;k<8;k++){
				if(map[i+dx[k]][j+dy[k]]==1) cnt++;
			}
			if(map[i][j]==1){
				if(cnt<2){map[i][j]=0;continue;}
				if(cnt==2 || cnt==3){map[i][j]=1;continue;}
				if(cnt>3){map[i][j]=0;continue;}
			}
			if(map[i][j]==0){
				if(cnt==3){map[i][j]=1;continue;}
			}
		}
	}
}

int main(){
	system("clear");
	init();
	while(1){
		go();
		p();
		system("sleep 0.01");
		system("clear");
	}

	return 0;
}



/*

2 4
5 7
3 6
5 7
8 6
4 5
3 5
1 6
7 5
8 9
10 5
5 10
2 5
6 7
3 4
6 5
2 7
2 6
4 8
4 9
9 4
5 7
7 6
5 3
3 7
7 8
8 9
9 4
12 11
13 24
5 14
5 15
5 16
4 15
4 16
4 17
6 2



*/