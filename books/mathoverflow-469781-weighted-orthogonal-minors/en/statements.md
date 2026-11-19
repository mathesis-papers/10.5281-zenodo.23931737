# Exact statements and complete proofs

The dependency chain is: contraction and equal mass in exterior powers → comparison for arbitrary coordinate families → finite layers for nonnegative weights → equal-mass cancellation for signed weights → negation for the lower bound → complex scalars and arbitrary degree → repeated lifts → equality, sharpness and the distance exponent. Source locators refer to the original manuscript, not this explanation’s chapter numbering.

## Notation and the contraction facts

Let $\mathbb K=\mathbb R$ or $\mathbb C$ and $[n]=\{1,\ldots,n\}$. The exterior power $\Lambda^k\mathbb K^n$ has the orthonormal basis $e_S=e_{i_1}\wedge\cdots\wedge e_{i_k}$ with $i_1<\cdots<i_k$. Exchanging two factors changes the sign; repeated factors give zero. A general element $u=\sum_{|S|=k}u_S e_S$ can be a sum of exterior products and need not be one exterior product. Set

$$
\|u\|^2=\sum_{|S|=k}|u_S|^2.
$$

Over $\mathbb C$ the inner product is conjugate-linear in its first variable, so $\langle z,x\rangle=\sum_i\overline{z_i}x_i$. Omit conjugation over $\mathbb R$.

Fix a unit vector $z$. In an orthonormal basis starting with $z$, every degree-$\ell$ form has a unique decomposition

$$
b=z\wedge c+d,
$$

$$
c\in\Lambda^{\ell-1}(z^\perp),\qquad
 d\in\Lambda^\ell(z^\perp).
$$

The two terms use disjoint orthonormal basis elements. Define $L_z(v)=z\wedge v$ and contraction $\iota_z=L_z^*$. On basis elements without $z$, exterior multiplication adds the unit factor $z$; on those already containing $z$, it gives zero. The adjoint therefore sends $z\wedge c$ to $c$ and $d$ to zero. Consequently

$$
\iota_z b=c,\qquad
\|\iota_zb\|\le\|b\|.
$$

If $u\in\Lambda^k(z^\perp)$ and $b=z\wedge u$, then

$$
\iota_zb=u,\qquad \|b\|^2=\|u\|^2. \tag{A}
$$

This holds in every exterior degree without decomposability. For $T=\{i_1<\cdots<i_\ell\}$, taking the conjugate transpose of the coordinate matrix of $L_z$ gives the basis formula

$$
\iota_z e_T=\sum_{j=1}^{\ell}(-1)^{j-1}
\overline{z_{i_j}}e_{T\setminus\{i_j\}}.
$$

Thus contraction at a coordinate reads only higher-degree coordinates containing it.

If $u=x\wedge y$ with $x,y\perp z$, its coordinates are

$$
p_{ij}=x_i y_j-x_j y_i,
$$

$$
q_{ijk}=\det\begin{pmatrix}
x_i&x_j&x_k\\y_i&y_j&y_k\\z_i&z_j&z_k
\end{pmatrix}.
$$

Moving $z$ past two factors preserves sign: $z\wedge x\wedge y=x\wedge y\wedge z$. Thus $b$ has triple coordinates $q$. Extend $q$ by alternation. The coordinate and mass forms of (A) are

$$
\sum_h\overline{z_h}q_{hij}=p_{ij},
$$

$$
\sum_{i<j}|p_{ij}|^2
=\sum_{i<j<k}|q_{ijk}|^2=M. \tag{B}
$$

Each set is counted once in increasing order; there are no extra factors of two or six.

## Local dependence controls every coordinate family

