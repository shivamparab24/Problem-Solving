-- Find products that have never appeared in any order.

SELECT product_id, product_name
from products
where product_id NOT IN (select product_id from order_items);