class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        res = []

        def dfs(r, c, visit, prevHeight):
            if (r,c) in visit or r<0 or c<0 or r==ROWS or c==COLS or heights[r][c] < prevHeight:
                return
            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for row in range(ROWS):
            dfs(row, 0, pacific, heights[row][0])                  # First row => connect to Pacific
            dfs(row, COLS-1, atlantic, heights[row][COLS-1])       # Last column => connect to Atlantic

        for col in range(COLS):
            dfs(0, col, pacific, heights[0][col])               # First column => connect to Pacific
            dfs(ROWS-1, col, atlantic, heights[ROWS-1][col])    # Last row - connect to Atlantic

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])
        
        return res
