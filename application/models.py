from .database import db

# Association tables need defined before classes

film_actor = db.Table(
    "film_actor",
    db.Column("film_id", db.Integer, db.ForeignKey("films.id"), primary_key=True),
    db.Column("actor_id", db.Integer, db.ForeignKey("actors.id"), primary_key=True),
)

film_genre = db.Table(
    "film_genre",
    db.Column("film_id", db.Integer, db.ForeignKey("films.id"), primary_key=True),
    db.Column("actor_id", db.Integer, db.ForeignKey("genres.id"), primary_key=True),
)

episode_actor = db.Table(
    "episode_actor",
    db.Column("episode_id", db.Integer, db.ForeignKey("tv_series_episodes.id"), primary_key=True),
    db.Column("actor_id", db.Integer, db.ForeignKey("actors.id"), primary_key=True),
)

episode_genre = db.Table(
    "episode_genre",
    db.Column("episode_id", db.Integer, db.ForeignKey("tv_series_episodes.id"), primary_key=True),
    db.Column("genre_id", db.Integer, db.ForeignKey("genres.id"), primary_key=True),
)


"""
When you define relationships, ensure you are consistently naming both sides the same when using back_populates eg:
class Parent(db.Model):
    ...
    children = relationship(back_populates="parents_with_different_relationship_name")

class Child(db.Model):
    ...
    parents_with_different_relationship_name = relationship(back_populates="children") 
"""

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

    actors = db.relationship('Actor', secondary='film_actor', back_populates='films')
    genres = db.relationship('Genre', secondary='film_genre', back_populates='films')


class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    films = db.relationship('Film', secondary='film_actor', back_populates='actors')
    episodes = db.relationship('TVSeriesEpisode', secondary='episode_actor', back_populates='actors')


class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    films = db.relationship('Film', secondary='film_genre', back_populates='genres')
    episodes = db.relationship('TVSeriesEpisode', secondary='episode_genre', back_populates='genres')


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
    tv_series_season_id = db.Column(db.Integer, db.ForeignKey('tv_series_seasons.id'))
    episode_number = db.Column(db.Integer)
    title = db.Column(db.String(255))
    release_year = db.Column(db.Integer)
    duration = db.Column(db.Time)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    seasons = db.relationship('TVSeriesSeason', back_populates='episodes')
    actors = db.relationship('Actor', secondary='episode_actor', back_populates='episodes')
    genres = db.relationship('Genre', secondary='episode_genre', back_populates='episodes')
