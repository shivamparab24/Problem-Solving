-- Find all orders placed by customers from the city 'Boston'.


select order_id, customer_id, order_date
from orders
where customer_id IN (
    select customer_id
    from customers
    where city = 'Boston'
);