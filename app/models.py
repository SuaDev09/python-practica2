from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))


class Series(db.Model):
    __tablename__ = 'series'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    state = db.Column(db.String(100))
    temporadas = db.Column(db.Integer)
    capPorTem = db.Column(db.Integer)
