class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Brute Force approach
        def isPalindrome(s):
            return s == s[::-1]
        longest = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if isPalindrome(s[i:j]) and len(s[i:j])>len(longest):
                    longest = s[i:j]
        return longest
