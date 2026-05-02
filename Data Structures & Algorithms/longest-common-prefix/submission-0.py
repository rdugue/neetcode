class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        longest = ""
        while True:
            for j, s in enumerate(strs):
                end_word = len(s) < i + 1
                if end_word and j == 0:
                    return longest 
                if end_word:
                    return longest[:-1]
                if j == 0:
                    longest += s[i]
                else:
                    if longest[-1] != s[i]:
                        return longest[:-1]
            i += 1
        return longest 