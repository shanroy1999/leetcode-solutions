class Solution:
    def hammingWeight(self, n: int) -> int:
        # Convert number to binary
        res = 0
        while n:
            res+=n%2
            n=n>>1
        return res