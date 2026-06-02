-- Find customers who have placed more orders than the average number of orders per customer.



SELECT
    c.customer_id,
    c.customer_name
FROM customers c

-- Join customers with their orders
JOIN orders o
    ON c.customer_id = o.customer_id

-- Create one group per customer
GROUP BY c.customer_id

-- Keep only customers whose order count
-- is greater than the average order count
HAVING COUNT(*) > (

    -- Calculate the average number of orders per customer
    SELECT AVG(order_count)
    FROM (

        -- Count orders for each customer
        SELECT
            COUNT(*) AS order_count
        FROM orders
        GROUP BY customer_id

    ) t
);





-- using CTE
-- Step 1: Calculate the number of orders placed by each customer
WITH customer_orders AS (
    SELECT
        customer_id,
        COUNT(*) AS order_count
    FROM orders
    GROUP BY customer_id
)

-- Step 2: Get customer details
SELECT
    c.customer_id,
    c.customer_name
FROM customers c

-- Join customer details with their order counts
JOIN customer_orders co
    ON c.customer_id = co.customer_id

-- Step 3: Keep only customers whose order count
-- is greater than the average order count across all customers
WHERE co.order_count > (
    SELECT AVG(order_count)
    FROM customer_orders
);