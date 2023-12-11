def find_exclusive_elements(sequence_a, sequence_b):
    exclusive_a = [x for x in sequence_a if x not in sequence_b]
    exclusive_b = [x for x in sequence_b if x not in sequence_a]
    return exclusive_a, exclusive_b

sequence_a = list(map(int, input("Введите последовательность A, разделенную пробелами: ").split()))
sequence_b = list(map(int, input("Введите последовательность B, разделенную пробелами: ").split()))

exclusive_elements_a, exclusive_elements_b = find_exclusive_elements(sequence_a, sequence_b)

print("Исходная последовательность A:", sequence_a)
print("Исходная последовательность B:", sequence_b)
print("Элементы, не входящие в B из A:", exclusive_elements_a)
print("Элементы, не входящие в A из B:", exclusive_elements_b)
