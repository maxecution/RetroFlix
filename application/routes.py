from flask import render_template

from application import app

#index render
@app.route('/index')
def index():
    return render_template('index.html')

#about us render
@app.route('/about_us')
def about_us():
    return render_template('about_us.html')