::: {.lemma #family-domination title="Coordinate-family comparison" mathesis="collected:mathoverflow-469781-weighted-orthogonal-minors:2:s2" status="written-proof" proof="pf-family-domination" doi="10.5281/zenodo.23931738" source="Lemma 2, Section 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/118"}
Let $n\ge3$, $x,y,z\in\mathbb R^n$, $\|z\|=1$, and $\langle z,x\rangle=\langle z,y\rangle=0$. For any family $F$ of unordered coordinate pairs, define

$$
N(F)=\{T:|T|=3,\ \exists S\in F,\ S\subset T\}.
$$

Then

$$
\sum_{\{i,j\}\in F,\ i<j}p_{ij}^2
\le\sum_{\{i,j,k\}\in N(F),\ i<j<k}q_{ijk}^2. \tag{C}
$$
:::

::: {.proof #pf-family-domination}
Let $P_F$ and $P_{N(F)}$ be the orthogonal projections retaining exactly those coordinates. Contraction at $\{i,j\}$ reads only triples containing that pair. For $\{i,j\}\in F$, all such triples lie in $N(F)$. Hence

$$
P_F\iota_z b=P_F\iota_z P_{N(F)}b.
$$

Using $u=\iota_zb$ and the fact that projections and contraction have norm at most one gives

$$
\begin{aligned}
\|P_Fu\|&=\|P_F\iota_zP_{N(F)}b\|\\
&\le\|\iota_zP_{N(F)}b\|\\
&\le\|P_{N(F)}b\|.
\end{aligned}
$$

Squaring proves (C). Empty $F$ gives zero on both sides; the full family gives equality by (B). No minor is divided by, so zero minors and dependent $x,y$ are included. This expands the argument of manuscript Lemma 2.
:::

## From families to signed weights

Let $a_{ij}=a_{ji}$ be arbitrary real off-diagonal weights, and define

$$
A(a)=\sum_{i<j}a_{ij}|p_{ij}|^2,
$$

$$
M_{ijk}(a)=\max\{a_{ij},a_{ik},a_{jk}\},
$$

$$
U(a)=\sum_{i<j<k}M_{ijk}(a)|q_{ijk}|^2.
$$

::: {.theorem #signed-minors title="Signed weighted upper comparison" mathesis="collected:mathoverflow-469781-weighted-orthogonal-minors:2:s1" status="written-proof" proof="pf-signed-minors" doi="10.5281/zenodo.23931738" source="Theorem 1, Sections 1 and 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/117"}
Let $n\ge3$, $x,y,z\in\mathbb R^n$, $\|z\|=1$, and $\langle z,x\rangle=\langle z,y\rangle=0$. Every real symmetric off-diagonal weight array satisfies $A(a)\le U(a)$. No normalization or mutual orthogonality of $x,y$ is assumed.
:::

::: {.proof #pf-signed-minors}
First suppose the weights are nonnegative. List their distinct positive values as $0<t_1<\cdots<t_s$, set $t_0=0$, and let $F_\ell=\{\{i,j\}:a_{ij}\ge t_\ell\}$. The finite layer identities are

$$
a_{ij}=\sum_{\ell=1}^s(t_\ell-t_{\ell-1})
\mathbf1_{\{i,j\}\in F_\ell},
$$

$$
M_{ijk}(a)=\sum_{\ell=1}^s(t_\ell-t_{\ell-1})
\mathbf1_{\{i,j,k\}\in N(F_\ell)}.
$$

The first telescopes. The second holds because a triple belongs to $N(F_\ell)$ exactly when its largest edge weight reaches $t_\ell$. Multiply (C) by the nonnegative number $t_\ell-t_{\ell-1}$ and sum. Interchanging finite sums proves $A(a)\le U(a)$. All-zero weights give an empty layer sum and two zero sides.

For arbitrary real weights, put $m=\min_{i<j}a_{ij}$ and $a'_{ij}=a_{ij}-m\ge0$. The finite index set for the minimum is nonempty since $n\ge3$. Every triple maximum decreases by $m$ as well. By (B),

$$
A(a')=A(a)-mM,
$$

$$
U(a')=U(a)-mM.
$$

The nonnegative case gives $A(a)-mM\le U(a)-mM$. Cancel the identical term. If $M=0$, all minors vanish and the conclusion still holds. Only finite identities are used; no limiting passage occurs. Source: manuscript Theorem 1 and its Section 3 proof.
:::

::: {.theorem #orthonormal-minors title="Original real orthonormal comparison" mathesis="collected:mathoverflow-469781-weighted-orthogonal-minors:2:s1" lean="D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.weighted_minors"}
For every natural number $n$, real orthonormal triple $x,y,z\in\mathbb R^n$, and real matrix satisfying $A_{ij}=A_{ji}$ and $A_{ij}>0$ for **all** $i,j$, put $a_{ij}=A_{ij}$ for $i\ne j$. Then $A(a)\le U(a)$, with increasing-index sums.
:::

::: proof
Orthonormality supplies unit $z$ and its perpendicularity to $x,y$. Such a triple is linearly independent, so $n\ge3$ and the preceding theorem applies. Diagonal entries do not enter the sums, but the all-entry strict positivity hypothesis is retained here to match the cited Lean declaration. No such triple exists below dimension three. This is the original-question specialization of manuscript Theorem 1; the full signed and weaker-hypothesis theorem has broader scope.
:::

## Complex scalars, both bounds, and all degrees

::: {.corollary #complex-minors title="Hermitian complex comparison" mathesis="collected:mathoverflow-469781-weighted-orthogonal-minors:2:s3" status="written-proof" proof="pf-complex-minors" doi="10.5281/zenodo.23931738" source="Corollary 3, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/119"}
Let $n\ge3$, $x,y,z\in\mathbb C^n$, $\|z\|=1$, and $\langle z,x\rangle=\langle z,y\rangle=0$ in the Hermitian inner product. For every real symmetric off-diagonal weight array, $A(a)\le U(a)$ with absolute squares.
:::

::: {.proof #pf-complex-minors}
The orthogonal decomposition at the start of this chapter works in Hermitian exterior powers. Adjoint contraction has coordinates $\sum_h\overline{z_h}q_{hij}$, rather than $\sum_h z_hq_{hij}$. This gives recovery and the absolute-square mass identity (B). Coordinate locality is unchanged; projections and contraction remain contractions, proving (C). The same finite layers and equal-mass shift give the weighted upper bound. Mutual orthogonality of $x,y$ is unnecessary. Source: manuscript Corollary 3.
:::

Also define

$$
m_{ijk}(a)=\min\{a_{ij},a_{ik},a_{jk}\},
$$

$$
L(a)=\sum_{i<j<k}m_{ijk}(a)|q_{ijk}|^2.
$$

::: {.corollary #two-sided title="Two-sided comparison" mathesis="collected:mathoverflow-469781-weighted-orthogonal-minors:2:s4" status="written-proof" proof="pf-two-sided" doi="10.5281/zenodo.23931738" source="Corollary 4, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/120"}
Under all the hypotheses of the real or complex theorem above, every real symmetric off-diagonal weight array satisfies

$$
L(a)\le A(a)\le U(a).
$$
:::

::: {.proof #pf-two-sided}
The upper bound is proved. Apply it to $-a$. Since $M_{ijk}(-a)=-m_{ijk}(a)$, we obtain $-A(a)\le-L(a)$. Multiplication by $-1$ reverses the inequality and proves the lower bound. Source: manuscript Corollary 4. This retains the explicit signed and weaker-vector-hypothesis extension of Miller–Bistroń’s orthonormal, nonnegative two-sided comparison.
:::

::: {.corollary #repeated-lifts title="Arbitrary degrees and repeated orthogonal lifts" mathesis="collected:mathoverflow-469781-weighted-orthogonal-minors:2:s5" status="written-proof" proof="pf-repeated-lifts" doi="10.5281/zenodo.23931738" source="Corollary 5, Section 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/121"}
Let $\mathbb K=\mathbb R$ or $\mathbb C$, let integers $k,r\ge1$ satisfy $k+r\le n$, and let $z_1,\ldots,z_r$ be orthonormal. Set

$$
V=\operatorname{span}(z_1,\ldots,z_r)^\perp.
$$

Take any $u\in\Lambda^kV$, without assuming decomposability, and put

$$
b=z_r\wedge\cdots\wedge z_1\wedge u.
$$

For every real weight array $(a_S)_{|S|=k}$ define

$$
A_k=\sum_{|S|=k}a_S|u_S|^2,
$$

$$
U_{k,r}=\sum_{|T|=k+r}
\left(\max_{\substack{S\subset T\\|S|=k}}a_S\right)|b_T|^2,
$$

$$
L_{k,r}=\sum_{|T|=k+r}
\left(\min_{\substack{S\subset T\\|S|=k}}a_S\right)|b_T|^2.
$$

Then $L_{k,r}\le A_k\le U_{k,r}$. All sets are subsets of $[n]$.
:::

::: {.proof #pf-repeated-lifts}
First let $r=1$. For any $F\subseteq\binom{[n]}k$, let $N(F)$ be the $(k+1)$-sets containing a member of $F$. Contraction at $S$ reads only coordinates at $T\supset S$. By (A) and the same projection identity,

$$
\sum_{S\in F}|u_S|^2\le
\sum_{T\in N(F)}|(z_1\wedge u)_T|^2.
$$

The full coordinate masses are equal. Finite layers prove the nonnegative upper bound, equal-mass shifting proves the real-weight upper bound, and negation proves the lower bound. All these steps apply to arbitrary forms; none uses decomposability.

For $r>1$, set $u_0=u$ and $u_j=z_j\wedge u_{j-1}$. At step $j$, every vector of $V$ and each of $z_1,\ldots,z_{j-1}$ is perpendicular to $z_j$. Therefore

$$
u_{j-1}\in\Lambda^{k+j-1}(z_j^\perp),
$$

so the one-step comparison applies and $\|u_j\|=\|u_{j-1}\|$. Define the intermediate upper weights by

$$
\alpha_0(S)=a_S,
$$

$$
\alpha_j(T)=
\max_{\substack{R\subset T\\|R|=k+j-1}}\alpha_{j-1}(R).
$$

Successive comparisons give $A_k\le\sum_{|T|=k+r}\alpha_r(T)|b_T|^2$. Inductively $\alpha_j(T)=\max_{S\subset T,|S|=k}a_S$: one inclusion follows by transitivity of containment; conversely every such $S$ extends within $T$ by $j-1$ elements to a suitable $R$. The finite nonempty sets ensure the extrema exist. Replacing maximum by minimum gives the intermediate lower bounds and hence $L_{k,r}\le A_k$. If $u=0$, all terms vanish; if $k+r=n$, the final level has one coordinate set and the proof still applies. Source: manuscript Corollary 5. No approximation or limit occurs.
:::

## Equality and the sharp coefficient

::: {.corollary #sharpness title="Constant-weight equality and sharpness" mathesis="collected:mathoverflow-469781-weighted-orthogonal-minors:2:s6" status="written-proof" proof="pf-sharpness" doi="10.5281/zenodo.23931738" source="Corollary 6, Section 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/122"}
Under all the hypotheses of the preceding result, constant real weights give equality on both sides, and the coefficient one in the nonnegative-weight upper bound cannot be uniformly reduced. For an orthonormal triple in dimension three, the original inequality is the elementary minimum/maximum comparison in the posing questions.
:::

::: {.proof #pf-sharpness}
Each orthogonal lift preserves norm, so $\|b\|^2=\|u\|^2$. If $a_S=c$, all three expressions equal $c\|u\|^2$, including $c<0$, $c=0$, and $u=0$. Choose $u=e_1\wedge\cdots\wedge e_k$, $z_j=e_{k+j}$, and constant weights $c>0$. Both sides equal $c$. Multiplying the upper bound’s right side by any universal coefficient less than one would fail on this example.

In dimension three an orthonormal triple gives an orthogonal matrix (unitary over $\mathbb C$), so $|q_{123}|^2=1$. Identity (B) gives $\sum_{i<j}|p_{ij}|^2=1$. Bounding each weight by the global minimum and maximum proves the comparison directly. This is manuscript Corollary 6, without a claim to classify all equality cases.
:::

## The exponent boundary for the linked distance

Here a distance matrix means a genuine finite metric: $d_{ii}=0$, $d_{ij}=d_{ji}>0$ for $i\ne j$, and the triangle inequality. A complex projective point $[x]$ is represented by a unit vector; multiplication by a global unit complex scalar gives the same point. Define

$$
D_p([x],[y])=
\left(\sum_{i<j}d_{ij}^p
|x_i y_j-x_j y_i|^2\right)^{1/p}.
$$

::: {.corollary #exponent title="Sharp exponent for the linked distance" mathesis="collected:mathoverflow-469781-weighted-orthogonal-minors:2:s7" status="written-proof" proof="pf-exponent" doi="10.5281/zenodo.23931738" source="Corollary 7, Section 5" request="https://github.com/the-omega-institute/trureturing-requests/issues/123"}
For every $n\ge2$, every such distance matrix, and every $0<p<2$, $D_p$ fails the triangle inequality. If all off-diagonal distances equal a single $c>0$, then $D_p$ is a metric on complex projective space for every $p\ge2$.
:::

::: {.proof #pf-exponent}
Put $s=2/p$, take $0<\theta<\pi/4$, and set

$$
x=\cos\theta\,e_1+\sin\theta\,e_2,
$$

$$
y=\cos\theta\,e_1-\sin\theta\,e_2,
\qquad z=e_1.
$$

These are unit vectors using only the first two coordinates, so

$$
D_p([x],[y])=d_{12}\sin^s(2\theta),
$$

$$
D_p([x],[z])=D_p([y],[z])
=d_{12}\sin^s\theta.
$$

The triangle inequality would require $(2\cos\theta)^s\le2$, equivalently $\cos\theta\le2^{p/2-1}$. For $p<2$, the right side is strictly below one. Choose explicitly

$$
0<\theta<\min\{\pi/4,\arccos(2^{p/2-1})\}
$$

to violate it. Cancellation is valid because $d_{12}>0$ and $\sin\theta>0$. This reproduces the small-angle obstruction of Miller–Bistroń, Remark 4.

If $d_{ij}=c$, expansion of the ordered double sum followed by division by two gives the Gram identity for unit vectors:

$$
\sum_{i<j}|p_{ij}|^2
=1-|\langle x,y\rangle|^2.
$$

Set $P_x=xx^*$ and $P_y=yy^*$. Expanding the trace gives

$$
\|P_x-P_y\|_{\mathrm{HS}}^2
=2-2|\langle x,y\rangle|^2.
$$

Therefore

$$
D_p([x],[y])
=c\left(\frac{\|P_x-P_y\|_{\mathrm{HS}}}{\sqrt2}\right)^s.
$$

The projector $P_x$ is phase-invariant, and $P_x=P_y$ exactly when $[x]=[y]$. The Hilbert–Schmidt norm gives symmetry, nonnegativity, separation and the underlying triangle inequality. For $p\ge2$ we have $0<s\le1$. If $a,b\ge0$, the case $a+b=0$ is immediate. Otherwise let $t=a/(a+b)$; the inequalities $t^s\ge t$ and $(1-t)^s\ge1-t$ give $(a+b)^s\le a^s+b^s$. This transfers the underlying triangle inequality to $D_p$. Source: manuscript Corollary 7. The full $p\ge2$ theorem for arbitrary distance matrices is credited to Miller–Bistroń and is not proved anew here.
:::
