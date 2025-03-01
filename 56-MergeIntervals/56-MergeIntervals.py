class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            prevEnd = output[-1][1]
            if start <= prevEnd:
                output[-1][1] = max(prevEnd, end)
            else:
                output.append([start, end])
        return output

        # Time complexity = O(N log N)