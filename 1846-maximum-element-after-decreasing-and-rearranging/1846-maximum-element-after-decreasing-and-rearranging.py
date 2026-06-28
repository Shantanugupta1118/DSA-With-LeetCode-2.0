class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        if len(arr) == 1 or len(arr) == 0: return 1

        arr.sort()

        print("arr: {}".format(arr))
        if arr[0] != 1:
            arr[0] = 1
        
        max_element = 0
        
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != 1 and arr[i] - arr[i-1] != 0: 
                arr[i] = arr[i-1]+1
            max_element = max(max_element, arr[i])
        return max_element
                
            