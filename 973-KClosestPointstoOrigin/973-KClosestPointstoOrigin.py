class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Brute Force Approach
        def distance(point):
            return point[0]**2 + point[1]**2
        sorted_points = sorted(points, key=distance)
        return sorted_points[:k]