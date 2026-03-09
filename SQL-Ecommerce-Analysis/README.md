# E-Commerce Sales & Customer Analysis using SQL

## Project Overview
This project focuses on analyzing an e-commerce database using SQL to extract valuable business insights related to customer behavior, sales performance, payment methods, and inventory management.

The database contains information about customers, orders, and products. By performing various SQL operations such as joins, aggregations, window functions, stored procedures, and triggers, the project demonstrates how SQL can be used for real-world business analysis and database automation.

---

## Business Problem

An e-commerce company wants to analyze its sales data to better understand:

• Which countries generate the most revenue  
• Who are the top spending customers  
• Which payment methods customers prefer  
• How product inventory changes after orders  
• How customer loyalty points can be managed effectively  

The goal is to use SQL queries to generate insights that help improve customer engagement, sales strategy, and inventory management.

---

## Database Structure

The project uses three main tables:

### Customers
Contains customer information such as:

- Customer ID
- Name
- Age
- Country
- City
- Email
- Loyalty Points

### Orders
Stores transaction details:

- Order ID
- Customer ID
- Product ID
- Order Date
- Order Value
- Quantity
- Payment Method
- Shipping Cost
- Order Status

### Products
Contains product inventory information:

- Product ID
- Product Name
- Stock Quantity

---

## Analysis Performed

### 1. Customer Loyalty Points Update
Customer loyalty points were updated based on age groups using a CASE statement.

Age-based loyalty update:

- Customers below 25 years receive bonus points
- Customers between 25 and 40 receive additional points
- Customers above 40 receive smaller increments

This simulates a loyalty rewards system used by companies.

---

### 2. Country-wise Sales Analysis
Customer and order tables were joined to calculate total sales by country.

Countries were categorized into:

- High Sales (Above 100000)
- Medium Sales (50000 – 100000)
- Low Sales (Below 50000)

This helps businesses identify their strongest markets.

---

### 3. Payment Method Analysis
Orders and products tables were joined to analyze product quantities purchased using different payment methods.

Payment methods analyzed:

- PayPal
- Bank Transfer
- Credit Card

This helps businesses understand customer payment preferences.

---

### 4. Top Customers by Spending
A window function (RANK) was used to identify the top 3 customers based on their total order value.

This analysis helps businesses identify their most valuable customers for targeted marketing and loyalty programs.

---

### 5. Product Inventory Analysis
Products with stock quantities greater than the average stock level were identified using subqueries and HAVING clauses.

This helps detect overstocked inventory and manage product supply more efficiently.

---

### 6. Stored Procedure – Retrieve Customer Orders
A stored procedure was created to retrieve all order details for a specific customer.

Example:

CALL ind_customer(860);

This simplifies retrieving order history for customer service or analysis.

---

### 7. Stored Procedure – Calculate Customer Spending
Another stored procedure calculates the total spending of a specific customer using an INOUT parameter.

Example:

CALL customer_spending(860, @tot_spent);
SELECT @tot_spent;

This helps measure customer lifetime value.

---

### 8. Trigger – Default Loyalty Points
A trigger was created to automatically assign loyalty points when a new customer is inserted without specifying loyalty points.

This ensures data consistency in the customer table.

---

### 9. Trigger – Automatic Stock Update
An AFTER INSERT trigger was implemented on the orders table.

Whenever a new order is placed:

• The product stock quantity automatically decreases.

This simulates a real-world inventory management system.

---

## SQL Concepts Used

This project demonstrates the following SQL concepts:

- CASE Statements
- INNER JOIN
- LEFT JOIN
- Aggregations (SUM, GROUP BY)
- Window Functions (RANK)
- Subqueries
- Stored Procedures
- Triggers
- Data Manipulation (UPDATE, INSERT, DELETE)

---

## Key Business Insights

• Customers aged between 25 and 40 contribute significantly to loyalty programs.

• High-performing countries generate sales above 100000, making them priority markets.

• Credit Card and PayPal appear to be popular payment methods among customers.

• A small number of top customers contribute a large portion of total revenue.

• Inventory automatically updates after new orders through trigger automation.

---


## Tools Used

SQL  
MySQL  
Relational Database Concepts  

---

## Future Improvements

• Build a Power BI dashboard for visualization  
• Perform time-based sales trend analysis  
• Implement customer segmentation analysis  
• Integrate Python for automated reporting  

---

## Author

Logeshwaran A  
Data Analyst | SQL | Python | Power BI | Excel
## Project Structure
