-- total sales and average price by device
-- select device,
-- sum("total_sales") ttoal_sales,
-- avg(total_sales) avg_sales
-- from "ecommerce_data"
-- group by device

-- distinct users and events by country
-- select country,
-- APPROX_COUNT_DISTINCT(user_id) as unique_users,
-- count(*) as event_count
-- from ecommerce_data
-- group by country
-- ORDER BY 2 DESC

-- total quantity and total price per product
-- select product_id,
-- sum(quantity) as total_quantity_sold,
-- sum(price) as total_price,
-- count(*) as number_of_prd_sold
-- from ecommerce_data
-- group by product_id
-- ORDER BY 4 DESC


-- time aggregation by minute
-- select
-- floor(__time to MINUTE) as data_minute,
-- count(*) as event_count,
-- sum(price) total_sales
-- from ecommerce_data
-- where __time >= CURRENT_TIMESTAMP - INTERVAL '1' DAY
-- group by FLOOR(__time to MINUTE)
