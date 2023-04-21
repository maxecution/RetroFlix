from flask import request
from application import app

@app.route('/sign_up)', method=['GET, POST'])
def submit_form():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    email = request.form['email']
    if request.form['password'] == request.form['password_check']:
        password = request.form['password']
    mail_list = request.form['mail_list']
