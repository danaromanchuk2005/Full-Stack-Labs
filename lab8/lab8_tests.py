import os
import unittest

# =====================================================================
# БЛОК ПІДГОТОВКИ: Автоматичне створення модулів з класами (ЛР №8)
# =====================================================================
# 1. Модуль магазину
with open("shop_models.py", "w", encoding="utf-8") as f:
    f.write('''\
class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def set_number_of_units(self, val):
        self.number_of_units = val

    def increment_number_of_units(self, val):
        self.number_of_units += val

class Discount(Shop):
    def __init__(self, shop_name, store_type):
        super().__init__(shop_name, store_type)
        self.discount_products = ["Яблука", "Банани", "Одяг"]
''')

# 2. Модуль користувача
with open("user_models.py", "w", encoding="utf-8") as f:
    f.write('''\
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
''')

# 3. Модуль адміністратора (успадковує User)
with open("admin_models.py", "w", encoding="utf-8") as f:
    f.write('''\
from user_models import User

class Privileges:
    def __init__(self):
        self.privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.priv = Privileges()
''')

# =====================================================================
# БЛОК ТЕСТУВАННЯ (UNITTEST)
# =====================================================================
# Імпортуємо щойно створені модулі
import shop_models
import user_models
import admin_models

class TestShop(unittest.TestCase):
    def setUp(self):
        # Цей метод запускається перед кожним тестом (готуємо "чистий" об'єкт)
        self.store = shop_models.Shop("Сільпо", "Супермаркет")

    def test_initial_units(self):
        # Перевіряємо, чи за замовчуванням кількість товарів дорівнює 0
        self.assertEqual(self.store.number_of_units, 0, "Початкова кількість товарів має бути 0")

    def test_set_units(self):
        # Перевіряємо метод встановлення кількості
        self.store.set_number_of_units(50)
        self.assertEqual(self.store.number_of_units, 50, "Метод set_number_of_units працює некоректно")

    def test_increment_units(self):
        # Перевіряємо метод додавання (інкременту)
        self.store.increment_number_of_units(10)
        self.store.increment_number_of_units(5)
        self.assertEqual(self.store.number_of_units, 15, "Метод increment не додає значення правильно")

class TestDiscount(unittest.TestCase):
    def test_discount_inheritance(self):
        # Перевіряємо, чи правильно працює успадкування від Shop
        discount_store = shop_models.Discount("Атб", "Дискаунтер")
        self.assertTrue(hasattr(discount_store, 'discount_products'), "Клас Discount не має списку товарів")
        self.assertEqual(discount_store.store_type, "Дискаунтер")

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = user_models.User("Богдана", "Романчук")

    def test_login_attempts(self):
        # Перевіряємо правильність підрахунку спроб входу
        self.assertEqual(self.user.login_attempts, 0)
        self.user.increment_login_attempts()
        self.user.increment_login_attempts()
        self.assertEqual(self.user.login_attempts, 2, "Інкремент логінів не працює")
        self.user.reset_login_attempts()
        self.assertEqual(self.user.login_attempts, 0, "Скидання логінів не працює")

class TestAdmin(unittest.TestCase):
    def test_admin_privileges(self):
        # Перевіряємо створення адміна та його привілеїв (агрегація класу Privileges)
        admin = admin_models.Admin("Юрій", "Скрипник")
        self.assertTrue(hasattr(admin, 'priv'), "Адмін не має об'єкта Privileges")
        self.assertIn("Allowed to ban users", admin.priv.privileges, "Немає прав на бан користувачів")

if __name__ == '__main__':
    # Запускаємо всі тести з детальнішим виведенням (verbosity=2)
    unittest.main(verbosity=2)