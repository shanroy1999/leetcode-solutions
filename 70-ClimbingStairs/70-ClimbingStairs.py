class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 1 => 1 step
        # n = 2 => (1 + 1)
        #       => 2
        # n = 3 => (1 + 1 + 1)
        #       => (1 + 2)
        #       => (2 + 1)
        # n = 4 => (1 + 1 + 1 + 1)
        #       => (1 + 2 + 1)
        #       => (1 + 1 + 2)
        #       => (2 + 1 + 1)
        #       => (2 + 2)
        # n = 5 => (1 + 1 + 1 + 1 + 1)
        #       => (2 + 1 + 1 + 1)
        #       => (1 + 2 + 1 + 1)
        #       => (1 + 1 + 2 + 1)
        #       => (1 + 1 + 1 + 2)
        #       => (2 + 2 + 1)
        #       => (1 + 2 + 2)
        #       => (2 + 1 + 2)

        # count(3) = count(2) + count(1)
        # count(4) = count(3) + count(2)
        # count(5) = count(4) + count(3)

        if n<=3:
            return n
        prev1 = 3
        prev2 = 2
        curr = 0

        for i in range(3, n):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return curr
