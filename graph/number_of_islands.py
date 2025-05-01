from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0  # inicializa o número de ilhas em zero
        visited = set()  # cria um set para guardar todos índices da matriz que já foram visitados
        rows, cols = len(grid), len(grid[0])  # largura e comprimento da matriz
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # direções em que a bfs deverá olhar

        def bfs(r, c):
            q = deque()
            visited.add((r, c))  # garante que o índice atual não será mais visitado
            q.append((r, c))  # coloca o índice na fila

            while q:
                row, col = q.popleft()
                for dr, dc in directions:  # loop para olhar para os 4 índices adjacentes ao atual
                    r, c = row + dr, col + dc
                    # 1 - verifica se o índice adjacente não está fora do grid, primeiro na linha depois na coluna
                    # 2 - verifica se o índice adjacente é um 1, representando parte da ilha
                    # 3 - verifica se o índice adjacente já foi visitado em algum momento
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited:
                        q.append((r, c))  # cria uma corrente para visitar todos nós "1" conectados possíveis
                        visited.add((r, c))  # marca o índice adjacente como visitado

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1  # encontrar um índice "1" não visitado significa que entrou em uma nova ilha
                    bfs(r, c)  # marca todos os índices "1" conectados ao "1" inicial como "visitados"

        return islands
