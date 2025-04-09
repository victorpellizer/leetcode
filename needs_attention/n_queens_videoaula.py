class Solution:
    def solveNQueens(
        self,
        n
    ):
        col = set()
        diag_positiva = set() # (r + c) a soma do valor da coluna e da linha é a mesma para todos na mesma diagonal positiva
        diag_negativa = set() # (r - c) a sub do valor da linha pela coluna é a mesma para todos na mesma diagonal positiva
        
        res = []
        tabuleiro = [["."] * n for i in range(n)] # cria N arrays de tamanho N, cada indice do array sendo '.'

        def backtrack(r):
            if r == n:
                copy = [''.join(linha) for linha in tabuleiro]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r + c) in diag_positiva or (r - c) in diag_negativa:
                    continue

                col.add(c)
                diag_positiva.add(r + c)
                diag_negativa.add(r - c)
                tabuleiro[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                diag_positiva.remove(r + c)
                diag_negativa.remove(r - c)
                tabuleiro[r][c] = "."

        backtrack(0)
        return res
    
Solution().solveNQueens(5)