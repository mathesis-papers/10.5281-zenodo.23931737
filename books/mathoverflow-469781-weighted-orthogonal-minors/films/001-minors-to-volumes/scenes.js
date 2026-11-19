/* Film 001: a focused explanation of the version-2 paper.
   Evidence scopes follow the corresponding narration; all numerical data are exact.
   The shared engine supplies timing, drawing, semantic colours and typography. */
'use strict';

function minorTitle(en, zh, a = 1) {
  txt(en, 960, 208, {size: 43, fam: F.disp, w: 700, align: 'center', c: C.white, a});
  txt(zh, 960, 262, {size: 31, fam: F.zh, align: 'center', c: C.cyan, a});
}
function minorMath(x, y, w, h, label, lines, a = 1, col = C.cyan, size = 43) {
  panel(x, y, w, h, a, col, label);
  const top = y + 50, bodyH = h - 50;
  lines.forEach((s, k) => txt(s, x + w / 2, top + bodyH * (k + 0.5) / lines.length,
    {size, fam: F.math, align: 'center', base: 'middle', c: C.white, a}));
}
function minorEdge(x1, y1, x2, y2, label, col, a = 1) {
  line(x1, y1, x2, y2, col, a, 4);
  txt(label, (x1 + x2) / 2, (y1 + y2) / 2 - 16,
    {size: 31, fam: F.mono, align: 'center', c: col, a});
}

SCENES.areas = S => {
  badgeQ(S, [[0, 'three dimensions', 'computed']]);
  minorTitle('Price the squared coordinate areas', '给坐标面积的平方标价');
  minorMath(110, 310, 800, 208, 'ORTHONORMAL EXAMPLE',
    ['x = (1,0,0)', 'y = (0,3/5,4/5)', 'z = (0,−4/5,3/5)'], 1, C.cyan, 34);
  minorMath(1010, 310, 800, 208, 'AREA SQUARES / VOLUME SQUARE',
    ['p₁₂² = 9/25    p₁₃² = 16/25', 'p₂₃² = 0         q₁₂₃² = 1'], at(S,1,0.8), C.cyan, 34);
  const masses = [9/25,16/25,0];
  masses.forEach((v,i) => {
    const x = 175 + i * 240;
    fillBox(x, 800 - 230 * v * at(S,1,1.1), 145, 230 * v * at(S,1,1.1), C.cyan, 0.85);
    txt(['12','13','23'][i], x+72, 839, {size:29, align:'center', c:C.dim});
  });
  minorMath(1010, 575, 800, 248, 'PRICES: 2, 5, 1',
    ['2 × 9/25 + 5 × 16/25 = 98/25', '1 ≤ 98/25 ≤ 5'], at(S,2,0.8), C.cyan, 34);
};

SCENES.question = S => {
  badgeQ(S, [[0, 'real orthonormal triple', 'lean']]);
  minorTitle('The original upper comparison', '原问题的上界：准确的形式证据范围');
  minorMath(130, 315, 1660, 190, 'REAL ORTHONORMAL x, y, z · A SYMMETRIC · EVERY ENTRY > 0',
    ['pᵢⱼ = xᵢyⱼ − xⱼyᵢ', 'qᵢⱼₖ = det [x; y; z] on columns i,j,k'], 1, C.lean, 36);
  minorMath(130, 555, 1660, 245, 'INCREASING INDICES · EACH PAIR / TRIPLE ONCE',
    ['Σᵢ<ⱼ aᵢⱼ pᵢⱼ² ≤ Σᵢ<ⱼ<ₖ max(aᵢⱼ,aᵢₖ,aⱼₖ) qᵢⱼₖ²'], at(S,1,0.8), C.lean, 42);
  const cite = leanCite('D5/S3/Geometry/ProbabilityTransport/WeightedProjectionMinors.weighted_minors');
  if(cite) txt('AlternatingArrayContraction.weighted_minors',960,858,
    {size:25,fam:F.mono,c:C.lean,align:'center',a:at(S,1,0.8)});
};

SCENES.contraction = S => {
  badgeQ(S, [[0, 'unit vector z', 'argued']]);
  minorTitle('Lift without changing total mass', '提升保持总质量，收缩恢复面积');
  txt('REAL VECTORS · ‖z‖ = 1 · z ⟂ x,y',960,318,
    {size:27,fam:F.math,c:C.argued,align:'center'});
  minorMath(130,365,760,300,'AREA DATA → VOLUME DATA',
    ['u = x ∧ y', 'b = z ∧ u', '‖b‖² = ‖u‖²'],at(S,1,0.8),C.argued,44);
  minorMath(1030,365,760,300,'CONTRACTION',
    ['ι_z b = u', '‖ι_z v‖ ≤ ‖v‖', 'pᵢⱼ = Σₖ zₖ qₖᵢⱼ'],at(S,1,0.8),C.argued,44);
  arrow(900,515,1015,515,C.cyan,at(S,1,0.8),4);
  txt('Only triples containing {i,j} can contribute to pᵢⱼ',960,774,
    {size:34,fam:F.disp,align:'center',c:C.white,a:Q(S,2,'only volumes')});
  txt('只读取包含这条边的体积坐标',960,828,
    {size:30,fam:F.zh,align:'center',c:C.cyan,a:at(S,2,0.8)});
};

