# 来源与证据范围

[原论文第 2 版](https://doi.org/10.5281/zenodo.23931738)由 Haobo Ma（Chrono AI, Singapore）和 Wenlin Zhang（National University of Singapore and Chrono AI, Singapore）署名，采用 CC BY 4.0 许可。版本 DOI 指向这份确切论文，概念 DOI 汇集各版本。讲解、演示稿和视频均围绕同一篇论文。

## Lean 陈述的准确范围

公开的 [`weighted_minors` 源码](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.lean#L593)陈述实数正交单位三元组、所有矩阵元均严格为正的对称矩阵上界，其中也要求对角元为正。定义使用实际行列式，最后的求和只计递增下标。源码允许任意自然维数，但正交单位三元组只有在维数至少为三时才存在。

[论文引用的源码版本](https://github.com/the-omega-institute/trureturing/blob/c55f6f7c7d7e3cf46b0a7da9efbba687448b29aa/D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.lean#L593)与[本书使用的源码版本](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.lean#L593)的模块字节完全相同；两个冻结状态记录都包含该公开定理。有序二元、三元质量定义分别除以二和六；最终定理将它们转换为递增下标求和，因此计数约定一致。

源码还有在较弱实数向量假设下的[私有坐标族证明](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.lean#L303)。冻结的私有声明记录已有的检查内容，但它尚不是本书可复用引用的公开结果。坐标族共享请求要求公开接口及无序子集的桥接，而非重新证明已有内容。[技术章节](statements.md)分别完整陈述并证明带符号上界、Hermitian 推广、带符号双侧界、任意外次数与多次提升、一般等号与锐性、距离指数。较窄的公开定理不覆盖这些完整范围。

原文报告了有限个精确有理数和复有理数例子；它们展示特定情形，不是全称命题的证明。本章中的数学证明不依赖这些计算，也不用极限。

## 原文定位

| 本讲解中的结果 | 原论文位置 |
| --- | --- |
| 带符号上界及正交单位特例 | 定理 1，第一、三节 |
| 坐标族比较 | 引理 2，第二节 |
| Hermitian 复数比较 | 推论 3，第三节 |
| 带符号双侧界 | 推论 4，第三节 |
| 任意外次数与多次正交提升 | 推论 5，第四节 |
| 常权重、系数锐性与三维情形 | 推论 6，第四节 |
| 距离指数与常距离情形 | 推论 7，第五节 |

## 参考文献与前人的具体贡献

- Haobo Ma and Wenlin Zhang, *Proof of the weighted-minor inequality in MathOverflow 469781*, version 2. [10.5281/zenodo.23931738](https://doi.org/10.5281/zenodo.23931738). 概念 DOI 为 [10.5281/zenodo.23931737](https://doi.org/10.5281/zenodo.23931737).
- meler, *Inequality involving minors of an orthogonal matrix*, [MathOverflow 469781](https://mathoverflow.net/q/469781), 23 April 2024; *Inequality involving a symmetric matrix and minors of an orthogonal matrix*, [Mathematics Stack Exchange 4902019](https://math.stackexchange.com/q/4902019), 19 April 2024.
- Russell Lyons, *Determinantal probability measures*, Publications Mathématiques de l’IHÉS **98** (2003), 167–212. [10.1007/s10240-003-0016-0](https://doi.org/10.1007/s10240-003-0016-0), 定理 6.2，第 183 页：嵌套子空间的投影行列式测度随机有序。应用于“包含 $F$ 中某一对”的递增事件，可得正交单位情形的坐标族比较。
- Rafał Bistroń, Michał Eckstein, Shmuel Friedland, Tomasz Miller and Karol Życzkowski, *A new class of distances on complex projective spaces*, [arXiv:2312.02583v1](https://arxiv.org/abs/2312.02583v1) (2023), 猜想 2.1. 发表于 Linear Algebra and its Applications **721** (2025), 577–611, [10.1016/j.laa.2024.10.017](https://doi.org/10.1016/j.laa.2024.10.017).
- Tomasz Miller and Rafał Bistroń, *Distances between pure quantum states induced by a distance matrix*, [arXiv:2509.14727v1](https://arxiv.org/abs/2509.14727v1), 18 September 2025: 引理 10、式 (27) 给出复数正交单位、非负权重的双侧比较；定理 2 证明完整距离定理；注记 4 给出 $p<2$ 障碍。对应 [v4](https://arxiv.org/abs/2509.14727v4), 4 October 2026, 中的定位分别为引理 13、式 (34)、定理 1 和注记 4。

这份讲解的主题是短小的收缩证明。原正交单位不等式与相关距离定理的前人成果如上明确归属。[贡献指南](contributing.md)中的共享请求协调具体范围的形式化，不把已证明结果称为数学猜想。
