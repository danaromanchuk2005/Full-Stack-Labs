import math # Для математичних обчислень (корінь, гіпотенуза)
import random # Для генерації випадкових списків
import time # Для вимірювання часу (завдання 9)

# --- ДЕКОРАТОР ДЛЯ ЗАВДАНЬ 6-8 (ВИМОГА ЗАВДАННЯ 9) ---
# Декоратор - це функція, яка "обгортає" іншу функцію для додавання нового функціоналу (тут: таймера)
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() # Засікаємо час ДО початку виконання
        result = func(*args, **kwargs) # Виконуємо саму функцію
        end_time = time.time() # Засікаємо час ПІСЛЯ виконання
        # Розраховуємо різницю і виводимо результат
        print(f"[Таймер] Функція {func.__name__} виконувалася {end_time - start_time:.5f} секунд.")
        return result # Повертаємо результат роботи функції
    return wrapper # Повертаємо обгортку

print("--- ЗАВДАННЯ 1 ---")
# Функція для розрахунку площі прямокутника
def rect_area(a, b):
    return a * b # Площа = ширина * довжина

for i in range(1, 4): # Цикл працює 3 рази (для трьох прямокутників)
    # Зчитуємо дві сторони, розбиваємо по пробілу, перетворюємо на float (дробові)
    sides = input(f"Введіть дві сторони прямокутника №{i} через пробіл (наприклад: 5 10): ").split()
    a, b = float(sides[0]), float(sides[1]) # Присвоюємо значення a і b
    print(f"Площа прямокутника №{i}: {rect_area(a, b)}")

print("\n--- ЗАВДАННЯ 2 ---")
# Функція для обчислення гіпотенузи (за теоремою Піфагора)
def calc_hypotenuse(katet1, katet2):
    return math.hypot(katet1, katet2) # Вбудована математична функція

print("Генеруємо два трикутники для перевірки...")
# Для швидкості і зручності генеруємо катети програмно
h1 = calc_hypotenuse(3, 4) # Катети 3 і 4 (гіпотенуза буде 5)
h2 = calc_hypotenuse(5, 12) # Катети 5 і 12 (гіпотенуза буде 13)
print(f"Гіпотенуза 1: {h1}, Гіпотенуза 2: {h2}")
# Порівнюємо гіпотенузи
if h1 > h2:
    print("Перша гіпотенуза більша за другу.")
elif h1 < h2:
    print("Друга гіпотенуза більша за першу.")
else:
    print("Гіпотенузи рівні.")

print("\n--- ЗАВДАННЯ 3 ---")
# Функція перевірки, чи точка лежить всередині кола
# Рівняння кола: (x-a)^2 + (y-b)^2 <= R^2
def is_inside(x, y, a, b, R):
    return (x - a)**2 + (y - b)**2 <= R**2

# Задаємо координати центру кола і радіус
a_circle, b_circle, R_circle = 0, 0, 5 
# Точки Р, F, L
P, F, L = (3, 4), (6, 6), (-1, -1) 
points = [P, F, L]
inside_count = 0 # Лічильник точок всередині кола
for pt in points:
    # Передаємо координати точки та кола у функцію
    if is_inside(pt[0], pt[1], a_circle, b_circle, R_circle):
        inside_count += 1
print(f"Кількість точок, що лежать всередині кола: {inside_count} з 3")

print("\n--- ЗАВДАННЯ 4 ---")
# Функція площі чотирикутника (кут між X і Y - прямий)
def quad_area(x, y, z, t):
    area_xy = 0.5 * x * y # Площа першого прямокутного трикутника
    d = math.hypot(x, y) # Діагональ (вона ж гіпотенуза першого трикутника)
    # Площа другого трикутника за формулою Герона (сторони Z, T, d)
    p = (z + t + d) / 2 # Півпериметр
    # Перевірка, чи взагалі можна побудувати такий трикутник (підкореневий вираз > 0)
    if p*(p-z)*(p-t)*(p-d) <= 0:
        return area_xy # Якщо фігура не замикається, повертаємо хоча б половину
    area_ztd = math.sqrt(p * (p - z) * (p - t) * (p - d))
    return area_xy + area_ztd # Загальна площа фігури

# Тестуємо на сторонах 3, 4, 4, 3 (утворюють прямокутник, складений з двох трикутників)
print(f"Площа чотирикутника (3, 4, 4, 3): {quad_area(3, 4, 4, 3)}")

