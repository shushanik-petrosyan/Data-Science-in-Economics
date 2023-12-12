def find_exclusive_elements(sequence_a, sequence_b):
    # Создаем список exclusive_a, содержащий элементы из sequence_a, которых нет в sequence_b
    exclusive_a = [x for x in sequence_a if x not in sequence_b]
    # Создаем список exclusive_b, содержащий элементы из sequence_b, которых нет в sequence_a
    exclusive_b = [x for x in sequence_b if x not in sequence_a]
    # Возвращаем оба списка
    return exclusive_a, exclusive_b

# Запрашиваем у пользователя ввод последовательностей A и B, разделенных пробелами, и преобразуем их в список целых чисел
sequence_a = list(map(int, input("Введите последовательность A, разделенную пробелами: ").split()))
sequence_b = list(map(int, input("Введите последовательность B, разделенную пробелами: ").split()))

# Получаем списки элементов, которые являются исключительными для каждой последовательности
exclusive_elements_a, exclusive_elements_b = find_exclusive_elements(sequence_a, sequence_b)

# Выводим исходные последовательности A и B, а также элементы, которые являются эксклюзивными для каждой последовательности
print("Исходная последовательность A:", sequence_a)
print("Исходная последовательность B:", sequence_b)
print("Элементы, не входящие в B из A:", exclusive_elements_a)
print("Элементы, не входящие в A из B:", exclusive_elements_b)
