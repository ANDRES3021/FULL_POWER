SELECT product.desc_product, product.price, product.serial_product, supplier.name, mov.date_mov
FROM product INNER JOIN mov ON product.mov_id = mov.id_mov
             INNER JOIN supplier ON supplier.id_supplier = mov.supplier_id;