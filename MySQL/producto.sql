CREATE TABLE IF NOT EXISTS producto (codigo_producto INT,
serial_producto INT, tipo VARCHAR(20), precio INT, movimiento_id INT,
PRIMARY KEY(codigo_producto, serial_producto, tipo),
FOREIGN KEY (movimiento_id) REFERENCES movimiento (id_movimiento));
