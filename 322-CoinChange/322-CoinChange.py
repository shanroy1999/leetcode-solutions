class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Top Down DP (Memoization)
        # Time Complexity = O(Coins * Amount)
        # Space Complexity = O(Amount)
        # coins.sort()
        # # Base Case - 0 coins required to make amount 0
        # memo = {0:0}

        # # minimum number of coins to make the amount
        # def min_coins(amt):
        #     # if amount is in the memo => return the memo at the amount
        #     if amt in memo:
        #         return memo[amt]
        #     # not able to make the amount so far
        #     minn = float('inf')
        #     for c in coins:
        #         diff = amt - c
        #         # if coin is too big => coin bigger than the amount
        #         if diff < 0:
        #             break
        #         # 1 => because we are using a coin
        #         # min_couns(diff) => minimum number of coins to make the diff
        #         minn = min(minn, 1+min_coins(diff))
        #     # Store the number of coins for the amount
        #     memo[amt] = minn
        #     return minn

        # result = min_coins(amount)
        # if result < float('inf'):
        #     return result
        # # if minimum coins is still infinity => cannot make the target amount
        # return -1

        # Bottom Up Approach - Dynamic Programming
        coins.sort()
        # Base case => 0 coins for 0 amount
        dp = [0]*(amount+1)
        # Loop through non base-cases
        for i in range(1, amount+1):
            # not able to make the amount so far
            minn = float("inf")
            for c in coins:
                diff = i - c
                # if coin is too big => coin bigger than the amount
                if diff < 0:
                    break
                # 1 => because we are using a coin
                # min_couns(diff) => minimum number of coins to make the diff
                minn = min(minn, 1+dp[diff])
            dp[i] = minn
        if dp[amount]<float("inf"):
            return dp[amount]
        return -1
