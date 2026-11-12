import random

# --- Підготовка: Створюємо модулі для завдань 8 і 9 ---
with open("shop_module.py", "w", encoding="utf-8") as f:
    f.write("""
class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
    def open_shop(self):
        print(f"Магазин {self.shop_name} ВІДКРИТИЙ!")
""")

with open("user_module.py", "w", encoding="utf-8") as f:
    f.write("""
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def greeting_user(self):
        print(f"Вітаємо, {self.first_name} {self.last_name} з модуля!")
""")

with open("admin_module.py", "w", encoding="utf-8") as f:
    f.write("""
from user_module import User
class Privileges:
    def __init__(self):
        self.privileges = ["Allowed to add message", "Allowed to ban users"]
    def show_privileges(self):
        print("Привілеї:", self.privileges)
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.priv = Privileges()
""")

print("--- Завдання 1: Клас Bank ---")
class Bank:
    def __init__(self, initial_balance):
        self.__balance = initial_balance
    def deposit(self, amount):
        self.__balance += amount
        print(f"Поповнено на {amount}. Баланс: {self.__balance}")
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Знято {amount}. Баланс: {self.__balance}")
        else:
            print("Недостатньо коштів!")
            
my_account = Bank(1000)
my_account.deposit(500)
my_account.withdraw(300)

print("\n--- Завдання 2: Клас Coin ---")
class Coin:
    def __init__(self):
        self.__sideup = "heads"
    def toss(self):
        self.__sideup = random.choice(["heads", "tails"])
        return self.__sideup

my_coin = Coin()
print("Підкидаємо монету 5 разів:")
for i in range(5): print(my_coin.toss(), end=" | ")
print()

print("\n--- Завдання 3: Клас Car ---")
class Car:
    def __init__(self, make, model, year):
        self.make = make; self.model = model; self.year = year; self.speed = 0
    def accelerate(self): self.speed += 5
    def brake(self): self.speed -= 5
    def get_speed(self): return self.speed

my_car = Car("Porsche", "911", 2026)
print("Розганяємось:")
for _ in range(5):
    my_car.accelerate()
    print(f"Швидкість: {my_car.get_speed()} км/год")
print("Гальмуємо:")
for _ in range(5):
    my_car.brake()
    print(f"Швидкість: {my_car.get_speed()} км/год")

print("\n--- Завдання 4: Класи Dog та Pets ---")
class Dog:
    mammal = True; nature = "Добрий"; breed = "Звичайна"
    def __init__(self, name, age):
        self.name = name; self.age = age
    def show_info(self):
        print(f"Собака {self.name}, Вік: {self.age}, Порода: {self.breed}")

class Husky(Dog):
    breed = "Хаскі"
    def bark(self): print(f"{self.name} каже: Ааа-ууууу!")

class Pets:
    def __init__(self, animals): self.animals = animals
    def print_pets(self):
        print(f"У мене є {len(self.animals)} собаки:")
        for pet in self.animals: pet.show_info()

dogs = [Dog("Рекс", 5), Husky("Локі", 2)]
my_pets = Pets(dogs)
my_pets.print_pets()
dogs[1].bark()

print("\n--- Завдання 5: Клас Buffer ---")
class Buffer:
    def __init__(self): self.elements = []
    def add(self, *a):
        self.elements.extend(a)
        while len(self.elements) >= 5:
            chunk = self.elements[:5]
            print(f"Сума п'ятірки {chunk}: {sum(chunk)}")
            self.elements = self.elements[5:]
    def get_current_part(self): return self.elements

buf = Buffer()
buf.add(1, 2, 3)
print("Поточний буфер:", buf.get_current_part())
buf.add(4, 5, 6, 7)

print("\n--- Завдання 6: Власний виняток (Exception) ---")
class NameLengthError(ValueError): pass
name_input = "Dana"
try:
    if len(name_input) < 10: raise NameLengthError(f"Помилка: '{name_input}' менше 10 символів!")
except NameLengthError as e:
    print(e)

print("\n--- Завдання 7: Римські цифри ---")
class RomanConverter:
    @staticmethod
    def to_roman(num):
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sybs = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ''; i = 0
        while num > 0:
            for _ in range(num // vals[i]):
                roman += sybs[i]; num -= vals[i]
            i += 1
        return roman
print(f"2026 римськими: {RomanConverter.to_roman(2026)}")

print("\n--- Завдання 8 та 9: Магазин та Адмін (з імпортом) ---")
import shop_module
all_store = shop_module.Shop("Сільпо", "Супермаркет")
all_store.open_shop()

import admin_module
admin = admin_module.Admin("Богдана", "Романчук")
print("Перевірка імпорту привілеїв:")
admin.priv.show_privileges()