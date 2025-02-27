# Python3
# Brute-force Solution
class Solution:
    def find(self, nums, a):
        for i in nums:
            if i == a:
                return True
        return False

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:  return 0
        maxi = 1
        for i in nums:
            conseq = 1
            while self.find(nums, i + conseq):
                conseq += 1
            maxi = max(maxi, conseq)
        return maxi