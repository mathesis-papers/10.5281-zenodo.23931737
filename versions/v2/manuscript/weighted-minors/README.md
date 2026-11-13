# Proof of the weighted-minor inequality in MathOverflow 469781

The note proves the displayed inequality in [MathOverflow 469781](https://mathoverflow.net/q/469781) and the identical question in [Mathematics Stack Exchange 4902019](https://math.stackexchange.com/q/4902019). Its contraction proof gives lower bounds with triple minima as well as upper bounds with triple maxima, arbitrary real weights, complex vectors, and arbitrary horizontal exterior forms under one or several orthogonal lifts. Constant weights give equality.

The orthonormal comparison follows from Russell Lyons's 2003 stochastic-domination theorem. A direct two-sided complex proof appears in [Miller and Bistroń, arXiv:2509.14727v1](https://arxiv.org/abs/2509.14727v1), Lemma 10, equation (27), first posted on 18 September 2025. Their Theorem 2 proves the broader distance-triangle conjecture linked in the posing thread, including every finite metric and all exponents p >= 2. In the [4 October 2026 revision](https://arxiv.org/abs/2509.14727v4), the corresponding locators are Lemma 13, equation (34), and Theorem 1. The note distinguishes these cited results from its self-contained exterior-algebra proofs.

## Contents

- `note.tex`: self-contained statements, proofs, source-item coverage, and references.
- `note.pdf`: readable mathematical note.
- `metadata.json`: title, creators, license, problem identifier, and scientific evidence links.
- `verify.py`: standard-library Python rational and Gaussian-rational finite checks.
- `verification.json`: deterministic output from `verify.py`.

## Build

Use Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, compile twice with `pdflatex note.tex`. The bibliography is embedded in the LaTeX source; BibTeX and additional data files are unnecessary.

Reproduce the finite checks with Python 3.10 or later:

```sh
python3 verify.py > verification.json
```

The pair-minor checks construct 32 rational orthonormal or perpendicular-pair examples in dimensions 3 through 6: 270,912 exhaustive pair-family comparisons, 3,200 signed-weight comparisons and threshold identities, and 32 exterior-energy identities.

The exterior-degree checks use 36 additional examples with (dimension, degree, number of lifts) equal to (4,1,1), (5,2,1), (6,2,2), (6,3,1), (6,3,2), and (6,1,3). Eighteen have nonreal Gaussian-rational coordinates, and twelve two-forms are certified nondecomposable by a nonzero exterior square. They check Hermitian orthonormality, horizontal contraction, recovery, equal mass, 11,598 subset-family inequalities and 2,304 two-sided signed-weight comparisons. Family enumeration is exhaustive in the 18 cases having at most ten source subsets; the other cases use the deterministic families specified in the script. These are finite consistency checks; the universal claims are proved in the note.

## Mathematical coverage

The declaration `AlternatingArrayContraction.weighted_minors` in the [pinned Lean file](https://github.com/the-omega-institute/trureturing/blob/c55f6f7c7d7e3cf46b0a7da9efbba687448b29aa/D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.lean) is the original real orthonormal-triple inequality for strictly positive symmetric weights. The note supplies written proofs for the weaker vector hypotheses, arbitrary real weights, complex vectors, both minimum and maximum bounds, and all exterior degrees with repeated orthogonal lifts. The broader distance triangle inequality from Conjecture 2.1 of arXiv:2312.02583v1 has the cited full proof of Miller and Bistroń, rather than a proof from the single-minor comparison alone.

Corollary 7 also gives the short obstruction for every exponent 0 < p < 2 and proves the constant-distance case for all p >= 2. The checker includes the exact p = 1 counterexample with long side 576/625 and sum of the other sides 18/25.

## Creators and license

Haobo Ma — ChronoAI Pte Ltd, Singapore.

Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore.

CC BY 4.0 (`cc-by-4.0`).
