class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
    # Approach 1 : Using a Hash Map

        # Step 1 : Count word frequencies
        # Step 2 : Sort the words first by frequency in descending order and then lexicographically
        # Step 3 : Return the first k words from sorted list
        word_count = Counter(words)
        sorted_words = sorted(word_count.keys(), key=lambda x: (-word_count[x], x))
        # return sorted_words[:k]

        # Time complexity = O(N log N) => N = number of words in list, sorting
        # Space Complexity = O(N) => sorting the word frequencies and the sorted list

    # Approach 2 : Using a min Heap

        # Step 1 : Count word frequencies
        # Step 2 : Use a min heap to find the top k frequent words
        #        : Heap elements - tuples of (-frequency, word) -> simulate max heap
        # Step 3 : Return the first k words from heap
        heap = []
        for word, count in word_count.items():
            heapq.heappush(heap, (-count, word))
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        # Time complexity - O(N log k) -> building heap -> O(N), each heap operation -> O(log k)
        # Space Complexity = O(N) => sorting word frequencies and the heap
        return result
