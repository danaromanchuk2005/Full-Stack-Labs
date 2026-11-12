import os
import time
import csv
from collections import Counter
from datetime import datetime

# =====================================================================
# БЛОК ПІДГОТОВКИ: Автоматичне створення потрібних файлів для лабораторної
# =====================================================================
# Для Завдання 1
with open("numbers.txt", "w", encoding="utf-8") as f:
    f.write("10\n20\n30\n40\n50\n60\n70\n80\n90\n100")
# Для Завдання 3 та 4
with open("learning_python.txt", "w", encoding="utf-8") as f:
    f.write("Python можна використати для створення веб-сайтів.\n")
    f.write("Python можна використати для штучного інтелекту та машинного навчання.\n")
    f.write("Python можна використати для аналізу великих даних.\n")
    f.write("Python можна використати для розробки ігор.\n")
# Для Завдання 6 (Коротка імітація великого англійського тексту)
with open("python_article.txt", "w", encoding="utf-8") as f:
    f.write("Python is a great programming language. " * 300) 
# Для Завдання 7 (Генеруємо тестовий marks.csv: Студент, Оцінка, Час, П1, П2, П3)
with open("marks.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Student", "Grade", "Time_min", "Q1", "Q2", "Q3"])
    writer.writerows([
        ["Student1", 95, 45, 1, 1, 1], ["Student2", 80, 45, 1, 0, 1],
        ["Student3", 60, 30, 0, 0, 1], ["Student4", 95, 50, 1, 1, 1],
        ["Student5", 100, 40, 1, 1, 1], ["Student6", 75, 30, 1, 1, 0]
    ])
# =====================================================================

print("--- ЗАВДАННЯ 1 ---")
# Зчитуємо 10 чисел з файлу numbers.txt, обчислюємо суму та записуємо в sum_numbers.txt
with open("numbers.txt", "r", encoding="utf-8") as f:
    # Читаємо рядки, прибираємо зайві пробіли/перенесення і перетворюємо на int
    numbers = [int(line.strip()) for line in f if line.strip()]

total_sum = sum(numbers)
print(f"Зчитані числа: {numbers}")
print(f"Сума чисел: {total_sum}")

# Записуємо отриману суму в новий файл
with open("sum_numbers.txt", "w", encoding="utf-8") as f:
    f.write(f"Сума чисел: {total_sum}\n")
print("Суму успішно записано у файл 'sum_numbers.txt'.")


print("\n--- ЗАВДАННЯ 2 ---")
# Зчитуємо довільну кількість чисел з командного рядка (через input для зручності)
input_nums = input("Введіть кілька цілих чисел через пробіл (наприклад: 4 7 10 15): ").split()
with open("parity_info.txt", "w", encoding="utf-8") as f:
    for num_str in input_nums:
        if num_str.isdigit() or (num_str.startswith('-') and num_str[1:].isdigit()):
            num = int(num_str)
            # Перевіряємо на парність і записуємо у файл
            parity = "парне" if num % 2 == 0 else "непарне"
            f.write(f"Число {num} є {parity}.\n")
print("Інформацію про парність записано у файл 'parity_info.txt'.")


print("\n--- ЗАВДАННЯ 3 ---")
# Зчитуємо файл, зберігаємо рядки у список і сортуємо за довжиною (від найбільшого)
with open("learning_python.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Сортуємо список рядків за їх довжиною (len) у зворотному порядку (reverse=True)
sorted_lines = sorted(lines, key=len, reverse=True)
print("Рядки, відсортовані за довжиною (за спаданням):")
for line in sorted_lines:
    print(line.strip())


print("\n--- ЗАВДАННЯ 4 ---")
# Створюємо новий каталог, якщо його ще не існує
new_dir = "C_language_data"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)

true_statements_file = os.path.join(new_dir, "true_statements.txt")
false_statements_file = os.path.join(new_dir, "false_statements.txt")

with open("learning_python.txt", "r", encoding="utf-8") as f_in, \
     open(true_statements_file, "w", encoding="utf-8") as f_true, \
     open(false_statements_file, "w", encoding="utf-8") as f_false:
     
    print("Проаналізуйте твердження для мови C (Введіть 'так' або 'ні'):")
    for line in f_in:
        # Замінюємо слово Python на C
        c_line = line.replace("Python", "C").strip()
        print(f"Твердження: {c_line}")
        answer = input("Це актуально для мови C? (т/н): ").strip().lower()
        
        # Розподіляємо твердження по різних файлах залежно від відповіді користувача
        if answer == 'т' or answer == 'так':
            f_true.write(c_line + "\n")
        else:
            f_false.write(c_line + "\n")
