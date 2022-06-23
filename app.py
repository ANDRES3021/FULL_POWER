from crypt import methods
from flask import render_template, request, redirect
from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'adminpwd'
app.config['MYSQL_DB'] = 'my_store'


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
        
        name = request.form['name']
        doc_ident = request.form['docident']
        cursor.execute('INSERT INTO client(name, doc_identify ) VALUES(%s, %s)',
        (name, doc_ident))
        # esta query nos permite relacionar llaves foraneas
        cursor.execute('INSERT INTO mov (client_id) SELECT MAX(id_client) FROM client')
        mysql.connection.commit()
        
        return redirect('/')
    
@app.route('/new_supplier', methods=['POST', 'GET'])
def addsupp_route():
    """ new supp """
    if mysql:
        print("Connection Successful!")
        cursor = mysql.connection.cursor()
    else:
        print("Connection Failed!")

    if request.method == 'POST':
        
        name = request.form['name']
        location = request.form['location']
        nit = request.form['nit']
        cursor.execute('INSERT INTO supplier (name, address_sup, NIT) VALUES(%s, %s, %s)',
        (name, location, nit))
        
        cursor.execute('INSERT INTO mov (supplier_id) SELECT MAX(id_supplier) FROM supplier')
                
        mysql.connection.commit()
            
            
        return redirect('/')

@app.route('/new_product', methods=['POST', 'GET'])
def addproduct_route():
    """ new product """
    if mysql:
        print("Connection Successful!")
        cursor = mysql.connection.cursor()
    else:
        print("Connection Failed!")

    if request.method == 'POST':
        
        quantity = request.form['quantity']
        ser_prod = request.form['serial']
        typep = request.form['type']
        precio = request.form['price']
        descrpp = request.form['descrpp']
        cursor.execute('INSERT INTO product (quantity, serial_product, type_prod, price, desc_product) VALUES(%s, %s, %s, %s, %s)',
        (quantity,ser_prod, typep, precio, descrpp))
        
        cursor.execute('INSERT INTO product(mov_id) SELECT MAX(id_mov) FROM mov')
        
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