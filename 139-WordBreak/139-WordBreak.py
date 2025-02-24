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
        dp[0] = [True]
        for i in range(1, len(s)+1):
            for w in wordDict:
                start = i - len(w)
                if start >=0 and dp[start] and s[start:i]==w:
                    dp[i] = True
                    break
        return dp[-1]
