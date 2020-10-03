# Week 4
## Divide and Conquer Algorithm
**Divide**: Break into **non-overlapping** subproblems of the **same type**.
**Conquer**: solve subproblems and combine.
Because each subproblem is the same type as our original problem, it is naturally to solve the problems recursively. 

## Linear Search in Array
**Input**: An array *A* with *n* elements. A key *k*.
**Output**: An index, *i*, where *A[i]=k*. If there is no such *i*, then NOT_FOUND.

Below is the recursive version.
``` python
LinearSearch(A, low, high, key):
    if high < low:
        return NOT_FOUND
    if A[low] == key:
        return low
    return LinearSearch(A, low+1, high, key)
```

A <span style="color:blue">recurrence relation</span> is an equation recursively defining a sequence of values. Example: Fibonacci numbers.

Recurrence defining worst-case time: *T(n) = T(n-1) + c* and *T(0) = c*. Thus, the worse-case runtime for LinearSearch is **O(n)**.

The iterative version of LinearSearch is:
```python
LinearSearch(A, low, high, key):
    for i in range(low, high):
        if A[i] == key:
            return i
    return NOT_FOUND
```

## Binary Search
**Input**: A sorted array *A*, elements in *A* can repeat, and a key *k*
**Output**: An index, *i*, where *A[i] = k*; Otherwise, the greatest index *i*, where *A[i] < k*; Otherwise, *low-1*.

```python
import math

BinarySearch(A, low, high, key):
    if high < low:
        return low - 1
    mid = math.floor(low + (high - low)/2)
    if key = A[mid]:
        return mid
    else if key < A[mid]:
        return BinarySearch(A, low, mid - 1, key)
    else if key > A[mid]:
        return BinarySearch(A, mid + 1, high, key)
```

