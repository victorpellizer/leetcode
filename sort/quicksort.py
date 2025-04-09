def quicksort(arr):
    def partition(low, high):
        pivot = arr[high] # seleciona o último elemento do (sub)array como pivô
        # obs: existem formas mais aprofundadas de se definir o pivô
        i = low - 1 # low-1 pois i começa "fora" do array
        for j in range(low, high):
            if arr[j] <= pivot: # verificar se o pivô, que é o item mais a direita, é menor que o item no j
                i += 1 # desloca o i para a direita
                arr[i], arr[j] = arr[j], arr[i] # troca o item em i pelo item em j
        arr[i + 1], arr[high] = arr[high], arr[i + 1] # coloca o pivô no lugar correto dentro do array
        return i + 1

    def quicksort_recursive(low, high):
        if low < high: # quando os ponteiros se encontrarem, encerra a recursão
            pi = partition(low, high) # vai dividir o array em dois e retornar o índice da partição
            quicksort_recursive(low, pi - 1) # passa todo o array antes da partição
            quicksort_recursive(pi + 1, high) # passa todo o array depois da partição

    quicksort_recursive(0, len(arr) - 1)
    return arr


test_array = [10, 7, 8, 9, 1, 5]
print("Unsorted array:", test_array)
sorted_array = quicksort(test_array)
print("Sorted array:", sorted_array)