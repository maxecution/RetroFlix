from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, current_user, logout_user

auth=Blueprint('auth', __name__)

# sign in auth
@auth.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        email_address = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email_address=email_address).first()
        if user:
            if check_password_hash(user.password, password):
                session['user_id'] = user.id
                session['user_email'] = user.email_address
                login_user(user, remember=True)
                return redirect(url_for('home'))         
            else:            
                flash('Invalid email or password', category='error')
        else:           
            flash('Invalid email or password', category='error')

    return render_template('sign_in.html', user=current_user)

# log out auth
@auth.route('/logout')
def logout():
    session.pop('user_email', None)
    logout_user()
    flash('Successfully logged out')
    return redirect(url_for('index'))

# sign up auth
@auth.route('/sign_up')
def sign_up():
    return render_template('sign_up.html', title='Sign Up')


