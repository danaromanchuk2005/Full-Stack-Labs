import os

# =====================================================================
# СКРИПТ-ГЕНЕРАТОР: Створює структуру Flask-проєкту
# =====================================================================

project_dir = "flask_band_app"
templates_dir = os.path.join(project_dir, "templates")

# Створюємо папки
os.makedirs(templates_dir, exist_ok=True)

# 1. Головний файл програми (app.py)
app_code = """from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_lab9'
# Налаштування бази даних SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///band.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель бази даних для Альбомів
class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

# Створення таблиць перед першим запитом
with app.app_context():
    db.create_all()

# Декоратор для перевірки авторизації
def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            flash('Будь ласка, авторизуйтесь для доступу.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# --- МАРШРУТИ (ROUTES) ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/albums')
def albums():
    all_albums = Album.query.order_by(Album.year.desc()).all()
    return render_template('albums.html', albums=all_albums)

@app.route('/album/<int:id>')
def album_detail(id):
    album = Album.query.get_or_404(id)
    return render_template('album_detail.html', album=album)

# --- CRUD (Додавання, Редагування, Видалення) ---
@app.route('/album/add', methods=['GET', 'POST'])
@login_required
def add_album():
    if request.method == 'POST':
        new_album = Album(
            title=request.form['title'],
            year=request.form['year'],
            description=request.form['description']
        )
        db.session.add(new_album)
        db.session.commit()
        flash('Альбом успішно додано!', 'success')
        return redirect(url_for('albums'))
    return render_template('album_form.html', action="Додати")

@app.route('/album/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_album(id):
    album = Album.query.get_or_404(id)
    if request.method == 'POST':
        album.title = request.form['title']
        album.year = request.form['year']
        album.description = request.form['description']
        db.session.commit()
        flash('Альбом оновлено!', 'success')
        return redirect(url_for('albums'))
    return render_template('album_form.html', action="Редагувати", album=album)

@app.route('/album/delete/<int:id>', methods=['POST'])
@login_required
def delete_album(id):
    album = Album.query.get_or_404(id)
    db.session.delete(album)
    db.session.commit()
    flash('Альбом видалено.', 'info')
    return redirect(url_for('albums'))

# --- АВТОРИЗАЦІЯ ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Проста авторизація для лабораторної (admin / admin)
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['logged_in'] = True
            flash('Ви успішно увійшли!', 'success')
            return redirect(url_for('albums'))
        else:
            flash('Неправильний логін або пароль.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Ви вийшли з системи.', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Для Heroku беремо порт з оточення
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
"""
with open(os.path.join(project_dir, "app.py"), "w", encoding="utf-8") as f:
    f.write(app_code)

# 2. Базовий HTML шаблон (base.html)
base_html = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Гурт "Синтаксис"</title>
    <!-- Підключаємо Bootstrap для красивого дизайну без написання CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{{ url_for('index') }}">🎸 Гурт "Синтаксис"</a>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item"><a class="nav-link" href="{{ url_for('about') }}">Про проєкт</a></li>
                    <li class="nav-item"><a class="nav-link" href="{{ url_for('history') }}">Історія гурту</a></li>
                    <li class="nav-item"><a class="nav-link" href="{{ url_for('albums') }}">Альбоми</a></li>
                </ul>
                <ul class="navbar-nav">
                    {% if session.get('logged_in') %}
                        <li class="nav-item"><a class="nav-link text-warning" href="{{ url_for('logout') }}">Вийти (Admin)</a></li>
                    {% else %}
                        <li class="nav-item"><a class="nav-link" href="{{ url_for('login') }}">Вхід</a></li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>
    <div class="container mt-4">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        
        {% block content %}{% endblock %}
    </div>
