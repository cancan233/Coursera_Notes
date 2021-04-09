# Week 4

## Aggregate operations

e.g. counting, adding, computing the average (mean), finding the minimum/maximum

| Function Name | Function Description                      | Example Invocation |
| ------------- | ----------------------------------------- | ------------------ |
| COUNT         | count all rows                            | COUNT(*)           |
| SUM           | add all supplied values and return result | SUM(salary)        |
| AVG           | return the average of all supplied values | AVG(salary)        |
| MIN           | return the lowest value                   | MIN(salary)        |
| MAX           | return the highest value                  | MAX(salary)        |

* SUM(1) is equal to COUNT(*): count the number of rows in a table
  * when you use a *scalar argument* to an aggregate function, then the aggregate function aggregates the same value over all the rows.

Examples:

```sql
SELECT COUNT(*) AS num_rows FROM employees;
```

```sql
SELECT SUM(salary) AS salary_total FROM employees;
```

```sql
SELECT MIN(salary) AS lowest_salary,
	   MAX(salary) AS highest_salary
    FROM employees;
```

* invalid mixing of aggregate and scalar operations

  * `SELECT salary - AVG(salary) FROM employees;` ( X )

  * `SELECT game, SUM(price) FROM fun.inventory;` ( X )

* Do not use aggregate expressions in the WHERE clauses.

### Populations and Samples

when analyze a dataset that describes a sample, it's important to phrase observations appropriately.

* make it clear whether a sample or a population is involved
* describe that sample or population accurately so the results are not overgeneralized

### **least** and **greatest** Functions

return the smallest or largest of the arguments that are passed to them.

```sql
SELECT greatest(red, green, blue) FROM crayons;
```

returns a result with 120 rows, each row giving the largest of the three RGB values.

## GOURP BY clause

* column reference

```sql
SELECT office_id, COUNT(*) AS num_employees
	FROM employees
	GROUP BY office_id;
```

* grouping expression
```sql
GROUP BY list_price < 10
--------------------------------
GROUP BY if(list_price < 10, 'low price', 'high price')
--------------------------------
GROUP BY CASE
	WHEN list_price < 10 THEN 'low price'
	ELSE 'high price'
  END
```

* column alias (with some SQL engines) (not work in Hive)

```sql
SELECT list_price < 10 AS low_price, COUNT(*) 
	FROM games GROUP BY low_price;
```

* Two or more of the above

```sql
SELECT min_age, max_players, COUNT(*)
	FROM games
	GROUP BY min_age, max_players;
```

```sql
SELECT min_age, list_price<10, COUNT(*)
	FROM games
	GROUP BY min_age, list_price<10;
```

* when using GROUP BY, the SELECT list can have only:
  * Aggregate expressions
  * Expressions used in GROUP BY
  * Literal values

```sql
SELECT min_age,
	   ROUND(AVG(list_price), 2) AS avg_list_price,
	   0.21 AS tax_rate, -- this is literal value
	   ROUND(AVG(list_price)*1.21, 2) AS avg_w_tax
	FROM games
	GROUP BY min_age;
```

* Use `SELECT DISTINCT` instead of using `GROUP BY` with no aggregation
* MySQL will show the result of `SELECT * FROM games GROUP BY min_age`. However, the result will be picked up arbitrary rows for each column.

### NULL values in Grouping and Aggregation

* in SQL, aggregate functions ignore NULL values.

![image-20210322204517537](https://i.imgur.com/wx40U7d.png)

(Answer: The **nullif** function is needed to prevent division by 0. The query should be similar to **SELECT AVG(distance/(nullif(air_time,0)/60)) FROM fly.flights;** )

* `SUM(column IS NOT NULL)`  to show how many columns is non-NULL

* `COUNT(column)`: return the number of rows is non-NULL

### COUNT function

`SELECT COUNT(DISTINCE aisle) FROM inventory;`

`SELECT COUNT(DISTNCT red, green, blue) FROM wax.crayons;`

In impala-shell, only one DISTINCT COUNT is allowed. It works in other SQL engine.

### shortcut for grouping

```sql
SELECT CASE WHEN dep_time IS NULL THEN 'missing'
    WHEN dep_time < 500 THEN 'night'
    WHEN dep_time < 1200 THEN 'morning'
    WHEN dep_time < 1700 THEN 'afternoon'
    WHEN dep_time < 2200 THEN 'evening'
    ELSE 'night'
  END AS dep_time_category
  COUNT(*)
FROM flights
GROUP BY dep_time_category; 
```

## Having clause

```sql
SELECT shop, SUM(price * qty) FROM inventory
	GROUP BY shop
	HAVING SUM(price * qty) > 300;
```

```sql
SELECT shop, COUNT(*) FROM inventory WHERE price < 20
	GROUP BY shop HAVING COUNT(*) >= 2;
```

## Week 4 Core Quiz

<img src="https://i.imgur.com/Xcdt56K.png" alt="image-20210322234848195"  />

![image-20210323005527814](https://i.imgur.com/8GwLkiM.png)

![image-20210322235626062](https://i.imgur.com/ohJhM9H.png)

![image-20210322234907219](https://i.imgur.com/QSd40KZ.png)

![image-20210322234915437](https://i.imgur.com/N5HfiSO.png)

![image-20210322234923344](https://i.imgur.com/19q5xLu.png)

![image-20210322234930842](https://i.imgur.com/PKwAwDN.png)

![image-20210322234938288](https://i.imgur.com/llavMFA.png)

![image-20210322234946153](https://i.imgur.com/QfKhfyP.png)

![image-20210322234958240](https://i.imgur.com/O5gPHut.png)

## Understanding Hive and Impala Version Differences

![image-20210323002539105](https://i.imgur.com/apQQG1s.png)

![image-20210323002548156](https://i.imgur.com/YF29zMC.png)

