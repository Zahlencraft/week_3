import json
import csv

data = [
    {"q": "List all products", "sql": 'SELECT * FROM products;', "intent": "List all records", "tables": ["products"], "cols": ["*"], "filters": [], "joins": []},
    {"q": "Get all customers", "sql": 'SELECT * FROM customers;', "intent": "List all records", "tables": ["customers"], "cols": ["*"], "filters": [], "joins": []},
    {"q": "Show all orders", "sql": 'SELECT * FROM orders;', "intent": "List all records", "tables": ["orders"], "cols": ["*"], "filters": [], "joins": []},
    {"q": "List all employees", "sql": 'SELECT * FROM employees;', "intent": "List all records", "tables": ["employees"], "cols": ["*"], "filters": [], "joins": []},
    {"q": "Get all offices", "sql": 'SELECT * FROM offices;', "intent": "List all records", "tables": ["offices"], "cols": ["*"], "filters": [], "joins": []},
    {"q": "Show all product lines", "sql": 'SELECT * FROM productlines;', "intent": "List all records", "tables": ["productlines"], "cols": ["*"], "filters": [], "joins": []},
    {"q": "List all payments", "sql": 'SELECT * FROM payments;', "intent": "List all records", "tables": ["payments"], "cols": ["*"], "filters": [], "joins": []},
    {"q": "Get product names and prices", "sql": 'SELECT "productName", "buyPrice" FROM products;', "intent": "List specific columns", "tables": ["products"], "cols": ["productName", "buyPrice"], "filters": [], "joins": []},
    {"q": "Get customer names and cities", "sql": 'SELECT "customerName", "city" FROM customers;', "intent": "List specific columns", "tables": ["customers"], "cols": ["customerName", "city"], "filters": [], "joins": []},
    {"q": "List employee first and last names", "sql": 'SELECT "firstName", "lastName" FROM employees;', "intent": "List specific columns", "tables": ["employees"], "cols": ["firstName", "lastName"], "filters": [], "joins": []},
    {"q": "Get all order dates", "sql": 'SELECT "orderDate" FROM orders;', "intent": "List specific columns", "tables": ["orders"], "cols": ["orderDate"], "filters": [], "joins": []},
    {"q": "Show product vendor list", "sql": 'SELECT DISTINCT "productVendor" FROM products;', "intent": "List unique column values", "tables": ["products"], "cols": ["productVendor"], "filters": [], "joins": []},
    {"q": "Get all product codes", "sql": 'SELECT "productCode" FROM products;', "intent": "List specific columns", "tables": ["products"], "cols": ["productCode"], "filters": [], "joins": []},
    {"q": "List all countries from offices", "sql": 'SELECT DISTINCT "country" FROM offices;', "intent": "List unique column values", "tables": ["offices"], "cols": ["country"], "filters": [], "joins": []},
    {"q": "Show all order statuses", "sql": 'SELECT DISTINCT "status" FROM orders;', "intent": "List unique column values", "tables": ["orders"], "cols": ["status"], "filters": [], "joins": []},
    {"q": "Get all payment amounts", "sql": 'SELECT "amount" FROM payments;', "intent": "List specific columns", "tables": ["payments"], "cols": ["amount"], "filters": [], "joins": []},
    {"q": "List all job titles", "sql": 'SELECT DISTINCT "jobTitle" FROM employees;', "intent": "List unique column values", "tables": ["employees"], "cols": ["jobTitle"], "filters": [], "joins": []},
    {"q": "Get customer phone numbers", "sql": 'SELECT "customerName", "phone" FROM customers;', "intent": "List specific columns", "tables": ["customers"], "cols": ["customerName", "phone"], "filters": [], "joins": []},
    {"q": "Show product MSRP values", "sql": 'SELECT "productName", "MSRP" FROM products;', "intent": "List specific columns", "tables": ["products"], "cols": ["productName", "MSRP"], "filters": [], "joins": []},
    {"q": "List order numbers", "sql": 'SELECT "orderNumber" FROM orders;', "intent": "List specific columns", "tables": ["orders"], "cols": ["orderNumber"], "filters": [], "joins": []},
    {"q": "Get orders with customer names", "sql": 'SELECT o."orderNumber", c."customerName" FROM orders o JOIN customers c ON o."customerNumber" = c."customerNumber";', "intent": "Join and list", "tables": ["orders", "customers"], "cols": ["orderNumber", "customerName"], "filters": [], "joins": ['orders.customerNumber = customers.customerNumber']},
    {"q": "Get employees with office city", "sql": 'SELECT e."firstName", e."lastName", o."city" FROM employees e JOIN offices o ON e."officeCode" = o."officeCode";', "intent": "Join and list", "tables": ["employees", "offices"], "cols": ["firstName", "lastName", "city"], "filters": [], "joins": ['employees.officeCode = offices.officeCode']},
    {"q": "Get payments with customer names", "sql": 'SELECT p."amount", c."customerName" FROM payments p JOIN customers c ON p."customerNumber" = c."customerNumber";', "intent": "Join and list", "tables": ["payments", "customers"], "cols": ["amount", "customerName"], "filters": [], "joins": ['payments.customerNumber = customers.customerNumber']},
    {"q": "Get order details with product names", "sql": 'SELECT od."orderNumber", p."productName", od."quantityOrdered" FROM orderdetails od JOIN products p ON od."productCode" = p."productCode";', "intent": "Join and list", "tables": ["orderdetails", "products"], "cols": ["orderNumber", "productName", "quantityOrdered"], "filters": [], "joins": ['orderdetails.productCode = products.productCode']},
    {"q": "Get products with product line description", "sql": 'SELECT p."productName", pl."textDescription" FROM products p JOIN productlines pl ON p."productLine" = pl."productLine";', "intent": "Join and list", "tables": ["products", "productlines"], "cols": ["productName", "textDescription"], "filters": [], "joins": ['products.productLine = productlines.productLine']},
    {"q": "Get customers with sales rep names", "sql": 'SELECT c."customerName", e."firstName" AS "repFirstName", e."lastName" AS "repLastName" FROM customers c JOIN employees e ON c."salesRepEmployeeNumber" = e."employeeNumber";', "intent": "Join and list", "tables": ["customers", "employees"], "cols": ["customerName", "firstName", "lastName"], "filters": [], "joins": ['customers.salesRepEmployeeNumber = employees.employeeNumber']},
    {"q": "Get orders with customer city", "sql": 'SELECT o."orderNumber", c."city" FROM orders o JOIN customers c ON o."customerNumber" = c."customerNumber";', "intent": "Join and list", "tables": ["orders", "customers"], "cols": ["orderNumber", "city"], "filters": [], "joins": ['orders.customerNumber = customers.customerNumber']},
    {"q": "Get employees and their manager", "sql": 'SELECT e."firstName" AS "empName", m."firstName" AS "managerName" FROM employees e LEFT JOIN employees m ON e."reportsTo" = m."employeeNumber";', "intent": "Self join and list", "tables": ["employees"], "cols": ["empName", "managerName"], "filters": [], "joins": ['employees.reportsTo = employees.employeeNumber']},
    {"q": "Get orderdetails with product vendor", "sql": 'SELECT od."orderNumber", p."productVendor" FROM orderdetails od JOIN products p ON od."productCode" = p."productCode";', "intent": "Join and list", "tables": ["orderdetails", "products"], "cols": ["orderNumber", "productVendor"], "filters": [], "joins": ['orderdetails.productCode = products.productCode']},
    {"q": "Get payments with customer country", "sql": 'SELECT p."amount", c."country" FROM payments p JOIN customers c ON p."customerNumber" = c."customerNumber";', "intent": "Join and list", "tables": ["payments", "customers"], "cols": ["amount", "country"], "filters": [], "joins": ['payments.customerNumber = customers.customerNumber']},
    {"q": "Count customers per country", "sql": 'SELECT "country", COUNT(*) FROM customers GROUP BY "country";', "intent": "Group and count", "tables": ["customers"], "cols": ["country", "COUNT(*)"], "filters": [], "joins": []},
    {"q": "Total payments per customer", "sql": 'SELECT "customerNumber", SUM("amount") FROM payments GROUP BY "customerNumber";', "intent": "Group and sum", "tables": ["payments"], "cols": ["customerNumber", "SUM(amount)"], "filters": [], "joins": []},
    {"q": "Number of orders per status", "sql": 'SELECT "status", COUNT(*) FROM orders GROUP BY "status";', "intent": "Group and count", "tables": ["orders"], "cols": ["status", "COUNT(*)"], "filters": [], "joins": []},
    {"q": "Products per product line", "sql": 'SELECT "productLine", COUNT(*) FROM products GROUP BY "productLine";', "intent": "Group and count", "tables": ["products"], "cols": ["productLine", "COUNT(*)"], "filters": [], "joins": []},
    {"q": "Employees per office", "sql": 'SELECT "officeCode", COUNT(*) FROM employees GROUP BY "officeCode";', "intent": "Group and count", "tables": ["employees"], "cols": ["officeCode", "COUNT(*)"], "filters": [], "joins": []},
    {"q": "Total stock per product vendor", "sql": 'SELECT "productVendor", SUM("quantityInStock") FROM products GROUP BY "productVendor";', "intent": "Group and sum", "tables": ["products"], "cols": ["productVendor", "SUM(quantityInStock)"], "filters": [], "joins": []},
    {"q": "Average buy price per product line", "sql": 'SELECT "productLine", AVG("buyPrice") FROM products GROUP BY "productLine";', "intent": "Group and average", "tables": ["products"], "cols": ["productLine", "AVG(buyPrice)"], "filters": [], "joins": []},
    {"q": "Orders per customer", "sql": 'SELECT "customerNumber", COUNT(*) FROM orders GROUP BY "customerNumber";', "intent": "Group and count", "tables": ["orders"], "cols": ["customerNumber", "COUNT(*)"], "filters": [], "joins": []},
    {"q": "Max MSRP per product line", "sql": 'SELECT "productLine", MAX("MSRP") FROM products GROUP BY "productLine";', "intent": "Group and max", "tables": ["products"], "cols": ["productLine", "MAX(MSRP)"], "filters": [], "joins": []},
    {"q": "Min buy price per vendor", "sql": 'SELECT "productVendor", MIN("buyPrice") FROM products GROUP BY "productVendor";', "intent": "Group and min", "tables": ["products"], "cols": ["productVendor", "MIN(buyPrice)"], "filters": [], "joins": []},
    {"q": "Total number of customers", "sql": 'SELECT COUNT(*) FROM customers;', "intent": "Count total", "tables": ["customers"], "cols": ["COUNT(*)"], "filters": [], "joins": []},
    {"q": "Total number of products", "sql": 'SELECT COUNT(*) FROM products;', "intent": "Count total", "tables": ["products"], "cols": ["COUNT(*)"], "filters": [], "joins": []},
    {"q": "Total revenue from payments", "sql": 'SELECT SUM("amount") FROM payments;', "intent": "Sum total", "tables": ["payments"], "cols": ["SUM(amount)"], "filters": [], "joins": []},
    {"q": "Average product price", "sql": 'SELECT AVG("buyPrice") FROM products;', "intent": "Average", "tables": ["products"], "cols": ["AVG(buyPrice)"], "filters": [], "joins": []},
    {"q": "Max payment amount", "sql": 'SELECT MAX("amount") FROM payments;', "intent": "Max", "tables": ["payments"], "cols": ["MAX(amount)"], "filters": [], "joins": []},
    {"q": "Min payment amount", "sql": 'SELECT MIN("amount") FROM payments;', "intent": "Min", "tables": ["payments"], "cols": ["MIN(amount)"], "filters": [], "joins": []},
    {"q": "Count total orders", "sql": 'SELECT COUNT(*) FROM orders;', "intent": "Count total", "tables": ["orders"], "cols": ["COUNT(*)"], "filters": [], "joins": []},
    {"q": "Total quantity in stock", "sql": 'SELECT SUM("quantityInStock") FROM products;', "intent": "Sum total", "tables": ["products"], "cols": ["SUM(quantityInStock)"], "filters": [], "joins": []},
    {"q": "Average MSRP", "sql": 'SELECT AVG("MSRP") FROM products;', "intent": "Average", "tables": ["products"], "cols": ["AVG(MSRP)"], "filters": [], "joins": []},
    {"q": "Number of employees", "sql": 'SELECT COUNT(*) FROM employees;', "intent": "Count total", "tables": ["employees"], "cols": ["COUNT(*)"], "filters": [], "joins": []},
]

# Write Task 1 output
with open('task1_ground_truth.md', 'w') as f:
    f.write('# Task 1: Ground Truth SQL Queries\n\n')
    for i, item in enumerate(data):
        f.write(f'## Question {i+1}: {item["q"]}\n')
        f.write(f'**SQL Query:**\n```sql\n{item["sql"]}\n```\n')
        f.write(f'**Explanation:** This query fulfills the intent to {item["intent"].lower()} by querying the {", ".join(item["tables"])} table(s).\n\n')

# Write Task 2 output
decompositions = []
for item in data:
    decompositions.append({
        "question": item["q"],
        "decomposition": {
            "intent": item["intent"],
            "tables": item["tables"],
            "columns": item["cols"],
            "filters": item["filters"],
            "joins": item["joins"]
        }
    })

with open('task2_decomposition.json', 'w') as f:
    json.dump(decompositions, f, indent=4)

print("Generated task1_ground_truth.md and task2_decomposition.json")
