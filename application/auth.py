from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .models import User, CardDetail, Subscription
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, current_user, logout_user,  login_required
from sqlalchemy.orm.exc import NoResultFound



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
@login_required
def logout():
    session.pop('user.email_address', None)
    session.pop('user.id', None)
    logout_user()
    session['user_id'] = None
    flash('Successfully logged out')
    return redirect(url_for('index'))


# sign up auth
@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    email = request.args.get('email', '')
    sub = request.args.get('sub', '')

    # Getting form data
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password_check')
        dob = request.form.get('dob')
        mailing = request.form.get('mail_list')
        pin = request.form.get('pin')
        user_sub = request.form.get('subs-select')
        ccName = request.form.get('cc-name')
        ccNumber = request.form.get('cc-number')
        ccExpiry = request.form.get('cc-expiry')
        ccCVV = request.form.get('cc-cvv')

        # Back end validation to avoid sql injection
        email_exists = User.query.filter_by(email_address=email).scalar() is not None
        if email_exists:
            flash('Email address is already registered.', 'error')
            return redirect(url_for('auth.sign_up'))

        # Adding new user to db

        password = generate_password_hash(password, method='sha256')
        sub=Subscription.query.filter_by(sub_type=user_sub).first()
        sub_id = sub.id

        user_card = CardDetail(name_on_card=ccName, card_number=ccNumber, expiry_date=ccExpiry, cvv=ccCVV)

        new_user = User(email_address=email, password=password, first_name=first_name, last_name=last_name, dob=dob, mailing=mailing, pin=pin, subscription_id=sub_id, cards=[user_card])
        
        db.session.add(new_user)
        db.session.commit()


        flash('Account registered successfully. Log in now to start enjoying our content.', 'success')
        return redirect(url_for('auth.sign_in'))


    return render_template('sign_up.html', title='Sign Up', email=email, sub=sub)


