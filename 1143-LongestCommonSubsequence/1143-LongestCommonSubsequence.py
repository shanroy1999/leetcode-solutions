class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2 Dimensional Dynamic programming using dp grid
        # 2 D grid of dimension len(text2)+1 and len(text1)+1
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        # Starting at the bottom right of the matrix and working the way up
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                # Characters match
                if text1[i] == text2[j]:
                    # Moving diagonally => Add the value 1 to the diagonal value
                    dp[i][j] = 1 + dp[i+1][j+1]
                # Characters dont match
                else:
                    # Move up / left => take the maximum
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        # Top left corner => will contain the final result
        return dp[0][0]

        # Time Complexity = O(N*M) => N = length of text1, M = length of text2