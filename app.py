import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-for-local-use') # Security: Keep secrets out of code in production
app.config['SQLALCHEMY_DATABASE_STRICT'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' # Using SQLite for easy portability

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User Model (Database Table)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- ROUTES ---

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Basic validation 
        if not username or not password:
            flash('All fields are required!')
            return redirect(url_for('register'))

        # Check if user exists
        user_exists = User.query.filter_by(username=username).first()
        if user_exists:
            flash('Username already exists.')
            return redirect(url_for('register'))

        # Secure password hashing 
        hashed_pw = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        # Check hash 
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        
        flash('Invalid credentials. Please try again.') # Error handling 
    return render_template('login.html')

@app.route('/dashboard')
@login_required # Protected route
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Automatically creates the database file
    app.run(debug=True)
