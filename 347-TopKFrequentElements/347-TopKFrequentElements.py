class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        result = sorted(d.keys(), key=lambda x: d[x], reverse=True)[:k]
        return result