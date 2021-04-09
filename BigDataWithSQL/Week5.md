# Week 5

## ORDER BY clause

return rows by default is ascending order. For descending order, `ORDER BY list_price DESC`

```sql
SELECT shop, SUM(qty) FROM inventory
	WHERE price IS NOT NULL
	GROUP BY shop
	ORDER BY shop;
```

### NULL value

* in impala and PostgreSQL, nulls sort as if they are higher than any non null value
* in Hive and MySQL, null sort as if they are lower than any non null value
* Alse, null can be ordered with `LAST` or `FIRST` keyword

```sql
SELECT shop, game, aisle, price
	FROM inventory
	ORDER BY aisle DESC NULLS LAST,
			price ASC NULLS FIRST;
```

### Using ORDER BY with Hive and Impala

For Hive only, the item in ORDER BY should be in SELECT list.

For Impala, `SELECT shop, game, price FROM inventory ORDER BY 3;`. Use index to indexing the sequence in SELECT list for ORDER BY iterm.

## LIMIT clause

`SELECT * FROM flights LIMIT 5;`

The limit clause must come after all the other clauses, and it's applied after all the other clauses.

The number that comes after the LIMIT keyword generally needs to be a *non-negative literal integers*. Some SQL engines will let you use an expression after the LIMIT keyword, but only a *constant numeric expression*, not an expression *with column references or column aliases*.

If there is a tie, return arbitrary. 

### Using LIMIT for Pagination

* Impala, PostgreSQL: `LIMIT limit OFFSET offset`
* Hive: `LIMIT offset, limit`
* MySQL supports both syntaxes
* Always use `ORDER BY` to arrange rows for pagination

## Review

Correct command Order: `SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT`

Execution Order: `FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT`.

## Core Quiz

![image-20210323202037957](https://i.imgur.com/5wjtBVY.png)

![image-20210323202048225](https://i.imgur.com/K80JjIs.png)

![image-20210323201426291](https://i.imgur.com/bE6OpX9.png)

![image-20210323201439636](https://i.imgur.com/55CcSAA.png)

![image-20210323201457721](https://i.imgur.com/IQdGppg.png)

![image-20210323201506192](https://i.imgur.com/o0RqhtO.png)

![image-20210323202113671](https://i.imgur.com/yTrdtdA.png)

![image-20210323201521366](https://i.imgur.com/hzqPhRV.png)

![image-20210323201531444](https://i.imgur.com/UX731EK.png)

![image-20210323202427521](https://i.imgur.com/WQPv9l9.png)

![image-20210323201555045](https://i.imgur.com/KhFbq47.png)

![image-20210323201604704](https://i.imgur.com/qgeUoFC.png)

## Honors Quiz

![image-20210323222913393](https://i.imgur.com/0wAK9Vp.png)

![image-20210323222924063](https://i.imgur.com/JwanFFz.png)