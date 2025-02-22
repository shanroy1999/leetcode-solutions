class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Step 1 : Normalize the content
        # Convert to lowercase and replace non-letter characters with spaces
        normalized_para = []
        for char in paragraph:
            if char.isalpha() or char == ' ':
                normalized_para.append(char.lower())
            else:
                normalized_para.append(' ')
        normalized_para = ''.join(normalized_para)

        # Step 2 : Split into words
        words = normalized_para.split()

        # Step 3 : Count word frequencies
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1

        # Step 4 : Filter banned words
        banned_set = set(banned)
        for word in banned_set:
            if word in word_count:
                del word_count[word]

        # Step 5 : Find most frequent word
        most_common = ""
        max_count = 0
        for word, count in word_count.items():
            if count > max_count:
                most_common = word
                max_count = count
        
        return most_common
