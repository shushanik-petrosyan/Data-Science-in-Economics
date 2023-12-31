import math  # Импорт модуля math для использования математических функций

# Функция для вычисления суммы ряда с фиксированным количеством членов
def calculate_series_fixed(x, n):
    y = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)  # Вычисление очередного члена ряда
        y += term  # Добавление члена ряда к сумме
    return y

# Функция для вычисления суммы ряда до достижения заданной точности
def calculate_series_until_epsilon(x, eps):
    y = 0
    i = 0
    term = x
    while abs(term) >= eps:
        y += term  # Добавление члена ряда к сумме
        i += 1
        term = -term * (x ** 2) * (2 * i - 1) / (2 * i + 1)  # Вычисление очередного члена ряда
    return y

x_value = float(input("Введите значение x: "))  # Ввод значения x
choice = input("Выберите метод вычисления (1 - фиксированное количество членов, 2 - до достижения заданной точности): ")

if choice == "1":
    number_of_terms = int(input("Введите количество членов ряда: "))  # Ввод количества членов ряда
    result = calculate_series_fixed(x_value, number_of_terms)  # Вычисление ряда с фиксированным количеством членов
    print(f"Значение ряда при x = {x_value} и {number_of_terms} членах: {result}")  # Вывод результата
elif choice == "2":
    epsilon = 1e-6  # Установка значения epsilon
    result = calculate_series_until_epsilon(x_value, epsilon)  # Вычисление ряда до достижения заданной точности
    print(f"Значение ряда при x = {x_value} и epsilon = {epsilon}: {result}")  # Вывод результата
else:
    print("Неверный выбор метода.")  # Вывод сообщения об ошибке
