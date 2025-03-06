class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Use a Breadth First Search => using a queue
        # Queue => keep track of rotten oranges position in the grid
        q = deque()
        timePassed, freshOranges = 0, 0
        ROWS, COLS = len(grid), len(grid[0])

        # Check initially the number of fresh and rotten oranges in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # If any fresh oranges
                if grid[r][c] == 1:
                    # Increment the count of fresh oranges
                    freshOranges += 1
                # If any rotten oranges
                elif grid[r][c] == 2:
                    # Append position of rotten to the queue
                    q.append([r, c])
        # Directions => move up, left, right, down
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        # Convert fresh oranges to rotten oranges
        while q and freshOranges > 0:
            for i in range(len(q)):
                # Pop the rotten orange and get its coordinate
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr+r, dc+c
                    # If out of bounds and if it is not a fresh orange
                    if(row<0 or row>=ROWS or col<0 or col>=COLS or grid[row][col]!=1):
                        continue
                    # Inbound fresh orange - Change the oranges to rotten
                    grid[row][col] = 2
                    # Add position of new rotten orange to the queue
                    q.append([row, col])
                    # Decrement the number of fresh oranges
                    freshOranges -= 1
            # Increment the time for each fresh orange converted to rotten
            timePassed+=1
        # return time if all freshoranges converted to rotten => else -1
        return timePassed if freshOranges == 0 else -1