</body>
</html>
"""
with open(os.path.join(templates_dir, "base.html"), "w", encoding="utf-8") as f: f.write(base_html)

# 3. Інші сторінки
html_files = {
    "index.html": "{% extends 'base.html' %}\n{% block content %}\n<h1>Ласкаво просимо!</h1>\n<p>Офіційний сайт легендарного інді-гурту 'Синтаксис'. Музика, що компілюється в душі.</p>\n{% endblock %}",
    "about.html": "{% extends 'base.html' %}\n{% block content %}\n<h1>Про проєкт</h1>\n<p>Цей сайт створено в рамках Лабораторної роботи №9 з використанням Flask, SQLite та Bootstrap.</p>\n{% endblock %}",
    "history.html": "{% extends 'base.html' %}\n{% block content %}\n<h1>Історія гурту</h1>\n<p>Гурт був заснований у 2026 році двома програмістами, які вирішили, що писати музику веселіше, ніж фіксити баги.</p>\n{% endblock %}",
    "login.html": """{% extends 'base.html' %}
{% block content %}
<h2>Вхід для адміністратора</h2>
<form method="POST">
    <div class="mb-3"><label>Логін</label><input type="text" name="username" class="form-control" required></div>
    <div class="mb-3"><label>Пароль</label><input type="password" name="password" class="form-control" required></div>
    <button type="submit" class="btn btn-primary">Увійти</button>
</form>
{% endblock %}""",
    "albums.html": """{% extends 'base.html' %}
{% block content %}
<h2>Дискографія</h2>
{% if session.get('logged_in') %}
    <a href="{{ url_for('add_album') }}" class="btn btn-success mb-3">+ Додати альбом</a>
{% endif %}
<div class="row">
    {% for album in albums %}
    <div class="col-md-4 mb-3">
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">{{ album.title }} ({{ album.year }})</h5>
                <p class="card-text">{{ album.description[:50] }}...</p>
                <a href="{{ url_for('album_detail', id=album.id) }}" class="btn btn-sm btn-primary">Детальніше</a>
                {% if session.get('logged_in') %}
                    <a href="{{ url_for('edit_album', id=album.id) }}" class="btn btn-sm btn-warning">Редагувати</a>
                    <form action="{{ url_for('delete_album', id=album.id) }}" method="POST" class="d-inline">
                        <button type="submit" class="btn btn-sm btn-danger" onclick="return confirm('Видалити?')">Видалити</button>
                    </form>
                {% endif %}
            </div>
        </div>
    </div>
    {% else %}
    <p>Альбомів поки немає.</p>
    {% endfor %}
</div>
{% endblock %}""",
    "album_detail.html": """{% extends 'base.html' %}
{% block content %}
<h2>{{ album.title }} ({{ album.year }})</h2>
<p class="lead">{{ album.description }}</p>
<a href="{{ url_for('albums') }}" class="btn btn-secondary">Назад до списку</a>
{% endblock %}""",
    "album_form.html": """{% extends 'base.html' %}
{% block content %}
<h2>{{ action }} альбом</h2>
<form method="POST">
    <div class="mb-3">
        <label>Назва альбому</label>
        <input type="text" name="title" class="form-control" value="{{ album.title if album else '' }}" required>
    </div>
    <div class="mb-3">
        <label>Рік випуску</label>
        <input type="number" name="year" class="form-control" value="{{ album.year if album else '2026' }}" required>
    </div>
    <div class="mb-3">
        <label>Опис</label>
        <textarea name="description" class="form-control" rows="4" required>{{ album.description if album else '' }}</textarea>
    </div>
    <button type="submit" class="btn btn-success">Зберегти</button>
    <a href="{{ url_for('albums') }}" class="btn btn-secondary">Скасувати</a>
</form>
{% endblock %}"""
}

for filename, content in html_files.items():
    with open(os.path.join(templates_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)

# 4. Файли для Heroku (Procfile та requirements.txt)
with open(os.path.join(project_dir, "Procfile"), "w", encoding="utf-8") as f:
    f.write("web: gunicorn app:app\n")

with open(os.path.join(project_dir, "requirements.txt"), "w", encoding="utf-8") as f:
    f.write("Flask==2.3.2\nFlask-SQLAlchemy==3.0.3\ngunicorn==20.1.0\n")

print(f"✅ Проєкт успішно згенеровано у папці '{project_dir}'!")
print("Щоб запустити сайт:")
print("1. Відкрийте термінал.")
print("2. Введіть: cd flask_band_app")
print("3. Введіть: pip3 install -r requirements.txt")
print("4. Введіть: python3 app.py")