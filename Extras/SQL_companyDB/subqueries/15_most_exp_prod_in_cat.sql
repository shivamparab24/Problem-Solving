-- Find the most expensive product(s) in each category.

SELECT
    product_id,
    product_name,
    category,
    price
FROM products
WHERE (category, price) IN (
    SELECT
        category,
        MAX(price)
    FROM products
    GROUP BY category
);




-- correlated subquery
SELECT
    product_id,
    product_name,
    category,
    price
FROM products p
WHERE price = (
    SELECT MAX(price)
    FROM products
    WHERE category = p.category
);



-- join
SELECT
    p.product_id,
    p.product_name,
    p.category,
    p.price
FROM products p
JOIN (
    SELECT
        category,
        MAX(price) AS max_price
    FROM products
    GROUP BY category
) m
ON p.category = m.category
AND p.price = m.max_price;



-- window function
SELECT
    product_id,
    product_name,
    category,
    price
FROM (
    SELECT *,
           RANK() OVER (
               PARTITION BY category
               ORDER BY price DESC
           ) AS rnk
    FROM products
) t
WHERE rnk = 1;