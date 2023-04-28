from flask import render_template, request, redirect, url_for, session

from application import app
from application.models import *
from sqlalchemy import or_


#terms render
@app.route('/terms_of_use')
def terms_of_use():
    return render_template('terms_of_use.html', title='Terms of Use')

#about us render
@app.route('/about_us')
def about_us():
    return render_template('about_us.html', title='About Us')

#careers render
@app.route('/careers')
def careers():
    return render_template('careers.html', title='Careers')

#contact us render
@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html', title='Contact Us')

#corporate info render
@app.route('/corp_info')
def corp_info():
    return render_template('corp_info.html', title='Corporate Information')

#faqs render
@app.route('/faq')
def faq():
    return render_template('faq.html', title='Frequently Asked Questions')

#help render
@app.route('/help')
def help():
    return render_template('help.html', title='Help')

#legal notices render
@app.route('/legal_notice')
def legal_notice():
    return render_template('legal_notice.html', title='Legal Notice')

#privacy notice render
@app.route('/privacy_notice')
def privacy_notice():
    return render_template('privacy_notice.html', title='Privacy Notice')

#film render
@app.route('/film')
def film():
    return render_template('film.html', title='Films')

#series render
@app.route('/series')
def series():
    return render_template('series.html', title='Series')

#home render
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

#account render
@app.route('/account', methods=['GET', 'POST'])
def account():
    return render_template('account.html', title='Account') #user=user

#sign up render
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        

        #db.session.add(user)
        #db.session.commit()

# user defines the name of the chosen DB
        #user = User(email=email, password=password, first_name=first_name, last_name=last_name, dob=dob)

        return redirect(url_for('home')) #should this redirect to home so theyre logged in or is it to account as its defining where the information is sent to??
    else:
        return render_template('sign_up.html', title='Sign Up')

#sign in render
@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html', title='Sign In')

#index render
@app.route('/index')
def index():
    return render_template('index.html', title='Index')

#search bar render
@app.route('/search')
def search():
    query = request.args.get('query')
    
    film_results = Film.query.filter(Film.title.contains(query)).all()
    
    tv_series = TVSeries.query.filter(TVSeries.title.contains(query)).all()
    
    actor_results = Actor.query.filter(Actor.name.contains(query)).all()
    actor_films = []
    for actor in actor_results:
        actor_films += actor.films
    
    genre_results = Genre.query.filter(Genre.genre.contains(query)).all()
    
    results = film_results + actor_films + genre_results + tv_series
    
    if len(results) == 0:
        broader_query = '%{}%'.format(query)
        results = db.session.query(Film).filter(or_(Film.title.like(broader_query), Film.description.like(broader_query))).all()
        results += db.session.query(TVSeries).filter(or_(TVSeries.title.like(broader_query), TVSeries.description.like(broader_query))).all()
        results += db.session.query(Actor).filter(or_(Actor.title.like(broader_query), Actor.description.like(broader_query))).all()       
        results += db.session.query(Genre).filter(or_(Genre.title.like(broader_query), Genre.description.like(broader_query))).all()
    
    if len(results) == 0:
        return "No results found for '{}'".format(query)
    else:
        return render_template('search_results.html', results=results)

#log out process - cannoty fully test until we have active 'users'
@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))