class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # def bsearch(low, high):
        #     mid = (low+high)//2
        #     if nums[mid] != target:
        #         if nums[mid] < target:
        #             return bsearch(mid, high)
        #         elif nums[mid] > target:
        #             return bsearch(low, mid)
        #     else:
        #         return mid
        # low, high = 0, len(nums)
        # return bsearch(low, high)

        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid-1
            else:
                low = mid + 1
        return -1

        