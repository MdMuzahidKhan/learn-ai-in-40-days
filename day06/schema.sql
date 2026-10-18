DROP TABLE IF EXISTS OrderItems;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Customers;

CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    country TEXT NOT NULL,
    city TEXT NOT NULL
);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
);

CREATE TABLE OrderItems (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO Customers (customer_id, customer_name, country, city) VALUES
(1, 'Alice', 'USA', 'New York'),
(2, 'Bob', 'India', 'Mumbai'),
(3, 'Charlie', 'USA', 'Chicago'),
(4, 'Diana', 'UK', 'London'),
(5, 'Ethan', 'India', 'Delhi'),
(6, 'Fatima', 'UAE', 'Dubai');

INSERT INTO Orders (order_id, customer_id, order_date) VALUES
(101, 1, '2024-01-10'),
(102, 2, '2024-01-15'),
(103, 1, '2024-02-05'),
(104, 4, '2024-02-20'),
(105, 2, '2024-03-01'),
(106, 5, '2024-03-10');

INSERT INTO Products (product_id, product_name, category, price) VALUES
(1, 'Laptop', 'Electronics', 800.00),
(2, 'Mouse', 'Electronics', 20.00),
(3, 'Keyboard', 'Electronics', 30.00),
(4, 'Notebook', 'Stationery', 5.00),
(5, 'Pen', 'Stationery', 2.00),
(6, 'Headphones', 'Electronics', 50.00);

INSERT INTO OrderItems (order_item_id, order_id, product_id, quantity) VALUES
(1, 101, 1, 1),
(2, 101, 2, 2),
(3, 102, 4, 5),
(4, 102, 5, 10),
(5, 103, 3, 1),
(6, 103, 2, 1),
(7, 104, 6, 2),
(8, 104, 4, 3),
(9, 105, 1, 1),
(10, 105, 5, 4),
(11, 106, 2, 3),
(12, 106, 3, 2);