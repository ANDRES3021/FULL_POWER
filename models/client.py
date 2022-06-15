#!/usr/bin/python3
from models.engine.db import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    numer_identy = db.Column(db.Integer, unique=True)
    
    def __init__(self, name, number_identy):
        self.name = name
        self.numer_identy = number_identy
 