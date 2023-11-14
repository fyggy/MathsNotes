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
Now let ${} \varphi :G\to{}H {}$ is a *homomorphism*, and suppose that ${} G$ is abelian. If $\varphi$ is surjective, then for all ${} x,\, y \in H {}$, we must have ${} a,\, b \in G$ such that ${} x=\varphi(a) {}$ and ${} y=\varphi(b) {}$. Therefore, 
$$
xy=\varphi (a)\varphi(b)=\varphi(ab)=\varphi(ba)=\varphi (b)\varphi(a)=yx
$$
Therefore, $H {}$ is commutative.
4. 
We see that ${} i \in \mathbb{C}\setminus \{ 0 \} {}$ has order $4$, but in ${} \mathbb{R}\setminus \{ 0 \} {}$, there are no elements of order 4. This is because if ${} x \in \mathbb{R}\setminus \{ 0 \}$, then if $x\neq-1 {}$ and ${} x\neq 1 {}$, then $x$ has infinite order. Otherwise, ${} |-1|=2$ and $|1|=1$. Therefore, ${} \mathbb{C}\setminus \{ 0 \}\not\cong\mathbb{R}\setminus \{ 0 \}$
5. 
Note that, by cantor, $\mathbb{R}$ and $\mathbb{Q}$ have different cardinalities; this means that there are no bijections from one to the other. Therefore, there can't be any isomorphism
6. 
Suppose there exists some homomorphism $\varphi:\mathbb{Z}\to{}\mathbb{Q}$. Then if ${} \varphi(1)=a {}$, then given ${} x \in \mathbb{Z} {}$, then $\varphi(x)=xa$. Now we also have ${} a / 2 \in \mathbb{Q}$. But $1/2 \notin \mathbb{Z}$, so there is no ${} x \in \mathbb{Z} {}$ such that $\varphi(z)=\frac{a}{2}$. Therefore, ${} \mathbb{Z} \not\cong\mathbb{Q} {}$, as required.
7. skip
8. 
We see that ${} |S_{n}|=n! {}$, and ${} |S_{m}|=m!$. There can only be a bijection if their cardinalities are the same. Therefore, we require that ${} n! =m!$, and since $!$ is bijective, then ${} n=m {}$.
9. Skiparoony
10. 
a)
