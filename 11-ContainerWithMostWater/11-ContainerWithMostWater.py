class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute Force approach
        # res = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         area = (j - i) * min(height[i], height[j])
        #         res = max(res, area)
        # return res

        # Time complexity = O(N^2)

        # Optimized approach - O(N) time complexity
        res = 0
        left = 0
        right = len(height)-1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)
            if(height[left] < height[right]):
                left+=1
            # elif(height[l] > height[r]):
            #     r-=1
            else:
                right-=1
                # l+=1
        return res