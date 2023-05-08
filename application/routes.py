from flask import render_template, request, redirect, url_for, session, flash, jsonify

from application import app
from application.models import *
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash

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
@login_required
def film():
    return render_template('film.html', title='Films')

#series render
@app.route('/series')
@login_required
def series():
    return render_template('series.html', title='Series')

#home render
@app.route('/home')
@login_required
def home():
    user = User.query.get(current_user.id)
    return render_template('home.html', title='Home', user=user)

#account render
@app.route('/account', methods=['GET'])
@login_required
def account():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id)
        return render_template('account.html', title='Account', user=user)
    else:
        return redirect(url_for('login'))

@app.route('/account/edit_account', methods=['GET', 'POST'])
@login_required
def edit_account():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id)
        if request.method == 'POST':
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email_address = request.form.get('email_address')
            password = request.form.get('password_check')
            dob = request.form.get('dob')
            mailing = request.form.get('mail_list')
            pin = request.form.get('pin')
            user_sub = request.form.get('subs-select')
            ccName = request.form.get('cc-name')
            ccNumber = request.form.get('cc-number')
            ccExpiry = request.form.get('cc-expiry')
            ccCVV = request.form.get('cc-cvv')

        # define form fields and types dynamically
        fields = {
            'email_address': 'Email Address',
            'password': 'Password',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'mailing': 'Subscribe to Mailing List',
            'pin': 'PIN',
            'subscription': 'Subscription Type',
            'cc-name': 'Name on Card',
            'cc-number': 'Card Number',
            'cc-expiry': 'Card Expiry Date',
            'cc-cvv': 'Card CVV'
        }

        field_types = {
            'email_address': 'email',
            'password': 'password',
            'first_name': 'text',
            'last_name': 'text',
            'mailing': 'checkbox',
            'pin': 'text',
            'subscription': 'select',
            'cc-name': 'text',
            'cc-number': 'text',
            'cc-expiry': 'text',
            'cc-cvv': 'text'
        }

        if email_address != user.email_address:
                email_exists = User.query.filter(User.email_address == email_address).first()
                if email_exists:
                    flash('Email address is already registered.', 'error')
                    return redirect(url_for('edit_account'))
                else:
                    user.email_address = email_address

        user.first_name = first_name
        user.last_name = last_name
        user.dob = dob
        user.mailing = mailing
        user.pin = pin
        sub = Subscription.query.filter_by(sub_type=user_sub).first()
        user.subscription_id = sub.id

        card = user.cards[0] if user.cards else None
        if card:
            card.name_on_card = ccName
            card.card_number = ccNumber
            card.expiry_date = ccExpiry
            card.cvv = ccCVV
        else:
            card = CardDetail(name_on_card=ccName, card_number=ccNumber, expiry_date=ccExpiry, cvv=ccCVV)
            user.cards.append(card)

        if password:
            user.password = generate_password_hash(password, method='sha256')

        db.session.commit()

        flash('Details changed successfully', 'success')
        return redirect(url_for('edit_account'))

    subscriptions = Subscription.query.all()

    return render_template('edit_account.html', title='Edit Account', user=user, fields=fields, field_types=field_types, subscriptions=subscriptions)

#index render
@app.route('/index')
def index():
    return render_template("index.html")


#search bar render'
@app.route('/search', methods=['GET'])
@login_required
def search():
    query = request.args.get('query')
    films = Film.query.filter(Film.title.ilike(f'%{query}%')).all()
    actors = Actor.query.filter(Actor.name.ilike(f'%{query}%')).all() 
    genres = Genre.query.filter(Genre.genre.ilike(f'%{query}%')).all()
    tv_series = TVSeries.query.filter(TVSeries.title.ilike(f'%{query}%')).all()
    actor_shows = dict()
    genre_tv_shows = dict()
    genre_films = dict()

    if actors:
        for actor in actors:
            if actor.episodes:
                tv_show = set()
                for episode in actor.episodes:
                    tv_show.add(episode.seasons.tv_series.title)
                actor_shows[actor.name]=list(tv_show)

    if genres:
        for genre in genres:
            tv_shows = TVSeries.query.join(TVSeriesSeason).join(TVSeriesEpisode).join(episode_genre).join(Genre).filter(Genre.genre == genre.genre).all()
            g_films = Film.query.join(film_genre).join(Genre).filter(Genre.genre == genre.genre).all()
            show_names = set()
            film_names = set()
            for show in tv_shows:
                show_names.add(show.title)
            genre_tv_shows[genre.genre] = show_names
            for film in g_films:
                film_names.add(film.title)
            genre_films[genre.genre] = film_names
            

    return render_template('search_results.html', query=query, films=films, actors=actors, genres=genres, tv_series=tv_series, actor_shows=actor_shows, genre_tv_shows=genre_tv_shows, genre_films=genre_films)


@app.route('/film/film_player/<string:name>')
@login_required
def film_player(name):
    film = Film.query.filter_by(title=name).first_or_404()
    video_file = "/videos/" + name.lower().replace(" ", "_") + ".mp4"
    pinCheck = False
    if film.age_rating == "R":
        pinCheck = True
    return render_template('film_player.html', film=film, pinCheck=pinCheck, video=video_file)

@app.route('/series/series_player/<string:name>/<string:episode>')
@login_required
def series_player(name, episode):
    series = TVSeries.query.filter_by(title=name).first_or_404()
        
    if series:
        season_number, episode_number = episode[1:].split('E')
        season_number = int(season_number)
        episode_number = int(episode_number)

        if name == "Friends" and season_number == 1:
            video_file = "/videos/" + name.lower().replace(" ", "_") + "_" + episode + ".mp4"
        else:
            video_file = "/videos/" + name.lower().replace(" ", "_") + ".mp4"
        season = TVSeriesSeason.query.filter_by(tv_series_id=series.id, season_number=season_number).first_or_404()

        if season:
            episode = TVSeriesEpisode.query.filter_by(tv_series_season_id=season.id, episode_number=episode_number).first_or_404()

    return render_template('series_player.html', series=series, season=season, episode=episode, video=video_file)

@app.route('/check_pin', methods=['POST'])
def check_pin():
    film_id = request.args.get('film')
    video = request.args.get('video')

    user = User.query.get(current_user.id)
    user_pin = user.pin
    input_pin = request.form['inputPin']

    film = Film.query.filter_by(id=film_id).first_or_404()
    
    if input_pin == user_pin:
        pinCheck = False
        return render_template('film_player.html', film=film, pinCheck=pinCheck, video=video) 
    else:
        pinCheck = True
        flash('Wrong Pin')
        return render_template('film_player.html', film=film, pinCheck=pinCheck, video=video) 



