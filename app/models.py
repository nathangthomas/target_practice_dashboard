from flask import Flask
from app import app
from flask import render_template

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String())
    name = db.Column(db.String())
    # session = db.relationship('session', lazy=True)
    # timeline = db.relationship('timeline', lazy=True)

    def __init__(self, name, session, timeline, date):
        self.name = name
        # self.session = session
        # self.timeline = timeline
        self.date = date

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Session(db.Model):
    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime())
    target_size = db.Column(db.Integer())
    hits = db.Column(db.Integer())
    misses = db.Column(db.Integer())
    user = db.relationship('User', lazy=True)
    timeline = db.relationship('Timeline', lazy=True)

    def __init__(self, date, target_size, hits, misses, user, timeline):
        self.date = date
        self.target_size = target_size
        self.hits = hits
        self.misses = misses
        self.user = user
        self.timeline = timeline


    def __repr__(self):
        return '<id {}>'.format(self.id)

class Timeline(db.Model):
    __tablename__ = 'timelines'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime())
    user = db.relationship('User', lazy=True)
    sessions = db.relationship('Session', lazy=True)

    def __init__(self, date, target_size, hits, misses, user, timeline):
        self.date = date
        self.user = user
        self.sessions = sessions


    def __repr__(self):
        return '<id {}>'.format(self.id)
