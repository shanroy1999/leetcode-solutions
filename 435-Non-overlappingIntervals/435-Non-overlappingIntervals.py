class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()            # Sort by start value by default
        count = 0
        prevEnd = intervals[0][1]   # Store the end value of the first interval and keep track
        for start, end in intervals[1:]:
            # Non overlapping interval
            if start >= prevEnd:
                # Update the end point for next comparison
                prevEnd = end
            # Overlapping interval
            else:
                count+=1
                # Take the minimum of the two endpoints
                prevEnd = min(end, prevEnd)
        return count

