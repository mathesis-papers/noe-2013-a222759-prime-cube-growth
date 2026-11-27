# 精确陈述与证明

以下改写自 Haobo Ma 和 Wenlin Zhang 的[论文第 2 版](https://doi.org/10.5281/zenodo.24405795)。设 $n\ge1$ 为整数，$R_e(n,p)$ 是 $\binom{np}{p}$ 除以 $p^e$ 的最小非负余数，$\pi(x)$ 是不超过 $x$ 的素数个数，$p_j$ 是第 $j$ 个素数。

::: {.theorem #thm-exact status="written-proof" proof="pf-thm-exact" doi="10.5281/zenodo.24405795" source="Theorem 1, Section 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/580" mathesis="collected:noe-2013-a222759-prime-cube-growth:2:s1" title="立方模数下的例外素数"}
设 $W(n)=\{p\text{ 为素数}:R_3(n,p)\ne n\}$。它恰为以下三部分的不交并：所有 $p^3\le n$ 的素数；若 $n<8$ 且 $n\bmod4\in\{2,3\}$ 则加入 $2$；若 $n<27$ 且 $n\bmod3=2$ 则加入 $3$。因此 $a(n)=|W(n)|$ 有限，等于 $\pi(\lfloor n^{1/3}\rfloor)$ 加上后两个条件的示性数（成立记 $1$，否则记 $0$）。对 $n\ge27$，两项修正均为零。
:::

::: {.proof #pf-thm-exact}
若 $p^3\le n$，则 $R_3(n,p)<p^3\le n$。若 $p^3>n$ 且 $p\ge5$，下述同余式使得区间内的余数恰等于 $n$。对 $2$ 和 $3$，分别计算 $\binom{2n}{2}-n=2n(n-1)$ 和 $\binom{3n}{3}-n=9n^2(n-1)/2$。前者被 $8$ 整除当且仅当 $n\equiv0,1\pmod4$；后者被 $27$ 整除当且仅当 $n\equiv0,1\pmod3$。只需在各自立方以下补计，不会重复。见原文第 2 节。
:::

::: {.lemma #lem-glaisher status="written-proof" proof="pf-lem-glaisher" doi="10.5281/zenodo.24405795" source="Lemma 2, Section 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/581" mathesis="collected:noe-2013-a222759-prime-cube-growth:2:s2" title="Glaisher 的同余式"}
对任意正整数 $n$ 和素数 $p\ge5$，有 $\binom{np}{p}\equiv n\pmod{p^3}$，包括 $p\mid n$。这是 Glaisher（1900）的结果；见 [Straub，第 2 节](https://doi.org/10.46298/dmtcs.2962)。
:::

::: {.proof #pf-lem-glaisher}
在同余式中，$j=1,\ldots,p-1$ 可作分母，因为它们与 $p$ 互素。令 $H_r=\sum_{j=1}^{p-1}j^{-r}$。模 $p$ 取逆只是重排非零余数，所以 $H_2\equiv\sum_{j=1}^{p-1}j^2\equiv0\pmod p$，这里平方和公式的分母 $6$ 可逆。把 $j$ 与 $p-j$ 配对，得 $2H_1\equiv-pH_2\equiv0\pmod{p^2}$。令 $S_2=\sum_{1\le i<j\le p-1}(ij)^{-1}$，则 $2S_2=H_1^2-H_2\equiv0\pmod p$。展开 $n\prod_{j=1}^{p-1}(1-np/j)$：三次及更高项含 $p^3$，一次项与二次项因上述消去也含 $p^3$，只剩 $n$。这里没有除以 $n$。见原文第 2 节。
:::

::: {.corollary #cor-growth status="written-proof" proof="pf-cor-growth" doi="10.5281/zenodo.24405795" source="Corollary 3, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/582" mathesis="collected:noe-2013-a222759-prime-cube-growth:2:s3" title="准确的增长门槛"}
对整数 $k\ge3$ 和 $n\ge1$，$a(n)\ge k$ 当且仅当 $n\ge p_k^3$。特别地，Noe 较强的条件 $n\ge p_{p_k^3}$ 足以推出这一计数下界。
:::

::: {.proof #pf-cor-growth}
$n<27$ 时只有 $2$、$3$ 可能入选；$n\ge27$ 时恰好数到所有 $p^3\le n$ 的素数。因而第三个以及之后的门槛恰是 $p_k^3$。前 $m$ 个素数都在 $2,\ldots,p_m$ 中，故 $p_m\ge m+1$，于是嵌套素数门槛严格更大。见原文第 3 节。
:::

逐项代入修正条件还得到：$a(n)\ge1$ 当且仅当 $n\notin\{1,4\}$；$a(n)\ge2$ 当且仅当 $n\ge27$ 或 $n\in\{2,8,11,14,17,20,23,26\}$。

::: {.corollary #cor-companion status="written-proof" proof="pf-cor-companion" doi="10.5281/zenodo.24405795" source="Corollary 4, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/583" mathesis="collected:noe-2013-a222759-prime-cube-growth:2:s4" title="最小的后续无例外素数"}
对每个 $n\ge1$，[A222760](https://oeis.org/A222760) 的 $b(n)$ 存在，即第一个大于 $\max(W(n)\cup\{1\})$ 的素数。若 $n\ne5$，则 $b(n)=p_{a(n)+1}$；而 $b(5)=5$。若 $n\ge27$，则 $b(n)=p_{\pi(\lfloor n^{1/3}\rfloor)+1}$。
:::

::: {.proof #pf-cor-companion}
最后一个例外之后的素数都满足余数等于 $n$；从任何更早的素数出发都会遇到该例外。集合为空时，从 $2$ 开始就可以。$n\ge27$ 时例外集合是素数的初始区段；$8\le n<27$ 时是 $\{2\}$ 或 $\{2,3\}$。检验 $1\le n<8$ 的条件，唯一不是初始区段的情形是 $W(5)=\{3\}$。见原文第 3 节。$n=2$ 的特例是 Wolstenholme 同余式的一个应用。
:::

::: {.corollary #cor-lower status="written-proof" proof="pf-cor-lower" doi="10.5281/zenodo.24405795" source="Corollary 5, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/584" mathesis="collected:noe-2013-a222759-prime-cube-growth:2:s5" title="两个较小模数"}
对任意 $n\ge1$，使 $R_e(n,p)\ne n$ 的素数的个数，在 $e=1,2$ 时分别为 $\pi(n)$ 和 $\pi(\lfloor\sqrt n\rfloor)$。
:::

::: {.proof #pf-cor-lower}
对所有奇素数，上面的乘积模 $p$ 只剩 $n$；将 $j$ 与 $p-j$ 配对，得 $H_1\equiv0\pmod p$，所以模 $p^2$ 也只剩 $n$。对 $p=2$，$2n(n-1)$ 总被 $4$ 整除。两种情形的余数都在 $n<p^e$ 时等于 $n$，在 $n\ge p^e$ 时小于 $n$。见原文第 3 节及 Noe 的第二条评论所引的 [A000720](https://oeis.org/A000720) 与 [A056811](https://oeis.org/A056811)。
:::

::: {.corollary #cor-linked status="written-proof" proof="pf-cor-linked" doi="10.5281/zenodo.24405795" source="Corollary 6, Section 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/585" mathesis="collected:noe-2013-a222759-prime-cube-growth:2:s6" title="素数幂计数的几种形式"}
给定正整数 $e,n$，令 $c_e(n)=\pi(n^{1/e})$。它计数 $p^e\le n$ 的素数，也就是 $\operatorname{lcm}(1,\ldots,n)$ 中指数至少为 $e$ 的素因子。当 $e=2$ 时，它也计数不超过 $n$ 且恰有三个正因子的整数，并等于不超过 $n$ 的两两互素合数集合的最大大小。

当 $j\ge1$ 时，$c_e(n)=j$ 当且仅当 $p_j^e\le n<p_{j+1}^e$；$j=0$ 的区间是 $1\le n<2^e$。作为形式幂级数，

$$
\sum_{n\ge1}c_e(n)x^n=\frac{\sum_{p\text{ 为素数}}x^{p^e}}{1-x}.
$$

$a(n)$ 的级数由 $e=3$ 的右式加上 $x^2+x^3+x^6+x^7+x^2\sum_{j=0}^{8}x^{3j}$ 得到。固定 $e$ 时，$c_e(n)\sim e n^{1/e}/\log n$，特别地 $a(n)\sim 3n^{1/3}/\log n$，其中 $\sim$ 表示比值趋于 $1$。
:::

::: {.proof #pf-cor-linked}
最小公倍数中 $p$ 的指数是满足 $p^r\le n$ 的最大 $r$。恰有三个因子的数正是素数平方。每个不超过 $n$ 的合数有一个不超过 $\sqrt n$ 的素因子；两两互素要求选出的因子互不相同，而取所有这些素数的平方就能达到上界。计数区间由相邻素数幂给出。每个素数幂 $p^e$ 从 $x^{p^e}$ 开始给后续每一项贡献 $1$，即 $x^{p^e}/(1-x)$，每个系数仅涉及有限个素数。立方计数多出的项来自两个有限修正。最后将 $t=n^{1/e}$ 代入素数定理 $\pi(t)\sim t/\log t$；$a(n)$ 在 $n\ge27$ 时等于 $c_3(n)$。见原文第 4 节对 [A056811](https://oeis.org/A056811) 和 [A000720](https://oeis.org/A000720) 各项解释的署名与出处。
:::

## Lean 证明的范围

[已有的 Lean 证明](https://github.com/the-omega-institute/trureturing/blob/3d781ae04219d5c99e87e82e3bbc3f6816e3691e/D5/S3/Arith/PrimeRemainders/OeisA222759Growth.lean#L25) 对 $k\ge3$、$n\ge1$ 和 $n\ge p_{p_k^3}$ 给出 $k$ 个不同的例外素数。它没有断言例外集合有限、没有把门槛降到 $p_k^3$，也没有证明逆向。以上较完整的结果来自原论文的书面证明；[准确门槛的形式化任务](https://github.com/the-omega-institute/trureturing-requests/issues/582)列明了尚待检查的陈述。
