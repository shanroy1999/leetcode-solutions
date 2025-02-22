class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            identifier, content = log.split(" ", 1)     # Return a list with 2 elements
            if content[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
            
        letter_logs.sort(key=lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0]))
        return letter_logs + digit_logs

        # Time complexity => O(N log N) => N = number of logs, Sorting step also there
        # Space complexity => O(N) => list of logs