# 🚀 Ultimate SQL Cheat Sheet & Mini-Course

*Your complete guide from SQL zero to hero* 📊

[![SQL](https://img.shields.io/badge/SQL-Database-blue)](https://github.com) [![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Table of Contents

1. [What is SQL?](#-what-is-sql)
2. [Setting Up SQL](#️-setting-up-sql)
3. [Basic Syntax](#-basic-syntax)
4. [Intermediate Queries](#-intermediate-queries)
5. [Advanced SQL](#-advanced-sql)
6. [Real-World Scenarios](#-real-world-scenarios)
7. [Performance Tips](#⚡-performance-tips)
8. [Common Pitfalls](#⚠️-common-pitfalls--gotchas)
9. [Practice Datasets](#-practice-datasets)
10. [Quick Reference](#-quick-reference)

---

## 🤔 What is SQL?

**SQL (Structured Query Language)** is the standard language for managing and manipulating relational databases. Think of it as the universal language that lets you "talk" to databases.

### 🎯 Key Use Cases

- **Data Retrieval**: Query databases to find specific information
- **Reporting & Analytics**: Generate business reports and insights
- **Data Management**: Insert, update, and delete records
- **Database Design**: Create and modify database structures
- **ETL Operations**: Extract, transform, and load data between systems

### 🏢 Where SQL is Used

- **Business Intelligence**: Dashboards, reports, KPIs
- **Web Applications**: User data, product catalogs, transactions
- **Data Science**: Data exploration, feature engineering
- **Finance**: Risk analysis, fraud detection, compliance reporting
- **Healthcare**: Patient records, research data, clinical trials

---

## 🛠️ Setting Up SQL

### Local Database Options

#### 🐘 PostgreSQL (Recommended for beginners)
```bash
# Install on macOS
brew install postgresql
brew services start postgresql

# Install on Ubuntu
sudo apt update
sudo apt install postgresql postgresql-contrib

# Connect
psql -U postgres
```

#### 🐬 MySQL
```bash
# Install on macOS
brew install mysql
brew services start mysql

# Install on Ubuntu
sudo apt install mysql-server

# Connect
mysql -u root -p
```

#### 🪶 SQLite (Simplest option)
```bash
# Install on macOS
brew install sqlite

# Install on Ubuntu
sudo apt install sqlite3

# Create/connect to database
sqlite3 mydatabase.db
```

### 🌐 Online SQL Playgrounds
- **DB Fiddle**: [db-fiddle.com](https://db-fiddle.com)
- **SQLiteOnline**: [sqliteonline.com](https://sqliteonline.com)
- **W3Schools SQL Tryit**: [w3schools.com/sql/trysql.asp](https://w3schools.com/sql/trysql.asp)

---

## 📖 Basic Syntax

### SELECT - Your First Query
```sql
-- Basic SELECT
SELECT column1, column2 FROM table_name;

-- Select all columns
SELECT * FROM employees;

-- Select with alias
SELECT first_name AS "First Name", 
       last_name AS "Last Name" 
FROM employees;
```

### WHERE - Filtering Data
```sql
-- Basic filtering
SELECT * FROM employees WHERE salary > 50000;

-- Multiple conditions
SELECT * FROM employees 
WHERE department = 'Engineering' 
  AND salary BETWEEN 60000 AND 100000;

-- Pattern matching
SELECT * FROM employees 
WHERE first_name LIKE 'John%';  -- Starts with 'John'

-- IN operator
SELECT * FROM employees 
WHERE department IN ('Engineering', 'Marketing', 'Sales');
```

### ORDER BY - Sorting Results
```sql
-- Single column sort
SELECT * FROM employees ORDER BY salary DESC;

-- Multiple column sort
SELECT * FROM employees 
ORDER BY department ASC, salary DESC;

-- Sort with LIMIT
SELECT * FROM employees 
ORDER BY hire_date DESC 
LIMIT 10;
```

### Common Operators
| Operator | Description | Example |
|----------|-------------|---------|
| `=` | Equal | `WHERE age = 25` |
| `!=` or `<>` | Not equal | `WHERE status != 'inactive'` |
| `>`, `<`, `>=`, `<=` | Comparison | `WHERE salary >= 50000` |
| `BETWEEN` | Range | `WHERE age BETWEEN 25 AND 35` |
| `LIKE` | Pattern match | `WHERE name LIKE 'J%'` |
| `IN` | List match | `WHERE city IN ('NYC', 'LA')` |
| `IS NULL` | Null check | `WHERE phone IS NULL` |

---

## 🔄 Intermediate Queries

### JOINs - Combining Tables

#### Sample Tables Setup
```sql
-- Employees table
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    salary DECIMAL(10,2)
);

-- Departments table
CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    budget DECIMAL(12,2)
);
```

#### INNER JOIN
```sql
-- Returns only matching records from both tables
SELECT e.name, d.name as department, e.salary
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;
```

#### LEFT JOIN
```sql
-- Returns all records from left table, matching from right
SELECT e.name, d.name as department
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;
```

#### RIGHT JOIN
```sql
-- Returns all records from right table, matching from left
SELECT e.name, d.name as department
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.id;
```

#### FULL OUTER JOIN
```sql
-- Returns all records when there's a match in either table
SELECT e.name, d.name as department
FROM employees e
FULL OUTER JOIN departments d ON e.department_id = d.id;
```

### GROUP BY & Aggregate Functions
```sql
-- Count employees by department
SELECT d.name, COUNT(e.id) as employee_count
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
GROUP BY d.id, d.name;

-- Average salary by department
SELECT d.name, 
       AVG(e.salary) as avg_salary,
       MIN(e.salary) as min_salary,
       MAX(e.salary) as max_salary
FROM departments d
INNER JOIN employees e ON d.id = e.department_id
GROUP BY d.id, d.name;
```

### HAVING - Filtering Groups
```sql
-- Departments with more than 5 employees
SELECT d.name, COUNT(e.id) as employee_count
FROM departments d
INNER JOIN employees e ON d.id = e.department_id
GROUP BY d.id, d.name
HAVING COUNT(e.id) > 5;
```

### Subqueries
```sql
-- Employees earning above average salary
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Departments with highest paid employee
SELECT d.name, 
       (SELECT MAX(salary) FROM employees WHERE department_id = d.id) as highest_salary
FROM departments d;

-- EXISTS example
SELECT name FROM employees e
WHERE EXISTS (
    SELECT 1 FROM departments d 
    WHERE d.id = e.department_id AND d.budget > 1000000
);
```

---

## 🎯 Advanced SQL

### Common Table Expressions (CTEs)
```sql
-- Basic CTE
WITH high_earners AS (
    SELECT name, salary, department_id
    FROM employees
    WHERE salary > 75000
)
SELECT he.name, he.salary, d.name as department
FROM high_earners he
JOIN departments d ON he.department_id = d.id;

-- Recursive CTE (Employee hierarchy)
WITH RECURSIVE employee_hierarchy AS (
    -- Anchor: Top-level managers
    SELECT id, name, manager_id, 1 as level
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Recursive: Their reports
    SELECT e.id, e.name, e.manager_id, eh.level + 1
    FROM employees e
    INNER JOIN employee_hierarchy eh ON e.manager_id = eh.id
)
SELECT * FROM employee_hierarchy ORDER BY level, name;
```

### Window Functions
```sql
-- Row number and ranking
SELECT 
    name,
    salary,
    department_id,
    ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) as row_num,
    RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as rank,
    DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as dense_rank
FROM employees;

-- Running totals and moving averages
SELECT 
    name,
    salary,
    SUM(salary) OVER (ORDER BY hire_date) as running_total,
    AVG(salary) OVER (ORDER BY hire_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg_3
FROM employees;

-- Lag and Lead
SELECT 
    name,
    salary,
    LAG(salary, 1) OVER (ORDER BY hire_date) as previous_salary,
    LEAD(salary, 1) OVER (ORDER BY hire_date) as next_salary
FROM employees;
```

### Indexing
```sql
-- Create indexes for better performance
CREATE INDEX idx_employee_department ON employees(department_id);
CREATE INDEX idx_employee_salary ON employees(salary);
CREATE INDEX idx_employee_name ON employees(name);

-- Composite index
CREATE INDEX idx_employee_dept_salary ON employees(department_id, salary);

-- Unique index
CREATE UNIQUE INDEX idx_employee_email ON employees(email);

-- Check existing indexes
-- PostgreSQL
SELECT * FROM pg_indexes WHERE tablename = 'employees';

-- MySQL
SHOW INDEX FROM employees;
```

### Transactions
```sql
-- Basic transaction
BEGIN;
    UPDATE employees SET salary = salary * 1.1 WHERE department_id = 1;
    INSERT INTO salary_audit (employee_id, old_salary, new_salary, change_date)
    SELECT id, salary / 1.1, salary, NOW() FROM employees WHERE department_id = 1;
COMMIT;

-- Transaction with rollback handling
BEGIN;
    UPDATE accounts SET balance = balance - 1000 WHERE id = 1;
    UPDATE accounts SET balance = balance + 1000 WHERE id = 2;
    
    -- Check if first account has sufficient funds
    IF (SELECT balance FROM accounts WHERE id = 1) < 0 THEN
        ROLLBACK;
    ELSE
        COMMIT;
    END IF;
```

---

## 🌍 Real-World Scenarios

### 📊 Business Reporting
```sql
-- Monthly sales report
SELECT 
    DATE_TRUNC('month', order_date) as month,
    COUNT(*) as total_orders,
    SUM(total_amount) as total_revenue,
    AVG(total_amount) as avg_order_value
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month;

-- Customer segmentation
WITH customer_metrics AS (
    SELECT 
        customer_id,
        COUNT(*) as order_count,
        SUM(total_amount) as total_spent,
        AVG(total_amount) as avg_order_value,
        MAX(order_date) as last_order_date
    FROM orders
    GROUP BY customer_id
)
SELECT 
    customer_id,
    CASE 
        WHEN total_spent > 10000 THEN 'VIP'
        WHEN total_spent > 5000 THEN 'High Value'
        WHEN total_spent > 1000 THEN 'Regular'
        ELSE 'Low Value'
    END as customer_segment,
    order_count,
    total_spent
FROM customer_metrics;
```

### 📈 Analytics Queries
```sql
-- Cohort analysis (simplified)
WITH first_orders AS (
    SELECT 
        customer_id,
        DATE_TRUNC('month', MIN(order_date)) as cohort_month
    FROM orders
    GROUP BY customer_id
),
cohort_data AS (
    SELECT 
        fo.cohort_month,
        DATE_TRUNC('month', o.order_date) as order_month,
        COUNT(DISTINCT o.customer_id) as customers
    FROM first_orders fo
    JOIN orders o ON fo.customer_id = o.customer_id
    GROUP BY fo.cohort_month, DATE_TRUNC('month', o.order_date)
)
SELECT * FROM cohort_data ORDER BY cohort_month, order_month;

-- Year-over-year growth
SELECT 
    product_category,
    EXTRACT(YEAR FROM order_date) as year,
    SUM(quantity * price) as revenue,
    LAG(SUM(quantity * price)) OVER (
        PARTITION BY product_category 
        ORDER BY EXTRACT(YEAR FROM order_date)
    ) as previous_year_revenue,
    ROUND(
        (SUM(quantity * price) - LAG(SUM(quantity * price)) OVER (
            PARTITION BY product_category 
            ORDER BY EXTRACT(YEAR FROM order_date)
        )) * 100.0 / LAG(SUM(quantity * price)) OVER (
            PARTITION BY product_category 
            ORDER BY EXTRACT(YEAR FROM order_date)
        ), 2
    ) as yoy_growth_percent
FROM order_items oi
JOIN orders o ON oi.order_id = o.id
GROUP BY product_category, EXTRACT(YEAR FROM order_date);
```

### 🔄 ETL Operations
```sql
-- Data cleaning: standardize phone numbers
UPDATE customers 
SET phone = REGEXP_REPLACE(
    REGEXP_REPLACE(phone, '[^0-9]', '', 'g'),
    '^1?(.{10})$',
    '+1-\1'
)
WHERE phone IS NOT NULL;

-- Upsert operation (PostgreSQL)
INSERT INTO customer_summary (customer_id, total_orders, total_spent, last_order_date)
SELECT 
    customer_id,
    COUNT(*) as total_orders,
    SUM(total_amount) as total_spent,
    MAX(order_date) as last_order_date
FROM orders
GROUP BY customer_id
ON CONFLICT (customer_id) DO UPDATE SET
    total_orders = EXCLUDED.total_orders,
    total_spent = EXCLUDED.total_spent,
    last_order_date = EXCLUDED.last_order_date;
```

---

## ⚡ Performance Tips

### Query Optimization Strategies

#### 1. Use Indexes Effectively
```sql
-- ❌ Avoid functions on indexed columns
SELECT * FROM orders WHERE YEAR(order_date) = 2024;

-- ✅ Better approach
SELECT * FROM orders WHERE order_date >= '2024-01-01' AND order_date < '2025-01-01';
```

#### 2. Limit Result Sets
```sql
-- ❌ Don't select unnecessary columns
SELECT * FROM large_table WHERE condition;

-- ✅ Select only needed columns
SELECT id, name, email FROM large_table WHERE condition;

-- ❌ No LIMIT on large datasets
SELECT * FROM orders ORDER BY order_date DESC;

-- ✅ Use LIMIT for pagination
SELECT * FROM orders ORDER BY order_date DESC LIMIT 50 OFFSET 100;
```

#### 3. Optimize JOINs
```sql
-- ❌ Cartesian product risk
SELECT * FROM table1, table2 WHERE table1.id = table2.id;

-- ✅ Explicit JOIN syntax
SELECT * FROM table1 INNER JOIN table2 ON table1.id = table2.id;

-- ✅ Filter early in subqueries
SELECT o.*, c.name
FROM orders o
JOIN (SELECT id, name FROM customers WHERE active = true) c ON o.customer_id = c.id;
```

### Execution Plan Analysis
```sql
-- PostgreSQL
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 123;

-- MySQL
EXPLAIN FORMAT=JSON SELECT * FROM orders WHERE customer_id = 123;

-- Look for:
-- - Sequential scans on large tables (add indexes)
-- - High cost operations
-- - Nested loop joins on large datasets
```

### Performance Monitoring
```sql
-- PostgreSQL: Find slow queries
SELECT 
    query,
    calls,
    total_time,
    mean_time,
    rows
FROM pg_stat_statements
ORDER BY total_time DESC
LIMIT 10;

-- MySQL: Enable slow query log
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 2;
```

---

## ⚠️ Common Pitfalls & Gotchas

### 1. NULL Handling
```sql
-- ❌ This won't work as expected
SELECT * FROM employees WHERE department_id != 5;
-- Won't return rows where department_id IS NULL

-- ✅ Handle NULLs explicitly
SELECT * FROM employees WHERE department_id != 5 OR department_id IS NULL;

-- ❌ NULL in aggregations
SELECT AVG(salary) FROM employees; -- Ignores NULL values

-- ✅ Be explicit about NULL handling
SELECT AVG(COALESCE(salary, 0)) FROM employees;
```

### 2. String Comparisons
```sql
-- ❌ Case sensitivity issues
SELECT * FROM users WHERE name = 'john'; -- Might miss 'John', 'JOHN'

-- ✅ Use proper case handling
SELECT * FROM users WHERE LOWER(name) = LOWER('john');
-- Or use ILIKE in PostgreSQL
SELECT * FROM users WHERE name ILIKE 'john';
```

### 3. Date/Time Pitfalls
```sql
-- ❌ Timezone issues
SELECT * FROM orders WHERE order_date = '2024-01-01';
-- Might not match due to time component

-- ✅ Use date ranges
SELECT * FROM orders 
WHERE order_date >= '2024-01-01' 
  AND order_date < '2024-01-02';

-- ❌ Implicit date conversion
SELECT * FROM orders WHERE order_date = 20240101;

-- ✅ Explicit date format
SELECT * FROM orders WHERE order_date = DATE('2024-01-01');
```

### 4. Division by Zero
```sql
-- ❌ Runtime error risk
SELECT revenue / orders_count FROM monthly_stats;

-- ✅ Safe division
SELECT 
    CASE 
        WHEN orders_count = 0 THEN 0 
        ELSE revenue / orders_count 
    END as avg_order_value
FROM monthly_stats;

-- Or use NULLIF
SELECT revenue / NULLIF(orders_count, 0) FROM monthly_stats;
```

### 5. GROUP BY Gotchas
```sql
-- ❌ Invalid GROUP BY (in strict SQL mode)
SELECT name, department, MAX(salary)
FROM employees
GROUP BY department;
-- 'name' should be in GROUP BY or an aggregate

-- ✅ Correct GROUP BY
SELECT department, MAX(salary)
FROM employees
GROUP BY department;

-- Or if you need the name too:
SELECT name, department, salary
FROM employees e1
WHERE salary = (
    SELECT MAX(salary) 
    FROM employees e2 
    WHERE e2.department = e1.department
);
```

---

## 📊 Practice Datasets

### 🎯 Beginner-Friendly Datasets

#### 1. **Northwind Database**
Classic sample database with customers, orders, products
- **PostgreSQL**: [GitHub - Northwind SQL](https://github.com/pthom/northwind_psql)
- **MySQL**: [GitHub - Northwind MySQL](https://github.com/dalers/mywind)

#### 2. **Sakila Database (MySQL)**
DVD rental store database
```bash
# Download and install
wget https://downloads.mysql.com/docs/sakila-db.tar.gz
tar -xzf sakila-db.tar.gz
mysql -u root -p < sakila-db/sakila-schema.sql
mysql -u root -p < sakila-db/sakila-data.sql
```

#### 3. **Chinook Database**
Music store database (available for multiple DB engines)
- **Download**: [GitHub - Chinook Database](https://github.com/lerocha/chinook-database)

### 🌐 Online Practice Platforms
- **HackerRank SQL**: [hackerrank.com/domains/sql](https://www.hackerrank.com/domains/sql)
- **LeetCode Database**: [leetcode.com/problemset/database/](https://leetcode.com/problemset/database/)
- **SQLZoo**: [sqlzoo.net](https://sqlzoo.net)
- **W3Resource SQL Exercises**: [w3resource.com/sql-exercises/](https://www.w3resource.com/sql-exercises/)

### 📈 Real-World Data Sources
- **Kaggle Datasets**: [kaggle.com/datasets](https://www.kaggle.com/datasets)
- **World Bank Data**: [data.worldbank.org](https://data.worldbank.org)
- **NYC Open Data**: [data.cityofnewyork.us](https://data.cityofnewyork.us)

---

## 📖 Quick Reference

### Essential SQL Commands
```sql
-- Data Definition Language (DDL)
CREATE TABLE, ALTER TABLE, DROP TABLE, CREATE INDEX

-- Data Manipulation Language (DML)
SELECT, INSERT, UPDATE, DELETE

-- Data Control Language (DCL)
GRANT, REVOKE

-- Transaction Control
BEGIN, COMMIT, ROLLBACK, SAVEPOINT
```

### Common Functions by Database

| Function | PostgreSQL | MySQL | SQLite | Description |
|----------|------------|-------|--------|-------------|
| String Length | `LENGTH()` | `LENGTH()` | `LENGTH()` | String length |
| Substring | `SUBSTRING()` | `SUBSTRING()` | `SUBSTR()` | Extract substring |
| Current Date | `CURRENT_DATE` | `CURDATE()` | `DATE()` | Current date |
| Current Time | `NOW()` | `NOW()` | `DATETIME()` | Current timestamp |
| Random | `RANDOM()` | `RAND()` | `RANDOM()` | Random number |
| Top N Records | `LIMIT n` | `LIMIT n` | `LIMIT n` | Limit results |

### Keyboard Shortcuts (Common SQL Editors)
- **Execute Query**: `Ctrl+Enter` (Windows/Linux), `Cmd+Enter` (Mac)
- **Execute Selected**: `Ctrl+Shift+Enter`
- **Comment/Uncomment**: `Ctrl+/`
- **Format SQL**: `Ctrl+Shift+F`

---

## 🎓 Next Steps

### Intermediate Learning Path
1. **Master JOINs**: Practice complex multi-table queries
2. **Window Functions**: Learn ranking, running totals, percentiles  
3. **Performance Tuning**: Study execution plans and indexing strategies
4. **Stored Procedures**: Learn database-specific programming features

### Advanced Topics
1. **Database Design**: Normalization, ER diagrams, schema design
2. **Data Warehousing**: Star/snowflake schemas, ETL processes
3. **NoSQL Integration**: Working with JSON columns, hybrid approaches
4. **Database Administration**: Backup/recovery, user management, security

### Specialized Areas
- **Analytics Engineering**: dbt, data modeling, testing
- **Data Engineering**: Airflow, pipeline orchestration
- **Business Intelligence**: Tableau, Power BI, data visualization
- **Machine Learning**: Feature engineering, model deployment

---

## 📚 Additional Resources

### 📖 Books
- **"SQL in 10 Minutes, Sams Teach Yourself"** by Ben Forta
- **"Learning SQL"** by Alan Beaulieu  
- **"High Performance MySQL"** by Baron Schwartz
- **"PostgreSQL: Up and Running"** by Regina Obe

### 🎥 Video Courses
- **Codecademy SQL Course**
- **DataCamp SQL Track**  
- **Coursera SQL Specializations**
- **YouTube: Derek Banas SQL Tutorial**

### 🌐 Documentation
- **PostgreSQL Docs**: [postgresql.org/docs/](https://www.postgresql.org/docs/)
- **MySQL Docs**: [dev.mysql.com/doc/](https://dev.mysql.com/doc/)
- **SQLite Docs**: [sqlite.org/docs.html](https://www.sqlite.org/docs.html)

---

**Happy Querying! 🎉**

*Remember: The key to mastering SQL is practice. Start with simple queries and gradually work your way up to complex analytics. Every expert was once a beginner!*

---

⭐ **Star this repository if it helped you!**

📧 **Questions?** Feel free to open an issue or reach out!

---

*Last Updated: June 2025 | Version 1.0*