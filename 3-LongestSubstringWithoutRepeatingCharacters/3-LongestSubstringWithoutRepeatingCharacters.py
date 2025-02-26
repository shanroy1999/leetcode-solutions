class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute Force
        # length = 0
        # max_length = 0
        # for i in range(len(s)):
        #     hashmap = [0]*256
        #     for j in range(i, len(s)):
        #         if hashmap[ord(s[j])]==1:
        #             break
        #         hashmap[ord(s[j])] = 1
        #         length = j-i+1
        #         max_length = max(length, max_length)
        # return max_length

        # Time complexity = O(N^2)
        # Space Complexity = O(1)

        # Optimized
        left, right, max_length = 0, 0, 0
        hashmap = [-1]*256
        while(right < len(s)):
            if hashmap[ord(s[right])] != -1:
                if hashmap[ord(s[right])] >= left:
                    left = hashmap[ord(s[right])]+1
            length = right-left+1
            max_length = max(length, max_length)
            hashmap[ord(s[right])] = right
            right+=1
        return max_length

        # Time complexity = O(N) => only moving right
        # Space Complexity = O(256)
