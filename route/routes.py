from flask import Blueprint, render_template, request, redirect
from models.client import Client
from models.supplier import Supplier
from models.engine.db import db

routes = Blueprint('routes', __name__)

#metodo get
@routes.route('/')
def hello_route():
    """ Hello flask. """
    return render_template('index.html')

#metodo post
@routes.route('/new_client', methods=['POST'])
def new_client():
    """ new cliente """
    #se trae el objeto de la clase
    name = request.form['name']
    number_identy = request.form['cedula']
    #se guarda para instanciar el objeto     
    new_client = Client(name, number_identy)
    db.session.add(new_client)
    db.session.commit()    
    
    return redirect('/')

@routes.route('/new_supplier', methods=['POST'])
def new_supllier():
    """ new supplier """
      
    name = request.form["name"]
    location = request.form["location"]
    identy = request.form['nit']
    new_supplier = Supplier(name, location, identy)
    
    db.session.add(new_supplier)
    db.session.commit()    
    
    return redirect('/')