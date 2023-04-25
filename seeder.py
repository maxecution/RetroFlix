from application import db, Actor, Genre, Film, FilmActor, FilmGenre

# Create actors
actors = [
    Actor(name='Sam Neill'),
    Actor(name='Laura Dern'),
    Actor(name='Jeff Goldblum'),
    Actor(name='Zach Galligan'),
    Actor(name='Phoebe Cates'),
    Actor(name='Hoyt Axton'),
    Actor(name='Bill Murray'),
    Actor(name='Dan Aykroyd'),
    Actor(name='Sigourney Weaver'),
    Actor(name='Henry Thomas'),
    Actor(name='Drew Barrymore'),
    Actor(name='Dee Wallace'),
    Actor(name='Harrison Ford'),
    Actor(name='Rutger Hauer'),
    Actor(name='Sean Young'),
    Actor(name='Arnold Schwarzenegger'),
    Actor(name='Michael Biehn'),
    Actor(name='Linda Hamilton'),
]

# Create genres
genres = [
    Genre(genre='Action'),
    Genre(genre='Adventure'),
    Genre(genre='Comedy'),
    Genre(genre='Family'),
    Genre(genre='Fantasy'),
    Genre(genre='Horror'),
    Genre(genre='Science Fiction'),
    Genre(genre='Thriller'),
]

# Create films
films = [
    Film(title='Jurassic Park', release_year=1993, duration='02:07:00', age_rating='PG-13', rating=8.2),
    Film(title='Gremlins', release_year=1984, duration='01:46:00', age_rating='PG', rating=7.3),
    Film(title='Ghostbusters', release_year=1984, duration='01:45:00', age_rating='PG', rating=7.8),
    Film(title='E.T. the Extra-Terrestrial', release_year=1982, duration='01:55:00', age_rating='PG', rating=7.9),
    Film(title='Blade Runner', release_year=1982, duration='01:57:00', age_rating='R', rating=8.1),
    Film(title='The Terminator', release_year=1984, duration='01:47:00', age_rating='R', rating=8.1),
]

# Add genre, actor and film data to the database
db.session.add_all(actors)
db.session.add_all(genres)
db.session.add_all(films)
db.session.commit()

# Create film_actor associations
films_actors = [
    FilmActor(film_id=1, actor_id=1), # Jurassic Park, Sam Neill
    FilmActor(film_id=1, actor_id=2), # Jurassic Park, Laura Dern
    FilmActor(film_id=1, actor_id=3), # Jurassic Park, Jeff Goldblum
    FilmActor(film_id=2, actor_id=4), # Gremlins, Zach Galligan
    FilmActor(film_id=2, actor_id=5), # Gremlins, Phoebe Cates
    FilmActor(film_id=2, actor_id=6), # Gremlins, Hoyt Axton
    FilmActor(film_id=3, actor_id=7), # Ghostbusters, Bill Murray
    FilmActor(film_id=3, actor_id=8), # Ghostbusters, Dan Aykroyd
    FilmActor(film_id=3, actor_id=9), # Ghostbusters, Sigourney Weaver
    FilmActor(film_id=4, actor_id=10), # E.T., Henry Thomas
    FilmActor(film_id=4, actor_id=11), # E.T., Drew Barrymore
    FilmActor(film_id=4, actor_id=12), # E.T., Dee Wallace
    FilmActor(film_id=5, actor_id=13), # Blade Runner, Harrison Ford
    FilmActor(film_id=5, actor_id=14), # Blade Runner, Rutger Hauer
    FilmActor(film_id=5, actor_id=15), # Blade Runner, Sean Young
    FilmActor(film_id=6, actor_id=16), # Terminator, Arnold Schwarzenegger
    FilmActor(film_id=6, actor_id=17), # Terminator, Michael Biehn
    FilmActor(film_id=6, actor_id=18) # Terminator, Linda Hamilton
]

# Add films_actors data to the database
db.session.add_all(films_actors)
db.session.commit()

# Create film_genre associations
films_genres = [
FilmGenre(film_id=1, genre_id=7), # Jurassic Park, Science Fiction
FilmGenre(film_id=1, genre_id=2), # Jurassic Park, Adventure
FilmGenre(film_id=1, genre_id=2), # Jurassic Park, Adventure
FilmGenre(film_id=1, genre_id=8), # Jurassic Park, Thriller
FilmGenre(film_id=2, genre_id=3), # Gremlins, Comedy
FilmGenre(film_id=2, genre_id=6), # Gremlins, Horror
FilmGenre(film_id=2, genre_id=5), # Gremlins, Fantasy
FilmGenre(film_id=3, genre_id=3), # Ghostbusters, Comedy
FilmGenre(film_id=3, genre_id=5), # Ghostbusters, Fantasy
FilmGenre(film_id=4, genre_id=7), # E.T., Science Fiction
FilmGenre(film_id=4, genre_id=4), # E.T., Family
FilmGenre(film_id=4, genre_id=2), # E.T., Adventure
FilmGenre(film_id=5, genre_id=7), # Blade Runner, Science Fiction
FilmGenre(film_id=5, genre_id=8), # Blade Runner, Thriller
FilmGenre(film_id=6, genre_id=7), # Terminator, Science Fiction
FilmGenre(film_id=6, genre_id=1) # Terminator, Action
]

# Add films_genres data to the database
db.session.add_all(films_genres)
db.session.commit()

print('Database seeded successfully!')
