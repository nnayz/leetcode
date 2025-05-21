class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        \\\
        Do not return anything, modify matrix in-place instead.
        \\\
        mp = {}
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    mp[i, \r\] = True
                    mp[j, \c\] = True
        
        for i in range(rows):
            for j in range(columns):
                if (i, \r\) in mp or (j, \c\) in mp:
                    matrix[i][j] = 0
            