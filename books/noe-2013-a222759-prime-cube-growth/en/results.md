# Exact statements and proofs

The statements and arguments below are adapted from Haobo Ma and Wenlin Zhang's [version 2](https://doi.org/10.5281/zenodo.24405795). Throughout, $n\ge1$ is an integer, $R_e(n,p)$ is the least nonnegative remainder of $\binom{np}{p}$ modulo $p^e$, $\pi(x)$ counts primes at most $x$, and $p_j$ is the $j$-th prime.

::: {.theorem #thm-exact status="written-proof" proof="pf-thm-exact" doi="10.5281/zenodo.24405795" source="Theorem 1, Section 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/580" mathesis="collected:noe-2013-a222759-prime-cube-growth:2:s1" title="Exact cubic exception set"}
Let $W(n)=\{p\text{ prime}:R_3(n,p)\ne n\}$. This is the disjoint union of the primes with $p^3\le n$, the singleton $\{2\}$ if $n<8$ and $n\bmod4\in\{2,3\}$, and the singleton $\{3\}$ if $n<27$ and $n\bmod3=2$. A singleton is omitted when its condition fails. Thus $a(n)=|W(n)|$ is finite and equals $\pi(\lfloor n^{1/3}\rfloor)$ plus the two indicators (one if the condition holds, zero otherwise). Both corrections vanish when $n\ge27$.
:::

::: {.proof #pf-thm-exact}
If $p^3\le n$, then $R_3(n,p)<p^3\le n$. If $p^3>n$ and $p\ge5$, the congruence below makes $n$ the remainder in the allowed range. For $2$ and $3$ the differences are $\binom{2n}{2}-n=2n(n-1)$ and $\binom{3n}{3}-n=9n^2(n-1)/2$. Divisibility by $8$ in the first case is equivalent to $n\equiv0,1\pmod4$; divisibility by $27$ in the second is equivalent to $n\equiv0,1\pmod3$. The extra exceptions occur only below the respective cubes, so none is counted twice. See Section 2 of the paper.
:::

::: {.lemma #lem-glaisher status="written-proof" proof="pf-lem-glaisher" doi="10.5281/zenodo.24405795" source="Lemma 2, Section 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/581" mathesis="collected:noe-2013-a222759-prime-cube-growth:2:s2" title="Glaisher's congruence"}
For every positive integer $n$ and prime $p\ge5$, $\binom{np}{p}\equiv n\pmod{p^3}$, including when $p\mid n$. This is Glaisher's 1900 result; see [Straub, Section 2](https://doi.org/10.46298/dmtcs.2962).
:::

::: {.proof #pf-lem-glaisher}
All the denominators $j=1,\ldots,p-1$ are invertible modulo powers of $p$. Set $H_r=\sum_{j=1}^{p-1} j^{-r}$. Inversion permutes the nonzero residues modulo $p$, so $H_2\equiv\sum_{j=1}^{p-1}j^2\equiv0\pmod p$ by the sum of squares formula (its denominator $6$ is invertible). Pairing $j$ with $p-j$ gives $2H_1\equiv-pH_2\equiv0\pmod{p^2}$. With $S_2=\sum_{1\le i<j\le p-1}(ij)^{-1}$ we have $2S_2=H_1^2-H_2\equiv0\pmod p$. In the expansion of $n\prod_{j=1}^{p-1}(1-np/j)$, terms of degree three and higher in $np$ vanish modulo $p^3$, and the linear and quadratic terms vanish by the two cancellations. Only $n$ remains. No division by $n$ is needed. See Section 2.
:::

::: {.corollary #cor-growth status="written-proof" proof="pf-cor-growth" doi="10.5281/zenodo.24405795" source="Corollary 3, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/582" mathesis="collected:noe-2013-a222759-prime-cube-growth:2:s3" title="Sharp growth threshold"}
For integers $k\ge3$ and $n\ge1$, $a(n)\ge k$ if and only if $n\ge p_k^3$. In particular, Noe's stronger hypothesis $n\ge p_{p_k^3}$ implies the count bound.
:::

::: {.proof #pf-cor-growth}
Below $27$ only $2$ and $3$ can be exceptions. From $27$ onward the exceptions are exactly the primes whose cubes have been reached. The $k$-th such event is $p_k^3$ for $k\ge3$. The first $m$ primes lie among $2,\ldots,p_m$, so $p_m\ge m+1$, and the nested-prime threshold is strictly larger. See Section 3.
:::

Substituting into the correction terms also gives the two small count levels: $a(n)\ge1$ iff $n\notin\{1,4\}$; $a(n)\ge2$ iff $n\ge27$ or $n\in\{2,8,11,14,17,20,23,26\}$.

::: {.corollary #cor-companion status="written-proof" proof="pf-cor-companion" doi="10.5281/zenodo.24405795" source="Corollary 4, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/583" mathesis="collected:noe-2013-a222759-prime-cube-growth:2:s4" title="Least eventual good prime"}
For every $n\ge1$, the [A222760](https://oeis.org/A222760) value $b(n)$ exists and is the first prime greater than $\max(W(n)\cup\{1\})$. For $n\ne5$ it is $p_{a(n)+1}$, but $b(5)=5$. When $n\ge27$, it is $p_{\pi(\lfloor n^{1/3}\rfloor)+1}$.
:::

::: {.proof #pf-cor-companion}
Every prime after the last exception is good, whereas starting at or before the last exception still encounters it. If the set is empty, start at $2$. At $n\ge27$ the witnesses are an initial segment of the primes. For $8\le n<27$ they are $\{2\}$ or $\{2,3\}$. Applying the two tests for $1\le n<8$ leaves $W(5)=\{3\}$ as the sole non-initial segment. See Section 3. The case $n=2$ uses the classical Wolstenholme congruence.
:::

::: {.corollary #cor-lower status="written-proof" proof="pf-cor-lower" doi="10.5281/zenodo.24405795" source="Corollary 5, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/584" mathesis="collected:noe-2013-a222759-prime-cube-growth:2:s5" title="The two smaller moduli"}
For $n\ge1$ the number of primes with $R_e(n,p)\ne n$ is $\pi(n)$ for $e=1$ and $\pi(\lfloor\sqrt n\rfloor)$ for $e=2$.
:::

::: {.proof #pf-cor-lower}
For every odd prime the product above reduces to $n$ modulo $p$. Pairing $j$ and $p-j$ gives $H_1\equiv0\pmod p$, so the product also reduces to $n$ modulo $p^2$. For $p=2$, $2n(n-1)$ is divisible by $4$. In either case the remainder equals $n$ when $n<p^e$ and is smaller than $n$ when $n\ge p^e$. See Section 3 and the second Noe comment's links to [A000720](https://oeis.org/A000720) and [A056811](https://oeis.org/A056811).
:::

::: {.corollary #cor-linked status="written-proof" proof="pf-cor-linked" doi="10.5281/zenodo.24405795" source="Corollary 6, Section 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/585" mathesis="collected:noe-2013-a222759-prime-cube-growth:2:s6" title="Prime-power counting in different forms"}
For positive integers $e,n$, set $c_e(n)=\pi(n^{1/e})$. It counts primes with $p^e\le n$, or primes with exponent at least $e$ in $\operatorname{lcm}(1,\ldots,n)$. For $e=2$ it also counts integers at most $n$ with exactly three positive divisors and gives the maximum size of a pairwise coprime collection of composite integers at most $n$.

For $j\ge1$, $c_e(n)=j$ exactly when $p_j^e\le n<p_{j+1}^e$; the zero interval is $1\le n<2^e$. As formal power series,

$$
\sum_{n\ge1}c_e(n)x^n=\frac{\sum_{p\text{ prime}}x^{p^e}}{1-x}.
$$

The series for $a(n)$ is the right side for $e=3$ plus $x^2+x^3+x^6+x^7+x^2\sum_{j=0}^8x^{3j}$. For fixed $e$, $c_e(n)\sim e n^{1/e}/\log n$, and in particular $a(n)\sim 3n^{1/3}/\log n$, where $\sim$ means the ratio tends to $1$.
:::

::: {.proof #pf-cor-linked}
The prime exponent in the least common multiple is the largest $r$ with $p^r\le n$. Exactly the prime squares have three divisors. Every composite at most $n$ has a prime factor at most $\sqrt n$; pairwise coprimality makes these chosen primes distinct, and the prime squares attain the resulting bound. Consecutive prime powers give the intervals. Each prime power $p^e$ contributes one to every coefficient starting at $x^{p^e}$, hence $x^{p^e}/(1-x)$; only finitely many primes contribute to any given coefficient. The two finite corrections give the extra cubic terms. Finally, substitute $t=n^{1/e}$ in the prime number theorem $\pi(t)\sim t/\log t$ and use $a(n)=c_3(n)$ for $n\ge27$. See Section 4 for the original credits for interpretations of [A056811](https://oeis.org/A056811) and [A000720](https://oeis.org/A000720).
:::

## What the Lean proof establishes

The [existing Lean proof](https://github.com/the-omega-institute/trureturing/blob/3d781ae04219d5c99e87e82e3bbc3f6816e3691e/D5/S3/Arith/PrimeRemainders/OeisA222759Growth.lean#L25) gives $k$ distinct prime exceptions for $k\ge3$, $n\ge1$, and $n\ge p_{p_k^3}$. It does not show finiteness of the full set, lower the hypothesis to $p_k^3$, or prove the converse. The fuller results above have written proofs in the paper. The [sharp-threshold formalization request](https://github.com/the-omega-institute/trureturing-requests/issues/582) describes the remaining statement without re-requesting the original implication.
