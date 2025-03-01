class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # total = float(-inf)
        # Brute force approach
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         total = max(total, sum(nums[i:j+1]))
        # return total

        # Time complexity = O(N^2)

        # Optimized approach - Sliding window
        maxSub = nums[0]
        currSum = 0
        for num in nums:
            # If we get a sum that is negative => reset the currSum to 0
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSub = max(currSum, maxSub)
        return maxSub