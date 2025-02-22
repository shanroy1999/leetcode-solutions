class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            identifier, content = log.split(" ", 1)     # Return a list with 2 elements
            if content[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((content, identifier, log))
            
        letter_logs.sort(key=lambda x: (x[0], x[1]))
        result = [log for (_, _, log) in letter_logs] + digit_logs
        return result

        # Time complexity => O(N log N) => N = number of logs, Sorting step also there
        # Space complexity => O(N) => list of logs