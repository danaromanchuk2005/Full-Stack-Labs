from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Завантажуємо навчену модель та векторизатор
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form["message"]
    # Перетворюємо введений текст у вектор
    vector = vectorizer.transform([text])
    # Отримуємо передбачення (1 - positive, 0 - negative)
    prediction = model.predict(vector)[0]
    
    result = "POSITIVE" if prediction == 1 else "NEGATIVE"
    
    return render_template("index.html", message=text, result=result)

if __name__ == "__main__":
    app.run(debug=True, port=8000)