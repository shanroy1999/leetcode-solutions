class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        return sorted(nums).index(target)
