class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0]*(n+1)         # Store the number of trusts of each person (people who trust the particular person)
        for a, b in trust:
            trusted[a] -= 1         # Decrement for the trustee
            trusted[b] += 1         # Increment for trusted
        for i in range(1, n+1):
            if trusted[i] == n-1:       # Town judge will always get (n-1) trusts
                return i                # Return the index of town judge
        # No judge found
        return -1
