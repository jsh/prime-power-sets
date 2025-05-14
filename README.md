# Means of Sets of Powers of Primes

## The Question

Let $S$ be the set of the first $n$ powers of the prime, $p$:

$S= \lbrace 1, p, p^2, ... p^k \mid 0 \leq k \lt n-1 \rbrace$

Next, let $T$ and $U$ be non-empty, non-intersecting subsets of $S$

* $T, U \subseteq S$
* $T, U \neq \emptyset$
* $T \cap U = \emptyset$

For example, if $S= \lbrace 1, 2, 4, ..., 256 \rbrace$
you could let $T= \lbrace 2, 8, 32 \rbrace$
and $U= \lbrace 1, 16 \rbrace$

Finally, let $\mu(T)$ and $\mu(U)$ be the means of $T$ and $U$.

Is it possible to choose $T$ and $U$ such that $\mu(T)=\mu(U)$?

## The Code

The code in this repo lets you pick a prime, $p$ (default=2), and a set size, $2^p$,
generates every possible $T$ and $U$, then reports non-intersecting pairs with identical means.

## The Approach for $p=2$

Consider sets of powers of two.

Each subset maps, 1 to 1, to a unique integer.
Every integer, $k$, can be written, base $2$, as a sum of powers of two.
Conversely, every subset of the set of powers of two corresponds to a unique integer.

Using the example above, $k_T=101010_2=42_{10}$, and $k_U=10001_2=17_{10}$
Testing whether the sets are disjoint (non-intersecting) only requires a boolean "and" of the two integers:

```
>>> 4 & 10 == 0  # non-intersecting
False
>>> 2 & 10 == 0  # intersecting
True
>>> k_T & k_U == 0  # disjoint
True
>>>
```

The set mean is just the integer divided by the number of 1-bits in the binary representation.
```
mean_T = k_T/k.bit_count()
```

So:

* For every $k < 2^n$, the binary representation of $k$ just has $0$'s and $1$'s. Use $k$ to represent the subset containing those powers of two.
* To find the set means divide by the number of 1-bits in the base-2 representation.
* Search for duplicated means. Collect all duplicates into lists of $k$'s that have the same means.
* Comb through each such list for subsets that don't intersect by *&*-ing each pair.
(`a & b` *and*s the binary representations of $a$ and $b$)
* Report integer pairs that correspond to non-intersecting subsets with the same means.

## Other values of $p$

Every integer has a $base_p$ representation, but most such integers don't represent subsets of $\lbrace p^{n-1} \rbrace$ .
The integers representing subsets only have $0$ s and $1$ s.
Thus, for $p=3$, $40_{10}=1111_3$ represents the subset $\lbrace 3^0, 3^1, 3^2, 3^3 \rbrace$.
In contrast, $29_{10}=302_3$, which has two $1$'s and three $9$'s,
contains duplicates, so it represents a collection but not a subset.

Still, we can use *almost* the same steps to find any non-overlapping subsets of $\lbrace p^{n-1} \rbrace$ with identical means.

* For every $k < 2^{n-1}$, generate its ***binary*** representation: just $0$'s and $1$'s.
* Treat each of these as a number with the same $0$ s and $1$ s, but in base $p$. For example, if $p=3$ and $k=15$, $15_{10} \rightarrow 1111_2 \rightarrow 1111_3 \rightarrow 40_{10}$.
(This step may feel a little odd. Stick with me.) $40_{10}$ is the subset's sum.
* To find the set mean, divide the sum by the number of elements in the subset. Note that this is, again, the number of 1-bits *in the base-2 representation of k*
In this case, $k=15$, and we want $\mu( \lbrace 1, 3, 9, 27 \rbrace)=40/4=10$
* Search for duplicated means. Collect all duplicates into lists of $k$ s that have the same means.
* Search each such list for subsets that don't intersect by *&*-ing the ***binary representations*** of their $k$ s.
* Report every integer pair that corresponds to non-intersecting subsets with the same means.

## A Partial Answer

For $p=2$, duplicates begin to appear at $n=14$ .

## Conjectures
* For odd primes, $p \gt 2$, I haven't yet found duplicates.
Perhaps finite, non-intersecting sets of powers of an odd prime, $p$, always have different means.

* Actually, I haven't found duplicate means for any base, prime or not, above $2$ . Perhaps $2$ is unique.

* For $p=2$ , whenever I've found duplicate means, those means are always integers. 
Perhaps the number of elements for such subsets always divides the sum.
