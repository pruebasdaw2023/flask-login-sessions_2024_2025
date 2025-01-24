from flask import Flask, render_template, request, flash,redirect, url_for
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_wtf.csrf import CSRFProtect

from config import config

# MODELS
from models.ModelUser import ModelUser

# ENTITIES
from models.entities.User import User


app = Flask(__name__)

db = MySQL(app)
login_manager_app = LoginManager(app)
csrf = CSRFProtect()

@login_manager_app.user_loader
def load_user(id):

    return ModelUser.get_by_id(db, id)



@app.route('/')
def index():

    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User(0, username, password)

        logged_user = ModelUser.login(db, user)

        if logged_user:
            
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:

                flash('Invalid password...')

                return render_template('auth/login.html')
        else:

            flash('User not found...')

            return render_template('auth/login.html')

    else:

        if current_user.is_authenticated:

            print('AUTENTICADO CON SESION')
            print(current_user.username)
            print(current_user.fullname)
            print(current_user.get_id())

            return redirect(url_for('home'))

        return render_template('auth/login.html')
    
@app.route('/home')
@login_required
def home():

    return render_template('home.html')

@app.route('/logout')
def logout():

    logout_user()
    return redirect(url_for('login'))


@app.route('/protected')
@login_required
def protected():

    return "<h1>Esto es una pagina para usuarios autenticados.</h1>"


def status_401(error):

    return redirect(url_for('login'))

def status_404(error):

    return '<h1>Pagina no encontrada.</h1>'



if __name__ == '__main__':

    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()