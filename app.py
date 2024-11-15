from flask import Flask, request, redirect, url_for, render_template, session, flash
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Enum

Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String(255), nullable=False)
    last_name = sa.Column(sa.String(255), nullable=False)
    email = sa.Column(sa.String(255), nullable=False)
    user_request = sa.Column(Enum("Messaging", "Consulting", "Newsletter"))
    avatar = sa.Column(sa.String(255), nullable=True)
    about = sa.Column(sa.Text, nullable=True)

engine = sa.create_engine("sqlite:///myproject.db")
Base.metadata.create_all(engine)
Sessionmaker = sessionmaker(bind=engine)
db_session = Sessionmaker()

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/register', methods=['POST', 'GET'])
def create_user():
    if request.method == "POST":
        fn = request.form['first_name']
        ln = request.form['last_name']
        email = request.form['email']
        new_user = User(first_name=fn, last_name=ln, email=email)
        db_session.add(new_user)
        db_session.commit()
        return redirect(url_for('login_user'))
    return render_template('register.html')

@app.route('/login', methods=['POST', 'GET'])
def login_user():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password'] 
        user = db_session.query(User).filter_by(email=email).first()
        if user:
            session['user_id'] = user.id
            session['user_name'] = user.first_name
            flash(f'خوش آمدید {user.first_name}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('ایمیل یا رمز عبور اشتباه است.', 'danger')
            return redirect(url_for('login_user'))
    return render_template('signin.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    flash('با موفقیت خارج شدید' , 'info')
    return redirect(url_for('login_user'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/register_page')
def register_page():
    return render_template('register.html')

@app.route('/search_result')
def search_result():
    return render_template('search_result.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == "__main__":
    app.run(debug=True)
