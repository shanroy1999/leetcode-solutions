class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Brute Force => calculate the distances -> sort the points based on distance -> return
        # time complexity = O(NlogN)
        res = []
        dist = []
        for x, y in points:
            d = x**2 + y**2
            dist.append([d, x, y])
        dist.sort(key=lambda x: x[0])
        for i in dist[:k]:
            res.append([i[1], i[2]])
        return res