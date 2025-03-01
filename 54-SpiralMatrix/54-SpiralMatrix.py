class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        while left < right and top < bottom:
            # Traverse through the first row (from left to right) and get every value in it
            for i in range(left, right):
                res.append(matrix[top][i])
            # Shift top pointer towards the bottom by 1
            top += 1
            # Traverse through the rightmost col (from top to bottom) and get every value in it
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            # Shift right pointer towards left by 1
            right -= 1
            if not(left<right and top < bottom):
                break
            # Traverse through the bottom row (from right to left) and get every value in it
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            # Shift bottom pointer towards top by 1
            bottom -= 1
            # Traverse through the leftmost col (from bottom to top) and get every value in it
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            # Shift left pointer towards right by 1
            left += 1
        return res