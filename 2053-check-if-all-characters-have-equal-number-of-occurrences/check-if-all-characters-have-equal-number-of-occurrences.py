class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}

        for char in s:
            freq[char]= freq.get(char,0)+1

        freq_set = set(freq.values())

        return len(freq_set)==1