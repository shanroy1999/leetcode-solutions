class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute Force Approach
        # nums.sort()
        # if len(nums)==0:
        #     return 0
        # l = 1
        # maxl = 1
        # for i in range(len(nums)-1):
        #     if(nums[i+1] == nums[i]):
        #         continue
        #     if(nums[i+1] == nums[i] + 1):
        #         l += 1
        #     else:
        #         l = 1
        #     maxl = max(maxl, l)
        # return maxl

        # Optimized approach
        if len(nums)==0:
            return 0
        numSet = set(nums)
        longest = 0
        for i in numSet:
            # Check if the number is start of a sequence
            if (i-1) not in numSet:
                length = 1
                while (i+length) in numSet:
                    length+=1
                longest = max(longest, length)
        return longest
