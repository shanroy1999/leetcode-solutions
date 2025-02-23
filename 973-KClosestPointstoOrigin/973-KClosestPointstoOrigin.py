class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0]**2 + point[1]**2

        # Brute Force Approach
        # sorted_points = sorted(points, key=distance)
        # return sorted_points[:k]

        # Time complexity = O(N log N) -> N = number of points + Sorting
        # Space complexity = O(N)

        # Optimized Approach
        # Calculate euclidean distance for each point from origin
        # push all points in a min-heap based on their distances
        # pop the top K points

        heap = []
        for point in points:
            heapq.heappush(heap, (-distance(point), point))
            if len(heap)>k:
                heapq.heappop(heap)
            
        return [point for (_, point) in heap]

        # Time complexity = O(N log k) => N = number of points
        # Space complexity = O(k) => storing the heap
