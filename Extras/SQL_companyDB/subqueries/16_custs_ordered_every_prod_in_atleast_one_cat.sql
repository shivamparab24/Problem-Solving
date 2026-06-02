-- Find customers who ordered every product in at least one category

SELECT DISTINCT
       c.customer_id,      -- customer id
       c.customer_name     -- customer name
FROM customers c
JOIN (
    SELECT o.customer_id,  -- customer
           p.category      -- category
    FROM orders o
    JOIN order_items oi
         ON oi.order_id = o.order_id      -- order -> items
    JOIN products p
         ON p.product_id = oi.product_id  -- item -> product
    GROUP BY o.customer_id,
             p.category                    -- per customer/category
    HAVING COUNT(DISTINCT p.product_id) =  -- products ordered
           (
               SELECT COUNT(*)             -- total products
               FROM products p2
               WHERE p2.category = p.category
           )
) completed_categories
ON c.customer_id = completed_categories.customer_id; -- matching customer



-- Using EXISTS + NOT EXISTS (relational division)

SELECT DISTINCT
       c.customer_id,      -- customer id
       c.customer_name     -- customer name
FROM customers c
WHERE EXISTS (

    -- at least one category
    SELECT 1
    FROM (
        SELECT DISTINCT category
        FROM products
    ) cat

    WHERE NOT EXISTS (

        -- missing products check
        SELECT p.product_id
        FROM products p
        WHERE p.category = cat.category

          AND NOT EXISTS (

                -- customer ordered product?
                SELECT 1
                FROM orders o
                JOIN order_items oi
                     ON oi.order_id = o.order_id
                WHERE o.customer_id = c.customer_id
                  AND oi.product_id = p.product_id
          )
    )
);



-- Using GROUP BY + HAVING

SELECT DISTINCT
       c.customer_id,      -- customer id
       c.customer_name     -- customer name
FROM customers c
JOIN (
      SELECT o.customer_id, -- customer
             p.category     -- category
      FROM orders o
      JOIN order_items oi
           ON o.order_id = oi.order_id      -- order -> items
      JOIN products p
           ON p.product_id = oi.product_id  -- item -> product
      GROUP BY o.customer_id,
               p.category                   -- per customer/category
      HAVING COUNT(DISTINCT p.product_id)   -- ordered products
           =
           (
             SELECT COUNT(*)                -- total category products
             FROM products p2
             WHERE p2.category = p.category
           )
     ) x
ON c.customer_id = x.customer_id;           -- matching customer



-- Using CTE

WITH category_products AS (
    SELECT category,              -- category
           COUNT(*) AS total_products
    FROM products
    GROUP BY category             -- total products/category
),
customer_products AS (
    SELECT o.customer_id,         -- customer
           p.category,            -- category
           COUNT(DISTINCT p.product_id) AS purchased_products
    FROM orders o
    JOIN order_items oi
         ON oi.order_id = o.order_id      -- order -> items
    JOIN products p
         ON p.product_id = oi.product_id  -- item -> product
    GROUP BY o.customer_id,
             p.category                   -- customer/category
)
SELECT DISTINCT
       c.customer_id,      -- customer id
       c.customer_name     -- customer name
FROM customers c
JOIN customer_products cp
     ON c.customer_id = cp.customer_id     -- customer match
JOIN category_products cat
     ON cp.category = cat.category         -- category match
WHERE cp.purchased_products = cat.total_products; -- all products ordered