CREATE TABLE IF NOT EXISTS movimiento (id_movimiento INT PRIMARY KEY,
fecha DATE, proveedor_id INT, cliente_id INT,
FOREIGN KEY (proveedor_id) REFERENCES proveedor (id_proveedor),
FOREIGN KEY (cliente_id) REFERENCES cliente (id_cliente));
