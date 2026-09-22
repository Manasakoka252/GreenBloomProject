# 🌱 Green Bloom Plants – Plant Inventory Management System

## 📌 Project Overview

**Green Bloom Plants** is a Python and MySQL-based plant inventory management system designed for a nursery shop.

The system helps manage plants, suppliers, customers, billing, stock, and sales reports through a simple menu-driven application.

## ✨ Features

### 🌿 Plant Management

* Add new plants
* View all plants
* Update plant price and quantity
* Delete plants
* Search plants by name

### 🚚 Supplier Management

* Add suppliers
* View suppliers
* Update supplier details
* Delete suppliers

### 👤 Customer Management

* Add customers
* Automatically generate customer IDs
* View customer details
* View customer purchase history

### 🧾 Billing

* Select a customer
* Select a plant
* Enter purchase quantity
* Calculate the total amount
* Generate a bill
* Automatically reduce plant stock
* Store sales information
* Validate available stock

### 📊 Reports

* Total sales
* Available plant stock
* Low-stock plants
* Customer purchase history

### 🔒 Error Handling

* Handles invalid numeric input
* Checks whether customers and plants exist
* Checks insufficient stock
* Uses database transactions with `commit()` and `rollback()`

## 🛠️ Technologies Used

* **Python**
* **MySQL**
* **mysql-connector-python**
* **VS Code**

## 📁 Project Structure

```text
GreenBloomProject/
│
├── main.py
├── db_connection.py
├── plant_module.py
├── supplier_module.py
├── customer_module.py
├── billing_module.py
├── reports_module.py
├── requirements.txt
├── database.sql
├── README.md
└── .gitignore
```

## 🗄️ Database

The project uses a MySQL database named:

```text
green_bloom_db
```

The database contains the following tables:

```text
plants
suppliers
customers
sales
```

### Plants

Stores plant details such as:

* Plant ID
* Plant name
* Category
* Price
* Quantity
* Supplier name

### Suppliers

Stores:

* Supplier ID
* Supplier name
* Phone
* City

### Customers

Stores:

* Customer ID
* Customer name
* Phone
* City

Customer IDs are automatically generated using MySQL `AUTO_INCREMENT`.

### Sales

Stores:

* Sale ID
* Customer ID
* Plant name
* Quantity
* Total amount
* Sale date

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Manasakoka252/GreenBloomProject.git
```

### 2. Open the project folder

```bash
cd GreenBloomProject
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Set up MySQL

Make sure MySQL is installed and running.

Use the SQL commands provided in:

```text
database.sql
```

to create the required database and tables.

### 5. Configure the database connection

Create a `.env` file in the project folder and add your MySQL password:

```text
DB_PASSWORD=your_mysql_password
```

The `.env` file is excluded from Git using `.gitignore`.

### 6. Run the application

```bash
python main.py
```


## ▶️ How to Run

Run the following command from the project folder:

```bash
python main.py
```

The application will display the main menu:

```text
===== Green Bloom Plants =====

1. Plant Module
2. Supplier Module
3. Customer Module
4. Billing Module
5. Reports Module
6. Exit
```

Select the required option and follow the instructions displayed by the application.

## 🔄 Application Workflow

```text
                Green Bloom Plants
                       │
       ┌───────────────┼───────────────┐
       │               │               │
     Plants         Suppliers       Customers
       │               │               │
       └───────────────┼───────────────┘
                       │
                    Billing
                       │
              ┌────────┴────────┐
              │                 │
        Stock Update        Sales Record
              │                 │
              └────────┬────────┘
                       │
                    Reports
```

## 📚 Concepts Used

This project demonstrates practical use of:

* Python variables
* Conditions
* Loops
* Functions
* Modules
* Exception handling
* MySQL database connectivity
* SQL CRUD operations
* `SELECT`, `INSERT`, `UPDATE`, and `DELETE`
* SQL `WHERE`
* SQL aggregate function `SUM()`
* Database transactions
* `commit()`
* `rollback()`

## 🎯 Project Objective

The objective of this project is to build a simple plant inventory management system that can:

* Manage plant stock
* Manage suppliers
* Manage customers
* Generate bills
* Record sales
* Track inventory
* Generate useful reports

## 👩‍💻 Author

**Manasa Koka**

B.Tech – Computer Science and Engineering
