class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        esq = 0
        res = 0

        for i, dir in enumerate(s):
            while s[dir] in char_set:
                char_set.remove(s[esq])
                esq += 1
            char_set.add(s[dir])
            res = max(res, len(char_set))
        return res