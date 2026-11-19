# 精确陈述与完整证明

本章给出故事中每一步的数学依据。逻辑顺序是：外幂中的收缩与等质量 → 任意坐标族的比较 → 非负权重分层 → 带符号权重的等质量消去 → 取负得到下界 → 复数与任意外次数 → 多次提升 → 等号、锐性与距离指数。原文定位均指原论文，而非本讲解的章节号。

## 记号与收缩的基本事实

令 $\mathbb K=\mathbb R$ 或 $\mathbb C$，$[n]=\{1,\ldots,n\}$。$\Lambda^k\mathbb K^n$ 是 $k$ 阶外幂：以所有 $e_S=e_{i_1}\wedge\cdots\wedge e_{i_k}$（$i_1<\cdots<i_k$）为正交单位基的空间。外积具有交换两因子变号、重复因子为零的规则。一般元素 $u=\sum_{|S|=k}u_S e_S$ 可以是若干外积之和，不要求它能写成一个外积。规定

$$
\|u\|^2=\sum_{|S|=k}|u_S|^2.
$$

复数内积对第一变量共轭线性，故 $\langle z,x\rangle=\sum_i\overline{z_i}x_i$。实数时共轭可略去。

固定单位向量 $z$。取以 $z$ 为第一个向量的正交单位基，将一个 $\ell$ 阶形式唯一分解为

$$
b=z\wedge c+d,
$$

$$
c\in\Lambda^{\ell-1}(z^\perp),\qquad
 d\in\Lambda^\ell(z^\perp).
$$

这两部分由不相交的正交单位基构成。令 $L_z(v)=z\wedge v$，收缩 $\iota_z=L_z^*$ 是它的伴随。对不含 $z$ 的基向量，外乘 $z$ 加上一个单位因子；对已含 $z$ 的基向量，外乘结果为零。因此伴随把 $z\wedge c$ 送到 $c$、把 $d$ 送到零，得到

$$
\iota_z b=c,\qquad
\|\iota_zb\|\le\|b\|.
$$

若 $u\in\Lambda^k(z^\perp)$、$b=z\wedge u$，则

$$
\iota_zb=u,\qquad \|b\|^2=\|u\|^2. \tag{A}
$$

这是每个外次数中的结论，不用可分解性假设。 对 $T=\{i_1<\cdots<i_\ell\}$，由 $L_z$ 在坐标基上的矩阵取共轭转置，可得收缩的逐坐标公式：

$$
\iota_z e_T=\sum_{j=1}^{\ell}(-1)^{j-1}
\overline{z_{i_j}}e_{T\setminus\{i_j\}}.
$$

因此恢复一个坐标只会读取包含它的较高阶坐标。

若 $u=x\wedge y$ 且 $x,y\perp z$，其坐标为

$$
p_{ij}=x_i y_j-x_j y_i,
$$

$$
q_{ijk}=\det\begin{pmatrix}
x_i&x_j&x_k\\y_i&y_j&y_k\\z_i&z_j&z_k
\end{pmatrix}.
$$

由于移动 $z$ 越过两个因子不改变符号，$z\wedge x\wedge y=x\wedge y\wedge z$，所以 $b$ 的三元坐标就是 $q$。将 $q$ 交替延拓，(A) 的坐标形式为

$$
\sum_h\overline{z_h}q_{hij}=p_{ij},
$$

$$
\sum_{i<j}|p_{ij}|^2
=\sum_{i<j<k}|q_{ijk}|^2=M. \tag{B}
$$

所有集合只按递增下标计一次，没有额外的二或六的因子。

## 从局部性到任意坐标族

