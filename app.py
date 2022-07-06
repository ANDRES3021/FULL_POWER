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
    """ Index """
    return render_template('index.html')

@app.route('/formcompra.html')
def compra_route():
    """ Compra """
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT product.desc_product, product.price, product.serial_product, supplier.name, mov.date_mov FROM product INNER JOIN mov ON product.mov_id = mov.id_mov INNER JOIN supplier ON supplier.id_supplier = mov.supplier_id')
    data = cursor.fetchall()
    print(data)   
    return render_template('formcompra.html',data=data)

@app.route('/formventas.html')
def ventas_route():
    """ Ventas """
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT product.desc_product, product.price, product.serial_product, client.name, mov.date_mov FROM product INNER JOIN mov ON product.mov_id = mov.id_mov INNER JOIN client ON client.id_client = mov.client_id')
    data = cursor.fetchall()
    print(data)
    cursor.execute("WITH productos_vendidos AS\
                  (SELECT id_product, serial_product\
                  FROM consulta WHERE type_prod= 'venta'),\
                  stock AS (SELECT *FROM consulta\
                  WHERE(id_product, serial_product)\
                  NOT IN (SELECT * FROM productos_vendidos))\
                  SELECT id_product, COUNT(serial_product)\
                  AS cantidad_productos\
                  FROM stock GROUP BY id_product")
    data1 = cursor.fetchall()
    print(data1)
    return render_template('formventas.html',data=data, data1=data1)

@app.route('/forminventario.html')
def inventario_route():
    """ Inventario """
    # venta = "venta"
    cursor = mysql.connection.cursor()
    venta = "venta"
    cursor.execute("WITH productos_vendidos AS\
                  (SELECT id_product, serial_product\
                  FROM consulta WHERE type_prod= 'venta'),\
                  stock AS (SELECT *FROM consulta\
                  WHERE(id_product, serial_product)\
                  NOT IN (SELECT * FROM productos_vendidos))\
                  SELECT id_product, COUNT(serial_product)\
                  AS cantidad_productos\
                  FROM stock GROUP BY id_product")
    data = cursor.fetchall()
    print(data)
    return render_template('forminventario.html',data=data)

@app.route('/formventasdeldia.html')
def venta_dia_route():
    """ Ventas del dia """
    return render_template('formventasdeldia.html')

@app.route('/formproveedores.html')
def proveedores_route():
    """ Proveedores """
    return render_template('formproveedores.html')



@app.route('/new_client', methods=['POST', 'GET'])
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

    return render_template('formventas.html')
        
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
      
        return render_template('formcompra.html')

@app.route('/new_product', methods=['POST', 'GET'])
def addproduct_route():
    """ new product """
    if mysql:
        print("Connection Successful!")
        cursor = mysql.connection.cursor()
    else:
        print("Connection Failed!")

    # if request.method == 'POST':
        
    quantity = request.form['quantity']
    ser_prod = request.form['serial']
    typep = request.form['type']
    precio = request.form['price']
    descrpp = request.form['descrpp']
    cursor.execute('INSERT INTO product (quantity, serial_product, type_prod, price, desc_product) VALUES(%s, %s, %s, %s, %s)',
    (quantity,ser_prod, typep, precio, descrpp))
    cursor.execute(f"""UPDATE product SET mov_id = (SELECT MAX(id_mov) FROM mov) WHERE serial_product = {ser_prod} AND type_prod = '{typep}'""")
    mysql.connection.commit()
    print(typep)
    
    return render_template('formventas.html')

    

@app.route('/edit')
def edit_route():
    """ new product """
    
    return "editado"

@app.route('/delete')
def delete_route():
    """ new product """
    
    return"borrado"



if __name__ == "__main__":
    app.run(debug=True, port=3000)