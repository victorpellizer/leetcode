class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        list_string = list(s)
        last_str = ''
        while list_string:
            last_str = ''.join(list_string)
            removed_letters = []
            index = 0
            while index < len(list_string):
                if list_string[index] not in removed_letters:
                    removed_letters.append(list_string[index])
                    del list_string[index]
                else:
                    index += 1
        return last_str

s = 'aabcbbca'
Solution().lastNonEmptyString(s)