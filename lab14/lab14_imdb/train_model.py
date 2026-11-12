import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import re

print("Завантаження датасету...")
# 1. Завантаження датасету
df = pd.read_csv("IMDB Dataset.csv")

# Перетворюємо текстові мітки ('positive', 'negative') на числа (1, 0)
df['label'] = df['sentiment'].map({'positive': 1, 'negative': 0})
df.rename(columns={'review': 'message'}, inplace=True)

# 2. Очищення тексту
def clean_text(text):
    text = text.lower()
    text = re.sub(r"<br\s*/?>", " ", text)  # Видаляємо HTML-теги перенесення рядка
    text = re.sub(r"http\S+", " url ", text)
    text = re.sub(r"[^a-zA-Z]", " ", text) # Залишаємо лише літери
    text = re.sub(r"\s+", " ", text).strip()
    return text

print("Очищення тексту (це може зайняти хвилину)...")
df["message"] = df["message"].apply(clean_text)

# 3. Розбиття на train/test
X_train, X_test, y_train, y_test = train_test_split(
    df["message"], df["label"], test_size=0.2, random_state=42
)

print("Векторизація...")
# 4. Векторизація тексту (обмежуємо кількість фіч для швидкодії)
vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1,2), min_df=5, max_features=15000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

print("Навчання моделі...")
# 5. Навчання моделі
model = LogisticRegression(max_iter=500)
model.fit(X_train_vec, y_train)

# Виводимо точність
print("Accuracy:", model.score(X_test_vec, y_test))

# 6. Збереження моделі та векторизатора
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
print("Модель і векторизатор успішно збережено!")