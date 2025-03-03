class Solution:
    def helperHouseRobber1(self, nums):
        rob1, rob2 = 0, 0
        for num in nums:
            newRob = max(num+rob1, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
    def rob(self, nums: List[int]) -> int:
        # Skip the 1st house
        # Skip the last house
        # input array with only 1 value => add nums[0] to the max
        return max(nums[0], self.helperHouseRobber1(nums[1:]), self.helperHouseRobber1(nums[:-1]))