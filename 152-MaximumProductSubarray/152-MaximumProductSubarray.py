class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMinProd, currMaxProd = 1, 1

        for num in nums:
            if num==0:
                currMinProd, currMaxProd = 1, 1
                continue
            temp = currMaxProd
            currMaxProd = max(num * currMaxProd, num * currMinProd, num)
            currMinProd = min(num * temp, num * currMinProd, num)
            res = max(res, currMaxProd, currMinProd)
        
        return res