class Solution:
    def numDecodings(self, s: str) -> int:
        # Dynamic Programming - Recursive Cache
        # If we get an empty string -> return 1
        dp = { len(s) : 1 }
        # Depth first search - Recursive function
        # i => current index/position of character in string s
        def dfs(i):
            # either the position is already cached or i is the last position of string
            if i in dp:
                return dp[i]
            # If first character of the string is 0 => invalid -> decode not possible -> return 0
            if s[i] == "0":
                return 0
            # If first character is not 0 => first character is 1-9
            # take the first character at i as single digit
            # subproblem => i+1
            res = dfs(i+1)
            # Check for the 2 digit characters
            # if we have a 2nd character coming after the current one
            # for 2 digit number => looking for 10-26 => 1st digit starts with either 1 or 2
            # 2nd digit can be 0-9 if 1st digit is 1
            # 2nd digit can be 0-6 if 1st digit is 26 since number < 26 (number of letters)
            if (i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                # Since we took a double digit value => i+2
                res += dfs(i+2)
            # cache the result
            dp[i] = res
            # return the result
            return res
        
        # decode the string
        return dfs(0)