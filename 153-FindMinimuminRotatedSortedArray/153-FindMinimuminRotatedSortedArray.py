class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left = 0
        right = len(nums)-1
        while left <= right:
            # If the array is already sorted in ascending order without rotation
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            middle = (left + right)//2
            res = min(res, nums[middle])
            if nums[middle] >= nums[left]:
                # Search the right portion of the array
                left = middle + 1
            else:
                # Search the left portion of the array
                right = middle - 1
        return res