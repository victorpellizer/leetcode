from collections import defaultdict


def isValidSudoku(board: list[list[str]]) -> bool:
    """Solução ótima, em complexidade de tempo (O(1)) para resolver o problema do Sudoku.
    Essa solução armazena os números encontrados em 3 sets: colunas, linhas e boxes 3x3.
    Se um número se repetir em qualquer um dos sets, significa que o Sudoku não é válido.
    Sudoku é um jogo expressado em quadro 9x9, composto por 9 boxes 3x3, e que pode ser representado por uma matriz.

    Obs: existe uma solução que não usa espaço adicional de memória, e que itera sobre o próprio array
    que é ótima em complexidade de espaço, mas que é péssima em complexidad de tempo O(nˆ2).
    """
    # defaultdict é um dict que permite adicionar itens a índices de um dict sem precisar declarar o índice previamente
    rows = defaultdict(set)
    col = defaultdict(set)
    boxes = defaultdict(set)

    for r in range(9):
        for c in range(9):
            current = board[r][c]  # salva o índice atual para não ter que acessar várias vezes
            if current == ".":  # se não for um número, apenas segue em frente
                continue

            # se o current já existir em algum dos sets, significa que o sudoku não é válido
            if current in rows[r] or current in col[c] or current in boxes[(r // 3, c // 3)]:
                return False

            # adiciona o número atual aos sets da linha, coluna e box
            rows[r].add(current)
            col[c].add(current)
            # para calcular em qual box um número pertence, é feita a divisão inteira por 3
            # as 3 primeiras linhas do sudoku vão estar sempre no box [0,Y]
            # as 3 primeiras colunas do sudoku vão estar sempre no box [X,0]
            # os boxes no sudoku vao de [0,0] até [2,2] (como se fossem índices de nível acima)
            boxes[(r // 3, c // 3)].add(current)

    # se não foi encontrada nenhuma inconsistência até agora, é porque é válido
    return True
