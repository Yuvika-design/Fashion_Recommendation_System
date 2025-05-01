from flask import Flask, render_template, request, url_for, redirect, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, UserPreference
from fashion_recommender import FashionRecommender
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fashion'  # Change this to a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mintumintu@localhost/fashion_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

recommender = FashionRecommender()

# Test database connection
try:
    with app.app_context():
        db.engine.connect()
        print("Database connection successful!")
except Exception as e:
    print(f"Database connection failed: {str(e)}")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('home'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('signup'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists')
            return redirect(url_for('signup'))
        
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        login_user(user)
        return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/recommend', methods=['POST'])
@login_required
def recommend():
    gender = request.form.get('gender')
    weather = request.form.get('weather')
    occasion = request.form.get('occasion')
    
    # Save user preference
    preference = UserPreference(
        user_id=current_user.id,
        gender=gender,
        favorite_style=occasion
    )
    db.session.add(preference)
    db.session.commit()
    
    recommendations = recommender.get_recommendation(gender, weather, occasion)
    return render_template('results.html', 
                         recommendations=recommendations,
                         gender=gender,
                         weather=weather,
                         occasion=occasion)

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True) 