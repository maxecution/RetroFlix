from flask import render_template

from application import app

#navbar render
@app.route('/navbar')
def navbar():
    return render_template('navbar.html')

#footer render
@app.route('/footer')
def footer():
    return render_template('footer.html')

#index render
@app.route('/index')
def index():
    return render_template('index.html')

#home render
@app.route('/home')
def home():
    return render_template('home.html')

#sign up render
@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

#sign in render
@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')

#about us render
@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

#careers render
@app.route('/careers')
def careers():
    return render_template('careers.html')

#contact render
@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

#corporate info render
@app.route('/corp_info')
def corp_info():
    return render_template('corp_info.html')

#faqs render
@app.route('/faq')
def faq():
    return render_template('faq.html')

#help render
@app.route('/help')
def help():
    return render_template('help.html')

#legal notices render
@app.route('/legal_notice')
def legal_notice():
    return render_template('legal_notice.html')

#privacy notice render
@app.route('/privacy_notice')
def privacy_notice():
    return render_template('privacy_notice.html')

#terms render
@app.route('/terms_of_use')
def terms_of_use():
    return render_template('terms_of_use.html')

#film render
@app.route('/film')
def film():
    return render_template('film.html')

#series render
@app.route('/series')
def series():
    return render_template('series.html')