from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Breadth First Search
        # Traverse grid to find all initially rotten oranges and add their positios to queue
        # Use BFS to spread rot to adjacent fresh orange level by level
        # Keep track of number of minutes elapsed
        # After BFS, check if any fresh oranges left => If yes -> return -1

        rows, cols = len(grid), len(grid[0])
        queue = deque()

        fresh = 0    # fresh oranges count
        minutes = 0   # minutes elapsed

        # Initialize queue with rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        # If no fresh oranges
        if fresh==0:
            return 0

        # Directions for adjacency
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # BFS to rot adjacent fresh oranges
        while queue and fresh>0:
            # number of rotten oranges currently in the queue
            level_size = len(queue)
            for _ in range(level_size):
                # Dequeue the rotten orange at position (r, c) from the queue and see neighbors
                r, c = queue.popleft()
                # Check if neighbor is a fresh orange
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2        # Make the fresh into rotten
                        fresh-=1
                        queue.append((nr, nc))
            minutes+=1
        
        return minutes if fresh == 0 else -1

