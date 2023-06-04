class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[start_index] = nums[i]
                start_index += 1
        return start_index
