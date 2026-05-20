# Task 1: Ground Truth SQL Queries

## Question 1: List all products
**SQL Query:**
```sql
SELECT * FROM products;
```
**Explanation:** This query fulfills the intent to list all records by querying the products table(s).

## Question 2: Get all customers
**SQL Query:**
```sql
SELECT * FROM customers;
```
**Explanation:** This query fulfills the intent to list all records by querying the customers table(s).

## Question 3: Show all orders
**SQL Query:**
```sql
SELECT * FROM orders;
```
**Explanation:** This query fulfills the intent to list all records by querying the orders table(s).

## Question 4: List all employees
**SQL Query:**
```sql
SELECT * FROM employees;
```
**Explanation:** This query fulfills the intent to list all records by querying the employees table(s).

## Question 5: Get all offices
**SQL Query:**
```sql
SELECT * FROM offices;
```
**Explanation:** This query fulfills the intent to list all records by querying the offices table(s).

## Question 6: Show all product lines
**SQL Query:**
```sql
SELECT * FROM productlines;
```
**Explanation:** This query fulfills the intent to list all records by querying the productlines table(s).

## Question 7: List all payments
**SQL Query:**
```sql
SELECT * FROM payments;
```
**Explanation:** This query fulfills the intent to list all records by querying the payments table(s).

## Question 8: Get product names and prices
**SQL Query:**
```sql
SELECT "productName", "buyPrice" FROM products;
```
**Explanation:** This query fulfills the intent to list specific columns by querying the products table(s).

## Question 9: Get customer names and cities
**SQL Query:**
```sql
SELECT "customerName", "city" FROM customers;
```
**Explanation:** This query fulfills the intent to list specific columns by querying the customers table(s).

## Question 10: List employee first and last names
**SQL Query:**
```sql
SELECT "firstName", "lastName" FROM employees;
```
**Explanation:** This query fulfills the intent to list specific columns by querying the employees table(s).

## Question 11: Get all order dates
**SQL Query:**
```sql
SELECT "orderDate" FROM orders;
```
**Explanation:** This query fulfills the intent to list specific columns by querying the orders table(s).

## Question 12: Show product vendor list
**SQL Query:**
```sql
SELECT DISTINCT "productVendor" FROM products;
```
**Explanation:** This query fulfills the intent to list unique column values by querying the products table(s).

## Question 13: Get all product codes
**SQL Query:**
```sql
SELECT "productCode" FROM products;
```
**Explanation:** This query fulfills the intent to list specific columns by querying the products table(s).

## Question 14: List all countries from offices
**SQL Query:**
```sql
SELECT DISTINCT "country" FROM offices;
```
**Explanation:** This query fulfills the intent to list unique column values by querying the offices table(s).

## Question 15: Show all order statuses
**SQL Query:**
```sql
SELECT DISTINCT "status" FROM orders;
```
**Explanation:** This query fulfills the intent to list unique column values by querying the orders table(s).

## Question 16: Get all payment amounts
**SQL Query:**
```sql
SELECT "amount" FROM payments;
```
**Explanation:** This query fulfills the intent to list specific columns by querying the payments table(s).

## Question 17: List all job titles
**SQL Query:**
```sql
SELECT DISTINCT "jobTitle" FROM employees;
```
**Explanation:** This query fulfills the intent to list unique column values by querying the employees table(s).

## Question 18: Get customer phone numbers
**SQL Query:**
```sql
SELECT "customerName", "phone" FROM customers;
```
**Explanation:** This query fulfills the intent to list specific columns by querying the customers table(s).

## Question 19: Show product MSRP values
**SQL Query:**
```sql
SELECT "productName", "MSRP" FROM products;
```
**Explanation:** This query fulfills the intent to list specific columns by querying the products table(s).

## Question 20: List order numbers
**SQL Query:**
```sql
SELECT "orderNumber" FROM orders;
```
**Explanation:** This query fulfills the intent to list specific columns by querying the orders table(s).

## Question 21: Get orders with customer names
**SQL Query:**
```sql
SELECT o."orderNumber", c."customerName" FROM orders o JOIN customers c ON o."customerNumber" = c."customerNumber";
```
**Explanation:** This query fulfills the intent to join and list by querying the orders, customers table(s).

## Question 22: Get employees with office city
**SQL Query:**
```sql
SELECT e."firstName", e."lastName", o."city" FROM employees e JOIN offices o ON e."officeCode" = o."officeCode";
```
**Explanation:** This query fulfills the intent to join and list by querying the employees, offices table(s).

## Question 23: Get payments with customer names
**SQL Query:**
```sql
SELECT p."amount", c."customerName" FROM payments p JOIN customers c ON p."customerNumber" = c."customerNumber";
```
**Explanation:** This query fulfills the intent to join and list by querying the payments, customers table(s).

## Question 24: Get order details with product names
**SQL Query:**
```sql
SELECT od."orderNumber", p."productName", od."quantityOrdered" FROM orderdetails od JOIN products p ON od."productCode" = p."productCode";
```
**Explanation:** This query fulfills the intent to join and list by querying the orderdetails, products table(s).

## Question 25: Get products with product line description
**SQL Query:**
```sql
SELECT p."productName", pl."textDescription" FROM products p JOIN productlines pl ON p."productLine" = pl."productLine";
```
**Explanation:** This query fulfills the intent to join and list by querying the products, productlines table(s).

## Question 26: Get customers with sales rep names
**SQL Query:**
```sql
SELECT c."customerName", e."firstName" AS "repFirstName", e."lastName" AS "repLastName" FROM customers c JOIN employees e ON c."salesRepEmployeeNumber" = e."employeeNumber";
```
**Explanation:** This query fulfills the intent to join and list by querying the customers, employees table(s).

