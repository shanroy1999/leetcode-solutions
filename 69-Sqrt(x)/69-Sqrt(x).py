class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        res = 0
        low = 1
        high = x
        while (low <= high):
            mid = low + (high - low)//2
            if mid*mid == x:
                return mid
            elif mid*mid <= x:
                low = mid+1
                res = mid
            else:
                high = mid-1
        return res