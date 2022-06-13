CREATE TABLE IF NOT EXISTS producto (codigo_producto INT PRIMARY KEY,
precio INT, movimiento_id INT,
FOREIGN KEY (movimiento_id) REFERENCES movimiento (id_movimiento));
