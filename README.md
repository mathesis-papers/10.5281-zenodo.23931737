# Proof of the weighted-minor inequality in MathOverflow 469781

**Authors:** Haobo Ma, Wenlin Zhang

We prove the displayed inequality in MathOverflow question 469781, which compares weighted squared two-by-two minors of an orthonormal pair with squared three-by-three minors, weighted by the largest edge weight of each triple. We prove the inequality by contraction in exterior algebra and a finite threshold decomposition. The proof gives both minimum and maximum bounds, permits signed weights and complex vectors, and extends to arbitrary exterior degrees and several orthogonal lifts. The orthonormal comparison follows from Lyons (2003); Miller and Bistroń (2025) give a direct two-sided proof and settle the linked distance-triangle conjecture.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.23931738](https://doi.org/10.5281/zenodo.23931738)
- Concept DOI: [https://doi.org/10.5281/zenodo.23931737](https://doi.org/10.5281/zenodo.23931737)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [mathoverflow-469781-weighted-orthogonal-minors](https://mathesis-omega-research.apps.chrono-ai.fun/papers/mathoverflow-469781-weighted-orthogonal-minors?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Proof of the weighted-minor inequality in MathOverflow 469781. Mathesis, version 2. https://doi.org/10.5281/zenodo.23931738

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/c55f6f7c7d7e3cf46b0a7da9efbba687448b29aa/D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.lean) | No public receipt |
| Lemma (s2) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/c55f6f7c7d7e3cf46b0a7da9efbba687448b29aa/D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.lean) | No public receipt |
| Corollary (s3) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/c55f6f7c7d7e3cf46b0a7da9efbba687448b29aa/D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.lean) | No public receipt |
| Corollary (s4) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/c55f6f7c7d7e3cf46b0a7da9efbba687448b29aa/D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.lean) | No public receipt |
| Corollary (s5) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/c55f6f7c7d7e3cf46b0a7da9efbba687448b29aa/D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.lean) | No public receipt |
| Corollary (s6) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/c55f6f7c7d7e3cf46b0a7da9efbba687448b29aa/D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.lean) | No public receipt |
| Corollary (s7) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/c55f6f7c7d7e3cf46b0a7da9efbba687448b29aa/D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/10.5281-zenodo.23931737/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/10.5281-zenodo.23931737/mathoverflow-469781-weighted-orthogonal-minors/zh/) · [Read in English](https://papers.trureturing.org/10.5281-zenodo.23931737/mathoverflow-469781-weighted-orthogonal-minors/en/)

[Slides](https://papers.trureturing.org/10.5281-zenodo.23931737/mathoverflow-469781-weighted-orthogonal-minors/slides/) ([sources](books/mathoverflow-469781-weighted-orthogonal-minors/slides/)) · [Videos](https://papers.trureturing.org/10.5281-zenodo.23931737/mathoverflow-469781-weighted-orthogonal-minors/films/) ([sources](books/mathoverflow-469781-weighted-orthogonal-minors/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/10.5281-zenodo.23931737/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `orthonormal-minors` | same | `D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.weighted_minors` |
| `signed-minors` | special case | `D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.weighted_minors` |
| `family-domination` | variant | `D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.weighted_minors` |
| `complex-minors` | special case | `D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.weighted_minors` |
| `two-sided` | special case | `D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.weighted_minors` |
| `repeated-lifts` | special case | `D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.weighted_minors` |
| `sharpness` | none | — |
| `exponent` | none | — |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/REVIEW.md).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/mathoverflow-469781-weighted-orthogonal-minors/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
