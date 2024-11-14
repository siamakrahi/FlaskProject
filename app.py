from flask import Flask, render_template
from models import *

app = Flask(__name__)


@app.route('/about/')
def about():
    return render_template ('about.html')

@app.route('/blog/')
def blog():
    return render_template ('blog.html')

@app.route('/index/')
def home():
    return render_template ('index.html')

@app.route('/register/')
def register():
    return render_template ('register.html')

@app.route('/signin/')
def signin():
    return render_template ('signin.html')

@app.route('/signout/')
def signout():
    return render_template ('signout.html')

@app.route('/service/')
def service():
    return render_template ('service.html')

@app.route('/team/')
def team():
    return render_template ('team.html')

@app.route('/contact/')
def contact():
    return render_template ('contact.html')
if __name__ == "__main__":
    app.run(debug=True)


# @app.route('/details/<int:id>') 
# def details(id):
#     u = session.query(User).get(id)
#     return render_template('details.html', u=u)


# @app.route('/delete/<int:id>') 
# def delete(id):
#     u = session.query(User).get(id)
#     session.delete(u)
#     session.commit()
#     return redirect(url_for('index'))

# @app.route('/update/<int:id>', methods=['POST', 'GET'])
# def update(id):
#     us = session.query(User).get(id)
#     if request.method == "POST":
#         fn = request.form['first_name']
#         ln = request.form['last_name']
#         e = request.form['email']
#         us.first_name = fn
#         us.last_name = ln
#         us.email = e
#         session.commit()
#         return redirect(url_for('index'))
#     return render_template('update.html', us=us)


# @app.route('/create', methods=['POST', 'GET']) 
# def create():
#     if request.method=="POST":
#         fn = request.form['first_name']
#         ln = request.form['last_name']
#         e = request.form['email']
#         email = request.form['email']
#         new_user = User(first_name=fn, last_name=ln, email=email)
#         session.add(new_user)
#         session.commit()
#         return redirect(url_for('index'))
#     return render_template('create.html')
# @app.route('/posts') 
# def posts():
#     return render_template('posts.html')


