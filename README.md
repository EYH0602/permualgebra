# Permualgebra

This package allows user to do permutations calculation in terms of Modern Algebra.

## Install

```bash
pip install permualgebra
```

## Permutation

### Definition

Let S be a set of n distinct elements. A **permutation** of S is a *bijection*

<img src="./pics/defn.png" alt="Definition" style="zoom:50%;" />

For example, let S = {1, 2, 3, 4, 5, 6}, define

|i|1|2|3|4|5|6|
|:---:|:---|:---|:---|:---|:---|:---|
|p(i)|6|3|2|4|5|1|

Or a permutation can be written in **cycle notation**, where we often *omit* the 1-cycles:

<img src="./pics/cycle.png" alt="cycle notation" style="zoom:50%;" />

this cycle notation is also the way that this package express a permutation.

The **length of a cycle** is the number of elements of S in that cycle.

The **length of a permutation** is the number of cycles in that permutation.

### Theorem

**Every permutation** on S = {1, ..., n} can be written as a product of disjoint cycles. i.e. no elements of S is repeated in the cycle description.

```python
import permualgebra as pm
p = pm.Permutation(["3 6 4 2", "1 3 4 6", "5 2 1 3"])
print(p)		# (3 6 4 2)(1 3 4 6)(5 2 1 3)
pSimplify = p.getSimplify()
print(pSimplify)# (1 2 6)(3 5)
p.simplify()
print(p)		# (1 2 6)(3 5)
```



Suppose we have 2 permutations: 

<img src="./pics/pq.png" alt="pq" style="zoom: 67%;" />

we can compose them as

<img src="./pics/compose.png" alt="compose" style="zoom: 50%;" />

**Note.** composition of permutations is <ins>not</ins> commutative.

<img src="./pics/not_commutative.png" alt="Not Commutative" style="zoom:58%;" />

This package implements the composition of permutation as *multiplication*. 

```python
import permualgebra as pm

p = pm.Permutation(["1 5", "2 4 6"])
q = pm.Permutation(["1 3 5 4", "2 6"])
p.simplify()
q.simplify()
print((p*q).getSimplify())	# (1 3)(4 5 6)
print((q*p).getSimplify())	# (1 4 2)(3 5)
```



## To Do

* [ ] Errors and Exceptions
* [ ] More detailed wiki and documentation. 