print(f"Результати розсортовано у папку '{new_dir}'.")


print("\n--- ЗАВДАННЯ 5 ---")
guest_file = "guest_book.txt"
# Створюємо порожній файл
open(guest_file, "w", encoding="utf-8").close() 

while True:
    name = input("Введіть ім'я гостя (або 'стоп' для завершення): ").strip()
    if name.lower() == 'стоп':
        break
    
    greeting = f"Вітаємо, {name}!"
    print(greeting)
    
    # Дописуємо вітання та поточний час у файл (режим 'a' - append)
    with open(guest_file, "a", encoding="utf-8") as f:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{current_time}] {greeting}\n")

# Отримуємо час створення та час останньої модифікації файлу через модуль os
creation_time = time.ctime(os.path.getctime(guest_file))
mod_time = time.ctime(os.path.getmtime(guest_file))
print(f"Файл {guest_file} створено: {creation_time}")
print(f"Останні зміни внесено: {mod_time}")


print("\n--- ЗАВДАННЯ 6 ---")
start_search_time = time.time() # Засікаємо час початку пошуку

with open("python_article.txt", "r", encoding="utf-8") as f:
    text = f.read().lower() # Читаємо все в нижньому регістрі

# Аналізуємо частоту слів
words = text.split()
word_counts = Counter(words)
most_common_words = word_counts.most_common(5) # Топ 5 найчастіших слів

end_search_time = time.time()
search_duration = end_search_time - start_search_time

result_str = f"Топ 5 слів: {most_common_words}\nЧас пошуку: {search_duration:.5f} сек.\n"
print(result_str)

# Зберігаємо результати з часовими мітками в окремий файл
analysis_file = "analysis_results.txt"
with open(analysis_file, "w", encoding="utf-8") as f:
    f.write(f"Час створення звіту: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(result_str)
print("Результати аналізу збережено у 'analysis_results.txt'.")


print("\n--- ЗАВДАННЯ 7 ---")
students_count = 0
grade_counts = Counter()
time_grades = {} # Для середньої оцінки за час
questions_stats = {"Q1": [], "Q2": [], "Q3": []}
best_efficiency = [] # Оцінка / Час

with open("marks.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        students_count += 1
        grade = int(row["Grade"])
        time_spent = int(row["Time_min"])
        
        grade_counts[grade] += 1
        
        # Групуємо оцінки за часом виконання
        if time_spent not in time_grades:
            time_grades[time_spent] = []
        time_grades[time_spent].append(grade)
        
        # Статистика правильних відповідей (1 - правильно, 0 - ні)
        questions_stats["Q1"].append(int(row["Q1"]))
        questions_stats["Q2"].append(int(row["Q2"]))
        questions_stats["Q3"].append(int(row["Q3"]))
        
        # Вираховуємо ефективність: бал за хвилину
        efficiency = grade / time_spent if time_spent > 0 else 0
        best_efficiency.append((row["Student"], grade, time_spent, efficiency))

print(f"Загальна кількість студентів: {students_count}")
print(f"Розподіл оцінок: {dict(grade_counts)}")

print("Середня оцінка за час виконання (хв):")
for t, grades in sorted(time_grades.items()):
    avg = sum(grades) / len(grades)
    print(f"  {t} хв: {avg:.1f} балів")

# Відсортуємо топ-5 за ефективністю (найбільший бал за хвилину)
best_efficiency.sort(key=lambda x: x[3], reverse=True)
top_5 = best_efficiency[:5]

# Записуємо детальну статистику в текстовий файл
with open("exam_stats.txt", "w", encoding="utf-8") as f:
    f.write("--- Статистика правильних відповідей ---\n")
    for q, results in questions_stats.items():
        correct_pct = (sum(results) / len(results)) * 100
        incorrect_pct = 100 - correct_pct
        f.write(f"{q}: Правильно {correct_pct:.1f}%, Неправильно {incorrect_pct:.1f}%\n")
        
    f.write("\n--- Топ 5 найкращих оцінок (Оцінка / Час) ---\n")
    for student, grade, t, eff in top_5:
        f.write(f"{student}: Оцінка {grade}, Час {t} хв (Ефективність: {eff:.2f} балів/хв)\n")
        
print("Повну статистику іспита збережено у 'exam_stats.txt'.")