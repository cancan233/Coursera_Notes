* DESCRIBE tablename; to show the information of the table.
* order of operations: 1) * and \ 2) + and -. 3) parentheses can override the sequences.

![image-20210320175344068](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210321011427.png)

* division: divide two integers might not result in an integer.

  * *decimal division*: result is not an integer. Symbol: /
  * *integer division*: the whole number part of the division. Symbol: DIV
  * *modulo*: only the remainder part of the division. Symbol: %

  The operator you use will also depend on which query engine you are using.

  For /, it is *decimal division* in Hive, Impala and MySQL but *integer division* in PostgreSQL and Presto when both of the operands are integers. Convert one of the operands into decimal before division in these two engines.

  For DIV, if one of the operands is integer, it will raise an error message. e.g. 17.0 DIV 5 = [ERROR]

  For modulo, it is cyclical and it can be used for non-integer.

* Column aliases: AS. eg. 5 AS shipping_fee. AS is optional here. e.g. 5 shipping_fee will produce the same result.
* Built-in functions: round(), ceil(), floor(), pow(), rand()
  *  round(4.5) --> 5, round(-4.5) --> -5. 
  * 0 <= rand() < 1, ceil(rand()*10)
  * trim('   Common string Functions    ') = 'Common string Functions'

* Data Type Conversion: cast(min_age AS STRING)
* SELECT DISTINCT: omit duplicate rows from the results set.

### Common String Functions

* length(str): return an integer value equal to the number of characters in the string argument **str**.
* reverse(str): returns the characters in the reverse order
* upper(str), lower(str): useful for doing case-insensitive string comparisons
* trim(str), ltrim(str), rtrim(str): remove whitespace at the ends of the argument **str**.
* lpad(str, n, padstr), rpad(str, n, padstr): take a string **str** and an integer *n* and return a string of length *n*. 
* substring(str, index, max_length): returns a portion of the original string. **index** indicates where to start the substring (1-indexing) and **max_length** is how many characters to include.
* concat(str1, str2,[, str3, ...]), concat_ws(sep, str1, str2[, str3, ...]): *concatenate strings*. ws stands for "with separator"

### FROM Clause

FROM <database>.<tablename>

### RESERVED WORDS

e.g. select, from, as, distinct, show, use

In a SELECT statement executed with Hive and Impala, identifiers (such as names of tables and columns) will work regardless of their case (upper, lower, or a mix).

### Case Sensitive

In Hive and Impala, all keywords, function names and identifiers are case insensitive. Only string comparisons are case sensitive.

Conventions:

* Keywords (like SELECT and FROM) are in uppercase
* Most other things are all lowercase, including identifiers and most function keywords

### Week 2 Core Quiz

![image-20210321004841632](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210321011435.png)

![image-20210321004917475](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210321011438.png)

The option "Listing all the data in a table" should also be checked.

![image-20210321004947773](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210321011440.png)

![image-20210321005020153](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210321011442.png)

![image-20210321005043372](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210321011447.png)

![image-20210321005052987](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210321011450.png)

![image-20210321005103867](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210321011452.png)

![image-20210321005115465](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210321011455.png)

![image-20210321005126011](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210321011457.png)

![image-20210321005133966](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210321011459.png)

![image-20210321005143212](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210321011501.png)

![image-20210321005154107](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210321011504.png)

## Honors Part

### Using Beeline in Non-interactive Mode

`beeline -u ... -e 'SELECT * FROM fun.games'` : no ; if only one command

`beeline -u ... -f myquery.sql` : execute a file containing HiveQL code using the -f option

`beeline --silent=true -u ...` : suppress the output information 

### Using Impala shell in Non-interactive Mode

`impala-shell -q 'SELECT * FROM fun.games'`

`impala-shell -f myquery.sql`

`impala-shell --quiet -f myquery.sql`

In file, to add comment

* --: ignore content after -- symbol
* /*  */: ignore content between these two symbols

### Formatting the output of beeline and impala-shell

* Beeline: change output format using `--outputformat=`
  * `csv2` for comma delimited
  * `tsv2` for tab delimited
  * header is included by default
  * `beeline -u ... --outputformat=csv2 -e 'SELECT * FROM fun.games'`
  * `beeline -u ... --showHeader=false --outputformat=csv2 -e 'SELECT * FROM fun.games'`: exclude header
* impala shell: use `--delimited`
  * tab is the default delimiter, header is excluded by default
  * `impala-shell --delimited --output_delimiter=',' -q 'SELECT * FROM fun.games'`
  * `impala-shell --delimited --print_header -q 'SELECT * FROM fun.games'`: show header

### Saving Hive and Impala query results to a file

* `beeline -u ... --outputformat=csv2 -e 'SELECT * FROM fun.games' > file.txt`
* `impala-shell --delimited --output_delimiter=',' -q 'SELECT * FROM fun.games' -o file.txt`

### Honored Quiz

![image-20210321180046418](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210321180046.png)

![image-20210321180101977](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210321180102.png)

![image-20210321180111124](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210321180111.png)

![image-20210321180120879](https://raw.githubusercontent.com/cancan233/notes_pics/main/img/20210321180120.png)