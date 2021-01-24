#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
long long a, b, c, d;
int A[45005], B[45005], C[45005], D[45005];// a b c d 对应的质因数分解
int prime[100001], size;
bool notPrime[100001];
int analyse (int * map, long long num) { // 将 num 进行质因数分解
    for (int i = 1; i <= size && num > 1; i++) { // 使用 45000 以内的质数对其进行分解
        while (num % prime[i] == 0) {
            map[i]++;
            num /= prime[i];
        }
    }
    if (num > 1) { // 如果剩余的数大于 1 ，那么这个数也一定是一个质数
        prime[++size] = num;
        map[size] = 1;
        return 1;
    }
    return 0;
} 
void init() { // 预处理出 45000 以内的所有质数
    for (int i = 2; i <= 50000; i++) {
        if (!notPrime[i])
            prime[++size] = i;
        for (int j = 1; j <= size && prime[j] * i <= 50000; j++) {
            notPrime[prime[j] * i] = true;
            if (i % prime[j] == 0)
                break;
        }
    }
}
void solve() {
    int tot = 0;
    scanf("%lld%lld%lld%lld", &a, &b, &c, &d);
    if(b > a || d < c)  {
        printf("0\n");
        return;
    }
    long long ans = 1;
    memset(A, 0, sizeof(A));
    memset(B, 0, sizeof(B));
    memset(C, 0, sizeof(C));
    memset(D, 0, sizeof(D));
    //将a b c d 分别进行质因数分解，并统计新添加的质数的个数
    tot += analyse(B, b);
    tot += analyse(A, a);
    tot += analyse(C, c);
    tot += analyse(D, d);
    for (int i = 1; i <= size; i++) {
        bool flag = false;
        if (D[i] == C[i] && A[i] == B[i])
            ans *= (D[i] - B[i] + 1);
        if (A[i] != B[i])//若A[i] != B[i] 那么结果的第i位一定与B[i]
            if (D[i] != C[i]) // 判断是否可以取到 B[i]
                flag = D[i] != B[i];
            if (D[i] == C[i])
                flag = B[i] > D[i];
        if (C[i] != D[i])//若C[i] != D[i] 那么结果的第 i 位一定与D[i] 相等
            if (A[i] != B[i])
                flag = D[i] != B[i];
            if (A[i] == B[i])
                flag = D[i] < B[i];
        if (flag) { //判断此组数据是否有解
            printf("0\n");
            return;
        }
    }
    printf("%lld\n", ans);
    size -= tot;//将预先处理处的大质数移去
}
int main() {
    //freopen("in.txt", "r", stdin);
   // freopen("out.txt", "w", stdout);
    init(); //预处理 45000 以内的所有质数
    int n;
    scanf("%d", &n);
    while (n--)
        solve();
    return 0;
}