class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force approach
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

        # hashmap = {}
        # for i, num in enumerate(nums):
        #     diff = target - num
        #     if diff in hashmap:
        #         return [hashmap[num], i]
        #     hashmap[diff] = i
        # return []