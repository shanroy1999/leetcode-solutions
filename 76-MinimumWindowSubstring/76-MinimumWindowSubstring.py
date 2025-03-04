class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": 
            return ""
        countNeed = {}
        countHave = {}
        result = [-1, -1]
        resultLength = float("inf")
        left = 0
        # Get all the counts of characters we need
        for char in t:
            countNeed[char] = 1 + countNeed.get(char, 0)
        
        have, need = 0, len(countNeed)
        for right in range(len(s)):
            char = s[right]
            countHave[char] = 1 + countHave.get(char, 0)
            # Compare the two hashmaps => see if the character counts matches exactly
            if char in countNeed and countHave[char] == countNeed[char]:
                have += 1
            while have == need:
                # Check if it is the minimum length of string
                if right-left+1 < resultLength:
                    result = [left, right]
                    resultLength = right - left + 1
                # If it is greater than the current resultLength => pop character from left
                # Pop from left of the window
                countHave[s[left]]-=1
                # Update the have if the character popped from countHave was a matching character
                if s[left] in countNeed and countHave[s[left]] < countNeed[s[left]]:
                    have -= 1
                left += 1
        left, right = result
        return s[left:right+1] if resultLength != float("inf") else ""