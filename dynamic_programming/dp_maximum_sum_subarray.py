class Solution:
    def max_subarray(numbers: list[int]):
        """Solução para encontrar a maior soma possível de um subarray"""
        best_sum = float("-inf")  # falso infinito negativo
        current_sum = 0
        for x in numbers:  # percorre o array
            current_sum = max(x, current_sum + x)  # soma o número atual à soma total anterior
            best_sum = max(best_sum, current_sum)  # altera o best_sum se a nova soma for a maior de todas
        return best_sum
