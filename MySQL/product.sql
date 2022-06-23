CREATE TABLE IF NOT EXISTS product (id_product INT NOT NULL AUTO_INCREMENT, quantity INT,
serial_product INT NOT NULL, type_prod VARCHAR(20), price INT, mov_id INT, desc_product VARCHAR(80),
PRIMARY KEY(id_product, serial_product, type_prod),
FOREIGN KEY (mov_id) REFERENCES mov (id_mov));
