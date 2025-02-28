class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = (left + right)//2
            if target == nums[middle]:
                return middle
            # Left sorted portion
            if nums[left] <= nums[middle]:
                if target > nums[middle] or target < nums[left]:
                    left = middle+1
                else:
                    right = middle-1
            # Right sorted portion
            else:
                if target < nums[middle] or target > nums[right]:
                    right = middle-1
                else:
                    left = middle+1
        return -1
