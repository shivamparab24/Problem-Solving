-- INSERT INTO departments (department_name)
-- VALUES
-- ('Engineering'),
-- ('HR'),
-- ('Finance'),
-- ('Sales'),
-- ('Marketing'),
-- ('Operations'),
-- ('Support');





-- INSERT INTO employees
-- (
--     first_name,
--     last_name,
--     email,
--     salary,
--     hire_date,
--     department_id
-- )
-- SELECT
--     'Employee',
--     gs::text,
--     'employee' || gs || '@company.com',
--     ROUND((50000 + random()*70000)::numeric,2),
--     CURRENT_DATE - ((random()*1500)::int),
--     (random()*6 + 1)::int
-- FROM generate_series(1,500) gs;






-- INSERT INTO projects
-- (
--     project_name,
--     start_date,
--     end_date,
--     budget
-- )
-- SELECT
--     'Project ' || gs,
--     CURRENT_DATE - ((random()*365)::int),
--     CURRENT_DATE + ((random()*365)::int),
--     ROUND((100000 + random()*900000)::numeric,2)
-- FROM generate_series(1,50) gs;






-- INSERT INTO employee_projects
-- (
--     employee_id,
--     project_id
-- )
-- SELECT DISTINCT
--     (random()*29 + 1)::int,
--     (random()*14 + 1)::int
-- FROM generate_series(1,100)
-- ON CONFLICT DO NOTHING;






-- INSERT INTO customers
-- (
--     customer_name,
--     email,
--     city,
--     country
-- )
-- SELECT
--     'Customer ' || gs,
--     'customer' || gs || '@mail.com',
--     (ARRAY[
--         'New York',
--         'Chicago',
--         'Seattle',
--         'Boston',
--         'Austin',
--         'Dallas',
--         'Denver',
--         'Atlanta'
--     ])[floor(random()*8 + 1)],
--     'USA'
-- FROM generate_series(1,50) gs;






-- INSERT INTO products
-- (
--     product_name,
--     category,
--     price,
--     stock_quantity
-- )
-- SELECT
--     'Product ' || gs,

--     (ARRAY[
--         'Electronics',
--         'Accessories',
--         'Networking',
--         'Office',
--         'Furniture'
--     ])[floor(random()*5 + 1)],

--     ROUND((20 + random()*2000)::numeric,2),

--     (random()*1000)::int

-- FROM generate_series(1,1000) gs;





-- INSERT INTO orders
-- (
--     customer_id,
--     order_date,
--     order_status
-- )
-- SELECT
--     (random()*24 + 1)::int,

--     DATE '2024-01-01'
--         + ((random()*365)::int),

--     (ARRAY[
--         'Completed',
--         'Pending',
--         'Cancelled'
--     ])[floor(random()*3 + 1)]

-- FROM generate_series(1,5000);





-- INSERT INTO order_items
-- (
--     order_id,
--     product_id,
--     quantity,
--     unit_price
-- )
-- SELECT
--     (random()*99 + 1)::int,
--     (random()*24 + 1)::int,
--     (random()*10 + 1)::int,
--     ROUND((20 + random()*2000)::numeric,2)

-- FROM generate_series(1,3000);




-- SELECT COUNT(*) FROM employees;
-- SELECT COUNT(*) FROM projects;
-- SELECT COUNT(*) FROM customers;
-- SELECT COUNT(*) FROM products;
-- SELECT COUNT(*) FROM orders;
-- SELECT COUNT(*) FROM order_items;




-- ==========================================
-- DEPARTMENTS
-- ==========================================

INSERT INTO departments (department_name)
VALUES
('Engineering'),
('HR'),
('Finance'),
('Sales'),
('Marketing'),
('Operations'),
('Support');



-- ==========================================
-- EMPLOYEES
-- ==========================================

INSERT INTO employees
(
    first_name,
    last_name,
    email,
    salary,
    hire_date,
    department_id
)
SELECT
    'Employee',
    gs::text,
    'employee' || gs || '@company.com',
    ROUND((50000 + random()*70000)::numeric,2),
    CURRENT_DATE - ((random()*1500)::int),
    (random()*6 + 1)::int
FROM generate_series(1,500) gs;



-- ==========================================
-- PROJECTS
-- ==========================================

INSERT INTO projects
(
    project_name,
    start_date,
    end_date,
    budget
)
SELECT
    'Project ' || gs,
    CURRENT_DATE - ((random()*365)::int),
    CURRENT_DATE + ((random()*365)::int),
    ROUND((100000 + random()*900000)::numeric,2)
FROM generate_series(1,50) gs;



-- ==========================================
-- EMPLOYEE PROJECTS
-- ==========================================

INSERT INTO employee_projects
(
    employee_id,
    project_id
)
SELECT DISTINCT
    (random()*499 + 1)::int,
    (random()*49 + 1)::int
FROM generate_series(1,3000)
ON CONFLICT DO NOTHING;



-- ==========================================
-- CUSTOMERS
-- ==========================================

