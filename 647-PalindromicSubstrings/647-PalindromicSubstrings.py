class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        # Brute force approach
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if s[i:j+1] == s[i:j+1][::-1]:
        #             count+=1
        # return count

        for i in range(len(s)):
            left = right = i
            # Check for inbound for odd length palindrome

            # count += self.countPalindrome(s, left, right)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count+=1
                left-=1
                right+=1
            # different initialization of left and right pointers for even lengths palindrome
            left = i
            right = i+1

            # count += self.countPalindrome(s, left, right)
            # Check for inbound for even length palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count+=1
                left-=1
                right+=1
        return count

    # def countPalindrome(self, str, l, r):
    #     res = 0
    #     while l >= 0 and r < len(str) and str[l] == str[r]:
    #         res+=1
    #         l-=1
    #         r+=1
    #     return res