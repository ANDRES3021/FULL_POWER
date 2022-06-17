from crypt import methods
from flask import render_template, request, redirect
from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'adminpwd'
app.config['MYSQL_DB'] = 'mi_negocio'


mysql = MySQL(app)

#metodo get
@app.route('/')
def index_route():
    """ inicio """
    return render_template('index.html')

@app.route('/new_client', methods=['POST'])
def addclient_route():
    """ new client """
    if mysql:
        print("Connection Successful!")
        cursor = mysql.connection.cursor()
    else:
        print("Connection Failed!")

    if request.method == 'POST':
        
        cedula = request.form['cedula']
        name = request.form['name']
        cursor.execute('INSERT INTO cliente (id_cliente, name) VALUES(%s, %s)',
        (cedula, name))
        mysql.connection.commit()
        
        return redirect('/')
    
@app.route('/new_supplier', methods=['POST'])
def addsupp_route():
    """ new supp """
    if mysql:
        print("Connection Successful!")
        cursor = mysql.connection.cursor()
    else:
        print("Connection Failed!")

    if request.method == 'POST':
        
        nit = request.form['nit']
        name = request.form['name']
        location = request.form['location']
        cursor.execute('INSERT INTO proveedor (id_proveedor, name, ubicacion) VALUES(%s, %s, %s)',
        (nit, name, location))
        mysql.connection.commit()
        
        return redirect('/')


@app.route('/new_product', methods=['POST'])
def addproduct_route():
    """ new product """
    if mysql:
        print("Connection Successful!")
        cursor = mysql.connection.cursor()
    else:
        print("Connection Failed!")

    if request.method == 'POST':
        
        cod_prod = request.form['codigo_producto']
        ser_prod = request.form['serial_producto']
        tipo = request.form['tipo']
        precio = request.form['precio']
        cursor.execute('INSERT INTO producto(codigo_producto, serial_producto, tipo, precio) VALUES(%s, %s, %s, %s)',
        (cod_prod, ser_prod, tipo, precio))
        mysql.connection.commit()
        
        return redirect('/')
    

@app.route('/edit')
def edit_route():
    """ new product """
    
    return "editado"

@app.route('/delete')
def delete_route():
    """ new product """
    
    return"borrado"



if __name__ == "__main__":
    app.run(debug=True, port=5000)