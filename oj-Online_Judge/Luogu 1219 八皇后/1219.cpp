#include <iostream>

using namespace std;

int num,sum,x[20];

bool place(int k)
{
    for(int j = 1;j<k;j++)
        if(abs(x[k] - x[j]) == abs(k-j)||x[j] == x[k])
            return false;
        return true;
}

void backtrack(int t)
{
    if(t>num)
    {
        sum++;
        if(sum<=3){for(int m = 1;m<=num;m++) cout<<x[m]<<" ";cout<<endl;}
        
    }
    else for(int i = 1;i<=num;i++)
         {
            x[t] = i;
            if(place(t)) backtrack(t+1);
         }
}

int main(){
	cin>>num;
	backtrack(1);
	cout<<sum<<endl;

}