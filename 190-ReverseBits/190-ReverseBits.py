class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # get the ith bit
            # to get first bit => we do n & 1
            # to get ith bit -> shift n to the right by i and then do &1
            bit = (n>>i) & 1
            res = res | (bit << (31-i))
        return res

        # Time Complexity = O(1) => iterate 32 bits