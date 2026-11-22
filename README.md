# Exact counts and sharp growth for OEIS A222759, first comment (12 March 2013): extending Glaisher (1900)

**Authors:** Haobo Ma, Wenlin Zhang

Extending Glaisher's (1900) congruence to exact literal-remainder counts, we determine OEIS A222759 and prove Noe's growth assertion in its first comment (12 March 2013; revision 12, 2 November 2024). For every positive integer n, its conjectured count equals pi(floor(n^(1/3))) plus two explicit corrections supported below 27. Consequently, for every k >= 3, the count is at least k exactly when n >= p_k^3, sharpening the stated sufficient threshold p_(p_k^3). The same description determines A222760, including its exceptional relation to A222759 at n=5. We give a self-contained proof, the counts modulo p and p^2, and elementary consequences for the linked prime-counting entries.

- PDF: [frozen public file](paper.pdf)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [noe-2013-a222759-prime-cube-growth](https://mathesis-omega-research.apps.chrono-ai.fun/papers/noe-2013-a222759-prime-cube-growth?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Exact counts and sharp growth for OEIS A222759, first comment (12 March 2013): extending Glaisher (1900). Mathesis, version 2. https://mathesis-omega-research.apps.chrono-ai.fun/papers/noe-2013-a222759-prime-cube-growth?version=2

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3d781ae04219d5c99e87e82e3bbc3f6816e3691e/D5/S3/Arith/PrimeRemainders/OeisA222759Growth.lean) | No public receipt |
| Lemma (s2) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3d781ae04219d5c99e87e82e3bbc3f6816e3691e/D5/S3/Arith/PrimeRemainders/OeisA222759Growth.lean) | No public receipt |
| Corollary (s3) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3d781ae04219d5c99e87e82e3bbc3f6816e3691e/D5/S3/Arith/PrimeRemainders/OeisA222759Growth.lean) | No public receipt |
| Corollary (s4) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3d781ae04219d5c99e87e82e3bbc3f6816e3691e/D5/S3/Arith/PrimeRemainders/OeisA222759Growth.lean) | No public receipt |
| Corollary (s5) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3d781ae04219d5c99e87e82e3bbc3f6816e3691e/D5/S3/Arith/PrimeRemainders/OeisA222759Growth.lean) | No public receipt |
| Corollary (s6) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3d781ae04219d5c99e87e82e3bbc3f6816e3691e/D5/S3/Arith/PrimeRemainders/OeisA222759Growth.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).
