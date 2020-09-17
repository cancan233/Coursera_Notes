# Week 3
## Largest Number
Form the largest number from a certain list of digits: Find the maximum number from the remaining digits and append them one by one.

## Car Fueling
**Input**: A car which can travel at most *L* kilometers with full tank, a source point *A*, a destination point *B* and *n* gas stations at distances $x_1 \leq x_2 \leq x_3 \leq \dots \leq x_n$ in kilometers from *A* along the path from *A* to *B*. 
**Output**: the minimum number of refills to get from *A* to *B*, besides refill at *A*.
**Greedy Choice**: Refill at the farthest reachable gas station

**Algorithm**:
* start at *A*
* refill at the farthest reachable gas station *G*
* Make *G* new *A*

## Algorithm Implementation

### Python Code

$A = x_0 \leq x_1 \leq x_2 \leq \dots \leq x_n \leq x_{n+1} = B$

```python
def MinRefills(x, n, L):
    numRefills, currentRefill = 0, 0
    while currentRefill <= n:
        lastRefill = currentRefill
        while (currentRefill <= n and x[currentRefill + 1] - x[lastRefill] <= L):
            currentRefill += 1
        if currentRefill == lastRefill:
            return False
        if currentRefill <= n:
            numRefill += 1
    return numRefills
```

### runtime analysis

The running time of MinRefills(x, n, L) is *O(n)*

## Main Ingredients of Greedy Algorithms

* break into sub-small problem

* safe move

A move is safe if there is an optimal solution consistent with this first move.

### General Strategy

* Make a greedy choice
* Prove that it is a safe move
* Reduce to the subproblem

## Celebration Party Problem

Organize children into the minimum possible number of groups such that the age of any two children in the same group differ by at most one year. 

```python
def naive_MinGroups(C):
    m = len(C)
    for each partition into groups C = G1 ... Gk, k is the group number
        good = true
        for i in range(1, k):
            if max(Gi) - min(Gi) > 1:
                good = false
        if good:
            m = min(m, k)
    return m
```

However, the above algorithm needs at least $2^n$ operations. (exponential)

In greedy algorithm, we need to define the safe move. In this case, the safe move is to cover the leftmost point with a unit segment with left end in this point.

```python
def PointsCoverSorted(x):
    """
    x is a list points ordered from small to large.
    """
	R = {}
	i = 1
    while i <= n:
        [left, right] = [x[i], x[i] + 1]
        R.add(left)
        R.add(right)
        i += 1
        while i <= n and x[i] <= right:
            i += 1
    return R
```

The running time of `PointsCoverSorted()` is $O(n)$.

Sorting in $O(n logn)$ and the total running time would be $O(nlogn)$

## Fractional Knapsack













