class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Brute Force approach
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if(nums[i] + nums[j] == target):
        #             return [i,j]
        # return []

        # Time complexity = O(N^2)
        # Space complexity = O(1)

    # Hashmap Approach
        hashmap = {}
        # Current number -> Key
        # Current index -> value

        # Iterate through the array
        for i, num in enumerate(nums):
            # Check if current number exists in hashmap
            if num in hashmap:
                return [hashmap[num], i]
            # Store the difference between target and current number in hashmap
            hashmap[target - num] = i
        
        # No solution found
        return []

        # Time complexity = O(N)
        # Space complexity = O(N)

        # (0, 2) -> 2 not in hashmap => hashmap[7] = 0
        # (1, 7) -> 7 in hashmap => return [0, 1]

        # (0, 3) -> 3 not in hashmap => hashmap[3] = 0
        # (1, 2) -> 2 not in hashmap => hashmap[4] = 1
        # (2, 4) -> 4 in hashmap => return [1, 2]