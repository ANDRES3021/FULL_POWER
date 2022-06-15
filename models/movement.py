#!/usr/bin/python3
from datetime import date
from enum import unique
from sqlalchemy import true
from models.engine.db import db
from models.client import Client
from models.supplier import Supplier



class Movement(db.Model):
    id_movement = db.Column(db.Integer, primary_key=true)
    date = db.Column(db.String(100), unique=True, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('client_id'))
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier_id'))
    
    def __init__(self, name, location):
        self.name = name
        self.location = location