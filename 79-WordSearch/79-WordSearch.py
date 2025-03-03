class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Brute force - Backtracking
        rows, cols = len(board), len(board[0])
        # Cannot visit same value twice
        visit = set()

        # Row, col, current character
        def dfs(row, col, i):
            if i==len(word):
                return True
            # Base case : out of bounds, 
            # visit (row, col) twice, 
            # if character is something we dont want
            if row < 0 or col < 0 or row >= rows or col >= cols or word[i]!=board[row][col] or (row, col) in visit:
                return False
            # Found a character that we need
            visit.add((row, col))
            res = (dfs(row+1, col, i+1) or
                  dfs(row-1, col, i+1) or
                  dfs(row, col+1, i+1) or
                  dfs(row, col-1, i+1))
            
            # Remove the position from path since already visited
            visit.remove((row, col))
            return res

        # Go through every single starting position => do DFS
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False

        # Time Complexity = O(m*n) * O(dfs) = O(m*n) * O(4^len(word)) = O(m*n*4^n)