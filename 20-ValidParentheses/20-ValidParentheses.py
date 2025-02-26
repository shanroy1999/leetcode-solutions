class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if  ( not stack or 
                (char == ")" and stack.pop() != "(") or 
                (char == "}" and stack.pop() != "{") or 
                (char == "]" and stack.pop() != "[")):
                    return False
        return not stack


