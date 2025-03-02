class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands_count = 0

        def dfs(r, c):
            # Base case : out of bounds or not the part of the islands
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c] == "0":
                return
            
            # Mark the current cell as visited
            grid[r][c] = "0"

            # Explore all four directions
            dfs(r+1, c)   # down
            dfs(r-1, c)   # up
            dfs(r, c+1)   # right
            dfs(r, c-1)   # left

        def bfs(r, c):
            queue = deque([(r, c)])
            while queue:
                row, col = queue.popleft()
                # Check if current cell is valid and part of an island
                if row<0 or row>=rows or col<0 or col>=cols or grid[row][col] == "0":
                    continue
                
                # Marks the current cell as visited
                grid[row][col] = "0"
                # Add all 4 directions to the queue
                queue.append((row+1, col))    # Down
                queue.append((row-1, col))    # Up
                queue.append((row, col+1))    # Right
                queue.append((row, col-1))    # Left

        # Traverse the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # dfs(r, c)
                    bfs(r, c)
                    islands_count+=1
        return islands_count