class Solution:
    # Brute Force approach
    # def isPrime(self, n):
    #     if n<2:
    #         return False
    #     for i in range(2, int(n**0.5)+1):
    #         if n%i==0:
    #             return False
    #     return True

    # Optimized approach
    def isPrime(self, n):
        if n<2:
            return False
        if n in (2, 3):
            return True
        if n%2 == 0 or n%3==0:
            return False
        # Check divisibility for numbers of the form 6k ± 1 up to sqrt(n)
        for i in range(5, int(math.isqrt(n)) + 1, 6):
            if n%i == 0 or n%(i+2) == 0:
                return False
        return True
    
    def isPalindrome(self, n):
        return str(n) == str(n)[::-1]

    def generatePalindromes(self, n):
        while True:
            if self.isPalindrome(n):
                yield n
            n+=1
            # Skip the range 10^7 to 10^8 as there are no prime palindromes in this range
            if 10**7 < n < 10**8:
              n = 10**8

    def primePalindrome(self, n: int) -> int:
        for palindrome in self.generatePalindromes(n):
            if self.isPrime(palindrome):
                return palindrome

    # Time Complexity = O(M sqrt(M)) => M = range of palindromes
    # Space Complexity = O(1) => only store the result
    
