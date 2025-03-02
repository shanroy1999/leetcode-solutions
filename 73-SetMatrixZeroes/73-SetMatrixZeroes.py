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
        rows, cols = len(matrix), len(matrix[0])
        col0 = 1
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]==0:
                    # If we encounter a 0 in any row/col => mark the first row/col as 1 in-place
                    matrix[row][0] = 0
                    # Cannot mark itself
                    if col != 0:
                        matrix[0][col] = 0
                    else:
                        col0 = 0
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
        
        if col0 == 0:
            for row in range(rows):
                matrix[row][0] = 0