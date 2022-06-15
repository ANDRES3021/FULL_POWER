from flask import Blueprint, render_template, request
from models.client import Client
from models.engine.db import db

clients = Blueprint('clients', __name__)

#metodo get
@clients.route('/')
def hello_route():
    """ Hello flask. """
    return render_template('index.html')

#metodo post
@clients.route('/new', methods=['POST'])
def new_route():
    """ new cliente """
    #se trae el objeto de la clase
    name = request.form['name']
    
    #se guarda para instanciar el objeto     
    new_client = Client(name)
    print(new_client)
    db.session.add(new_client)
    db.session.commit()    
    
    return "SAVE"