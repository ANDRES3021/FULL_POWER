-- a script that prepares a MySQL server for the project

FLUSH PRIVILEGES;
CREATE DATABASE IF NOT EXISTS my_store;
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'adminpwd';
GRANT ALL PRIVILEGES ON my_store.* TO 'admin'@'localhost';
GRANT SELECT ON performance_schema.* TO 'admin'@'localhost';