## Question 27: Get orders with customer city
**SQL Query:**
```sql
SELECT o."orderNumber", c."city" FROM orders o JOIN customers c ON o."customerNumber" = c."customerNumber";
```
**Explanation:** This query fulfills the intent to join and list by querying the orders, customers table(s).

## Question 28: Get employees and their manager
**SQL Query:**
```sql
SELECT e."firstName" AS "empName", m."firstName" AS "managerName" FROM employees e LEFT JOIN employees m ON e."reportsTo" = m."employeeNumber";
```
**Explanation:** This query fulfills the intent to self join and list by querying the employees table(s).

## Question 29: Get orderdetails with product vendor
**SQL Query:**
```sql
SELECT od."orderNumber", p."productVendor" FROM orderdetails od JOIN products p ON od."productCode" = p."productCode";
```
**Explanation:** This query fulfills the intent to join and list by querying the orderdetails, products table(s).

## Question 30: Get payments with customer country
**SQL Query:**
```sql
SELECT p."amount", c."country" FROM payments p JOIN customers c ON p."customerNumber" = c."customerNumber";
```
**Explanation:** This query fulfills the intent to join and list by querying the payments, customers table(s).

## Question 31: Count customers per country
**SQL Query:**
```sql
SELECT "country", COUNT(*) FROM customers GROUP BY "country";
```
**Explanation:** This query fulfills the intent to group and count by querying the customers table(s).

## Question 32: Total payments per customer
**SQL Query:**
```sql
SELECT "customerNumber", SUM("amount") FROM payments GROUP BY "customerNumber";
```
**Explanation:** This query fulfills the intent to group and sum by querying the payments table(s).

## Question 33: Number of orders per status
**SQL Query:**
```sql
SELECT "status", COUNT(*) FROM orders GROUP BY "status";
```
**Explanation:** This query fulfills the intent to group and count by querying the orders table(s).

## Question 34: Products per product line
**SQL Query:**
```sql
SELECT "productLine", COUNT(*) FROM products GROUP BY "productLine";
```
**Explanation:** This query fulfills the intent to group and count by querying the products table(s).

## Question 35: Employees per office
**SQL Query:**
```sql
SELECT "officeCode", COUNT(*) FROM employees GROUP BY "officeCode";
```
**Explanation:** This query fulfills the intent to group and count by querying the employees table(s).

## Question 36: Total stock per product vendor
**SQL Query:**
```sql
SELECT "productVendor", SUM("quantityInStock") FROM products GROUP BY "productVendor";
```
**Explanation:** This query fulfills the intent to group and sum by querying the products table(s).

## Question 37: Average buy price per product line
**SQL Query:**
```sql
SELECT "productLine", AVG("buyPrice") FROM products GROUP BY "productLine";
```
**Explanation:** This query fulfills the intent to group and average by querying the products table(s).

## Question 38: Orders per customer
**SQL Query:**
```sql
SELECT "customerNumber", COUNT(*) FROM orders GROUP BY "customerNumber";
```
**Explanation:** This query fulfills the intent to group and count by querying the orders table(s).

## Question 39: Max MSRP per product line
**SQL Query:**
```sql
SELECT "productLine", MAX("MSRP") FROM products GROUP BY "productLine";
```
**Explanation:** This query fulfills the intent to group and max by querying the products table(s).

## Question 40: Min buy price per vendor
**SQL Query:**
```sql
SELECT "productVendor", MIN("buyPrice") FROM products GROUP BY "productVendor";
```
**Explanation:** This query fulfills the intent to group and min by querying the products table(s).

## Question 41: Total number of customers
**SQL Query:**
```sql
SELECT COUNT(*) FROM customers;
```
**Explanation:** This query fulfills the intent to count total by querying the customers table(s).

## Question 42: Total number of products
**SQL Query:**
```sql
SELECT COUNT(*) FROM products;
```
**Explanation:** This query fulfills the intent to count total by querying the products table(s).

## Question 43: Total revenue from payments
**SQL Query:**
```sql
SELECT SUM("amount") FROM payments;
```
**Explanation:** This query fulfills the intent to sum total by querying the payments table(s).

## Question 44: Average product price
**SQL Query:**
```sql
SELECT AVG("buyPrice") FROM products;
```
**Explanation:** This query fulfills the intent to average by querying the products table(s).

## Question 45: Max payment amount
**SQL Query:**
```sql
SELECT MAX("amount") FROM payments;
```
**Explanation:** This query fulfills the intent to max by querying the payments table(s).

## Question 46: Min payment amount
**SQL Query:**
```sql
SELECT MIN("amount") FROM payments;
```
**Explanation:** This query fulfills the intent to min by querying the payments table(s).

## Question 47: Count total orders
**SQL Query:**
```sql
SELECT COUNT(*) FROM orders;
```
**Explanation:** This query fulfills the intent to count total by querying the orders table(s).

## Question 48: Total quantity in stock
**SQL Query:**
```sql
SELECT SUM("quantityInStock") FROM products;
```
**Explanation:** This query fulfills the intent to sum total by querying the products table(s).

## Question 49: Average MSRP
**SQL Query:**
```sql
SELECT AVG("MSRP") FROM products;
```
**Explanation:** This query fulfills the intent to average by querying the products table(s).

## Question 50: Number of employees
**SQL Query:**
```sql
SELECT COUNT(*) FROM employees;
```
**Explanation:** This query fulfills the intent to count total by querying the employees table(s).

