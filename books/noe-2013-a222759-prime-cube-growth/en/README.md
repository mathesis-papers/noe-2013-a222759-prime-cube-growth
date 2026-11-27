# Exact counts and sharp growth for OEIS A222759, first comment (12 March 2013): extending Glaisher (1900)

*Source paper: Haobo Ma and Wenlin Zhang, [version 2](https://doi.org/10.5281/zenodo.24405795), CC BY 4.0. The question comes from T. D. Noe's first comment on [OEIS A222759](https://oeis.org/A222759), dated March 12, 2013.*

## How large can a remainder be?

Fix a positive integer $n$. For each prime $p$, there are $\binom{np}{p}$ ways to choose $p$ objects from $np$ objects. Divide that number by $p^3$ and take the least nonnegative remainder, $R_3(n,p)$. Call $p$ an exception if that remainder **is not the integer $n$ itself**. Write $W(n)$ for the set of exception primes and $a(n)$ for its size.

Take $n=8$ and $p=2$. The coefficient $\binom{16}{2}=120$ has remainder $0$ upon division by $8$. Even though $0$ and $8$ are congruent modulo $8$, the remainder is not $8$. In fact, there is no need to compute the coefficient: the remainder is always between $0$ and $p^3-1$. If $p^3\le n$, then $p$ must be counted, including at equality.

If $p^3>n$, then $n$ fits in the remainder range, but that alone does not make it the remainder. For $p\ge5$, [Glaisher's congruence](results.md#lem-glaisher) supplies the missing fact: $\binom{np}{p}-n$ is divisible by $p^3$. So the remainder really is $n$. Two primes need their own calculations. Below $8$, count $2$ as an extra exception when $n$ leaves remainder $2$ or $3$ upon division by $4$. Below $27$, count $3$ as an extra exception when $n$ leaves remainder $2$ upon division by $3$.

## Count the steps instead of computing the coefficients

From $27$ onward both extra conditions disappear. Counting exception primes is then the same as counting prime cubes at most $n$.

| $n$ | $W(n)$ | $a(n)$ |
|---:|:---|---:|
| $5$ | $\{3\}$ | $1$ |
| $8$ | $\{2,3\}$ | $2$ |
| $9$ | $\{2\}$ | $1$ |
| $124$ | $\{2,3\}$ | $2$ |
| $125$ | $\{2,3,5\}$ | $3$ |
| $343$ | $\{2,3,5,7\}$ | $4$ |

The early drop from $8$ to $9$ shows why this is not always an increasing count. But the third exception first appears at the cube of the third prime, $5$. After that, each new prime cube adds one to the count. Write $p_k$ for the $k$-th prime, starting at $p_1=2$. For $k\ge3$, there are at least $k$ exceptions **exactly when** $n\ge p_k^3$. Noe's condition was $n\ge p_{p_k^3}$: take the cube, then use it as an index in the prime list. For $k=3$ the older sufficient threshold is $691$; the first value that actually works is $125$.

## How many is not the same as how far

[OEIS A222760](https://oeis.org/A222760) asks for the least prime from which that prime and every later prime are free of exceptions. This depends on the **last** exception, not just how many there are. At $n=5$, the only exception is $3$. Although $2$ itself is good, starting at $2$ still leaves $3$ ahead, so the answer is $5$. For every other input the exceptions are an initial segment of the primes (possibly empty), so the answer is the $(a(n)+1)$-st prime.

::: {.film src="010-remainder-range"}
Follow the remainder range to the first appearance of a third exception.
:::

The remainder-range argument also works modulo $p$ and $p^2$; in those cases even $2$ and $3$ need no extra corrections. Do not extrapolate the congruence to higher powers: $\binom{10}{5}=252$ has remainder $252$, not $2$, modulo $5^e$ for every $e\ge4$. This counterexample defeats a uniform congruence, but does not count the exceptions at higher powers.

[Exact statements and proofs](results.md) give the formulas, thresholds, and the scope of the existing Lean proof.
