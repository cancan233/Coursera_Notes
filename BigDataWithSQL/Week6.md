# Week 6

UNION and JOIN

## UNION and UNION ALL

```sql
SELECT id, name FROM fun.games
UNION ALL
SELECT id, name FROM toy.toys;
```

```sql
SELECT country FROM customers
UNION DISTINCT  -- it will return unique rows
SELECT country FROM offices;
```

* the default UNION is identical to UNION DISTINCT.
* the select list should have same number of columns, same column names, same data type. Trick: use column aliases and CAST to match
* the returned results will in arbitrary order.
* CAST return NULL: When cast a character string column whose values *do not* represent numbers to a numeric column, it will return a column of NULL values (in Hive and Impala) or zeros (in MySQL).
* CAST return truncated values: when convert decimal number values to integer values. In MySQL or PostgreSQL, it rounds the decimal.

### Using ORDER BY and LIMIT with UNION

```sql
SELECT name, list_price AS price FROM games
UNION ALL
SELECT name, price FROM toys
ORDER BY price; 
-- this works in MySQL and PostgreSQL. it will order the final table by price. But not work in Impala and Hive.

SELECT name, list_price AS price FROM games ORDER BY price
UNION ALL
SELECT name, price FROM toys ORDER BY price;
-- this will return the results in arbitrary order. Not work.
```

Use subquery to return an ordered result.

LIMIT is similar. `LIMIT` at the end of one select will only work on that select.

## JOINS

```sql
SELECT toys.id AS id, toys.name AS toy, 
		price, maker_id, makers.name AS maker, city 
		-- if it is *, it will all columns from two tables, which will restust in two 'name' columns.
	FROM toys JOIN makers
		ON toys.maker_id = makers.id;
```

* you can use table aliases, such as `toys AS t JOIN makers as m` to simplify the notation. (AS here can be neglected.)

### INNER JOINS

<img src="https://i.imgur.com/n70hwzX.png" alt="image-20210324014255246" style="zoom:80%;" />

The order of join here doesn't matter.

### OUTER JOINS

For non-match entry, it will insert NULL value.

* LEFT OUTER JOINS

<img src="https://i.imgur.com/RqNDJf4.png" alt="image-20210324015208440" style="zoom:70%;" /><img src="https://i.imgur.com/WmVFanl.png" alt="image-20210324020837050" style="zoom:70%;" />

* RIGHT OUTER JOINS

<img src="https://i.imgur.com/0sK6hkP.png" alt="image-20210324015230235" style="zoom: 70%;" /><img src="https://i.imgur.com/SsLhhno.png" alt="image-20210324020509645" style="zoom:80%;" />

* FULL OUTER JOINS

<img src="https://i.imgur.com/irMfXTO.png" alt="image-20210324015324040" style="zoom:80%;" />

### Joining Three or More Tables

use the same syntax as with two tables, but with more JOINs added at the end of the FROM clause. Each JOIN should have its own ON keyword and join condition.

```sql
SELECT c.name AS customer_name,
	o.total AS order_total,
	e.first_name AS employee_name
	FROM customers c
		JOIN orders o ON c.cust_id = o.cust_id
		JOIN employees e ON o.empl_id = e.empl_id;
```

## Core Quiz

![image-20210324022711486](https://i.imgur.com/utYNXRI.png)

![image-20210324023909514](https://i.imgur.com/8zUNjbh.png)

![image-20210324023920989](https://i.imgur.com/bgkVJYr.png)

![image-20210324023018189](https://i.imgur.com/qOqnGCo.png)

![image-20210324023025536](https://i.imgur.com/YTsE580.png)

![image-20210324024025922](https://i.imgur.com/0lu7z2F.png)

![image-20210324024707216](https://i.imgur.com/kcwT8ZE.png)

![image-20210324024718255](https://i.imgur.com/2vQ5e3g.png)

![image-20210324023042858](https://i.imgur.com/a2pgcaS.png)

![image-20210324023050750](https://i.imgur.com/uP5bMP2.png)

![image-20210324024729247](https://i.imgur.com/e1V8ixp.png)

![image-20210324024737868](C:%5CUsers%5CUSER%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210324024737868.png)

## Advanced Joins

### Handling NULL values in Join Key Columns

`<=>` is shorthand of "IS NOT DISDINCT FROM", use this operation for NULL. It will includes the row with NULL.

```sql
SELECT c.cust_id, name, total
	FROM customers_with_null c JOIN orders_with_null o
		ON c.cust_id <=> o.cust_id;
```

### Non-Equijoins

Not allowed in Hive. 

### Cross Joins

return the cross product, also known as the Cartesian product, of the datasets.

* in many SQL engines, a cross join will be performed if the join condition is omitted.

### Left Semi-Joins

return only records from the table on the left for which there is a match in the table on the right. Both Hive and Impala allow semi joins.

```sql
SELECT DISTINCT manufacturer, model
	-- no data from right table are allowed here
	FROM planes p LEFT SEMI JOIN flights f
		ON p.tailnum = f.tailnum AND f.distance > 400 * 1.15;
		-- the only place where a column from the right table is used is in the join condition.
```

### Specifying Two or More Join Conditions

```sql
ON f.year = w.year
	AND f.month = w.month
	AND f.day = w.day
	AND f.origin = w.airport
```

When the pairs of corresponding columns have identical names in the two tables, you can use the `USING` keyword for such multiple join conditions.

```sql
SELECT ...
	FROM table 1 JOIN table 2
		USING (city, state);
```

## Honors Quiz

![image-20210326024613900](https://i.imgur.com/5SNbTsy.png)

![image-20210326024626071](https://i.imgur.com/yZicEdj.png)

![image-20210326024637856](https://i.imgur.com/QyPRsG2.png)

![image-20210326024647236](https://i.imgur.com/0gfZfC6.png)