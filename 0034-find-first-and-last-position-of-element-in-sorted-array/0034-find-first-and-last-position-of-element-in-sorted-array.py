class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findPositionFunction(nums, target, isFirst):
            left, right, res = 0, len(nums)-1, -1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    res = mid
                    if isFirst:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return res

        firstIdx = findPositionFunction(nums, target, True)
        if firstIdx == -1:
            return [-1, -1]
        
        secondIdx = findPositionFunction(nums, target, False)
        return [firstIdx, secondIdx]