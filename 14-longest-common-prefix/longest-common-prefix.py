class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        result = ""
        prefix = strs[0] # assuming with first letter of string(Array)
        n = len(prefix)
        for i in range(n):
            curr_str = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != curr_str:
                    return result
            result += curr_str
        return result
