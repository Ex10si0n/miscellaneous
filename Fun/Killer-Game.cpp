#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;
struct player{
	int job;
	string name;
}p[10];
int police,doctor,limitor,killer,spector;
int needle[15],roll[10]={0,1,2,3,4,5},lg,lb;
bool alive[15]={0,1,1,1,1,1},limited[15];
int tg[10][10];
void randomization(){
	lg=3,lb=2;
	string name; int t;
	srand((unsigned)time(0));
	for(int i=1;i<=rand();i++) 
		next_permutation(roll+1,roll+6);
	for(int i=1;i<=5;i++){	
		cout<<"输入玩家名字："; cin>>name;
		cout<<"玩家编号："<<i<<endl;
		cout<<"职业：";
		p[i].job=roll[i];
		p[i].name=name;
		if(roll[i]==1){
			police=i;
			cout<<"警察\n"<<endl;
			cout<<"每一回合可以验证一位玩家的身份\n可以得到此角色的阵营\n但是验证无间道为好人(实际为坏人)\n限制者为坏人(实际为好人)"<<endl;		
		}
		if(roll[i]==2){
			doctor=i;
			cout<<"医生\n"<<endl;
			cout<<"每一回合可以给一位玩家打针\n针会挂载于玩家身上\n一根针可以挡杀手或无间道的一刀 且该玩家身上的针数字归零\n连续挂载两针的玩家死亡"<<endl;		
		}
		if(roll[i]==3){
			limitor=i;
			cout<<"限制者\n"<<endl;
			cout<<"每一回合可以限制一位玩家的行动"<<endl;		
		}
		if(roll[i]==4){
			killer=i;
			cout<<"杀手\n"<<endl;
			cout<<"每一回合可以杀掉一位玩家\n但是你不知道无间道的身份"<<endl;		
		}
		if(roll[i]==5){
			spector=i;
			cout<<"无间道\n"<<endl;
			cout<<"每一回合可以杀掉一位玩家\n但是你不知道杀手的身份"<<endl;		
		}
		cout<<"\n\n\n\n\n\n\n\n\n\n输入任意字符按Enter完成阅读"<<endl;
		string tt;
		cin>>tt;
		system("clear");
	}
}

