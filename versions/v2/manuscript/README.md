# Exact counts and sharp growth for OEIS A222759, first comment (12 March 2013): extending Glaisher (1900)

Haobo Ma (ChronoAI Pte Ltd, Singapore) and Wenlin Zhang (National University of Singapore; ChronoAI Pte Ltd, Singapore). November 6, 2026. Revision 2. CC BY 4.0.

For every positive integer `n`, the bad primes for the literal remainder `binomial(n*p,p) mod p^3 != n` are exactly the primes with `p^3 <= n`, together with `2` when `n < 8` and `n mod 4` is `2` or `3`, and `3` when `n < 27` and `n mod 3` is `2`. The note proves the exact count, the sharp threshold `n >= p_k^3` for every `k >= 3`, and the corresponding least eventual good prime.

## Build

The source is self-contained LaTeX with an embedded bibliography. Use Tectonic 0.17.0:

```sh
tectonic --untrusted note.tex
```

Alternatively, use a standard TeX installation with the AMS, Latin Modern, geometry, booktabs and hyperref packages:

```sh
pdflatex -no-shell-escape note.tex
pdflatex -no-shell-escape note.tex
```

BibTeX is unnecessary because the bibliography is embedded.

## Reproduce the finite integer checks

Python 3.8 or later and its standard library suffice:

```sh
python3 verify.py --output verification.json
```

This downloads the public tables from [A222759](https://oeis.org/A222759/b222759.txt) and [A222760](https://oeis.org/A222760/b222760.txt). Their exact content hashes appear in `verification.json`. For offline use, download those two files into a directory and pass `--oeis-directory DIRECTORY`. Running the program again replaces the selected output file.

The program compares exact binomial remainders for `1 <= n <= 512`, all 25 primes at most 97, and exponents 1, 2 and 3 (38,400 comparisons); it also checks all 8,700 binomials in the original Mathematica range (`1 <= n <= 87`, first 100 primes), both published 10,000-term tables, and six sharp-threshold boundaries. Further checks cover both small count levels and the companion relation through 10,000; generating-function coefficients, least-common-multiple exponents and three-divisor counts through 512; the maximum pairwise-coprime composite collection through 64 by exhaustive dynamic programming; and the factorial and partition interpretations through 128. Expected overall output: `"status": "pass"`.

## Mathematical coverage

- `note.tex` contains complete written proofs of the exact witness set, counts, sharp threshold, companion formula, smaller-modulus counts, elementary linked interpretations and generating functions; the asymptotics invoke the classical prime number theorem.
- The declaration `D5.S3.Arith.PrimeRemainders.OeisA222759Growth.result` in the [pinned Lean file](https://github.com/the-omega-institute/trureturing/blob/3d781ae04219d5c99e87e82e3bbc3f6816e3691e/D5/S3/Arith/PrimeRemainders/OeisA222759Growth.lean) proves the original sufficient threshold with `k` distinct prime witnesses. The source's `P(j)` is the one-based prime enumeration for positive `j`.
- `verification.json` describes the finite integer comparisons. General finiteness and the exact count follow from the written congruence argument, not from a finite prime cutoff.
- For exponents at least 4, the uniform congruence is not asserted in the source; it fails for `(n,p)=(2,5)`. The note does not classify the number of bad primes for those exponents.

The exact companion relation is `b(n)=p_(a(n)+1)` except at `n=5`, where `b(5)=5`. Its `n=2` congruence is Wolstenholme's (1862), also recorded in [MathWorld, equation (6)](https://mathworld.wolfram.com/CentralBinomialCoefficient.html) with attribution to Noe (2005). The complete formula extends this special case.

The classical congruence is credited to Glaisher (1900), following Straub, *A q-analog of Ljunggren's binomial congruence*, DMTCS Proceedings AO (2011), 897–902, [doi:10.46298/dmtcs.2962](https://doi.org/10.46298/dmtcs.2962), Section 2. The application distinguishes literal remainders from congruence and supplies the exceptional primes.

## License

The note, metadata and verification program are licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). The public OEIS pages and tables retain their own stated terms.
