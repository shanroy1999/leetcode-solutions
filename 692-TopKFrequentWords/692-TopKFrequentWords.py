class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Step 1 : Use Hash Map to Count word frequencies
        # Step 2 : Sort the words first by frequency in descending order and then lexicographically
        # Step 3 : Return the first k words from sorted list
        word_count = Counter(words)
        sorted_words = sorted(word_count.keys(), key=lambda x: (-word_count[x], x))

        return sorted_words[:k]
