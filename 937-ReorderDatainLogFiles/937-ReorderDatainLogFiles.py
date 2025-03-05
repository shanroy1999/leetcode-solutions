class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            logSplit = log.split(" ", 1)
            if any(char.isdigit() for char in logSplit[1]):
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        
        # sorted by identifier first
        # then sorted by content
        letter_logs.sort(key=lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0]))
        return letter_logs + digit_logs