::: {.lemma #family-domination title="坐标族比较" mathesis="collected:mathoverflow-469781-weighted-orthogonal-minors:2:s2" status="written-proof" proof="pf-family-domination" doi="10.5281/zenodo.23931738" source="Lemma 2, Section 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/118"}
设 $n\ge3$，$x,y,z\in\mathbb R^n$，$\|z\|=1$，且 $\langle z,x\rangle=\langle z,y\rangle=0$。对任意无序坐标对集合 $F$，定义

$$
N(F)=\{T:|T|=3,\ \exists S\in F,\ S\subset T\}.
$$

则

$$
\sum_{\{i,j\}\in F,\ i<j}p_{ij}^2
\le\sum_{\{i,j,k\}\in N(F),\ i<j<k}q_{ijk}^2. \tag{C}
$$
:::

::: {.proof #pf-family-domination}
记 $P_F$、$P_{N(F)}$ 为保留相应坐标、将其余坐标置零的正交投影。收缩在 $\{i,j\}$ 坐标只读取包含该对的三元组。如果 $\{i,j\}\in F$，这些三元组全在 $N(F)$ 中。因此

$$
P_F\iota_z b=P_F\iota_z P_{N(F)}b.
$$

结合 $u=\iota_zb$ 和投影、收缩的范数均不超过一，得

$$
\begin{aligned}
\|P_Fu\|&=\|P_F\iota_zP_{N(F)}b\|\\
&\le\|\iota_zP_{N(F)}b\|\\
&\le\|P_{N(F)}b\|.
\end{aligned}
$$

平方就是 (C)。$F$ 为空时两边为零；$F$ 为全部坐标对时由 (B) 得等号。证明不除以任何子式，故零子式和线性相关的 $x,y$ 都已包括。论证按原文引理 2 展开。
:::

## 从坐标族到带符号权重

记 $a_{ij}=a_{ji}$ 为任意实数非对角权重，并定义

$$
A(a)=\sum_{i<j}a_{ij}|p_{ij}|^2,
$$

$$
M_{ijk}(a)=\max\{a_{ij},a_{ik},a_{jk}\},
$$

$$
U(a)=\sum_{i<j<k}M_{ijk}(a)|q_{ijk}|^2.
$$

::: {.theorem #signed-minors title="带符号权重上界" mathesis="collected:mathoverflow-469781-weighted-orthogonal-minors:2:s1" status="written-proof" proof="pf-signed-minors" doi="10.5281/zenodo.23931738" source="Theorem 1, Sections 1 and 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/117"}
设 $n\ge3$，$x,y,z\in\mathbb R^n$，$\|z\|=1$、$\langle z,x\rangle=\langle z,y\rangle=0$。对于所有实数对称非对角权重，均有 $A(a)\le U(a)$。$x,y$ 不要求归一化或彼此垂直。
:::

::: {.proof #pf-signed-minors}
先设权重非负。将所有不同的正权重列为 $0<t_1<\cdots<t_s$，置 $t_0=0$，并令 $F_\ell=\{\{i,j\}:a_{ij}\ge t_\ell\}$。有限的分层恒等式为

$$
a_{ij}=\sum_{\ell=1}^s(t_\ell-t_{\ell-1})
\mathbf1_{\{i,j\}\in F_\ell},
$$

$$
M_{ijk}(a)=\sum_{\ell=1}^s(t_\ell-t_{\ell-1})
\mathbf1_{\{i,j,k\}\in N(F_\ell)}.
$$

第一个恒等式是望远镜求和；第二个成立是因为一个三元组属于 $N(F_\ell)$ 当且仅当它的最大边权达到 $t_\ell$。将 (C) 乘以非负数 $t_\ell-t_{\ell-1}$ 后相加，交换有限求和，就得到 $A(a)\le U(a)$。全零权重对应空的层和，两边为零。

一般实数权重令 $m=\min_{i<j}a_{ij}$，$a'_{ij}=a_{ij}-m\ge0$。因 $n\ge3$，取最小值的有限集合非空。每个三元组的最大值也减去 $m$。由 (B)，

$$
A(a')=A(a)-mM,
$$

$$
U(a')=U(a)-mM.
$$

非负情形给出 $A(a)-mM\le U(a)-mM$；消去同一项即可。若 $M=0$，所有子式均为零，结论仍成立。这里只用有限恒等式，不涉及极限。来源：原文定理 1、第三节证明。
:::

::: {.theorem #orthonormal-minors title="原实数正交单位比较" mathesis="collected:mathoverflow-469781-weighted-orthogonal-minors:2:s1" lean="D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.weighted_minors"}
对任意自然数 $n$、实数正交单位三元组 $x,y,z\in\mathbb R^n$，以及满足 $A_{ij}=A_{ji}$、**所有** $i,j$ 均有 $A_{ij}>0$ 的实矩阵，将 $a_{ij}=A_{ij}$（$i\ne j$），则 $A(a)\le U(a)$。求和只包含递增下标。
:::

::: proof
正交单位性给出单位 $z$ 及其与 $x,y$ 的垂直性。这样的三元组线性无关，所以 $n\ge3$；应用上一定理。对角元虽不进入求和，但此处保留所有矩阵元严格为正的假设，与所引 Lean 声明一致。低于三维不存在这样的三元组。此结论是原文定理 1 的原问题特例；上一定理的带符号及弱假设全称结论具有更大范围。
:::

## 复数、双侧界与一般外次数

::: {.corollary #complex-minors title="Hermitian 复数比较" mathesis="collected:mathoverflow-469781-weighted-orthogonal-minors:2:s3" status="written-proof" proof="pf-complex-minors" doi="10.5281/zenodo.23931738" source="Corollary 3, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/119"}
将定理中的向量改为 $x,y,z\in\mathbb C^n$，假设 $n\ge3$、$\|z\|=1$、Hermitian 正交 $\langle z,x\rangle=\langle z,y\rangle=0$。任意实数对称非对角权重仍满足 $A(a)\le U(a)$，其中使用绝对值平方。
:::

::: {.proof #pf-complex-minors}
本章的正交分解在 Hermitian 外幂中原样成立。伴随收缩的坐标是 $\sum_h\overline{z_h}q_{hij}$，而非 $\sum_h z_hq_{hij}$。由此得到恢复恒等式和 (B) 的绝对值平方版本。坐标局部性不变，投影和收缩仍为压缩映射，所以 (C) 也成立。按同一有限层和、等质量平移证明上界；无须 $x,y$ 互相垂直。来源：原文推论 3。
:::

另外定义

$$
m_{ijk}(a)=\min\{a_{ij},a_{ik},a_{jk}\},
$$

$$
L(a)=\sum_{i<j<k}m_{ijk}(a)|q_{ijk}|^2.
$$

::: {.corollary #two-sided title="双侧比较" mathesis="collected:mathoverflow-469781-weighted-orthogonal-minors:2:s4" status="written-proof" proof="pf-two-sided" doi="10.5281/zenodo.23931738" source="Corollary 4, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/120"}
在上述实数或复数定理的全部假设下，对任意实数对称非对角权重有

$$
L(a)\le A(a)\le U(a).
$$
:::

::: {.proof #pf-two-sided}
上界已证。把上界用于 $-a$，利用 $M_{ijk}(-a)=-m_{ijk}(a)$，得到 $-A(a)\le-L(a)$。乘以 $-1$ 并反向即得下界。来源：原文推论 4。Miller–Bistroń 的正交单位、非负权重双侧比较在此具有明确的较弱向量假设和带符号推广。
:::

::: {.corollary #repeated-lifts title="任意外次数与多次正交提升" mathesis="collected:mathoverflow-469781-weighted-orthogonal-minors:2:s5" status="written-proof" proof="pf-repeated-lifts" doi="10.5281/zenodo.23931738" source="Corollary 5, Section 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/121"}
令 $\mathbb K=\mathbb R$ 或 $\mathbb C$，整数 $k,r\ge1$ 且 $k+r\le n$。设 $z_1,\ldots,z_r$ 正交归一，并置

$$
V=\operatorname{span}(z_1,\ldots,z_r)^\perp.
$$

取任意 $u\in\Lambda^kV$，不要求可分解，令

$$
b=z_r\wedge\cdots\wedge z_1\wedge u.
$$

对所有实数数组 $(a_S)_{|S|=k}$，定义

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

则 $L_{k,r}\le A_k\le U_{k,r}$。所有集合均为 $[n]$ 的子集。
:::

::: {.proof #pf-repeated-lifts}
先取 $r=1$。对于任意 $F\subseteq\binom{[n]}k$，让 $N(F)$ 为包含其中某一集合的所有 $(k+1)$ 元集合。收缩在 $S$ 坐标只读取 $T\supset S$ 的坐标；由 (A) 和同一投影恒等式，

$$
\sum_{S\in F}|u_S|^2\le
\sum_{T\in N(F)}|(z_1\wedge u)_T|^2.
$$

全部坐标质量相等。照前面的层和证明非负权重上界、等质量平移证明实权重上界、取负证明下界。这些步骤对任意形式有效，没有使用 $u$ 可分解。

对 $r>1$，令 $u_0=u$、$u_j=z_j\wedge u_{j-1}$。在第 $j$ 步，$V$ 中的每个向量和 $z_1,\ldots,z_{j-1}$ 都垂直于 $z_j$。因此

$$
u_{j-1}\in\Lambda^{k+j-1}(z_j^\perp),
$$

一阶结论可用，且 $\|u_j\|=\|u_{j-1}\|$。定义上界中间权重

$$
\alpha_0(S)=a_S,
$$

$$
\alpha_j(T)=
\max_{\substack{R\subset T\\|R|=k+j-1}}\alpha_{j-1}(R).
$$

逐步比较得 $A_k\le\sum_{|T|=k+r}\alpha_r(T)|b_T|^2$。归纳证明 $\alpha_j(T)=\max_{S\subset T,|S|=k}a_S$：一边由子集传递性；另一边因为每个这样的 $S$ 都能在 $T$ 内添 $j-1$ 个元素构成所需 $R$。有限非空集合保证极值存在。以最小值替代同理，逐步下界给出 $L_{k,r}\le A_k$。$u=0$ 时全零，$k+r=n$ 时最后只有一个坐标集合，证明仍有效。来源：原文推论 5。此论证没有近似或极限。
:::

## 等号与系数一的锐性

::: {.corollary #sharpness title="常权重等号与锐性" mathesis="collected:mathoverflow-469781-weighted-orthogonal-minors:2:s6" status="written-proof" proof="pf-sharpness" doi="10.5281/zenodo.23931738" source="Corollary 6, Section 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/122"}
在上一结论的全部假设下，常数实权重给出双侧等号；非负权重上界的系数一不可统一减小。对于三维正交单位三元组，原不等式是原提问中的初等最小值、最大值比较。
:::

::: {.proof #pf-sharpness}
每次正交提升都保范数，因此 $\|b\|^2=\|u\|^2$。若 $a_S=c$，三个和均等于 $c\|u\|^2$，包括 $c<0$、$c=0$ 和 $u=0$。取 $u=e_1\wedge\cdots\wedge e_k$，$z_j=e_{k+j}$，所有权重为 $c>0$，则两侧同为 $c$。若上界右端统一乘以小于一的系数，这个例子立刻失效。

三维正交单位三元组组成正交（复数时酉）矩阵，故 $|q_{123}|^2=1$。由 (B)，$\sum_{i<j}|p_{ij}|^2=1$。直接把每项权重夹在全局最小、最大值之间即可。这是原文推论 6；它没有声称给出所有等号情形。
:::

## 相关距离的指数边界

这里的距离矩阵是一个真正有限度量：$d_{ii}=0$、$d_{ij}=d_{ji}>0$（$i\ne j$），并满足三角不等式。复射影点 $[x]$ 由单位向量表示，相差整体单位复数因子的向量代表同一点。定义

$$
D_p([x],[y])=
\left(\sum_{i<j}d_{ij}^p
|x_i y_j-x_j y_i|^2\right)^{1/p}.
$$

::: {.corollary #exponent title="相关距离的锐指数" mathesis="collected:mathoverflow-469781-weighted-orthogonal-minors:2:s7" status="written-proof" proof="pf-exponent" doi="10.5281/zenodo.23931738" source="Corollary 7, Section 5" request="https://github.com/the-omega-institute/trureturing-requests/issues/123"}
对于每个 $n\ge2$、每个这样的距离矩阵及每个 $0<p<2$，$D_p$ 都不满足三角不等式。若所有非对角距离均为同一常数 $c>0$，则对每个 $p\ge2$，$D_p$ 是复射影空间上的距离。
:::

::: {.proof #pf-exponent}
令 $s=2/p$，取 $0<\theta<\pi/4$ 以及

$$
x=\cos\theta\,e_1+\sin\theta\,e_2,
$$

$$
y=\cos\theta\,e_1-\sin\theta\,e_2,
\qquad z=e_1.
$$

三个向量均为单位向量，且只用前两个坐标。因此

$$
D_p([x],[y])=d_{12}\sin^s(2\theta),
$$

$$
D_p([x],[z])=D_p([y],[z])
=d_{12}\sin^s\theta.
$$

三角不等式将要求 $(2\cos\theta)^s\le2$，等价于 $\cos\theta\le2^{p/2-1}$。当 $p<2$ 时，右边严格小于一。可直接选

$$
0<\theta<\min\{\pi/4,\arccos(2^{p/2-1})\},
$$

使要求失败。$d_{12}>0$ 和 $\sin\theta>0$ 保证约去因子合法。这是 Miller–Bistroń 注记 4 的小角度障碍，原文在此重述。

若 $d_{ij}=c$，展开有序双重和并除以二，得到单位向量的 Gram 恒等式

$$
\sum_{i<j}|p_{ij}|^2
=1-|\langle x,y\rangle|^2.
$$

另一方面，令 $P_x=xx^*$、$P_y=yy^*$，展开迹得

$$
\|P_x-P_y\|_{\mathrm{HS}}^2
=2-2|\langle x,y\rangle|^2.
$$

故

$$
D_p([x],[y])
=c\left(\frac{\|P_x-P_y\|_{\mathrm{HS}}}{\sqrt2}\right)^s.
$$

$P_x$ 对相位不变，且 $P_x=P_y$ 当且仅当 $[x]=[y]$；Hilbert–Schmidt 范数给出对称性、非负性、分离性和底层三角不等式。若 $p\ge2$，则 $0<s\le1$。对 $a,b\ge0$，$a+b=0$ 时显然；否则令 $t=a/(a+b)$，由 $t^s\ge t$、$(1-t)^s\ge1-t$ 得 $(a+b)^s\le a^s+b^s$。这将底层三角不等式传给 $D_p$。来源：原文推论 7。一般距离矩阵在 $p\ge2$ 的完整定理归于 Miller–Bistroń，本文没有重新证明它。
:::
