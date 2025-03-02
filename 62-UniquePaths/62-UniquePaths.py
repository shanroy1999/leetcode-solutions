class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Dynamic Programming
        # Bottom row will be all 1's
        row = [1]*n
        # Iterate through all other rows except the bottom row
        # Iterate until we get to the top row
        for i in range(m-1):
            # new row will be above the bottom row
            newRow = [1]*n
            # go through every column except the rightmost column
            # rightmost column => all values 1
            for j in range(n-2, -1, -1):
                # newRow value = Right value + Bottom value
                newRow[j] = newRow[j+1] + row[j]
            # Update the row
            row = newRow
        # Return the value at top left corner of the grid
        return row[0]

        # Time Complexity = O(N*M)
        # Space Complexity = O(N) => length of the row