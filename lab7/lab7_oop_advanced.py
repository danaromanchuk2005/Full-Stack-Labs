import os
import csv
import string

# Блок для безпечного підключення бібліотеки графіків (matplotlib)
try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

# =====================================================================
# БЛОК ПІДГОТОВКИ: Автоматичне створення CSV файлів для Завдання 4
# =====================================================================
def create_mock_csv(filename, num_students):
    with open(filename, "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "grade", "time_min", "q1", "q2", "q3", "q4", "q5"])
        import random
        for i in range(1, num_students + 1):
            grade = random.choice([60, 75, 80, 95, 100])
            time_m = random.randint(20, 60)
            q = [random.choice([0, 1]) for _ in range(5)]
            writer.writerow([f"S{i:03d}", grade, time_m] + q)

create_mock_csv("kmr1.csv", 20)
create_mock_csv("kmr2.csv", 25)
# =====================================================================

print("================ ЗАВДАННЯ 1: Alphabet та EngAlphabet ================")

class Alphabet:
    # Статичні атрибути для української мови
    lang = "UA"
    letters = list("АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ")

    def __init__(self, lang=lang, letters=letters):
        self.lang = lang
        self.letters = letters

    def print_alphabet(self):
        print(f"Алфавіт ({self.lang}):", " ".join(self.letters))

    def letters_num(self):
        return len(self.letters)

    def is_ua_lang(self, text):
        # Перевіряє, чи є хоча б одна українська літера в тексті
        text = text.upper()
        return any(char in self.letters for char in text)

class EngAlphabet(Alphabet):
    __en_letters_num = 26 # Приватний статичний атрибут

    def __init__(self):
        # Виклик батьківського __init__ з англійськими параметрами
        super().__init__(lang="En", letters=list(string.ascii_uppercase))

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        # Перевизначений метод повертає статичний атрибут
        return self.__en_letters_num

    @staticmethod
    def example():
        return "Python is a great programming language!"

# Тести для Завдання 1
eng_alpha = EngAlphabet()
eng_alpha.print_alphabet()
print(f"Кількість букв в англійському алфавіті: {eng_alpha.letters_num()}")
print(f"Чи 'J' відноситься до English? -> {eng_alpha.is_en_letter('J')}")
ua_alpha = Alphabet()
print(f"Чи 'Щ' відноситься до Української? -> {ua_alpha.is_ua_lang('Щ')}")
print(f"Приклад англійського тексту: {EngAlphabet.example()}")


print("\n================ ЗАВДАННЯ 2: Human, House, SmallHouse ================")

class House:
    def __init__(self, area=50, price=50000):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount / 100)

class SmallHouse(House):
    def __init__(self, price=30000):
        # Викликаємо конструктор батька, жорстко задаючи площу 40
        super().__init__(area=40, price=price)

class Human:
    default_name = "Unknown"
    default_age = 0

    def __init__(self, name=default_name, age=default_age, money=0, house=None):
        self.name = name
        self.age = age
        self.__money = money   # Приватний атрибут
        self.__house = house   # Приватний атрибут

    def info(self):
        house_status = "Є будинок" if self.__house else "Немає будинку"
        print(f"Ім'я: {self.name}, Вік: {self.age}, Гроші: {self.__money}$, Статус: {house_status}")

    @staticmethod
    def default_info():
        print(f"Дефолтне ім'я: {Human.default_name}, Дефолтний вік: {Human.default_age}")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house
        print(f"Угода успішна! Куплено будинок за {price}$.")

    def earn_money(self, amount):
        self.__money += amount
        print(f"Зароблено {amount}$. Поточний баланс: {self.__money}$")

    def buy_house(self, house, discount=10):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print(f"[ПОПЕРЕДЖЕННЯ] Недостатньо грошей для покупки! Потрібно {price}$, а є {self.__money}$.")

# Тести для Завдання 2
Human.default_info()
person = Human(name="Богдана", age=23, money=10000)
person.info()
cozy_house = SmallHouse(price=35000)
person.buy_house(cozy_house) # Спроба купити (грошей мало)
person.earn_money(30000)     # Заробляємо
person.buy_house(cozy_house) # Друга спроба
person.info()


print("\n================ ЗАВДАННЯ 3: Apple, AppleTree, Gardener ================")

class Apple:
    states = {0: "Відсутнє", 1: "Цвітіння", 2: "Зелене", 3: "Червоне"}

    def __init__(self, index):
        self._index = index
        self._state = 0 # Початкова стадія (Відсутнє)

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3

class AppleTree:
    def __init__(self, count):
        self.apples = [Apple(i) for i in range(1, count + 1)]

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        return all(apple.is_ripe() for apple in self.apples)

    def give_away_all(self):
        self.apples = []
        print("Дерево тепер порожнє. Урожай зібрано!")

class Gardener:
    def __init__(self, name, tree):
        self.name = name
        self._tree = tree

    def work(self):
        print(f"Садівник {self.name} працює (поливає дерево)...")
        self._tree.grow_all()

    def harvest(self):
        if self._tree.all_are_ripe():
            print(f"Садівник {self.name} збирає врожай!")
            self._tree.give_away_all()
        else:
            print("[ПОПЕРЕДЖЕННЯ] Яблука ще не дозріли. Рано збирати!")

    @staticmethod
    def apple_base(tree):
        print(f"Довідка: На дереві {len(tree.apples)} яблук.")
        for apple in tree.apples:
            print(f" Яблуко №{apple._index} - Стадія: {Apple.states[apple._state]}")

