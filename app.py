#!/usr/bin/python3
""" Starts Flask. """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from route.clients import clients

app = Flask(__name__)

#conexion a la base de datos toca crear un usuario
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:adminpwd@localhost/mi_negocio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(clients)
