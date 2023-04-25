from application.database import db

class Film(db.Model):
    __tablename__ = 'films'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    release_year = db.Column(db.Integer)
    duration = db.Column(db.Time)
    age_rating = db.Column(db.Text)
    rating = db.Column(db.Float(3,  1))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    actors = db.relationship('Actor', secondary='films_actors', back_populates='films')
    genres = db.relationship('Genre', secondary='films_genres', back_populates='films')

class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    films = db.relationship('Film', secondary='films_actors', back_populates='actors')

class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    films = db.relationship('Film', secondary='films_genres', back_populates='genres')

class FilmActor(db.Model):
    __tablename__ = 'films_actors'
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('Film.id'))
    actor_id = db.Column(db.Integer, db.ForeignKey('Actor.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


class FilmGenre(db.Model):
    __tablename__ = 'films_genres'
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('Film.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


class TVSeries(db.Model):
    __tablename__ = 'tv_series'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    release_year = db.Column(db.Integer)
    age_rating = db.Column(db.String(255))
    rating = db.Column(db.Float(3, 1))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    seasons = db.relationship('TVSeriesSeason', back_populates='tv_series')


class TVSeriesSeason(db.Model):
    __tablename__ = 'tv_series_seasons'
    id = db.Column(db.Integer, primary_key=True)
    tv_series_id = db.Column(db.Integer, db.ForeignKey('tv_series.id'))
    release_year = db.Column(db.Integer)
    season_number = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    tv_series = db.relationship('TVSeries', back_populates='seasons')
    episodes = db.relationship('TVSeriesEpisode', back_populates='seasons')


class TVSeriesEpisode(db.Model):
    __tablename__ = 'tv_series_episodes'
    id = db.Column(db.Integer, primary_key=True)
    tv_series_season_id = db.Column(db.Integer, db.ForeignKey('TVSeriesSeason.id'))
    episode_number = db.Column(db.Integer)
    title = db.Column(db.String(255))
    release_year = db.Column(db.Integer)
    duration = db.Column(db.Time)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    season = db.relationship('TVSeriesSeason', back_populates='episodes')
    actors = db.relationship('Actor', secondary='tv_series_episodes_actors', back_populates='episodes')
    genres = db.relationship('Genre', secondary='tv_series_episodes_genres', back_populates='episodes')


class TVSeriesEpisodeActors(db.Model):
    __tablename__ = 'tv_series_episodes_actors'
    id = db.Column(db.Integer, primary_key=True)
    tv_series_episode_id = db.Column(db.Integer, db.ForeignKey('TVSeriesEpisode.id'))
    actor_id = db.Column(db.Integer, db.ForeignKey('Actor.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


class TVSeriesEpisodeGenre(db.Model):
    __tablename__ = 'tv_series_episodes_genres'
    id = db.Column(db.Integer, primary_key=True)
    tv_series_episode_id = db.Column(db.Integer, db.ForeignKey('TVSeriesEpisode.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('Genre.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
