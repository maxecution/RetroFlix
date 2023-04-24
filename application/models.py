from application.database import db

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    release_year = db.Column(db.Integer)
    duration = db.Column(db.Time)
    age_rating = db.Column(db.Text)
    rating = db.Column(db.Decimal(3,1))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())