class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        k = 0
        for i in range(len(nums)):
            while(nums[i] < target):
                k+=1
                break
        return k