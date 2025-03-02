class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Brute Force approach => mark rows and cols containing 0 as -1 and then mark them 0
        # Time complexity = O(N^3)
        # rows, cols = len(matrix), len(matrix[0])

        # def markRow(row):
        #     for col in range(cols):
        #         if matrix[row][col] != 0:
        #             matrix[row][col] = -1
        
        # def markCol(col):
        #     for row in range(rows):
        #         if matrix[row][col] != 0:
        #             matrix[row][col] = -1

        # for row in range(rows):
        #     for col in range(cols):
        #         if matrix[row][col] == 0:
        #             markRow(row)
        #             markCol(col)
        
        # for row in range(rows):
        #     for col in range(cols):
        #         if matrix[row][col] == -1:
        #             matrix[row][col] = 0


        # Approach 2 : Keep track of rows and cols having atleast one zero using arrays
        # Once arrays marked => mark the entire row and col as 0 for respective positions
        # rows, cols = len(matrix), len(matrix[0])
        # rowArr = [0]*rows
        # colArr = [0]*cols

        # for row in range(rows):
        #     for col in range(cols):
        #         if matrix[row][col] == 0:
        #             rowArr[row] = 1
        #             colArr[col] = 1

        # for row in range(rows):
        #     for col in range(cols):
        #         if rowArr[row] == 1 or colArr[col] == 1:
        #             matrix[row][col] = 0

        # Approach 3 : Do the same as approach 2 but with in-place
        # first row and first col => becomes rowArr and colArr like in Approach 2
        # first row and first col => tell which row / col in matrix to zero out
        rows, cols = len(matrix), len(matrix[0])
        # Extra variable to tell if first row is 0 or not
        rowZero = 1
        # Iterate through every row and col
        # Determine which row/col need to be zero
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]==0:
                    # initialize the first col as 0 in-place
                    matrix[row][0] = 0
                    # Cannot mark for top left position
                    if col != 0:
                        matrix[0][col] = 0
                    else:
                        rowZero = 0
        # Iterating every row and col other than 1st row and 1st col
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] != 0:
                    # Check for first col and first row
                    if(matrix[0][col] == 0 or matrix[row][0] == 0):
                        matrix[row][col] = 0
        # Check for the overlapping cell in first col and first row i.e. 0,0
        if matrix[0][0] == 0:
            for col in range(cols):
                matrix[0][col] = 0
        # If we have to zero out the first row
        if rowZero == 0:
            for row in range(rows):
                matrix[row][0] = 0