class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:              # if the digit is 0 to 8 => simply add 1 and return
                digits[i] += 1
                return digits
            digits[i] = 0                   
            # if digit is 9 => make the last digit 0 and add 1 behind
            if i==0:                        
                return [1] + digits         