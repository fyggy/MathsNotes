---
tags:
  - ns_rep_theory
  - exercises
  - chapter
date: 2024-01-09
---
[[Directory]], [[Lie Theory 1]]
Ex 1: 
Let $S {}$ be a non-empty open set in ${} \mathbb{R}^{n} {}$. Since $S {}$ is non-empty, then let ${} p \in S {}$ be a point in $S$. Then since $S {}$ is open, then there exists an open ball ${} B_{p} \subseteq S {}$ centred at $p$ with some non-zero radius ${} \varepsilon_{p} {}$. Associate such an open ball with every such point $p {}$. Now let ${} \mathcal{C}=\{ B_{p} \mid p \in S \} {}$. Now let
$$
S'=\bigcup_{B\in \mathcal{C}} B
$$
and note that, given ${} p \in S {}$, there exists some ${} B \in \mathcal{C} {}$ with ${} p \in B {}$, and ${} B \subseteq S' {}$, so ${} p \in S' {}$. Likewise, given ${} p \in S' {}$, then there exists some ball ${} B \subseteq S {}$ with ${} p \in B {}$, so ${} p \in S {}$. Therefore, ${} S'=S {}$, and the set of all open balls is a basis of the topology ${} \mathcal{T}  {}$on $\mathbb{R}^{n}$.