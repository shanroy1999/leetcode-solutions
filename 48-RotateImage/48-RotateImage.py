class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Pointers appoach => top, left, bottom, right
        left = 0
        right = len(matrix)-1

        # Store the top left value in a temp variable
        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                # Save the top left value of the matrix in a temp var
                topLeft = matrix[top][left + i]

                # Move bottom left into top left
                matrix[top][left + i] = matrix[bottom-i][left]

                # Move bottom right into bottom left
                matrix[bottom - i][left] = matrix[bottom][right-i]

                # Move top right into bottom right
                matrix[bottom][right-i] = matrix[top+i][right]

                # Move top left into top right
                matrix[top+i][right] = topLeft
            
            # Update pointer
            right -= 1
            left += 1

        