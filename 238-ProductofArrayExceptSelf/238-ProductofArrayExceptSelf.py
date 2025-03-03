class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefixProd, suffixProd = 1, 1
        for i in range(len(nums)):
            res[i] = prefixProd
            # Update prefixProd
            prefixProd *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            # Multiply the prefixProd (already in place) and the suffixProd
            res[i] *= suffixProd
            # Update suffixProd
            suffixProd *= nums[i]
        return res