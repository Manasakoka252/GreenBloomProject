CREATE DATABASE IF NOT EXISTS green_bloom_db;
USE green_bloom_db;

-- Plants table
CREATE TABLE IF NOT EXISTS plants (
    plant_id INT PRIMARY KEY,
    plant_name VARCHAR(100),
    category VARCHAR(50),
    price FLOAT,
    quantity INT,
    supplier_name VARCHAR(100)
);


-- Suppliers table
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id VARCHAR(10) PRIMARY KEY,
    supplier_name VARCHAR(100),
    phone VARCHAR(20),
    city VARCHAR(50)
);


-- Customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100),
    phone VARCHAR(20),
    city VARCHAR(50)
);


-- Sales table
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    plant_name VARCHAR(100),
    quantity INT,
    total_amount FLOAT,
    sale_date DATE
);