class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force approach
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        # Time Complexity = O(N * N)
        # Space Complexity = O(1)

        # Optimized Approach
        hashmap = {}
        for i, num in enumerate(nums):
            if num in hashmap:
                return [hashmap[num], i]
            hashmap[target - num] = i
        return []

        # Time Complexity = O(N)
        # Space Complexity = O(N)