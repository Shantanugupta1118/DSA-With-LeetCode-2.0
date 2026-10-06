class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        mat = [[0] * rows for _ in range(cols)]

        for i in range(cols):
            for j in range(rows):
                mat[i][j] = matrix[j][i]
        return mat