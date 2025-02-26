class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # pref = strs[0]
        # pref_length = len(pref)
        # for s in strs[1:]:
        #     while s[:pref_length] != pref:
        #         pref_length -=1
        #         if pref_length == 0:
        #             return ""
        #         pref = pref[:pref_length]
        # return pref

        ans = ""
        sorted_strs = sorted(strs)
        first_str = sorted_strs[0]
        last_str = sorted_strs[-1]
        for i in range(min(len(first_str), len(last_str))):
            if first_str[i] != last_str[i]:
                return ans
            ans += first_str[i]
        return ans
