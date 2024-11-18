from flask import Flask, request, redirect, url_for, render_template, session, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import *
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

engine = sa.create_engine("sqlite:///myproject3.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@app.route('/create_user', methods=['POST', 'GET'])
def create_user(): 
    if request.method == "POST": 
        try: 
            fname = request.form.get('fname') 
            lname = request.form.get('lname') 
            email = request.form.get('email') 
            password = request.form.get('password')
            if not all([fname, lname, email, password]): 
                flash('لطفا تمام فیلدها را پر کنید.', 'error') 
                return render_template('register_page.html') 
            hashed_password = generate_password_hash(password) 
            new_user = User(fname=fname, lname=lname, email=email, password=hashed_password) 
            with Session() as db_session: 
                db_session.add(new_user) 
                db_session.commit()
            flash('کاربر با موفقیت ثبت شد', 'success') 
            return redirect(url_for('login_user')) 
        except Exception as e:
            app.logger.exception(f'Error creating user: {e}') 
            flash(f'خطا در ثبت نام: {e}', 'danger') 
            return render_template('register_page.html') 
    return render_template('register_page.html') 

@app.route('/register_page') 
def register_page(): 
    return render_template('register_page.html')

@app.route('/login_user', methods=['POST', 'GET']) 
def login_user(): 
    if request.method == "POST": 
        try: 
            email = request.form.get('email') 
            password = request.form.get('password') 
            with Session() as db_session: 
                user = db_session.query(User).filter_by(email=email).first() 
                if user and check_password_hash(user.password, password): 
                    session['user_id'] = user.id 
                    flash(f'خوش آمدید {user.fname}!', 'success') 
                    return redirect(url_for('profile'))
                else: 
                    flash('ایمیل یا رمز عبور اشتباه است.', 'danger') 
        except Exception as e: 
            flash(f'خطا در ورود: {e}', 'danger') 
    return render_template('signin_page.html') 

@app.route('/signin_page') 
def signin_page(): 
    return render_template('signin_page.html') 

@app.route('/update/<int:user_id>', methods=['POST', 'GET']) 
def update_user(user_id): 
    if 'user_id' not in session or session['user_id'] != user_id: 
        return redirect(url_for('profile')) 
    try: 
        with Session() as db_session: 
            user = db_session.query(User).get(user_id) 
            if user is None: 
                abort(404) 
    
            if request.method == "POST": 
                fname = request.form.get('fname') 
                lname = request.form.get('lname') 
                email = request.form.get('email') 
                password = request.form.get('password') 
    
                if not all([fname, lname, email]): 
                    flash('لطفا تمام فیلدها را پر کنید.', 'error') 
                    return redirect(url_for('profile'))
    
                user.fname = fname 
                user.lname = lname 
                user.email = email 
                if password: 
                    user.password_hash = generate_password_hash(password)
                db_session.commit() 
                flash('اطلاعات با موفقیت بروزرسانی شد.', 'success') 
                return redirect(url_for('profile')) 
            else: 
                return render_template('profile.html', user=user) 

    except Exception as e: 
        flash(f'خطایی در بروزرسانی اطلاعات رخ داد: {e}', 'error') 
        return render_template('error.html')
    
@app.route('/delete/<int:id>', methods=['POST'])
def delete_user(id): 
    if 'user_id' not in session or session['user_id'] != id: 
        return redirect(url_for('login_user')) 
    try: 
        with Session() as db_session: 
            user = db_session.query(User).get(id) 
            if user: 
                db_session.delete(user) 
                db_session.commit() 
                session.pop('user_id', None) 
                session.pop('user_name', None) 
                flash('حساب کاربری با موفقیت حذف شد.', 'success') 
                return redirect(url_for('login_user')) 
            else: 
                flash('کاربری با این شناسه یافت نشد.', 'error') 
                return redirect(url_for('login_user')) 
    except Exception as e: 
        flash(f'خطایی در حذف حساب کاربری رخ داد: {e}', 'error') 
        return render_template('error.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    flash('با موفقیت خارج شدید' , 'info')
    return redirect(url_for('login_user'))

@app.route('/search_result')
def search_result():
    return render_template('search_result.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/profile') 
def profile(): 
    if 'user_id' not in session: 
        return redirect(url_for('login')) 
    with Session() as db_session: 
        user = db_session.query(User).get(session['user_id']) 
    if user: 
        return render_template('profile.html', user=user) 
    else: 
        return "User not found" 

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

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == "__main__":
    app.run(debug=True)