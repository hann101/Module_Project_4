from policy import db
from datetime import datetime

class User(db.Model):
	""" Create user table"""
	id = db.Column(db.Integer, primary_key=True)
	password = db.Column(db.String(200), nullable=False)
	level = db.Column(db.String(120), nullable=False)