class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # writer=reader=0
        # n=len(nums)
        # while n>0:
        #     if nums[reader]!=val:
        #         nums[writer]=nums[reader]
        #         writer+=1
        #         reader+=1
        #     else:
        #         reader+=1
        #     n-=1
        # return writer

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
