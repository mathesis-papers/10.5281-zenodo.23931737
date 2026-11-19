# Sources and evidence scope

The [original paper, version 2](https://doi.org/10.5281/zenodo.23931738), is by Haobo Ma (Chrono AI, Singapore) and Wenlin Zhang (National University of Singapore and Chrono AI, Singapore), under CC BY 4.0. The version DOI identifies this exact paper; the concept DOI groups its versions. This explanation, presentation and film teach the same paper.

## What the Lean statement says

The public [`weighted_minors` source](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.lean#L593) states the original real orthonormal-triple upper bound for a symmetric matrix with strictly positive entries, including its diagonal. It uses the literal determinants and sums only over increasing indices. The source allows any natural dimension; an orthonormal triple can exist only for dimensions at least three.

The [paper’s cited source revision](https://github.com/the-omega-institute/trureturing/blob/c55f6f7c7d7e3cf46b0a7da9efbba687448b29aa/D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.lean#L593) and the [book’s source revision](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.lean#L593) have identical module bytes. Both corresponding frozen-state records contain the public theorem. The formal definitions of ordered pair/triple mass divide by two/six; the final theorem converts those to increasing-index sums. This accounts for the apparent difference in summation conventions.

There is also an existing [private family-domination proof](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.lean#L303) under the weaker real vector hypotheses. Its frozen private declaration records checked proof content; it is not a reusable public result citation in this book. The family handoff requests that public interface and its unordered-subset bridge. The full signed theorem, Hermitian extension, signed two-sided comparison, arbitrary-degree repeated lifts, general equality/sharpness statement and distance exponent are given with their complete written proofs in the [technical chapter](statements.md). Their scope is not certified by the narrower public theorem.

The manuscript reports finite exact rational and Gaussian-rational examples. They illustrate cases, rather than prove all-parameter statements. The mathematical arguments here use no such computation and no limiting passage.

## Original-source locators

| Result in this explanation | Original manuscript location |
| --- | --- |
| Signed upper comparison and its orthonormal specialization | Theorem 1, Sections 1 and 3 |
| Coordinate-family comparison | Lemma 2, Section 2 |
| Hermitian complex comparison | Corollary 3, Section 3 |
| Signed two-sided comparison | Corollary 4, Section 3 |
| Arbitrary degree and repeated orthogonal lifts | Corollary 5, Section 4 |
| Constant weights, sharp coefficient, dimension three | Corollary 6, Section 4 |
| Distance exponent and constant-distance case | Corollary 7, Section 5 |

## References and the role of earlier work

- Haobo Ma and Wenlin Zhang, *Proof of the weighted-minor inequality in MathOverflow 469781*, version 2. [10.5281/zenodo.23931738](https://doi.org/10.5281/zenodo.23931738). The concept DOI is [10.5281/zenodo.23931737](https://doi.org/10.5281/zenodo.23931737).
- meler, *Inequality involving minors of an orthogonal matrix*, [MathOverflow 469781](https://mathoverflow.net/q/469781), 23 April 2024; *Inequality involving a symmetric matrix and minors of an orthogonal matrix*, [Mathematics Stack Exchange 4902019](https://math.stackexchange.com/q/4902019), 19 April 2024.
- Russell Lyons, *Determinantal probability measures*, Publications Mathématiques de l’IHÉS **98** (2003), 167–212. [10.1007/s10240-003-0016-0](https://doi.org/10.1007/s10240-003-0016-0), Theorem 6.2, p. 183: nested projection determinantal measures are stochastically ordered. Applied to the increasing event of containing a pair from $F$, this gives the orthonormal family comparison.
- Rafał Bistroń, Michał Eckstein, Shmuel Friedland, Tomasz Miller and Karol Życzkowski, *A new class of distances on complex projective spaces*, [arXiv:2312.02583v1](https://arxiv.org/abs/2312.02583v1) (2023), Conjecture 2.1. Published in Linear Algebra and its Applications **721** (2025), 577–611, [10.1016/j.laa.2024.10.017](https://doi.org/10.1016/j.laa.2024.10.017).
- Tomasz Miller and Rafał Bistroń, *Distances between pure quantum states induced by a distance matrix*, [arXiv:2509.14727v1](https://arxiv.org/abs/2509.14727v1), 18 September 2025: Lemma 10, equation (27), gives the complex orthonormal nonnegative two-sided comparison; Theorem 2 proves the full distance theorem; Remark 4 supplies the $p<2$ obstruction. The corresponding locators in [v4](https://arxiv.org/abs/2509.14727v4), 4 October 2026, are Lemma 13, equation (34), Theorem 1, and Remark 4.

The short contraction proof is the subject of this explanation. The original orthonormal inequality and the linked distance theorem receive the prior-work credit stated above. The shared requests in the [contribution guide](contributing.md) coordinate formalization of precise scopes; they are not new mathematical conjectures.
