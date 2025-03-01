class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # New Interval not overlapping with current interval
            # End value of new interval < start value of current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # If not overlapping with the ith index interval => not overlapping with the following intervals as well
                # So append the following intervals directly
                return res + intervals[i:]
            # Start value of new interval > end value of current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # New Interval overlapping with current interval
            # Start => minimum of start values of new interval and current interval
            # End => maximum of end values of new interval and current interval
            else:
                # Update the new Interval
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                # This newInterval can still be overlapping with other intervals which will come up
        # If new not overlapping conditions never executes
        res.append(newInterval)
        return res

        # Time complexity = O(N) => iterating once
        # Space Complexity = O(N) => res list