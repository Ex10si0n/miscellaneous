'''
Algorithms Tags: Greedy
Effeciency: Good 98/24

Descendent values of dict d to filter by the given d values
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        # Input is guaranteed to be within the range from 1 to 3999.

        d = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),(40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        ans = ''
        for i in d:
            k = num//i[0]
            if k:
                # print(t, i, d[i])
                num -= k * i[0]
                ans += i[1]*k
                # print(ans)
        return ans
