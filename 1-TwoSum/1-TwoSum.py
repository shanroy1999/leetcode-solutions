class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force approach
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i,j]
        return []

        # hashmap = {}
        # for i in range(len(nums)):
        #     hashmap[nums[i]] = i
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in hashmap and hashmap[complement] != i:
        #         return [i, hashmap[complement]]
        # return []