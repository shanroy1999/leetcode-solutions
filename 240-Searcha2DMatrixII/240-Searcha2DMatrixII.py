class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute force approach
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == target:
        #             return True
        # return False
        # Time complexity = O(M X N) => M = no of rows, N = no of columns

        # Optimized Approach
        # Start from top right corner of the matrix
        # if current element == target => return True
        # if current element > target => move left
        # if current element < target => move down
        # Time complexity = O(M + N) => M = no of rows, N = no of columns
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols-1
        
        while row<rows and col>=0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1                        # Move left
            else:
                row += 1                        # Move down
        
        return False