# Тести для Завдання 3
tree = AppleTree(3)
dana_gardener = Gardener("Богдана", tree)
Gardener.apple_base(tree) # Початкова довідка
dana_gardener.harvest()   # Спроба зібрати відразу
for _ in range(3):        # Працюємо 3 рази, щоб яблука стали "Червоними"
    dana_gardener.work()
Gardener.apple_base(tree) # Перевіряємо стадію
dana_gardener.harvest()   # Збираємо врожай


print("\n================ ЗАВДАННЯ 4: KmrCsv, Statistic, Plots, KmrWork ================")
# --- Базові класи (Міксини) ---
class KmrCsv:
    def __init__(self, ref="", num=1):
        self.ref = ref
        self.num = num
        self._data = []

    def load_data(self):
        self._data = []
        with open(self.ref, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self._data.append(row)

    def file_info(self):
        print(f"Файл: КМР №{self.num}, Виконали студентів: {len(self._data)}")

class Statistic:
    def avg_stat(self, data):
        if not data: return ()
        q_keys = [k for k in data[0].keys() if k.startswith('q')]
        stats = []
        for q in q_keys:
            correct = sum(int(row[q]) for row in data)
            stats.append((correct / len(data)) * 100)
        return tuple(stats)

    def marks_stat(self, data):
        marks = {}
        for row in data:
            g = int(row['grade'])
            marks[g] = marks.get(g, 0) + 1
        return marks

    def marks_per_time(self, data):
        mpt = {}
        for row in data:
            mpt[row['id']] = int(row['grade']) / int(row['time_min'])
        return mpt

    def best_marks_per_time(self, data, bottom_margin, top_margin):
        filtered = []
        for row in data:
            g = int(row['grade'])
            if bottom_margin <= g <= top_margin:
                filtered.append((row['id'], g, g / int(row['time_min'])))
        # Сортуємо за середнім балом (індекс 2) за спаданням і беремо топ-5
        filtered.sort(key=lambda x: x[2], reverse=True)
        return tuple(filtered[:5])

class Plots:
    def set_cat(self, cat_name):
        self.cat = cat_name
        if not os.path.exists(self.cat):
            os.mkdir(self.cat)

    def _check_plt(self):
        if not MATPLOTLIB_AVAILABLE:
            print("[INFO] Бібліотека matplotlib не встановлена. Графік пропущено. Щоб малювати, введіть у терміналі: pip3 install matplotlib")
            return False
        return True

    def avg_plot(self, avg_tuple, filename="avg_plot.png"):
        if not self._check_plt(): return
        plt.figure()
        plt.bar([f"Q{i+1}" for i in range(len(avg_tuple))], avg_tuple, color='skyblue')
        plt.title("Відсоток правильних відповідей")
        plt.savefig(os.path.join(self.cat, filename))
        plt.close()
        print(f"Графік збережено: {filename}")

    def marks_plot(self, marks_dict, filename="marks_plot.png"):
        if not self._check_plt(): return
        plt.figure()
        plt.bar(list(marks_dict.keys()), list(marks_dict.values()), color='lightgreen', width=3)
        plt.title("Розподіль оцінок")
        plt.savefig(os.path.join(self.cat, filename))
        plt.close()
        print(f"Графік збережено: {filename}")

# --- Головний клас, що успадковує всі 3 класи (Множинне наслідування) ---
class KmrWork(KmrCsv, Statistic, Plots):
    kmrs = {}
    cat = "KMR_Results"

    def __init__(self, ref, num):
        # Ініціалізуємо базовий клас Csv
        KmrCsv.__init__(self, ref, num)
        self.load_data()
        self.set_cat(self.cat)
        KmrWork.kmrs[num] = ref

    def compare_csv(self, other_kmr):
        s1, s2 = len(self._data), len(other_kmr._data)
        avg_g1 = sum(int(r['grade']) for r in self._data) / s1
        avg_g2 = sum(int(r['grade']) for r in other_kmr._data) / s2
        avg_t1 = sum(int(r['time_min']) for r in self._data) / s1
        avg_t2 = sum(int(r['time_min']) for r in other_kmr._data) / s2

        report = (
            f"--- ПОРІВНЯННЯ КМР {self.num} та КМР {other_kmr.num} ---\n"
            f"Студентів: {s1} проти {s2}\n"
            f"Середній бал: {avg_g1:.1f} проти {avg_g2:.1f}\n"
            f"Середній час (хв): {avg_t1:.1f} проти {avg_t2:.1f}\n"
        )
        print(report)
        with open(os.path.join(self.cat, "comparison.txt"), "w", encoding="utf-8") as f:
            f.write(report)

    def compare_avg_plots(self, other_kmr):
        # Генеруємо графіки для обох КМР
        self.avg_plot(self.avg_stat(self._data), f"kmr{self.num}_avg.png")
        self.avg_plot(self.avg_stat(other_kmr._data), f"kmr{other_kmr.num}_avg.png")


# Тести для Завдання 4
print("--- Ініціалізація КМР ---")
kmr1 = KmrWork("kmr1.csv", 1)
kmr2 = KmrWork("kmr2.csv", 2)

kmr2.file_info()
print("Словник оцінок КМР 2:", kmr2.marks_stat(kmr2._data))
print("Топ 5 швидких і розумних (бал > 75):", kmr2.best_marks_per_time(kmr2._data, 75, 100))

print("\n--- Генерація графіків для КМР 2 ---")
kmr2.avg_plot(kmr2.avg_stat(kmr2._data), "kmr2_single_avg.png")
kmr2.marks_plot(kmr2.marks_stat(kmr2._data), "kmr2_marks.png")

print("\n--- Порівняння КМР 1 та КМР 2 ---")
kmr1.compare_csv(kmr2)
kmr1.compare_avg_plots(kmr2)