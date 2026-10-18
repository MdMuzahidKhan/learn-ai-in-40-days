.headers on
.mode column

SELECT 'Query 1: Select all customers from USA' AS info;
SELECT *
FROM Customers
WHERE country = 'USA';

SELECT 'Query 2: Total orders per customer' AS info;
SELECT c.customer_name, COUNT(o.order_id) AS total_orders
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name;

SELECT 'Query 3: Customer name and order date using JOIN' AS info;
SELECT c.customer_name, o.order_date
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id;

SELECT 'Query 4: Top 3 products by total quantity sold' AS info;
SELECT p.product_name, SUM(oi.quantity) AS total_quantity_sold
FROM OrderItems oi
JOIN Products p ON oi.product_id = p.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity_sold DESC
LIMIT 3;

SELECT 'Query 5: Customers who have never placed an order' AS info;
SELECT c.customer_name
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

SELECT 'Query 6: Total revenue per product' AS info;
SELECT p.product_name, SUM(oi.quantity * p.price) AS total_revenue
FROM OrderItems oi
JOIN Products p ON oi.product_id = p.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_revenue DESC;

SELECT 'Query 7: Total spending per customer' AS info;
SELECT c.customer_name, SUM(oi.quantity * p.price) AS total_spending
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN OrderItems oi ON o.order_id = oi.order_id
JOIN Products p ON oi.product_id = p.product_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spending DESC;

SELECT 'Query 8: Orders placed in February 2024' AS info;
SELECT order_id, customer_id, order_date
FROM Orders
WHERE order_date BETWEEN '2024-02-01' AND '2024-02-29';

SELECT 'Query 9: Average product price by category' AS info;
SELECT category, AVG(price) AS average_price
FROM Products
GROUP BY category;

SELECT 'Query 10: Products never ordered' AS info;
SELECT p.product_name
FROM Products p
LEFT JOIN OrderItems oi ON p.product_id = oi.product_id
WHERE oi.order_item_id IS NULL;