print("\n--- ЗАВДАННЯ 5 ---")
# Вводимо межу N
n_limit = int(input("Введіть межу N для пошуку чисел (наприклад: 50): "))
# Вводимо дільники
divisors = [int(x) for x in input("Введіть дільники через пробіл (наприклад: 2 3): ").split()]
result_task5 = [] # Список для знайдених чисел
for num in range(1, n_limit + 1):
    # all() перевіряє, чи число ділиться на всі введені дільники без остачі (== 0)
    if all(num % d == 0 for d in divisors):
        result_task5.append(num)
print(f"Числа, що діляться на {divisors}: {result_task5}")

print("\n--- ЗАВДАННЯ 6 (з декоратором) ---")
@timer_decorator # Підключаємо наш декоратор для виміру часу
def find_max_divisors(m, n):
    max_div_count = 0 # Найбільша кількість дільників
    best_num = m # Число з найбільшою кількістю
    for i in range(m, n + 1):
        # Рахуємо дільники (x ділить i без остачі)
        divs = sum(1 for x in range(1, i + 1) if i % x == 0)
        if divs > max_div_count:
            max_div_count = divs
            best_num = i
    return best_num, max_div_count

res_num, res_divs = find_max_divisors(1, 100) # Шукаємо в діапазоні від 1 до 100
print(f"Число {res_num} має найбільше дільників ({res_divs}) в інтервалі [1, 100].")

print("\n--- ЗАВДАННЯ 7 (з декоратором) ---")
@timer_decorator
def find_primes(n, output_format="count"):
    primes = [] # Список простих чисел
    for num in range(2, n + 1):
        is_prime = True # Припускаємо, що число просте
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0: # Якщо знайшли дільник
                is_prime = False # Число не просте
                break
        if is_prime:
            primes.append(num) # Додаємо в список
    
    # Вибір формату виведення
    if output_format == "list":
        print(f"Прості числа (списком): {primes}")
    elif output_format == "column":
        print("Прості числа (у стовпчик):")
        for p in primes: print(p)
    else: # За замовчуванням (count)
        print(f"Знайдено простих чисел: {len(primes)}")
    return primes

find_primes(100, "list") # Викликаємо функцію з виведенням списком

print("\n--- ЗАВДАННЯ 8 (з декоратором і обробкою винятків) ---")
@timer_decorator
def filter_list(lst, bottom_str, upper_str):
    try:
        # Пробуємо перетворити введені дані на цілі числа
        bottom = int(bottom_str)
        upper = int(upper_str)
        # Знаходимо мінімум і максимум масиву
        MIN, MAX = min(lst), max(lst)
        # Формуємо межі вибірки
        lower_bound = MIN + bottom
        upper_bound = MAX - upper
        
        # Якщо межі наклалися (нижня стала більшою за верхню)
        if lower_bound > upper_bound:
            raise ValueError("Вихід за межі діапазону (MIN+bottom > MAX-upper)!")
            
        # Формуємо новий список за умовою
        new_list = [x for x in lst if lower_bound <= x <= upper_bound]
        return new_list
        
    except ValueError as e: # Ловимо помилки типів (дробові, букви або межі)
        print(f"[ПОМИЛКА] {e} (Введено букви, дроби або порушено межі)")
        return []

random_list = [random.randint(1, 100) for _ in range(20)] # Генеруємо список з 20 чисел
print(f"Початковий список: {random_list}")
print(f"MIN: {min(random_list)}, MAX: {max(random_list)}")
b_in = input("Введіть значення bottom (ціле число): ")
u_in = input("Введіть значення upper (ціле число): ")
print(f"Відфільтрований список: {filter_list(random_list, b_in, u_in)}")

print("\n--- ЗАВДАННЯ 9 (Тестування швидкості для 10^n) ---")
# Запускаємо функції для десятків, сотень і тисяч елементів (10^1, 10^2, 10^3)
# Більше 10^4 не беремо, щоб комп'ютер не завис на кілька хвилин :)
for power in range(1, 4): 
    elements = 10**power
    print(f"\n--- Перевірка для N = {elements} ---")
    find_max_divisors(1, elements) # Виклик 6 завдання
    find_primes(elements, "count") # Виклик 7 завдання
    # Виклик 8 завдання з випадковим списком потрібного розміру
    big_list = [random.randint(1, elements) for _ in range(elements)]
    filter_list(big_list, 0, 0)