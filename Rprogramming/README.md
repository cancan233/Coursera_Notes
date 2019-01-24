#R Programming

- [Week 1: Writing code/setting your working directory](#Week 1: Writing code/ setting your working directory)

###Week 1: Writing code/ setting your working directory

* `getwd()`: get working directory

* `dir()`or `ls()`: list files

* ```R
  myfunction <- function(x){
      y <- rnorm(100)
      mean(y)
  }
  
  second <- function(x){
      x + norm(length(x))
  }
  ```

* save functions as function.R | `source("myfunction.R")` | `myfunction(x) or second(x)` 

* Asking Questions

  * What steps will reproduce the problem?
  * What is the expected output?
  * What do you see instead?
  * What version of the product (e.g. R, packages, etc.) are you using?
  * What operating system?
  * Additional information
  * Subject Headers **R 3.0.2 Im() funtion on Mac OS X 10.9.1 -- seg fault on large data frame** 

* Data types

  * ```Inf``` reprensents infinity

  * ```c()``` or ```vector()``` function creates vectors of objects, e.g. ```x <- c()```

    ```R
    > x <- vector("numeric", length = 10)
    > x
     [1] 0 0 0 0 0 0 0 0 0 0
    ```

  * when different types are mixed in a vector, *coercion* occurs so that every element in the vector is of the same class.

    ```R
    > x <- 0:6
    > class(x)
    [1] "integer"
    > as.numeric(x)
    [1] 0 1 2 3 4 5 6
    ```

  * **lists** can contain elements of different classes.

  * **Matrices** : ```matrix(nrow = , ncol = )```; ```dim()```; ```attributes()```

    * constructed column-wise.
    * ```cbind()```;```rbind()```

  * **Factors**: represent categorical data  ```factor(c())```

    * ```lm()```; ```glm()```
    * ```table()```
    * ```unclass``` will bring factors into lower class vector.