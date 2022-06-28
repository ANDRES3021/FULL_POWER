SELECT product.desc_product, product.price, product.serial_product, client.name, mov.date_mov
FROM product INNER JOIN mov ON product.mov_id = mov.id_mov
             INNER JOIN client ON client.id_client = mov.client_id;
