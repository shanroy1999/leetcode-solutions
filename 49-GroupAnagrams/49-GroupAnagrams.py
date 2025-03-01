class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)   # Mapping character count of each string to list of anagrams
        for s in strs:
            count = [0] * 26      # a - z characters => 26
            for c in s:
                count[ord(c) - ord("a")] +=1
            
            res[tuple(count)].append(s) # Group anagrams together
        
        return list(res.values())

        # Time complexity = O(M * N)

