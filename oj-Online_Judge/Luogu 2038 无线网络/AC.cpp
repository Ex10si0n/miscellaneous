#include<iostream>
using namespace std;
int A[150][150];
int main()
{
    int d=0,MAX=0;
    long long n=0,ans=0;
    cin>>d>>n;
    int x=0,y=0,k=0;
    for(int l=1;l<=n;l++)
    {
        cin>>x>>y>>k;
        for(int i=y-d;i<=y+d;i++)
        {
            for(int j=x-d;j<=x+d;j++)
            {
                if(i>=0 && i<=128 && j>=0 && j<=128)
                {
                    A[i][j]+=k;
                    if(A[i][j]>MAX){MAX=A[i][j];}
                }
            }
        }
    }
    for(int i=0;i<=128;i++)
        {
            for(int j=0;j<=128;j++)
            {
                if(A[i][j]==MAX){ans++;}
            }
        }
    cout<<ans<<" "<<MAX;
    return 0;
}