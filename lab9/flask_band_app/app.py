from flask import Flask, render_template, request, redirect, url_for, session, flash
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
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
