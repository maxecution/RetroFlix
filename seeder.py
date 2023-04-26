from application import db, Actor, Genre, Film
from application import app

# Create actors

sam_neill = Actor(name='Sam Neill')
laura_dern = Actor(name='Laura Dern')
jeff_goldblum = Actor(name='Jeff Goldblum')
zach_galligan = Actor(name='Zach Galligan')
phoebe_cates = Actor(name='Phoebe Cates')
hoyt_axton = Actor(name='Hoyt Axton')
bill_murray = Actor(name='Bill Murray')
dan_aykroyd = Actor(name='Dan Aykroyd')
sigourney_weaver = Actor(name='Sigourney Weaver')
henry_thomas = Actor(name='Henry Thomas')
drew_barrymore = Actor(name='Drew Barrymore')
dee_wallace = Actor(name='Dee Wallace')
harrison_ford = Actor(name='Harrison Ford')
rutger_hauer = Actor(name='Rutger Hauer')
sean_young = Actor(name='Sean Young')
arnold_schwarzenegger = Actor(name='Arnold Schwarzenegger')
michael_biehn = Actor(name='Michael Biehn')
linda_hamilton = Actor(name='Linda Hamilton')


actors = [
    sam_neill,   
    laura_dern,   
    jeff_goldblum,   
    zach_galligan,   
    phoebe_cates,   
    hoyt_axton,   
    bill_murray,   
    dan_aykroyd,   
    sigourney_weaver,   
    henry_thomas,   
    drew_barrymore,   
    dee_wallace,   
    harrison_ford,   
    rutger_hauer,   
    sean_young,   
    arnold_schwarzenegger,   
    michael_biehn,   
    linda_hamilton
]


# Create genres

action = Genre(genre='Action')
adventure = Genre(genre='Adventure')
comedy = Genre(genre='Comedy')
family = Genre(genre='Family')
fantasy = Genre(genre='Fantasy')
horror = Genre(genre='Horror')
science_fiction = Genre(genre='Science Fiction')
thriller = Genre(genre='Thriller')

genres = [
    action,    
    adventure,    
    comedy,    
    family,    
    fantasy,    
    horror,    
    science_fiction,    
    thriller
]


# Create films

jurassic_park = Film(title='Jurassic Park', release_year=1993, duration='02:07:00', age_rating='PG-13', rating=8.2)
gremlins = Film(title='Gremlins', release_year=1984, duration='01:46:00', age_rating='PG', rating=7.3)
ghostbusters = Film(title='Ghostbusters', release_year=1984, duration='01:45:00', age_rating='PG', rating=7.8)
et = Film(title='E.T. the Extra-Terrestrial', release_year=1982, duration='01:55:00', age_rating='PG', rating=7.9)
blade_runner = Film(title='Blade Runner', release_year=1982, duration='01:57:00', age_rating='R', rating=8.1)
terminator = Film(title='The Terminator', release_year=1984, duration='01:47:00', age_rating='R', rating=8.1)

films = [
    jurassic_park,    
    gremlins,    
    ghostbusters,    
    et,   
    blade_runner,    
    terminator
]


# Add genre, actor and film data to the database

with app.app_context():
    db.session.add_all(actors)
    db.session.add_all(genres)
    db.session.add_all(films)
    db.session.commit()
    
    # Create film_actor associations

    jurassic_park.actors.append(sam_neill)
    jurassic_park.actors.append(laura_dern)
    jurassic_park.actors.append(jeff_goldblum)
    gremlins.actors.append(zach_galligan)
    gremlins.actors.append(phoebe_cates)
    gremlins.actors.append(hoyt_axton)
    ghostbusters.actors.append(bill_murray)
    ghostbusters.actors.append(dan_aykroyd)
    ghostbusters.actors.append(sigourney_weaver)
    et.actors.append(henry_thomas)
    et.actors.append(drew_barrymore)
    et.actors.append(dee_wallace)
    blade_runner.actors.append(harrison_ford)
    blade_runner.actors.append(rutger_hauer)
    blade_runner.actors.append(sean_young)
    terminator.actors.append(arnold_schwarzenegger)
    terminator.actors.append(michael_biehn)
    terminator.actors.append(linda_hamilton)

    # Create film_genre associations

    jurassic_park.genres.append(science_fiction)
    jurassic_park.genres.append(adventure)
    jurassic_park.genres.append(thriller)
    gremlins.genres.append(comedy)
    gremlins.genres.append(horror)
    gremlins.genres.append(fantasy)
    ghostbusters.genres.append(comedy)
    ghostbusters.genres.append(fantasy)
    et.genres.append(science_fiction)
    et.genres.append(family)
    et.genres.append(adventure)
    blade_runner.genres.append(science_fiction)
    blade_runner.genres.append(thriller)
    terminator.genres.append(science_fiction)
    terminator.genres.append(action)

    db.session.commit()


print('Database seeded successfully!')
