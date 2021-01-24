'''
Algorithms Tags: None
Effeciency: Normal

Sad about I don't know the pythonic code
'''
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min = []
        nu = []
        for col in range(len(matrix)):
            _min = 100001
            where = 0
            for row in range(len(matrix[col])):
                if _min > matrix[col][row]:
                    _min = matrix[col][row]
                    where = row
            row_min.append(_min)
            nu.append(where)
        _max = 0
        col_max = []
        for j in range(len(matrix[0])):
            _max = 0
            for i in range(len(nu)):
                _max = max(_max, matrix[i][j])
            col_max.append(_max)
        ans = []
        for i in col_max:
            if i in row_min:
                ans.append(i)
        return ans
