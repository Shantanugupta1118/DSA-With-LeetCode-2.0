class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # low, high = 0, len(nums)-1
        # while low <= high:
        #     mid = (low+high)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         high = mid - 1
        #     else:
        #         low = mid + 1
        # return low

        def bsearch(low, high):
            if low > high:
                return low
            mid = (high+low)//2
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                return bsearch(mid+1, high)
            else:
                return bsearch(low, mid-1)
        return bsearch(0, len(nums)-1)