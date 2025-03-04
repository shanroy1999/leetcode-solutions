class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Brute force Backtracking
        wordDict = set(wordDict)
        def backtrack(i):
            # done with the string
            if i==len(s):
                # Add spaces to the words found and append to the result list
                res.append(" ".join(curr))
            for j in range(i, len(s)):
                w = s[i:j+1]
                # Iterate through the words in the wordDict set
                if w in wordDict:
                    # If we found the word in input, Append the word to current list if 
                    curr.append(w)
                    # Backtrack from the j+1 index
                    backtrack(j+1)
                    # Pop the word once done backtracking
                    curr.pop()
        # The current list of words
        curr = []
        res = []
        backtrack(0)
        return res
