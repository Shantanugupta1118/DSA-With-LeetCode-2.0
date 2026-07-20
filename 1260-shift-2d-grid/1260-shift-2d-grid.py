class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        k %= total_elements
        if k == 0:
            return grid
        def reverse_virtual_1d(left: int, right: int):
            while left < right:
                r1, c1 = left // n, left % n
                r2, c2 = right // n, right % n
                
                grid[r1][c1], grid[r2][c2] = grid[r2][c2], grid[r1][c1]
                
                left += 1
                right -= 1
        reverse_virtual_1d(0, total_elements - 1)        
        reverse_virtual_1d(0, k - 1)
        reverse_virtual_1d(k, total_elements - 1)
        
        return grid
