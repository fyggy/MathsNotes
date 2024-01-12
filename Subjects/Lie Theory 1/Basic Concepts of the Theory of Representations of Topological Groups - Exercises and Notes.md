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
Ex 2:
Let ${} \{ X_{j} \}_{j=1}^{n}  {}$ be a family of separated topological spaces. Let 
$$
X=X_{1} \times  \dots \times X_{n}
$$
be a topological space with the induced topology. Now let ${} x,\, y \in X {}$. Then ${} x=(x_{1},\,\dots,\,x_{n}) {}$ and ${} y=(y_{1},\,\dots,\,y_{n}) {}$. Since $X_{1},\,\dots,\,X_{n} {}$ are separated, then there exist neighbourhoods ${} U_{1},\,\dots,\,U_{n} {}$ of ${} x_{1},\,\dots,\,x_{n} {}$ and $V_{1},\,\dots,\,V_{n} {}$ of ${} y_{1},\,\dots,\,y_{n} {}$ with ${} U_{j} \cap V_{j} = \varnothing {}$. Now consider the sets ${} X \supseteq U=U_{1} \times{\dots}\times U_{n} {}$ and ${} X \supseteq V_{1} \times{\dots}\times V_{n} {}$. Clearly these are open and contain ${} x {}$ and $y$, so are neighbourhoods. They also clearly have empty intersection, so $X$ is separated. 