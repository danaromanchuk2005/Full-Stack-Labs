import csv
import datetime

# --- Підготовка: створюємо стартовий файл контактів ---
with open("contacts.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["surname", "first_name", "nickname", "birth_date"])
    writer.writerow(["Романчук", "Богдана", "Dana", "2003-05-15"])
    writer.writerow(["Скрипник", "Юрій", "Yura", "2002-11-20"])

print("--- Завдання 1: Клас Person ---")
class Person:
    def __init__(self, surname, first_name, birth_date_str, nickname=""):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        # Розбираємо рядок дати
        parts = birth_date_str.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        self.birth_date = datetime.date(year, month, day)

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return str(age)

    def get_fullname(self):
        return f"{self.surname} {self.first_name}"

print("Клас Person успішно створено.")

print("\n--- Завдання 2: Функція modifier ---")
def modifier(filename):
    persons = []
    out_filename = "modified_" + filename
    
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            p = Person(row['surname'], row['first_name'], row['birth_date'], row['nickname'])
            persons.append(p)
            
    fieldnames = ['surname', 'first_name', 'fullname', 'nickname', 'birth_date', 'age']
    with open(out_filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for p in persons:
            writer.writerow({
                'surname': p.surname,
                'first_name': p.first_name,
                'fullname': p.get_fullname(),
                'nickname': p.nickname,
                'birth_date': p.birth_date.strftime("%Y-%m-%d"),
                'age': p.get_age()
            })
    print(f"Файл {out_filename} успішно розширено (додано fullname та age).")

modifier("contacts.csv")