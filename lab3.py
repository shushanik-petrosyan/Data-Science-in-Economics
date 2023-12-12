import csv
# 1. Сначала определяется класс Record, который представляет отдельную запись в базе данных.
#  У него есть три атрибута: ФИО студента, группа и средний балл.
class Record:
    def __init__(self, fio, group, average_score):
        self.fio = fio
        self.group = group
        self.average_score = average_score

# Затем определяется класс SimpleDB, представляющий саму базу данных.
#  В конструкторе этого класса инициализируется пустой список записей.
class SimpleDB:
    def __init__(self):
        self.records = []

# загружает записи из файла CSV и добавляет их в базу данных.
    def load_from_csv(self, filename):
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                self.records.append(Record(row[0], row[1], float(row[2])))

# сохраняет записи из базы данных в файл CSV.
    def save_to_csv(self, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['FIO', 'Group', 'Average Score'])
            for record in self.records:
                writer.writerow([record.fio, record.group, record.average_score])

# выводит все записи на экран.
    def display_records(self):
        for record in self.records:
            print(f"FIO: {record.fio}, Group: {record.group}, Average Score: {record.average_score}")

#  добавляет новую запись
    def add_record(self, fio, group, average_score):
        self.records.append(Record(fio, group, average_score))

# ищет запись по ключевому полю (ФИО)
    def search_by_key(self, key):
        for record in self.records:
            if record.fio == key:
                print(f"Record found - FIO: {record.fio}, Group: {record.group}, Average Score: {record.average_score}")
                return
        print("Record with the given key not found.")

# удаляет запись по ключевому полю (ФИО).
    def delete_record(self, key):
        for record in self.records:
            if record.fio == key:
                self.records.remove(record)
                print("Record deleted successfully.")
                return
        print("Record with the given key not found.")

#  выполняет индивидуальное задание - агрегирует данные по группам и выводит информацию 
# о количестве элементов и среднем значении среднего балла в каждой группе.
    def individual_task(self):
        group_data = {}
        for record in self.records:
            if record.group in group_data:
                group_data[record.group].append(record.average_score)
            else:
                group_data[record.group] = [record.average_score]

        for group, scores in group_data.items():
            print(f"Group: {group} - Count: {len(scores)} - Average Score: {sum(scores) / len(scores)}")

# В функции main создается экземпляр класса SimpleDB 
# и запускается бесконечный цикл, предлагающий пользователю выбрать операцию.
def main():
    db = SimpleDB()

    while True:
        print("\nМеню операций:")
        print("1. Загрузка базы из файла формата csv")
        print("2. Сохранение базы в файл формата csv")
        print("3. Вывод содержимого базы на экран")
        print("4. Добавление новой записи в базу")
        print("5. Поиск и вывод на экран записи по ключевому полю")
        print("6. Удаление записи по ключевому полю")
        print("7. Выполнение индивидуального задания. (Агрегировать данные по второму полю. Вывести на экран информацию вида (2 поле) – (количество элементов) – (среднее значение поля 3)")
        print("8. Выход")

        choice = input("Введите номер операции: ")

        if choice == '1':
            filename = input("Введите имя файла для загрузки: ")
            db.load_from_csv(filename)
        elif choice == '2':
            filename = input("Введите имя файла для сохранения: ")
            db.save_to_csv(filename)
        elif choice == '3':
            db.display_records()
        elif choice == '4':
            fio = input("Введите ФИО студента: ")
            group = input("Введите группу: ")
            average_score = float(input("Введите средний балл: "))
            db.add_record(fio, group, average_score)
        elif choice == '5':
            key = input("Введите ключевое поле для поиска: ")
            db.search_by_key(key)
        elif choice == '6':
            key = input("Введите ключевое поле для удаления: ")
            db.delete_record(key)
        elif choice == '7':
            db.individual_task()
        elif choice == '8':
            print("Завершение работы.")
            break
        else:
            print("Некорректный выбор операции. Повторите попытку.")


# 5. В зависимости от выбора пользователя вызывается 
# соответствующий метод класса SimpleDB для выполнения соответствующей операции.
# 6. Программа завершает выполнение, если пользователь выбирает операцию "Выход".
if __name__ == "__main__":
    main()
