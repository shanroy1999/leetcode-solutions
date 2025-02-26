class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # METHOD 1 : 
        # return nums*2

        # METHOD 2 : 
        # return nums + nums

        # METHOD 3 : 
        # nums.extend(nums)
        # return nums

        # Time Complexity = O(N)
        # Space Complexity = O(N)

        # METHOD 4:
        n = len(nums)
        result = [0]*(2 * n)        # Create new list of size 2n
        for i in range(n):
            result[i] = nums[i]
            result[i + n] = nums[i]
        return result
