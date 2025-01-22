class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force approach
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[j] == target - nums[i]:
        #             return [i,j]
        # return []

        # Hashmap approach 1
        # hashMap = {}
        # for i in range(len(nums)):
        #     hashMap[nums[i]] = i
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in hashMap and hashMap[complement] != i:
        #         return [i, hashMap[complement]]
        # return []

        # HashMap approach 2
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        return []