int main(int argc, char const *argv[]){
	system("clear");
	cout<<"==欢迎来到杀人牌(Terminal Edition)==\nstart game for at least 5 players\nver beta 1.0\nby Ex10si0n Yan\nGithub: https://github.com/ex10si0n\n\n\n\n\n\n输入任意字符按Enter完成阅读"<<endl;
	string bin;
	cin>>bin;
	system("clear");
	randomization();
	int k=0;
	while(true){
		k++;
		
		if(lg==0 && lb==0){
			system("clear");
			cout<<"游戏结果：平局"<<endl;
			break;
		}
		if(lb==0){
			system("clear");
			cout<<"游戏结果：好人阵营胜利"<<endl;
			break;
		}
		if(lg==0){
			system("clear");
			cout<<"游戏结果：坏人阵营胜利"<<endl;
			break;
		}
		system("clear");

		int target;
		memset(limited,0,sizeof(limited));
		if(alive[limitor]){
			cout<<"限制者行动\n选择目标："<<endl;
			for(int i=1;i<=5;i++){
				cout<<i<<". "<<p[i].name<<endl;
			}
			cin>>target;
			tg[3][k]=target;
			limited[p[target].job]=1;
			system("clear");
		}else{
			cout<<"限制者出局"<<endl;
			cout<<"\n\n\n\n\n\n\n\n\n\n输入任意字符按Enter完成阅读"<<endl;
			string tt;
			cin>>tt;
			system("clear");
		}

		if(alive[police]){

			cout<<"警察行动\n选择目标："<<endl;
			for(int i=1;i<=5;i++){
				cout<<i<<". "<<p[i].name<<endl;
			}
			cin>>target;
			tg[1][k]=target;
			if(limited[1]==1){
				target=0;
			}
			cout<<"他的身份为：";
			if(target==0){
				cout<<"无效"<<endl;
			}
			if(p[target].job==1){
				cout<<"Good Guy";
			}
			if(p[target].job==2){
				cout<<"Good Guy";
			}
			if(p[target].job==3){
				cout<<"Bad Guy";
			}
			if(p[target].job==4){
				cout<<"Bad Guy";
			}
			if(p[target].job==5){
				cout<<"Good Guy";
			}
			limited[1]=0;
			cout<<"\n\n\n\n\n\n\n\n\n\n输入任意字符按Enter完成阅读"<<endl;
			string tt;
			cin>>tt;
			system("clear");
		}else{
			cout<<"警察出局"<<endl;
			cout<<"\n\n\n\n\n\n\n\n\n\n输入任意字符按Enter完成阅读"<<endl;
			string tt;
			cin>>tt;
			system("clear");
		}

		if(alive[doctor]){
			cout<<"医生行动\n选择目标："<<endl;
			for(int i=1;i<=5;i++){
				cout<<i<<". "<<p[i].name<<endl;
			}
			cin>>target;
			tg[2][k]=target;
			if(limited[2]==1){
				target=0;
			}
			needle[target]++;
			if(needle[target]>=2){
				alive[target]=0;
				if(p[target].job>=4){
					lb--;
				}
				else if(p[target].job>0){
					lg--;
				}
			}
			limited[2]=0;
			system("clear");		
		}else{
			cout<<"医生出局"<<endl;
			cout<<"\n\n\n\n\n\n\n\n\n\n输入任意字符按Enter完成阅读"<<endl;
			string tt;
			cin>>tt;
			system("clear");
		}

		if(alive[killer]){
			cout<<"杀手行动\n选择目标："<<endl;
			for(int i=1;i<=5;i++){
				cout<<i<<". "<<p[i].name<<endl;
			}
			cin>>target;
			tg[4][k]=target;
			if(limited[4]==1){
				target=0;
			}
			if(needle[target]){
				needle[target]=0;
			}else{
				alive[target]=0;
				if(p[target].job>=4){
					lb--;
				}
				else if(p[target].job>0){
					lg--;
				}
			}
			limited[4]=0;
			system("clear");
		}else{
			cout<<"杀手出局"<<endl;
			cout<<"\n\n\n\n\n\n\n\n\n\n输入任意字符按Enter完成阅读"<<endl;
			string tt;
			cin>>tt;
			system("clear");
		}

		if(alive[spector]){
			cout<<"无间道行动\n选择目标："<<endl;
			for(int i=1;i<=5;i++){
				cout<<i<<". "<<p[i].name<<endl;
			}
			cin>>target;
			tg[5][k]=target;
			if(limited[5]==1){
				target=0;
			}
			if(needle[target]){
				needle[target]=0;
			}else{
				alive[target]=0;
				if(p[target].job>=4){
					lb--;
				}
				else if(p[target].job>0){
					lg--;
				}
			}
			limited[5]=0;
			system("clear");
		}else{
			cout<<"无间道出局"<<endl;
			cout<<"\n\n\n\n\n\n\n\n\n\n输入任意字符按Enter完成阅读"<<endl;
			string tt;
			cin>>tt;
			system("clear");
		}


			cout<<"今晚结果："<<endl;
			for(int i=1;i<=5;i++){
				cout<<i<<". "<<p[i].name;
				if(alive[i]==0) cout<<"  OUT"<<endl;
				else cout<<endl;
			}
			cout<<"\n请指认投票："<<endl;
			cin>>target;
			alive[target]=0;
			if(p[target].job>=4) lb--;
			else lg--;

			system("clear");



	}
	cout<<endl;

	cout<<"警察:"<<p[police].name<<" ";
	cout<<"医生:"<<p[doctor].name<<" ";
	cout<<"限制:"<<p[limitor].name<<" ";
	cout<<"杀手:"<<p[killer].name<<" ";
	cout<<"无间:"<<p[spector].name<<" ";
	cout<<endl;
	
	cout<<"角色   第一天   第二天   第三天   第四天   第五天   第六天   第七天\n";
	for(int i=1;i<=5;i++){
		if(i==1) cout<<"警察:  ";
		if(i==2) cout<<"医生:  ";
		if(i==3) cout<<"限制:  ";
		if(i==4) cout<<"杀手:  ";
		if(i==5) cout<<"无间:  ";
		p[0].name="nul";
		for(int j=1;j<=7;j++){
			cout<<tg[i][j]<<"."<<p[tg[i][j]].name<<"    ";
		}
		cout<<endl;
	}
	return 0;
}


