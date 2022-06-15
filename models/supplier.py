#!/usr/bin/python3
from enum import unique
from sqlalchemy import true
from models.engine.db import db


class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=true)
    name = db.Column(db.String(100), unique=True, nullable=False)
    location = db.Column(db.String(100), unique=True, nullable=False)
    identy = db.Column(db.Integer, unique=True)
    
    def __init__(self, name, location, identy):
        self.name = name
        self.location = location
        self.identy = identy
 