class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if(nums[i]!=val):
                nums[index] = nums[i]
                index+=1
        return index

        # nums = [3, 2, 2, 3], val = 3
        # index = 0 => nums[index] = 3
        # i in range(len(nums)) => i = 0, 1, 2, 3
        # i = 0 => nums[i] = 3
        #       => nums[i] = val = 3
        # i = 1 => nums[i] = 2
        #       => nums[i] != val => nums[0] (=nums[index]) = nums[i] = 2
        #       => index = 1
        # i = 2 => nums[i] = 2
        #       => nums[i] != val => nums[1] (=nums[index]) = nums[i] = 2
        #       => index = 2
        # i = 3 => nums[i] = 3
        #       => nums[i] = val = 3
        # nums => [2, 2]
        # => return index => index = 2