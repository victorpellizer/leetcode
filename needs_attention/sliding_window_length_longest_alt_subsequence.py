class Solution:
    def alt_subsequence_best(self, x: list[int]) -> int:
        """Solução para encontrar o comprimento da maior substring
        de 0's e 1's sem repetir"""
        if len(x) == 0:
            return 0

        max_ = 1  # max initialized as 1 because x can never be empty
        low, high = 0, 0  # start both pointers on index 0
        while high < len(x) - 1:  # move the high pointer until the end of the array
            high += 1  # moves the high pointer to the right
            # if two consecutive numbers of the array are equal, it means the window must be reset
            if x[high - 1] == x[high]:
                low = high  # moves the lower pointer to the same index as the higher
            # stores the new window size if it's the biggest found
            max_ = max(max_, high - low + 1)
        return max_
