#include <iostream>
#include <stack>
#include <sstream>
using namespace std;

const int MOD = 10000;
stack <int> s;//定义一个栈

int main()
{
    int d,ans = 0;
    char c = ' ';
    string str;
    cin >> str;//读入
    stringstream ss;
    ss << str;
    while (true)
        {
            ss >> d;//截取数字，显然，表达式的第一位必定是数字
            if (c == '*')//若读入的c为称号
                {
                    d = d  % MOD * s.top();//将之前读入数字与栈顶数字相乘
                    s.pop();//将栈顶元素弹出
                }
            s.push(d);//将成绩
            if (!(ss >> c)) break;
        }
    while (!s.empty())//累加栈内元素
        {
            ans = (ans + s.top()) % MOD;
            s.pop();
        }
    cout << ans;//输出结果
    return 0;
}