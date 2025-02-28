class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Brute Force Approach
        # if len(s)<=1:
        #     return s
        # max_length = 1
        # max_str = s[0]
        # for i in range(len(s)-1):
        #     for j in range(i+1, len(s)):
        #         if j-i+1 > max_length and s[i:j+1] == s[i:j+1][::-1]:
        #             max_length = j-i+1
        #             max_str = s[i:j+1]
        # return max_str

        # Time complexity = O(N^3)
        # Space Complexity = O(1)

        # Expand from the middle
        if not s:
            return ""

        def expandAroundCenter(str, left, right):
            # Out of bound check
            while left >= 0 and right < len(str) and str[left] == str[right]:
                left -= 1
                right += 1
            return right-left-1
        
        start = 0
        end = 0

        for i in range(len(s)):
            odd = expandAroundCenter(s, i, i)
            even = expandAroundCenter(s, i, i+1)

            max_length = max(odd, even)
            if max_length > end-start:
                start = i - (max_length-1)//2
                end = i + max_length//2
        return s[start:end+1]
