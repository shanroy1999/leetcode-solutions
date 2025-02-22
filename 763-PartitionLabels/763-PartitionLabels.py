class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Track the last occurences -> Create a dictionary to store last occurence index of each character
        # Two pointer approach to partition the string
        # start and end -> represent current partition
        # Iteration through string -> update "end" to maximum last occurence index
        # current index reaches "end" -> partition found => add length to result, update "start"

        # Step 1 : Track last occurence of each character
        last_occurence = {}
        for i, char in enumerate(s):
            last_occurence[char] = i

        # Step 2 : Partition the string
        result = []
        start = 0
        end = 0
        for i, char in enumerate(s):
            end = max(end, last_occurence[char])
            # If reached the end of current partition
            if i == end:
                result.append(end - start + 1)
                start = end+1

        # Time complexity = O(N) -> N = length of the string -> traverse string twice to build last_occurence and partitioning
        # Space Complexity = O(1) -> last_occurence stores at most 26 characters
        
        return result