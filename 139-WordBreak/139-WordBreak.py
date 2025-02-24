class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Brute Force approach
        # def canSegment(s, wordDict):
        #     if not s:
        #         return True
        #     for i in range(1, len(s)+1):
        #         prefix = s[:i]
        #         if prefix in wordDict and canSegment(s[i:], wordDict):
        #             return True
        #     return False
        # return canSegment(s, set(wordDict))

        # Optimized approach
        # Dynamic Programming
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
