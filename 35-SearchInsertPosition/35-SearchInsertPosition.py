class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 2 pointer approach - Binary Search
        left = 0
        right = len(nums) - 1
        while left<=right:
            mid = (left+right)//2
            if(nums[mid] == target):   # return positon if target found
                return mid
            elif(nums[mid] < target):  # search right half
                left = mid+1
            elif(nums[mid] > target):  # search left half
                right = mid-1
        return left

        # [1, 3, 5, 6], target = 5
        # left = 0, right = 3
        # 0<=3 => mid = 1 => nums[mid] = 3 => 3 < target => left = mid+1 = 2
        # 2<=3 => mid = 2 => nums[mid] = 5 => 5 = target => return mid => return 2

        # [1, 3, 5, 6], target = 2
        # left = 0, right = 3
        # 0<=3 => mid = 1 => nums[mid] = 3 => 3 > target => right = mid-1 = 0
        # 0<=0 => mid = 0 => nums[mid] = 1 => 1 < target => left = mid+1 = 1
        # 1>0 -> return left => return 1

        # [1, 3, 5, 6], target = 7
        # left = 0, right = 3
        # 0<=3 => mid = 1 => nums[mid] = 3 => 3 < target => left = mid+1 = 2
        # 2<=3 => mid = 2 => nums[mid] = 3 => 3 < target => left = mid+1 = 3
        # 3<=3 => mid = 3 => nums[mid] = 5 => 5 < target => left = mid+1 = 4
        # 4>3 -> return left => return 4