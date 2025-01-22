class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j+=1
        return j

        # [1, 2, 3, 3, 4, 4]
        # range(1, len(nums)) => i = 1,2,3,4,5

        # j = 1 -> nums[1] = 2
        # i = 1 -> nums[1] = 2, nums[0] = 1 
        # 2!=1 -> nums[1](= nums[1]) = 2, j = 2

        # j = 2 -> nums[2] = 3
        # i = 2 -> nums[2] = 3, nums[1] = 2 
        # 3!=2 -> nums[2](= nums[2]) = 3, j = 3

        # j = 3 -> nums[3] = 3
        # i = 3 -> nums[3] = 3, nums[2] = 3
        # 3=3

        # j = 3 -> nums[3] = 3
        # i = 4 -> nums[4] = 4, nums[3] = 3
        # 4!=3 -> nums[3](= nums[4]) = 4, j = 4

        # j = 4 -> nums[4] = 4
        # i = 5 -> nums[5] = 4, nums[4] = 4
        # 4=4

        # return j => j = 4 -> array(1,2,3,4)