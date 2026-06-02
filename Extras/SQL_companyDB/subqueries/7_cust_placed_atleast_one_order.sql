-- Find customers who have placed at least one order.

select customer_id, customer_name
from customers c
where EXISTS (
    select 1
    from orders
    where orders.customer_id = c.customer_id
)



-- select
--     distinct c.customer_id,
--     c.customer_name
-- from customers c
-- join orders o
-- on o.customer_id = c.customer_id
-- order by c.customer_id;