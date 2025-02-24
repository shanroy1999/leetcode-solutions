class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")" : "(", "}" : "{", "]" : "["}
        for char in s:
            if char in hashmap.values():
                stack.append(char)
            elif char in hashmap.keys():
                if not stack or hashmap[char] != stack.pop():
                    return False
        return not stack
