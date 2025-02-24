class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        l = [key for key, _ in sorted(hashmap.items(), key=lambda x: x[1], reverse=True)]
        return l[:k]