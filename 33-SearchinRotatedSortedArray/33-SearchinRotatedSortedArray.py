class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = (left + right) // 2
            # IF the middle element itself is the target => return middle
            if nums[middle] == target:
                return middle
            # Identify the sorted half
            # If Left half is sorted
            if nums[middle] >= nums[left]:
                # Check if the target lies in the sorted left half
                if nums[middle] >= target and target >= nums[left]:
                    right = middle-1
                # If target doesnt lie in the sorted left half => check the right half
                else:
                    left = middle+1
            # If right half is sorted
            else:
                # Check if the target lies in the sorted right half
                if nums[middle] <= target and target <= nums[right]:
                    left = middle + 1
                # If target doesnt lie in the sorted right half => check the left half
                else:
                    right = middle - 1
        return -1