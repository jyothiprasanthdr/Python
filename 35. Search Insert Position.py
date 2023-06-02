class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #  Used Binary Search Algo here to achieve O(log n)
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l
