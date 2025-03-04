class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Take only the alphanumeric characters from string
        s = ''.join(c.lower() for c in s if c.isalnum())
        # Two Pointer approach
        # i = 0
        # j = len(s)-1
        # while i<j:
        #     if s[i] != s[j]:
        #         return False
        #     i+=1
        #     j-=1
        # return True

        return s == s[::-1]
            