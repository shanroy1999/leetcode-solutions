class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(choose, curr, total):
            # Base case for success
            # If current total matches the target => store the combination
            if total == target:
                res.append(curr.copy())
                return
            # If the current total exceeds the target => stop or explore other combinations
            if choose >= len(candidates) or total > target:
                return
            
            # Recursive step
            # Include a candidate
            curr.append(candidates[choose])
            dfs(choose, curr, total+candidates[choose])
            curr.pop()
            dfs(choose+1, curr, total)
        dfs(0, [], 0)
        return res
