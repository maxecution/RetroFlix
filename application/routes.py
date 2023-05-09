from flask import render_template, request, redirect, url_for, session, flash, jsonify
from builtins import getattr
from application import app
from application.models import *
from flask_login import current_user, login_required, logout_user
from werkzeug.security import generate_password_hash


context = {
    'getattr': getattr
}


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

@app.route('/edit_account/<string:field>', methods=['GET', 'POST'])
def edit_account(field):
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id) # retrieve user info from database
    else:
        flash('Please log in to access your account.')
        return redirect(url_for('login'))
    
    current_value = getattr(user, field)

    if request.method == 'GET':

        if field == 'email_address':
            current_value = user.email_address
        elif field == 'password':
            current_value = ''
        elif field == 'first_name':
            current_value = user.first_name
        elif field == 'last_name':
            current_value = user.last_name
        elif field == 'mailing':
            current_value = user.mailing
        elif field == 'pin':
            current_value = user.pin
        elif field == 'subscription':
            current_value = user.subscription.sub_type
        else:
            field == 'card_details'
            card = user.cards[0]
            current_value = {
                'card_number': card.card_number,
                'expiry_date': card.expiry_date,
                'cvv': card.cvv
            }

    if request.method == 'POST':
        # update user information in database
        if field == 'email_address':
            user.email_address = request.form['new_{}'.format(field)]
        elif field == 'password':
            user.password = generate_password_hash(request.form['new_{}'.format(field)])
        elif field == 'first_name':
            user.first_name = request.form['new_{}'.format(field)]
        elif field == 'last_name':
            user.last_name = request.form['new_{}'.format(field)]
        elif field == 'mailing':
            user.mailing = request.form['new_{}'.format(field)]
        elif field == 'pin':
            user.pin = request.form['new_{}'.format(field)]
        elif field == 'subscription':
            # update user subscription information
            user.subscription.sub_type = request.form['sub_type']
        else:
            field == 'card_details'
            # update card information
            card = user.cards[0] # assuming there's only one card per user
            card.card_number = request.form['card_number']
            card.expiry_date = request.form['expiry_date']
            card.cvv = request.form['cvv']

        db.session.commit() # commit changes to database
        flash('Your account information has been updated successfully.')
        return redirect(url_for('account'))
    else:
        return render_template('edit_account.html', field=field, user=user, current_value=current_value)
    

@app.route('/delete-account', methods=['GET', 'POST'])
@login_required
def delete_account():
    if request.method == 'POST':
        # Check if user really wants to delete account
        if request.form.get('confirm_delete') == 'yes':
            # Delete all user details from the database
            user = User.query.filter_by(email=session['user_email']).first()
            db.session.delete(user)
            db.session.commit()
            logout_user()
            flash('Your account has been successfully deleted')
            return redirect(url_for('index'))
    # Render the confirmation page if user hasn't confirmed yet
    return render_template('delete_account.html')
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



