# Week 3

## WHERE Clause

only affects which rows are returned not which columns are returned.

#### Expressions in SELECT list

* becomes column in result
* multiple expressions
* different data types allowed

#### Expressions in WHERE list

* filters rows in result
* only one expression
* expression must be Boolean
* cannot be in the SELECT list

Examples:

```sql
SELECT name
  FROM fun.games
  WHERE list_price < 10;
```

### Using Operators and Functions in the WHERE Clause

* comparison operators

```sql
SELECT color, red + green + blue > 650 AS light
  FROM wax.crayons;
```

* data types and precision

  * when comparing numbers, sql will stop compare at some points. For example. 1/3 = 0.33333333333333333333 evaluates to true.
  * use rounding to avoid ambiguous comparison

* use backslash (\\) for escaping interior single quotes

* LIKE operator: used to match partial strings.  it is case-sensitive in hive and impala.

  ```sql
  SELECT * FROM inventory
    WHERE shop LIKE '%ice%';
  ```

* logical operators: AND, OR, NOT 

  ```sql
  SELECT * FROM fun.games WHERE NOT name = 'Risk';
  ```

  * Order of Operations: NOT, AND, OR. parentheses can override the order.

* Other relational operators

  * IN

    ```sql
    SELECT * FROM fun.games
      WHERE name IN ('Monopoly', 'Clue', 'Risk');
    ```

  * BETWEEN

    ```sql
    SELECT * FROM fun.games
      WHERE min_age BETWEEN 8 AND 10;
    ```

### Working with Missing Values

* WHERE : True will be included in results
* NULL does not mean false; it means "unknown"
* WHERE : False or NULL will be excluded from results
* you cannot test for NULL using =, <, >, .... Any value compared to NULL evaluates to NULL
* you need to use **IS NULL** operator or **IS NOT NULL** operator
* **IS DISTINCT FROM** non-NULL: the results will includes those NULL rows.
* **IS NOT DISTINCT FROM** or **<=>**
* An empty string, also called a zero-length string, ('') is not the same thing as a NULL value
* The literal string 'NULL' is also not the same as NULL

#### Conditional Functions

* if 

  ```sql
  SELECT shop, game, 
  		if(price IS NULL, 8.99, price)
  			AS correct_price
  	FROM fun.inventory;
  ```

* CASE

  ```sql
  SELECT shop, game, price,
  		CASE WHEN price IS NULL THEN
  				'missing price'
  			WHEN price > 10 THEN
  				'high price'
  			ELSE 'low price'
  		END AS price_category
  	FROM fun.inventory;
  ```

* nullif: replace with NULL if condition is met.

  ```sql
  SELECT distance / nullif(air_time, 0) * 60 AS avg_speed
  	FROM fly.flights;
  ```

* ifnull: replace the NULL with the value

  ```sql
  SELECT ifnull(air_time, 340) AS air_time_no_nulls
  	FROM fly.flights WHERE origin = 'EWR' AND dest = 'SFO';
  ```

* coalesce: Coalesce can take any number of arguments, and it returns the value of the first argument, that's not NULL. If they're all NULL, it returns NULL.

  ```sql
  SELECT coalesce(arr_time, sched_arr_time) AS real_or_sched_arr_time
  	FROM fly.flights;
  ```

  ```sql
  SELECT coalesce(arr_time, sched_arr_time) AS real_or_sched_arr_time
  	FROM fly.flights;
  ```


### Core Quiz

![image-20210322015732879](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210322015733.png)

![image-20210322015743617](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210322015743.png)

![image-20210322015758067](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210322015758.png)

![image-20210322015808594](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210322015808.png)

![image-20210322020355910](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210322020355.png)

![image-20210322015832739](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210322015832.png)

![image-20210322015846053](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210322015846.png)

![image-20210322020708405](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210322020708.png)

![image-20210322015857935](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210322015858.png)

![image-20210322015908580](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210322015908.png)

## Using Hive and Impala in Scripts and Applications

```sql
-- set a variable containing the name of the game
SET hivevar:game=Monopoly;
-- return the list price of the game
SELECT list_price FROM fun.games WHERE name = '${hivevar:game}';
-- return the price of the game at game shops
SELECT shop, price FROM fun.inventory WHERE game = '${hivevar:game}';
```

If want to run the same file with different variable values:

```sql
SELECT hex FROM wax.crayons WHERE color = '${hivevar:color}';
```

Then run the script from the command line:

```bash
beeline -u ... --hivevar color="Red" -f hex_color.sql
```

If there are several different variables need to change the value:

```sql
SELECT color FROM wax.crayons
	WHERE red = ${hivevar:red} AND
		green = ${hivevar:green} AND
		blue = ${hivevar:blue};
```

Then in command line:

```bash
beeline -u ... --hivevar red="238" \
			  --hivevar green="32" \
			  --hivevar blue="77" \
			  -f color_from_rgb.sql
```

In Impala-shell, we use `${var:color}`.

#### Calling Beeline and Impala Shell from Scripts

```shell
#!/bin/bash
impala-shell \ 
  --quiet \ 
  --delimited \ 
  --output_delimiter=',' \ 
  --print_header \
  -q 'SELECT * FROM fly.flights WHERE air_time = 0;' \
  -o zero_air_time.csv
mail \
  -a zero_air_time.csv \
  -s 'Flights with zero air_time' \
  fly@example.com \
  <<< 'Do you know why air_time is zero in these rows?'
```

```bash
chomod 755 email_results.sh
```

* impyla: a python package