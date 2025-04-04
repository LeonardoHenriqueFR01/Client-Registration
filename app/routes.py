from flask import render_template, request, redirect, url_for, session, Blueprint
from flask_login import login_required, current_user, login_user
from app import db
from .models import User, Avista, Financia
from werkzeug.security import generate_password_hash, check_password_hash
from time import sleep


main = Blueprint('main', __name__)

# Rota para página principal
@main.route('/')
def home():
    return render_template('index.html')

# Rota para página de cadastro e login
@main.route('/register')
def register():
    return render_template('register.html')

# Rota para página para cadastrar clientes
@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Rota para fazer cadastro
@main.route('/get_user_cadastro', methods=['POST', 'GET'])
def get_user_cadastro():
    error_message = None

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        user_exists = User.query.filter((User.name == name) | (User.email == email)).first()

        if user_exists:
            error_message = 'Nome ou Email já cadastrado!'
            return render_template('register.html', error_cadastro=error_message)
        else:
            hash_password = generate_password_hash(password)
            
            user = User(name=name, email=email, password=hash_password)

            db.session.add(user)
            db.session.commit()

            sleep(3)

            return redirect(url_for('main.dashboard'))
        
    return render_template('register.html')

# Rota para fazer login
@main.route('/get_user_login', methods=['POST', 'GET'])
def get_user_login():
    error_message = None

    if request.method == 'POST':
        name = request.form.get('name_login')
        email = request.form.get('email_login')
        password = request.form.get('password_login')

        user_exists = User.query.filter((User.name == name) | (User.email == email)).first()

        if user_exists and check_password_hash(user_exists.password, password):
            login_user(user_exists)

            sleep(3)

            return redirect(url_for('main.dashboard'))
        else:
            error_message = 'Dados inválidos!'
            return render_template('register.html', error_login=error_message)
        
    return render_template('register.html')

# Rota para cadastrar um cliente avista
@main.route('/get_user_avista', methods=['POST', 'GET'])
@login_required
def user_get_avista():
    if request.method == 'POST':
        name = request.form.get('name_avista')
        name_vehicle = request.form.get('name_vehicle_avista')
        value_vehicle = request.form.get('value_vehicle_avista')
        value_prohibited = request.form.get('value_prohibited_avista')

        new_info = Avista(name=name, name_vehicle=name_vehicle, value_vehicle=value_vehicle, value_prohibited=value_prohibited, user_id=current_user.id)
        
        db.session.add(new_info)
        db.session.commit()

        sleep(3)

        return redirect(url_for('main.dashboard'))
    
    return render_template('dashboard.html')

# Rota para cadastrar cliente financiamento
@main.route('/get_user_financia', methods=['POST', 'GET'])
@login_required
def get_user_financia():
    if request.method == 'POST':
        name = request.form.get('name')
        name_vehicle = request.form.get('name_vehicle')
        value_vehicle = request.form.get('name_vehicle')
        value_prohibited = request.form.get('value_prohibeted')
        installments = request.form.get('installments')

        new_info = Financia(name=name, name_vehicle=name_vehicle, value_vehicle=value_vehicle, value_prohibited=value_prohibited, installments=installments, user_id=current_user.id)

        db.session.add(new_info)
        db.session.commit()

        sleep(3)

        return redirect(url_for('main.dashboard'))
    
    return render_template('dashboard.html')
