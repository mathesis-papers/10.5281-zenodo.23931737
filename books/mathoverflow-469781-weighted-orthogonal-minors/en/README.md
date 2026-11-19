# From coordinate areas to coordinate volumes

Give the coordinate projections of a parallelogram different prices. Add a perpendicular unit direction to make a parallelepiped. If each coordinate volume receives the highest price among its three coordinate areas, the total price of the squared volumes bounds the total price of the squared areas from above. Using the lowest price gives a lower bound. This is the inequality explained in this paper.

**Original paper:** Haobo Ma and Wenlin Zhang, *Proof of the weighted-minor inequality in MathOverflow 469781*, version 2, [version DOI: 10.5281/zenodo.23931738](https://doi.org/10.5281/zenodo.23931738). Haobo Ma: Chrono AI, Singapore; Wenlin Zhang: National University of Singapore and Chrono AI, Singapore.

## Start with squares and addition

In three dimensions take three mutually perpendicular unit vectors:

$$
x=(1,0,0),\qquad y=(0,3/5,4/5),
$$

$$
z=(0,-4/5,3/5).
$$

The vectors $x,y$ span a parallelogram of area one. Its oriented areas when projected onto the coordinate planes are

$$
p_{12}=3/5,\quad p_{13}=4/5,\quad p_{23}=0.
$$

The subscript $12$ means we keep only the first and second coordinates. In general $p_{ij}=x_i y_j-x_j y_i$, a two-by-two determinant, also called a minor. Reversing the coordinate order changes its sign, so the comparison uses squares. The squared projected areas add to $9/25+16/25=1$.

Give the three planes weights $a_{12}=2$, $a_{13}=5$, $a_{23}=1$. The weighted sum of squared areas is

$$
2\cdot\frac9{25}+5\cdot\frac{16}{25}
=\frac{98}{25}.
$$

After adjoining $z$, the volume is the determinant $q_{123}=1$. The comparison becomes

$$
1\le\frac{98}{25}\le5.
$$

This says that a weighted average with total mass one lies between the smallest and largest prices. This three-dimensional calculation already appears in the posing questions.

## Why do higher dimensions need an idea?

In $n$ dimensions every coordinate pair gives an area minor, and every coordinate triple gives a volume minor. We need not picture a four-dimensional solid: choose coordinates in small groups and compute familiar two-by-two and three-by-three determinants.

For example, in four dimensions take

$$
x=e_1,\qquad y=(e_2+e_3)/\sqrt2,\qquad z=e_4.
$$

Here $e_i$ has a one in coordinate $i$ and zeros elsewhere. Only $p_{12},p_{13}$ are nonzero, each with square $1/2$; only $q_{124},q_{134}$ are nonzero, again with squares $1/2$. Set

$$
(a_{12},a_{13},a_{14})=(1,3,2),
$$

$$
(a_{23},a_{24},a_{34})=(0,4,2).
$$

The area price is $(1+3)/2=2$. Triple $124$ contains edge prices $1,2,4$, while triple $134$ contains $3,2,2$. Thus

$$
\text{lower bound}=(1+2)/2=3/2,
$$

$$
\text{upper bound}=(4+3)/2=7/2.
$$

We get $3/2\le2\le7/2$. Edge $14$ belongs to both triples. In general there is much more overlap. We cannot arbitrarily match each area to a volume and add separate estimates. The proof must control any chosen collection of areas at once.

## Choose edges, then keep all triangles containing them

Think of coordinate labels as vertices, coordinate pairs as edges, and coordinate triples as triangles. Choose any edge family $F$. Let $N(F)$ contain every triangle with at least one chosen edge. The key comparison is

$$
\sum_{\{i,j\}\in F}p_{ij}^2
\le \sum_{\{i,j,k\}\in N(F)}q_{ijk}^2.
$$

Each edge and triangle is counted once. We do not repeatedly add an edge for each triangle containing it. In our four-dimensional example, $F=\{12\}$ receives nonzero volume mass only from $q_{124}$: both sides are $1/2$. For $F=\{12,13\}$ the nonzero volume squares add to one, and again there is equality.

Why does this work for every $F$? Package all the area coordinates into a vector $u$, and all the volume coordinates into another vector $b$. Adjoining a perpendicular unit vector $z$ preserves length. A reverse operation, called **contraction**, removes the $z$ direction, recovers $u$, and never increases length. Here length squared means the sum of all coordinate squares.

The crucial property is local dependence: recovering $p_{ij}$ uses only volume coordinates containing both $i$ and $j$. Over the real numbers,

$$
p_{ij}=\sum_k z_k q_{kij},
$$

where permuting indices changes $q$ according to the determinant sign rule. Discarding all volume coordinates outside $N(F)$ before contraction still recovers every area coordinate in $F$. Both contraction and discarding coordinates cannot increase length, giving the family comparison. The [complete proof](statements.md) explains why contraction cannot increase length.

## Build each price from layers

First suppose the weights are nonnegative. The prices $1,3,4$ can be built from three layers of thickness $1$, $2$, and $1$. A price-three edge reaches the first two layers; a price-four edge reaches all three.

At each level $t$, select all edges priced at least $t$. A triangle is retained exactly when at least one of its edges reaches $t$. Equivalently, **its largest edge price reaches $t$**. Apply the family comparison at each level, multiply by the layer thickness, and add. The left side reconstructs the original edge prices; the right side reconstructs each triangle’s maximum edge price.

This explains the maximum. It comes from the logic of “at least one selected edge,” rather than a mysterious determinant estimate. There are finitely many weight values, so the argument uses finite sums without integration or limits. Tied prices share a layer, and zero prices add no layer.

## Why can prices be negative?

Let $m$ be the smallest price. Subtract $m$ from every price to make them nonnegative. The essential fact is equal total mass:

$$
\sum_{i<j}p_{ij}^2
=\sum_{i<j<k}q_{ijk}^2=M.
$$

The change subtracts $mM$ from the area price. Every triangle maximum also decreases by $m$, so it subtracts exactly $mM$ from the volume price. Once the nonnegative comparison is proved, the identical terms cancel. Without equal mass, this cancellation would have no justification.

Finally negate every price. The maximum of the negative prices is minus the minimum of the original prices. Apply the upper bound to $-a$ and multiply by $-1$ to obtain the lower bound for $a$.

## What does the full result allow?

The real theorem requires just that $z$ be a unit vector perpendicular to both $x$ and $y$. The latter two need not be unit vectors, mutually perpendicular, or even linearly independent. If they are dependent, every minor vanishes and both sides are zero.

The complex version uses $|p|^2$, $|q|^2$ and Hermitian perpendicularity, which includes complex conjugation. Its contraction formula must be

$$
p_{ij}=\sum_k\overline{z_k}q_{kij}.
$$

The general version replaces areas by alternating coordinate data of degree $k$. Such data can be a sum of volume data rather than the exterior product of a single list of vectors. To adjoin $r$ mutually perpendicular unit directions successively, the initial data must lie in the exterior power of their **common perpendicular space**. Each final coordinate set of size $k+r$ uses the minimum or maximum over all its original-size subsets. Saying “add several directions” alone does not suffice: perpendicularity must remain available at every step.

Constant weights give equality. A nonzero exterior product of coordinate unit vectors with positive constant weights shows that the coefficient one in the upper bound cannot be uniformly reduced. The paper does not classify all equality cases for nonconstant weights.

## The question and the earlier mathematics

The user **meler** posed the question in April 2024 on [MathOverflow 469781](https://mathoverflow.net/q/469781) and [Mathematics Stack Exchange 4902019](https://math.stackexchange.com/q/4902019). The original question assumes a real orthonormal triple and a strictly positive symmetric weight matrix.

Russell Lyons’s 2003 comparison theorem for determinantal probability measures already implies the orthonormal case: interpret squared areas and volumes as probabilities and compare the event “contains a chosen edge.” Tomasz Miller and Rafał Bistroń’s 2025 direct proof gives both bounds for complex orthonormal triples and nonnegative weights. This paper explains a short contraction proof and its signed, weaker-hypothesis and exterior-degree extensions.

The linked discussion also concerns distances on complex projective space. Unit vectors differing by a single overall complex phase represent the same point. Given distances $d_{ij}$ between coordinate labels, one defines

$$
D_p([x],[y])=
\left(\sum_{i<j}d_{ij}^p|p_{ij}|^2\right)^{1/p}.
$$

Miller–Bistroń proved that every finite distance matrix gives a distance for $p\ge2$. This paper cites that full theorem, reproduces the small-angle obstruction for $p<2$, and proves the constant-distance case directly. The former conjecture is settled. The [technical chapter](statements.md) retains the angle choice and the full constant-distance argument.

## A focused explanation and further reading

The film follows the same route from projected areas through family comparison, price layers and cancellation for negative weights.

::: {.film src="001-minors-to-volumes"}
From areas to volumes: why the largest edge price controls the total. English narration with aligned Chinese and English subtitles.
:::

The seminar presentation adds precise hypotheses, complex conjugation and the dependency chain for repeated lifts.

::: {.slides src="seminar"}
Aligned Chinese and English academic slides, with speaker notes and a technical appendix.
:::

[Exact statements and complete proofs](statements.md) follow this story. [Sources and evidence scope](sources.md) gives original locators and direct Lean source links. The original real orthonormal, strictly positive comparison has a corresponding Lean theorem; the full signed, complex and arbitrary-degree results retain their individual written proofs. [Contribute to the mathematics and formalization](contributing.md) links the same shared requests.
