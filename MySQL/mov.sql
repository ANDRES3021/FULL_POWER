CREATE TABLE IF NOT EXISTS mov (id_mov INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
date_mov TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
ON UPDATE CURRENT_TIMESTAMP, supplier_id INT, client_id INT,
FOREIGN KEY (supplier_id) REFERENCES supplier (id_supplier),
FOREIGN KEY (client_id) REFERENCES client (id_client));
