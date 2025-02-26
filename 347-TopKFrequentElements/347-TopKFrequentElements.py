# Python Solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Method 1
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        l = [key for key, _ in sorted(hashmap.items(), key=lambda x: x[1], reverse=True)]
        return l[:k]

        # Method 2
        # hashmap = {}
        # for num in nums:
        #     hashmap[num] = 1 + hashmap.get(num, 0)
        # buckets = [[] for i in range(len(nums)+1)]
        # for key, val in hashmap.items():
        #     buckets[val].append(key)
        # ans = []
        # for i in range(len(buckets)-1, 0, -1):
        #     for num in buckets[i]:
        #         ans.append(num)
        #         if len(ans) == k:
        #             return ans
