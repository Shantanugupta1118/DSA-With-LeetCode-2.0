class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sum_left = sum_right = 0
        q_left = q_right = 0
        
        for i in range(half):
            if num[i] == '?':
                q_left += 1
            else:
                sum_left += int(num[i])
                
        for i in range(half, n):
            if num[i] == '?':
                q_right += 1
            else:
                sum_right += int(num[i])
                
        sum_diff = sum_left - sum_right
        q_diff = q_left - q_right
        
        if q_diff % 2 != 0:
            return True
        
        return sum_diff + (q_diff // 2) * 9 != 0