import math

def calculate_series_fixed(x, n):
    y = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
        y += term
    return y

def calculate_series_until_epsilon(x, eps):
    y = 0
    i = 0
    term = x
    while abs(term) >= eps:
        y += term
        i += 1
        term = -term * (x ** 2) * (2 * i - 1) / (2 * i + 1)
    return y

x_value = float(input("Введите значение x: "))
choice = input("Выберите метод вычисления (1 - фиксированное количество членов, 2 - до достижения заданной точности): ")

if choice == "1":
    number_of_terms = int(input("Введите количество членов ряда: "))
    result = calculate_series_fixed(x_value, number_of_terms)
    print(f"Значение ряда при x = {x_value} и {number_of_terms} членах: {result}")
elif choice == "2":
    epsilon = 1e-6
    result = calculate_series_until_epsilon(x_value, epsilon)
    print(f"Значение ряда при x = {x_value} и epsilon = {epsilon}: {result}")
else:
    print("Неверный выбор метода.")