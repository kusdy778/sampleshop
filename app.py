from flask import Flask, render_template, redirect, request, url_for, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from datetime import datetime
import random

app = Flask(__name__, static_folder='static')

# uncomment that in order to use sqlite database for testing
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/sampleshop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configurer la clé secrète pour les sessions
app.secret_key = 'vTOTO20203'

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

# Initialiser l'extension Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

             

# Routes pour le store

# Modèle User
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    products = db.relationship('products', backref='user', lazy=True)

# Modèle Product
class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)  # NOT NULL
    

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) 

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Please check your username and password.', 'danger')
    
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/signup')
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Vérification de la correspondance des mots de passe
        if password != confirm_password:
            return render_template('signup.html', error_message='Les mots de passe ne correspondent pas')

        # Enregistrement de l'utilisateur dans la base de données ou autre logique de traitement
        new_user = User(username=username, password=password)

        # Ajouter l'utilisateur à la base de données
        db.session.add(new_user)
        db.session.commit()
        
        # informer Flask Login que cette user est authentifié
        login_user(new_user)

        # Redirection vers la page de succès ou autre page
        return redirect('/dashboard')

    return render_template('signup.html')






@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')



if __name__ == '__main__':
    app.run(debug=True)

