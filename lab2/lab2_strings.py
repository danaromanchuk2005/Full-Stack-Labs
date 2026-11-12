print("--- ЗАВДАННЯ 1 ---")
# Створюємо змінну з красивим текстом про Київ для перших 8 завдань
text = "Київ: історична столиця України. Тут є все: парки, архітектура, смачна їжа. Багато туристів приїжджають сюди щороку. Прогулянка Подолом залишає прекрасні спогади. Це просто чудове місто!"
print(f"Базовий текст:\n{text}") # Виводимо базовий текст на екран
letter = input("Введіть літеру для пошуку слів (наприклад, 'п'): ") # Просимо ввести літеру
# text.split() розбиває текст на слова. 
# Перебираємо кожне слово (w), робимо його маленьким (.lower()) і перевіряємо першу літеру (.startswith)
words_with_letter = [w for w in text.split() if w.lower().startswith(letter.lower())]
print(f"Кількість слів на літеру '{letter}': {len(words_with_letter)}") # Виводимо результат

print("\n--- ЗАВДАННЯ 2 ---")
# Метод .count() рахує, скільки разів символ ':' зустрічається в тексті
colons_count = text.count(':') 
# Метод .replace() замінює всі двокрапки ':' на відсотки '%'
text_task2 = text.replace(':', '%') 
print(f"Кількість замін двокрапки: {colons_count}") # Виводимо кількість замін
print(f"Текст після заміни:\n{text_task2}") # Виводимо змінений текст

print("\n--- ЗАВДАННЯ 3 ---")
# Рахуємо кількість крапок у нашому тексті
dots_count = text_task2.count('.') 
# Видаляємо крапки (просто замінюємо крапку на порожнечу '')
text_task3 = text_task2.replace('.', '') 
print(f"Кількість видалених крапок: {dots_count}") # Виводимо результат

print("\n--- ЗАВДАННЯ 4 ---")
# Рахуємо кількість літер 'а' в тексті
a_count = text_task3.count('а') 
# Замінюємо всі українські літери 'а' на 'о'
text_task4 = text_task3.replace('а', 'о') 
# Функція len() рахує загальну кількість символів у всьому рядку
total_chars = len(text_task4) 
print(f"Кількість замін 'а' на 'о': {a_count}") 
print(f"Загальна кількість символів у рядку: {total_chars}") 

print("\n--- ЗАВДАННЯ 5 ---")
# Метод .lower() перетворює абсолютно всі ВЕЛИКІ літери в тексті на маленькі
text_task5 = text_task4.lower() 
print(f"Текст малими літерами:\n{text_task5}") # Виводимо текст у нижньому регістрі

print("\n--- ЗАВДАННЯ 6 ---")
# Рахуємо всі літери 'о' (включаючи ті, що ми щойно замінили в 4 завданні)
o_count = text_task5.count('о') 
# Видаляємо всі літери 'о', замінюючи їх на порожнечу ''
text_task6 = text_task5.replace('о', '') 
print(f"Кількість видалених літер 'о': {o_count}") 
print(f"Текст без літер 'о':\n{text_task6}") 

print("\n--- ЗАВДАННЯ 7 ---")
# Знаходимо середину рядка (ділимо довжину тексту націло на 2)
half_len = len(text_task6) // 2 
# Беремо ПЕРШУ половину рядка і замінюємо в ній літеру 'п' на зірочку '*'
first_half = text_task6[:half_len].replace('п', '*') 
# Беремо ДРУГУ половину рядка без змін
second_half = text_task6[half_len:] 
# Склеюємо обидві половини назад в один текст
text_task7 = first_half + second_half 
print(f"Текст із зірочками у першій половині:\n{text_task7}") 

print("\n--- ЗАВДАННЯ 8 ---")
# Просимо користувача ввести ціле слово для пошуку
search_word = input("Введіть слово для пошуку в тексті (наприклад, 'місто'): ") 
# Рахуємо, скільки разів це слово зустрічається
word_count = text.lower().count(search_word.lower()) 
print(f"Слово '{search_word}' зустрічається {word_count} раз(ів).") 

print("\n--- ЗАВДАННЯ 9 ---")
# Створюємо новий текст АНГЛІЙСЬКОЮ мовою про Лондон для завдань 9-13
en_text = "London is a famous city. New tourists visit this beautiful place. We took a map and went on a trip. Nature in Hyde Park is amazing. We can walk non-stop to the top."
print(f"Англійський текст:\n{en_text}") 
# Метод .title() робить першу літеру КОЖНОГО слова великою
en_text_title = en_text.title() 
print(f"Текст, де всі слова з великої літери:\n{en_text_title}") 

print("\n--- ЗАВДАННЯ 10 ---")
# Вводимо літеру, на яку ПОЧИНАЮТЬСЯ слова
start_l = input("Введіть літеру, на яку ПОЧИНАЮТЬСЯ слова (наприклад, 'n'): ").lower() 
# Вводимо літеру, на яку ЗАКІНЧУЮТЬСЯ слова
end_l = input("Введіть літеру, на яку ЗАКІНЧУЮТЬСЯ слова (наприклад, 'p'): ").lower() 

# Шукаємо слова, що починаються на першу літеру
words_starting = [w.strip('.,?!') for w in en_text.split() if w.strip('.,?!').lower().startswith(start_l)]
# Шукаємо слова, що закінчуються на другу літеру
words_ending = [w.strip('.,?!') for w in en_text.split() if w.strip('.,?!').lower().endswith(end_l)]

print(f"Слова, що починаються на '{start_l}': {words_starting}") 
print(f"Слова, що закінчуються на '{end_l}': {words_ending}")
print("\n--- ЗАВДАННЯ 11 ---")
# Створюємо рядок, який містить всі англійські голосні літери
vowels = "aeiouy" 
# Проходимо по кожній літері тексту і рахуємо, якщо вона є в vowels
vowel_count = sum(1 for char in en_text.lower() if char in vowels) 
print(f"Кількість голосних літер в англійському тексті: {vowel_count}") 

print("\n--- ЗАВДАННЯ 12 ---")
# Створюємо рядок з усіма англійськими приголосними літерами
consonants = "bcdfghjklmnpqrstvwxz" 
# Проходимо по тексту і рахуємо приголосні
cons_count = sum(1 for char in en_text.lower() if char in consonants) 
print(f"Кількість приголосних літер в англійському тексті: {cons_count}") 

print("\n--- ЗАВДАННЯ 13 ---")
# Шукаємо власні назви (слова з великої літери). 
# Метод .istitle() перевіряє, чи слово написане з великої літери
names = [w.strip('.,?!') for w in en_text.split() if w.istitle()]
print(f"Список імен та власних назв з тексту: {names}")