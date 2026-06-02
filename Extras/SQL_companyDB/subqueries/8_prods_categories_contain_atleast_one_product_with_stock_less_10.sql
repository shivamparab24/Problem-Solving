-- Find products that belong to categories containing at least one product with stock quantity less than 10.



-- using IN
select
    p.product_id,
    p.product_name,
    p.category
from products p
where p.category IN (
    select DISTINCT category
    from products
    where stock_quantity < 10
);


-- using EXISTS
SELECT
    p1.product_id,
    p1.product_name,
    p1.category
FROM products p1
WHERE EXISTS (
    SELECT 1
    FROM products p2
    WHERE p2.category = p1.category
        AND p2.stock_quantity < 10
);