INSERT INTO customers
(
    customer_name,
    email,
    city,
    country
)
SELECT
    'Customer ' || gs,
    'customer' || gs || '@mail.com',
    (
        ARRAY[
            'New York',
            'Chicago',
            'Seattle',
            'Boston',
            'Austin',
            'Dallas',
            'Denver',
            'Atlanta'
        ]
    )[floor(random()*8 + 1)],
    'USA'
FROM generate_series(1,50) gs;



-- ==========================================
-- PRODUCTS
-- ==========================================

INSERT INTO products
(
    product_name,
    category,
    price,
    stock_quantity
)
SELECT
    'Product ' || gs,
    (
        ARRAY[
            'Electronics',
            'Accessories',
            'Networking',
            'Office',
            'Furniture'
        ]
    )[floor(random()*5 + 1)],
    ROUND((20 + random()*2000)::numeric,2),
    (random()*1000)::int
FROM generate_series(1,1000) gs;



-- ==========================================
-- ORDERS
-- ==========================================

INSERT INTO orders
(
    customer_id,
    order_date,
    order_status
)
SELECT
    (random()*49 + 1)::int,
    DATE '2024-01-01' + ((random()*365)::int),
    (
        ARRAY[
            'Completed',
            'Pending',
            'Cancelled'
        ]
    )[floor(random()*3 + 1)]
FROM generate_series(1,5000);



-- ==========================================
-- ORDER ITEMS
-- ==========================================

INSERT INTO order_items
(
    order_id,
    product_id,
    quantity,
    unit_price
)
SELECT
    (random()*4999 + 1)::int,
    (random()*999 + 1)::int,
    (random()*10 + 1)::int,
    ROUND((20 + random()*2000)::numeric,2)
FROM generate_series(1,15000);



-- =====================================================
-- SPECIAL DATA FOR SQL PRACTICE
-- =====================================================

--------------------------------------------------------
-- CUSTOMER 1 BOUGHT ALL ELECTRONICS PRODUCTS
--------------------------------------------------------

INSERT INTO orders
(
    customer_id,
    order_date,
    order_status
)
VALUES
(
    1,
    CURRENT_DATE,
    'Completed'
);

INSERT INTO order_items
(
    order_id,
    product_id,
    quantity,
    unit_price
)
SELECT
    currval('orders_order_id_seq'),
    product_id,
    1,
    price
FROM products
WHERE category = 'Electronics';



--------------------------------------------------------
-- CUSTOMERS 2-6 BOUGHT ALL NETWORKING PRODUCTS
--------------------------------------------------------

DO $$
DECLARE
    c INTEGER;
    oid INTEGER;
BEGIN

    FOR c IN 2..6 LOOP

        INSERT INTO orders
        (
            customer_id,
            order_date,
            order_status
        )
        VALUES
        (
            c,
            CURRENT_DATE,
            'Completed'
        )
        RETURNING order_id INTO oid;

        INSERT INTO order_items
        (
            order_id,
            product_id,
            quantity,
            unit_price
        )
        SELECT
            oid,
            product_id,
            2,
            price
        FROM products
        WHERE category = 'Networking';

    END LOOP;

END $$;



--------------------------------------------------------
-- CUSTOMER 10 BOUGHT EVERY PRODUCT
--------------------------------------------------------

INSERT INTO orders
(
    customer_id,
    order_date,
    order_status
)
VALUES
(
    10,
    CURRENT_DATE,
    'Completed'
);

INSERT INTO order_items
(
    order_id,
    product_id,
    quantity,
    unit_price
)
SELECT
    currval('orders_order_id_seq'),
    product_id,
    1,
    price
FROM products;



--------------------------------------------------------
-- EMPLOYEE 1 WORKS ON EVERY PROJECT
--------------------------------------------------------

INSERT INTO employee_projects
(
    employee_id,
    project_id
)
SELECT
    1,
    project_id
FROM projects
ON CONFLICT DO NOTHING;



--------------------------------------------------------
-- EMPLOYEES 2-10 WORK ON MANY PROJECTS
--------------------------------------------------------

INSERT INTO employee_projects
(
    employee_id,
    project_id
)
SELECT
    e.employee_id,
    p.project_id
FROM
(
    SELECT generate_series(2,10) employee_id
) e
CROSS JOIN
(
    SELECT project_id
    FROM projects
    LIMIT 10
) p
ON CONFLICT DO NOTHING;



--------------------------------------------------------
-- EMPLOYEE 500 HAS NO PROJECTS
--------------------------------------------------------

DELETE
FROM employee_projects
WHERE employee_id = 500;



--------------------------------------------------------
-- DEPARTMENT 1 HIGH SALARY OUTLIER
--------------------------------------------------------

UPDATE employees
SET salary = salary + 100000
WHERE department_id = 1;



--------------------------------------------------------
-- PRODUCT NEVER ORDERED
--------------------------------------------------------

INSERT INTO products
(
    product_name,
    category,
    price,
    stock_quantity
)
VALUES
(
    'Never Ordered Product',
    'Electronics',
    999.99,
    100
);