class Solution:
    def chainOfStrings(self, n: int):
        """Solução para descobrir uma sequência de strings em um array de modo que cada string é uma
        sub-sequência da próxima string, e o comprimento de cada string é exatamente um a mais que a anterior
        Ex: len(s[i]) == len(s[i-1] + 1
        """


"""
Q2-> We are given a number of strings in an array and we need to find a chain of strings such that every string is a subsequence of its next string and every string’s length should exactly be one more than its previous string. i.e, length of s[i] = length of s[i-1]+1.
I solved this question by combining two concepts together i.e DP and To check whether a string is a subsequence of another string or not.
"""