SCENES.families = S => {
  badgeQ(S, [[0, 'any family of edges', 'argued']]);
  minorTitle('Discard irrelevant triples first', '先保留邻接三元组，再收缩并投影');
  txt('REAL · ‖z‖ = 1 · z ⟂ x,y',960,310,{size:27,fam:F.math,align:'center',c:C.argued});
  panel(120,350,630,305,1,C.cyan,'SELECTED EDGE FAMILY F');
  minorEdge(205,580,430,410,'12',C.cyan);
  minorEdge(430,410,660,580,'13',C.cyan);
  ['1','2','3'].forEach((s,i)=>txt(s,[430,205,660][i],[390,618,618][i],{size:30,c:C.white,align:'center'}));
  panel(1020,350,780,305,1,C.mag,'N(F): ALL TRIPLES WITH A CHOSEN EDGE');
  ['123','124','134'].forEach((s,i)=>chip(1080+i*235,460,190,92,s,C.mag,at(S,0,1.0),38));
  arrow(775,500,990,500,C.cyan,at(S,0,1.0),4);
  txt('Example: F = {12,13} in four coordinates',960,700,
    {size:28,fam:F.disp,align:'center',c:C.dim});
  minorMath(150,740,1620,145,'FAMILY DOMINATION',
    ['Σ edges in F p² ≤ Σ triples in N(F) q²'],at(S,2,0.8),C.argued,42);
};

SCENES.layers = S => {
  badgeQ(S, [[0, 'nonnegative prices', 'argued']]);
  minorTitle('A maximum is the last occupied layer', '最大边价决定三角形达到哪一层');
  panel(120,330,880,485,1,C.cyan,'EDGE PRICES: 1, 3, 4');
  const base=742, unit=86, width=150;
  const values=[1,3,4], xs=[220,470,720], thickness=[1,2,1];
  const progress=at(S,0,1.7);
  values.forEach((v,i)=>{
    let low=0;
    thickness.forEach((h,j)=>{
      const used=Math.max(0,Math.min(v-low,h));
      if(used>0) fillBox(xs[i],base-(low+used)*unit*progress,width,used*unit*progress-3,[C.cyan,C.mag,C.dim][j],0.8);
      low+=h;
    });
    txt(String(v),xs[i]+width/2,base+46,{size:40,fam:F.math,align:'center',c:C.white});
  });
  [1,3,4].forEach(t=>{
    dashed(165,base-unit*t,945,base-unit*t,C.dim,0.7,1.5);
    txt('t='+t,936,base-unit*t-9,{size:24,c:C.dim,align:'right'});
  });
  minorMath(1080,330,720,270,'AT EVERY LEVEL t',
    ['some edge price ≥ t', '⇕', 'maximum edge price ≥ t'],at(S,1,0.8),C.argued,35);
  minorMath(1080,650,720,165,'ADD THE FAMILY BOUNDS',
    ['1 = 1   3 = 1+2   4 = 1+2+1'],at(S,2,0.8),C.argued,32);
};

SCENES.signed = S => {
  badgeQ(S, [[0, 'negative prices', 'argued']]);
  minorTitle('Equal mass is what permits signed prices', '带符号平移的关键：两边质量相等');
  txt('REAL · ‖z‖ = 1 · z ⟂ x,y · aᵢⱼ = aⱼᵢ ∈ ℝ',960,316,
    {size:29,fam:F.math,align:'center',c:C.argued});
  minorMath(150,350,1620,160,'SHIFT EVERY EDGE PRICE',
    ['m = min aᵢⱼ       a′ᵢⱼ = aᵢⱼ − m ≥ 0'],1,C.argued,43);
  minorMath(150,555,770,205,'AREA TOTAL',
    ['Σ p² = M', 'E(a′) = E(a) − mM'],at(S,1,0.8),C.argued,40);
  minorMath(1000,555,770,205,'VOLUME TOTAL',
    ['Σ q² = M', 'U(a′) = U(a) − mM'],at(S,1,0.8),C.argued,40);
  const a=Q(S,1,'That term cancels');
  line(500,723,817,723,C.mag,a,3);line(1350,723,1667,723,C.mag,a,3);
  txt('Negate prices: max(−a) = −min(a)  ⇒  L(a) ≤ E(a) ≤ U(a)',960,849,
    {size:35,fam:F.math,align:'center',c:C.white,a:at(S,2,0.8)});
};

SCENES.credit = S => {
  badgeQ(S, [[0, 'earlier theorem', 'argued']]);
  minorTitle('Locality → layers → equal-mass cancellation', '局部性 → 分层 → 等质量消去');
  minorMath(140,325,1640,190,'MATHEMATICAL CREDIT',
    ['meler: the question · Lyons (2003): the orthonormal comparison',
     'Miller–Bistroń (2025): a direct two-sided proof'],1,C.argued,34);
  minorMath(140,565,1640,270,'PAPER VERSION 2 · DOI: 10.5281/zenodo.23931738',
    ['Haobo Ma — Chrono AI, Singapore',
     'Wenlin Zhang — National University of Singapore',
     'and Chrono AI, Singapore'],at(S,1,0.8),C.cyan,36);
};

FILM.poster = () => {
  background(24, TL.scenes[0], 0, 4);
  minorTitle('From areas to volumes', '从面积到体积');
  minorMath(160,330,1600,190,'THE MECHANISM',
    ['selected edges → containing triples', 'local contraction → finite price layers'],1,C.cyan,44);
  minorMath(160,575,1600,190,'QUESTION POSED BY meler · PRIOR WORK: LYONS / MILLER–BISTROŃ',
    ['Haobo Ma · Wenlin Zhang', 'Proof of the weighted-minor inequality in MathOverflow 469781'],1,C.cyan,32);
  txt('Haobo Ma: Chrono AI, Singapore',960,842,{size:27,fam:F.disp,align:'center',c:C.white});
  txt('Wenlin Zhang: National University of Singapore and Chrono AI, Singapore',960,892,
    {size:27,fam:F.disp,align:'center',c:C.white});
};
