from flask import render_template, request, redirect, url_for, session
#from flask_sqlalchemy import SQLAlchemy
from application import app

#!!!this code should import an external db and then store the data in it from the sign up page. It should then
#import that data into the account page!!!

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'<----DB link
#db = SQLAlchemy(app)

#class User(db.*insert_name_here*):
    #id = db.Column(db.Integer, primary_key=True)
    #email = db.Column(db.String(80), unique=True, nullable=False)
    #password = db.Column(db.String(120), unique=True, nullable=False)
    #first_name = db.Column(db.String(120), nullable=False)
    #last_name = db.Column(db.String(120), nullable=False)
    #dob = db.Column(db.String(120), nullable=False)


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
    
    def perform_search(query):
        pages = []
        results = []
        for page in pages:
            if query.lower() in page.lower():
                results.append(page)
        if len(results) == 0:
            return "No results found for '{}'".format(query)
        else:
            return results
    
    results = perform_search(query)
    return render_template('search_results.html', results=[results])

#log out process - cannoty fully test until we have active 'users'
@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))