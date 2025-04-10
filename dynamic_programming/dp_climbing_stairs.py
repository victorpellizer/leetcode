class Solution:
    def climbStairs(self, n: int):
        """Solução para descobrir quantas formas possíveis existe de subir uma escada,
        sendo que é possível subir 1 ou 2 degraus de uma vez"""
        dp = [0] * (n + 1)  # inicia o array com n+1 slots
        dp[0] = 1  # existe uma maneira de chegar no degrau zero
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
