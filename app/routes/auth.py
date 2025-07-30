from flask import Blueprint, request, redirect, url_for, flash, render_template, session
from app.models import User
from app import db

auth_bp = Blueprint('auth', __name__)
    

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash('Invalid credentials, please try again.', 'error')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    from app.models import User
    from app import db
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Check if user exists
        if User.query.filter_by(username=username).first():
            flash('Username already taken, choose another.', 'error')
        else:
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash(f'Welcome, {username}! Registration successful. Please log in.', 'success')
            return redirect(url_for('auth.login'))
    return render_template('register.html')
