# Means of Sets of Powers of Primes

## The Question

Let $S$ be the set of the first $n$ powers of the prime, $p$:

$S=$ `{`$1, p, p^2, ... p^k \mid 0 \leq k \lt n-1$`}`

Next, let $T$ and $U$ be non-empty, non-intersecting subsets of $S$

* $T, U \subseteq S$
* $T, U \neq \emptyset$
* $T \cap U = \emptyset$

For example, if $S=$ `{` $1, 2, 4, ..., 256$ `}`
you could let $T=$ `{` $2, 8, 32$ `}`
and $U=$ `{` $1, 16$ `}`

Finally, let $\mu(T)$ and $\mu(U)$ be the means of $T$ and $U$.

Is it possible to choose $T$ and $U$ such that $\mu(T)=\mu(U)$?

## The Code

The code in this repo lets you pick a set size, $n$ and a prime, $p$,
generates every possible $T$ and $U$, then for all non-intersecting pairs, asks whether any of their means are the same.

## The Approach for $p=2$

Consider sets of powers of two.

Each subset corresponds to a unique integer.
Every integer, $k$, can be written, base $2$, as a sum of powers of two.
Conversely, every subset of the set of powers of two corresponds to a unique integer.

Using the earlier example, $k_T=101010_2=42_{10}$, and $k_U=10001_2=17_{10}$
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

* For every $k < 2^n$, the binary representation:
* just $0$'s and $1$'s. Each represents a distinct subset.
* To find the set means divide by the number of 1-bits in the base-2 representation.
* Search for duplicated means. Collect all duplicates into lists of $k$ that have the same means.
* Search each such list for subsets that don't intersect.
* Report integer pairs that correspond to non-intersecting subsets with the same means.

## Other values of $p$

Every integer has a $base_p$, representation, but subsets of `{` $p^k$ `}` only have $0$ and $1$ in that representation.
Thus, for $p=5$, $101_5=26_{10}$ is the subset `{` $5^0, 5^2$ `}`, but $302_5=77_{10}$ corresponds to a collection of two $1$'s and three $25$'s.
This has duplicates, so it's a collection but not a subset.

Still, we can use *almost* the same steps.

* For every $k < 2^n$, generate the ***binary*** representation: just $0$'s and $1$'s.
* Treat each of these as a number with $0$'s and $1$'s base $p$. For example, $k=5 \rightarrow 101_2 \rightarrow 101_5 \rightarrow 26_{10}$.
(This step may feel a little odd.)
* To find the set means, once again divide by the number of 1-bits. Note that you can use the 1-bits *in the base-2 representation*.
In this case, $\mu($ `{` $1, 25$ `}`$)=26/2=13$
* Search for duplicated means. Collect all duplicates into lists of $k$ that have the same means.
* Search each such list for subsets that don't intersect by *and*-ing their ***binary*** representations.
(`a & b` *and*s together the binary representations of $a$ and $b$)
* Report integer pairs that correspond to non-intersecting subsets with the same means.

## A Partial Answer

For $p=2$, duplicates begin to appear at $n=14$ .
For odd primes, $p \gt 2$, I haven't yet found duplicates.

## Conjectures
* Finite, non-intersecting sets of powers of an odd prime, $p$, have different means.
