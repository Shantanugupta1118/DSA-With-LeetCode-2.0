class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def bsearch(low, high):
            if low > high:
                return -1
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return bsearch(mid+1, high)
            else:
                return bsearch(low, mid-1)
        low, high = 0, len(nums)-1
        return bsearch(low, high)

        # low, high = 0, len(nums)-1
        # while low <= high:
        #     mid = (low+high)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif target < nums[mid]:
        #         high = mid-1
        #     else:
        #         low = mid + 1
        # return -1

        