---
tags:
  - dnf_algebra
  - exercises
date: 2023-11-14
---
[[Directory]], [[D&F Abstract Algebra]]
[[Abstract Algebra - David S. Dummit, Richard M. Foote.pdf#page=53|Exercise Sheet]]
1. Let ${} G, H {}$ be groups, and let $\varphi:G\to{}H {}$ be a homomorphism. 
a)
Let ${} x \in G$. We work by induction on $n$. When ${} n=1$, then $\varphi(x^{1})=\varphi (x)^{1}$, so the base case holds. Now suppose that the statement holds for ${} n=k {}$, that is, ${} \varphi(x^{k})=\varphi(x)^{k} {}$. Now we have
$$
\begin{align}
\varphi(x^{k+1})=\varphi(x^{k}x)=\varphi(x^{k})\varphi(x)=\varphi(x)^{k}\varphi(x)=\varphi(x)^{k+1}
\end{align}
$$
Therefore, by induction, we see that this holds for all ${} n \in  \mathbb{Z}^{+} {}$
b) 
Let ${} x \in G {}$. First see that
$$
\varphi(1)\varphi(x)=\varphi(1x)=\varphi (x)
$$
Therefore, ${} \varphi(1)=1 {}$
Now we see that
$$
\varphi(x)\varphi(x^{-1})=\varphi (x x^{-1})=\varphi(1)=1
$$
Therefore, ${} \varphi(x^{-1})=\varphi(x)^{-1}$, as required.
2. skip
3. 
Let $\varphi:G\to{}H {}$ be a isomorphism, and let ${} a,\, b \in G$. Now see that, if $H {}$ is abelian, then
$$
ab=\varphi(\varphi ^{-1}(a))\varphi(\varphi ^{-1}(b))=\varphi(\varphi ^{-1}(b)\varphi ^{-1}(a))=ba
$$
This also works if ${} x,\, y\in G {}$ and $G$ is abelian. Therefore, $G$ is abelian iff $H$ is abelian.