class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        totalSum = 0
        row, col = 0, len(mat)-1
        length_n = len(mat)

        while row < length_n:
            totalSum = totalSum + mat[row][row] + mat[row][col]
            row += 1
            col -= 1
        
        if length_n%2 != 0:
            mid = length_n // 2
            totalSum -= mat[mid][mid]
        
        return totalSum
        