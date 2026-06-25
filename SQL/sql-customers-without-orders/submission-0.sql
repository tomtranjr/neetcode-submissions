-- Write your query below
-- with customer_order as (
--     select customer_id
--     from orders
-- )
-- select name
-- from customers
-- where id not in customer_order

select name
from customers
where id not in (select customer_id from orders)