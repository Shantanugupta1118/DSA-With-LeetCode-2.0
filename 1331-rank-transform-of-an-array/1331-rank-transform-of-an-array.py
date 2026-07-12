class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        copied_arr = sorted(arr)
        idx = {}
        count = 1
        for i in copied_arr:
            if i not in idx:
                idx[i] = count
                count += 1
        
        return [idx[arr[i]] for i in range(len(arr))]