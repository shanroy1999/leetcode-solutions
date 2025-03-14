class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window approach
        count = {}
        res = 0
        left = 0

        # for right in range(len(s)):
        #     count[s[right]] = 1 + count.get(s[right], 0)

        #     while (right-left+1) - max(count.values()) > k:
        #         count[s[left]]-=1
        #         left += 1
            
        #     res = max(res, right-left+1)
        # return res

        # Time complexity = O(N)

        # Sliding window approach with MaxFrequency
        maxFreq = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxFreq = max(count[s[right]], maxFreq)

            while (right-left+1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right-left+1)
        return res

        # Time Complexity = O(256)