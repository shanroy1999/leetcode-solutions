class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy Approach
        # Trying to reach the last index of input array
        goal = len(nums)-1

        # Start from the last index
        for i in range(len(nums)-1, -1, -1):
            # Shift the goal post if we are able to reach the goal from the adjacent index val
            if nums[i] + i >= goal:
                goal = i
        
        # If the goal reached the first index => return True => able to jump to the goal
        return goal == 0

        # Time Complexity = O(N)
        # Space Complexity = O(1)