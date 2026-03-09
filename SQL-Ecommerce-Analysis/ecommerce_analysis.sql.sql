create database project1;
set autocommit = off ;
-- task 1

update project1.customers set loyalty_points = case
when age<25 then loyalty_points +10
when age between 25 and  40 then loyalty_points + 10
else loyalty_points + 5
end ;
select * from project1.customers;

-- task 2

create table tot_order_val as select c.country,c.customer_id,o.order_value from project1.customers c join project1.orders o on c.customer_id = o.customer_id ;
select * from project1.tot_order_val;
select country, sum(order_value) as sum_ord_value, case 
when sum(order_value) > 100000 then 'high'
when sum(order_value)  between 50000 and 100000 then 'medium'
else 'low'
end as sales_category
from tot_order_val
group by country
order by sum_ord_value;

-- task 3

create table tot_pay_method as select o.product_id,o.payment_method,p.stock_quantity from project1.orders o join project1.products p on o.product_id = p.product_id ;
select * from tot_pay_method;
select
sum( case when payment_method = 'paypal' then stock_quantity else 0 end) as pay_pal_qty,
sum( case when payment_method = 'bank transfer' then stock_quantity else 0 end) as bank_transfer_qty,
sum( case when payment_method = 'credit card' then stock_quantity else 0 end) as credit_card_qty
from tot_pay_method ;

-- task 4

select customer_id,tot_order_val,customer_rank from (
select c.customer_id,sum(order_value) as tot_order_val,
rank() over( order by sum(order_value) desc) as customer_rank from 
project1.customers c left join project1.orders o on c.customer_id = o.customer_id
group by c.customer_id) as task_4
where customer_rank <= 3
order by customer_rank;

-- task 5
SELECT 
  product_name,
  sum(stock_quantity) as total_quantity
from project1.products
group by  product_name
having sum(stock_quantity) > (
  select avg(stock_quantity) from task5
);

-- task 6

delimiter // 
create procedure ind_customer(in cust_id int)
begin
select order_id, customer_id, product_id, order_date, order_status, quantity, discount, shipping_cost, payment_method, order_value from project1.orders 
where customer_id = cust_id;
end // 
delimiter ;
drop procedure ind_customer;
call ind_customer(860);

-- task 7

delimiter //
create procedure customer_spending( in cust_id int,inout tot_spent int)
begin
select sum(order_value) into tot_spent from project1.orders
where customer_id = cust_id ;

end //
delimiter ;

call customer_spending(860,@tot_spent);
select @tot_spent;

-- task 8

delimiter // 
create trigger cust_upd_loyalty_points before insert on project1.customers for each row
begin 
if new.loyalty_points is null 
then set new.loyalty_points = 0;
end if;
end // 
delimiter ;
drop trigger cust_upd_loyalty_points;
insert into project1.customers 
values(5005,'kohli','theking@cricket.biz'	,'male'	,35	,'india','delhi',2012-05-16,2025-06-03,null);
delete from project1.customers where customer_id in (5002,5003);
alter table project1.customers modify loyalty_points varchar(50);
SELECT * FROM project1.customers ;

-- task 9

delimiter // 
create trigger new_order_quantity_upd after insert on project1.orders for each row
begin 
update project1.products
set stock_quantity = stock_quantity - new.quantity
where product_id = new.product_id;
end //
delimiter ;
drop trigger new_order_quantity_upd;
insert into project1.orders 
values(5001,4688,7,2024-05-02,'Shipped',3,0.02,18.69,'Credit Card',143.34);
SELECT * FROM project1.products;
commit;

