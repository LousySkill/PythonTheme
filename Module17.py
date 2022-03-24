import random

def sort_by_inserts(list_input):
    list_int = list_input
    for i in range(1, len(list_int)):
        a = list_int[i]
        b = i
        while b > 0 and list_int[b - 1] > a:
            list_int[b] = list_int[b - 1]
            b -= 1
        list_int[b] = a
    return list_int


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


sequence_numbers_string = input("Введите последовательность чисел через пробел(Пример: 1 2 3 4 5): ")
element = int(input("Введите одно из чисел, введенного выше: "))

sequence_numbers_list = list(map(int, sequence_numbers_string.split(sep=" ")))

sequence_sorted = sort_by_inserts(sequence_numbers_list)
print("Количество элементов по возрастанию: ", sequence_sorted)

element_index = binary_search(sequence_sorted, element, 0, len(sequence_sorted))
print("Индекс элемента  из отсортированнного списка: ", element_index)

