import random
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

# =0. Тoken та Банк питань з Python та ООП =
TOKEN = "8791127204:AAGifPlBHJ_mENxRKmCSr06EhLJpH6vT1yA"  # Замініть на токен від @BotFather

QUESTIONS_POOL = [
    {
        "question": "Що таке ООП у Python?",
        "options": ["Об'єктно-орієнтоване програмування", "Операційна система процесора", "Обов'язковий об'єкт папки", "Об'єднаний пакет програм"],
        "correct": 0
    },
    {
        "question": "Який метод використовується як конструктор класу в Python?",
        "options": ["__start__", "__init__", "__create__", "__new_class__"],
        "correct": 1
    },
    {
        "question": "Що означає принцип інкапсуляції в ООП?",
        "options": ["Множинне наслідування класів", "Приховування внутрішнього стану та даних об'єкта", "Створення копій об'єктів", "Звільнення пам'яті"],
        "correct": 1
    },
    {
        "question": "Яка бібліотека у Python використовується для створення вебдодатків?",
        "options": ["Pandas", "Flask", "Matplotlib", "NumPy"],
        "correct": 1
    },
    {
        "question": "Що повертає функція type() у Python?",
        "options": ["Значення змінної", "Тип даних об'єкта", "Довжину об'єкта", "Адресу в пам'яті"],
        "correct": 1
    },
    {
        "question": "Який ключовий рядок використовується для оголошення функції в Python?",
        "options": ["function", "fun", "def", "define"],
        "correct": 2
    },
    {
        "question": "Що робить оператор `super()` в класах Python?",
        "options": ["Знищує батьківський клас", "Звертається до методів батьківського класу", "Створює глобальну змінну", "Очищає кеш"],
        "correct": 1
    },
    {
        "question": "Який тип даних є незмінним (immutable) у Python?",
        "options": ["list", "dict", "set", "tuple"],
        "correct": 3
    },
    {
        "question": "Яке розширення за замовчуванням мають файли модулів Python?",
        "options": [".pt", ".py", ".pn", ".python"],
        "correct": 1
    },
    {
        "question": "Який метод дозволяє перетворити об'єкт Python у рядок для виведення?",
        "options": ["__str__", "__to_string__", "__print__", "__format__"],
        "correct": 0
    }
]

# Словник для збереження сесій користувачів (стан проходження тесту)
user_sessions = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # 1. Випадковий порядок питань (рандомізація)
    shuffled_questions = random.sample(QUESTIONS_POOL, len(QUESTIONS_POOL))
    
    # Перемішуємо варіанти відповідей для кожного питання, зберігаючи індекс правильної
    for q in shuffled_questions:
        correct_text = q["options"][q["correct"]]
        random.shuffle(q["options"])
        q["correct"] = q["options"].index(correct_text)

    # Ініціалізуємо сесію користувача
    user_sessions[user_id] = {
        "questions": shuffled_questions,
        "current_index": 0,
        "score": 0,
        "start_time": datetime.now()
    }
    
    await update.message.reply_text(
        "👋 Вітаю! Це тестовий Telegram-бот з мови Python та ООП.\n"
        "Вам буде запропоновано 10 випадкових запитань.\n"
        "Почнемо тестування! 🚀"
    )
    await send_question(update, context)

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    session = user_sessions.get(user_id)
    
    if not session:
        return

    idx = session["current_index"]
    
    # Якщо питання закінчилися — формуємо звіт
    if idx >= len(session["questions"]):
        await finish_test(update, context)
        return

    q_data = session["questions"][idx]
    
    # Створюємо інлайн-кнопки з варіантами відповідей
    keyboard = []
    for i, option in enumerate(q_data["options"]):
        keyboard.append([InlineKeyboardButton(option, callback_data=f"ans_{i}")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    text = f"<b>Питання {idx + 1} з 10:</b>\n\n{q_data['question']}"
    
    if update.callback_query:
        await update.callback_query.message.edit_text(text, reply_markup=reply_markup, parse_mode="HTML")
    else:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="HTML")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    user_id = update.effective_user.id
    session = user_sessions.get(user_id)
    
    if not session:
        await query.message.reply_text("Будь ласка, запустіть тест спочатку за допомогою команди /start")
        return

    selected_option = int(query.data.split("_")[1])
    idx = session["current_index"]
    q_data = session["questions"][idx]
    
    # Перевірка правильності відповіді (вимога п. 5)
    if selected_option == q_data["correct"]:
        session["score"] += 1
        feedback = "Правильно!"
    else:
        correct_ans = q_data["options"][q_data["correct"]]
        feedback = f" Неправильно. Правильна відповідь: <b>{correct_ans}</b>"

    await query.message.reply_text(feedback, parse_mode="HTML")
    
    # Переходимо до наступного питання
    session["current_index"] += 1
    await send_question(update, context)

async def finish_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    session = user_sessions.pop(user_id, None)
    
    if not session:
        return

    end_time = datetime.now()
    duration = end_time - session["start_time"]
    
    # Формуємо підсумковий звіт (вимога п. 6)
    report = (
        "📊 <b>РЕЗУЛЬТАТИ ТЕСТУВАННЯ</b>\n"
        "----------------------------------------\n"
        f"🎯 Набрано балів: <b>{session['score']} з 10</b>\n"
        f"📅 Дата проходження: {session['start_time'].strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"⏱ Тривалість: {duration.seconds} секунд(-и)\n"
        "----------------------------------------\n"
        "Дякуємо за проходження тесту! Для повторного запуску введіть /start"
    )
    
    if update.callback_query:
        await update.callback_query.message.reply_text(report, parse_mode="HTML")
    else:
        await update.message.reply_text(report, parse_mode="HTML")

def main():
    # Ініціалізація додатку бота
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Бот успішно запущено і готовий до роботи...")
    app.run_polling()

if __name__ == "__main__":
    main()