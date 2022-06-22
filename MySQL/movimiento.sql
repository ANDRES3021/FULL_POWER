CREATE TABLE IF NOT EXISTS movimiento (id_movimiento INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
ON UPDATE CURRENT_TIMESTAMP, proveedor_id INT, cliente_id INT,
FOREIGN KEY (proveedor_id) REFERENCES proveedor (id_proveedor),
FOREIGN KEY (cliente_id) REFERENCES client (id_client));
