class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        inf = float('inf')
        min_len = [inf] * n
        
        ans = inf
        current_sum = 0
        left = 0
        min_so_far = inf
        
        for right in range(n):
            current_sum += arr[right]
            
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
                
            if current_sum == target:
                curr_len = right - left + 1
                
                if left > 0 and min_len[left - 1] != inf:
                    ans = min(ans, curr_len + min_len[left - 1])
                
                min_so_far = min(min_so_far, curr_len)
                
            min_len[right] = min_so_far
            
        return ans if ans != inf else -1