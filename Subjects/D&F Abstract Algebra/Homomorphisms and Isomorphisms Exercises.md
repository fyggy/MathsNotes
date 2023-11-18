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
10. skip
11. skip 
12. skip
13. 
Let ${} G, H {}$ be groups, and let ${} \varphi :G\to{}H {}$ be a homomorphism. Let $I$ be image of $\varphi$ in $H {}$, that is
$$
I=\{ x \in H\mid \exists a \in G:\varphi(a)=x \}
$$First observe that, obviously, ${} I\subseteq H {}$. Then we check the group axioms. First we see that it is clear that the group operation of ${} H {}$ is associative in ${} I {}$. Then we see that, since ${} \varphi(1)=1 {}$, then ${} 1 \in I {}$. Finally, we see that, if ${} \varphi(a) \in I$, then ${} \varphi(a)^{-1}=\varphi(a^{-1})\in I$. Therefore, $I\leq H$

Now suppose that $\varphi$ is injective. Then, we see that $\varphi_{|I}:G\to{}I {}$ is surjective by definition, and injective by hypothesis. It is also still a homomorphism, as that does not care about the codomain of $\varphi$. Therefore, $\varphi_{|I} {}$ is an isomorphism.

Suppose that $I=H {}$. Then, it is clear by definition that $\varphi {}$ is surjective
14. 
Let ${} G, H {}$ be groups, and let $\varphi:G\to{}H {}$ be a homomorphism. Let ${} K {}$ be the *kernel* of ${} \varphi {}$ in $G$, that is
$$
K=\{ a \in G\mid\varphi(a)=1 \}
$$First we observe that, obviously, ${} K\subseteq G {}$. Now we check the group axioms. Firstly, it is clear that the operation on $G {}$ is still associative on $K$. Next, if ${} a,\, b \in K$, then 
$$
\varphi(ab)=\varphi(a)\varphi(b)=1\cdot 1=1
$$
So ${} ab \in K {}$. Now since ${} \varphi(1)=1 {}$, then ${} 1 \in K {}$. Finally, if ${} a \in K$, then 
$$
\varphi(a^{-1})=\varphi (a)^{-1}=1^{-1}=1
$$
So ${} a^{-1} \in K$. Therefore, $K$ is a group, so $K\leq G {}$.

Now suppose that ${} \varphi {}$ is injective. Then, by the definition of injectivity, then if ${} \varphi(a)=\varphi(b) {}$, then ${} a=b {}$. First note that ${} 1 \in K {}$, as $\varphi(1)=1 {}$. Then suppose that we have some ${} a \in G {}$ such that ${} a \in K {}$, that is ${} \varphi(a)=1$. By the definition of injectivity, we have $\varphi(a)=1=\varphi(1)$, therefore, ${} a=1$. Therefore, $K=\{ 1 \}$.

Now suppose that $K=\{ 1 \}$. Now suppose we have some ${} a,\, b \in G {}$ such that ${} \varphi(a)=\varphi(b) {}$. Then
$$
\begin{align}
 \varphi(a) & =\varphi(b)   \\
\varphi (a)\varphi(b)^{-1} & =1 \\
\varphi(ab^{-1}) & =1
 \end{align}
$$
Since ${} K=\{ 1 \} {}$, then ${} ab^{-1}=1 {}$. Therefore, ${} a=b {}$. Therefore, $\varphi$ is injective, as required
15. 
Let $\pi:\mathbb{R}^{2}\to{}\mathbb{R}$ such that ${} \pi((x,\, y))=x$. Now let $a,\, b,\, c,\, d\in \mathbb{R}$. Then we have
$$
\pi((a,\, b))\pi((c,\, d))=ac=\pi((ac,\,  bd))
$$Therefore, $\pi$ is a homomorphism. Now we see that, if ${} \pi((a,\, b))=1 {}$, then $a=1$, but there are no bounds on $b {}$. Therefore, the kernel of $\pi {}$ is
$$
\{ (1,\, x)\mid x \in \mathbb{R} \}
$$
16. By exact same logic as above, the kernel of ${} \pi_{1} {}$ is ${} A {}$ and the kernel of ${} \pi_{2} {}$ is ${} B$
17. 
skip
18. 
Let $G$ be a group. Let $\varphi:G\to{}G$ be defined by $\varphi(x)=x^{2}$.
Working ${} (\Rightarrow )$. Suppose that $\varphi$ is a homomorphism. Therefore, given $a,\, b \in G {}$, we have
$$
(ab)^{2}=abab=\varphi(ab)=\varphi(a)\varphi(b)=a^{2}b^{2}
$$
We see that we have ${} abab=a a b b {}$, so by the cancellation law, $ba=ab$. Therefore, $G {}$ is abelian

Now working ${} (\Leftarrow )$. Suppose that $G$ is abelian. Therefore, given ${} a,\,  b \in G {}$, we have
$$
\varphi(a)\varphi(b)=a^{2}b^{2}=a a b b=abab=(ab)^{2}=\varphi(ab)
$$
Therefore, $\varphi$ is a homomorphism. 
19. skip
20. skip
21. 
Let ${} \varphi:\mathbb{Q}\to{}\mathbb{Q} {}$ such that ${} \varphi(x)=kx {}$ for some ${} k \in \mathbb{Q}$. First, suppose that ${} \varphi(x)=\varphi(y) {}$. Then ${} kx=ky$, so we have ${} x=y$. Therefore, $\varphi$ is injective. Now suppose we have ${} a \in \mathbb{Q} {}$. Then ${} a / k \in \mathbb{Q} {}$, as $\mathbb{Q}$ is a field, and $\varphi(a / k)=k \frac{a}{k}=a$. Therefore, $\varphi$ is surjective. Therefore, $\varphi$ is a automorphism
22. 
Let $A$ be a commutative group, and let ${} k \in \mathbb{Z} {}$. Now let ${} \varphi:A\to{}A {}$, defined by ${} \varphi(a)=a^{k}$. Let ${} a,\, b \in A {}$. Then ${} \varphi(ab)=(ab)^{k}=a^{k}b^{k}=\varphi (a)\varphi (b) {}$, so $\varphi$ is a homomorphism. Now suppose that ${} k=-1$. Then if ${} \varphi(a)=\varphi (b) {}$, then $a^{-1}=b^{-1}$. Now we have
$$
a=ab^{-1}b=a a^{-1}b=b
$$So $\varphi$ is injective. 
Now let $a \in A {}$. There must exist some ${} a^{-1} \in A {}$. Now we have
$$
\varphi(a^{-1})=(a^{-1})^{-1}=a
$$
So $\varphi$ is surjective, so it is a automorphism.
23. 
Let $G$ be a group, and let $\sigma$ be an automorphism of $G$. We have ${} \sigma(g)=g {}$ iff ${} g=1$. Now suppose that ${} \sigma^{2}=1$ is the identity map. Let $a,\, b \in G$. Let $\varphi:G\to{}G {}$ be defined by ${} x\mapsto x^{-1}\sigma(x) {}$. If ${} \varphi(x)=1 {}$, then
$$
\begin{align}
 \varphi(x)=x^{-1}\sigma(x) & =1   \\
\sigma(x) & =x
 \end{align}
$$Which is a contradiction unless ${} x=1 {}$. Therefore, $x=1 {}$.
Now if ${} \varphi(a)=\varphi(b) {}$, then ${} a^{-1}\sigma(a)=b^{-1}\sigma(b) {}$. Now we have
$$
\begin{align}
a^{-1}\sigma(a) & =b^{-1}\sigma(b) \\
ba^{-1}\sigma(a)\sigma(b^{-1}) & =1 \\
(ab^{-1})\sigma(ab^{-1}) & =1 \\
\varphi(ab^{-1}) & =1
\end{align}
$$
So ${} ab^{-1}=1 {}$, or ${} a=b$. Therefore, $\varphi$ is injective. As $G$ is finite, and $\varphi:G\to{}G {}$, then $\varphi$ must also be surjective. Therefore, there exists some ${} x \in G {}$ such that for all ${} a \in G$, ${} a=x^{-1}\sigma(x) {}$. Now we have
$$
\begin{align}
a & =x^{-1}\sigma(x) \Rightarrow \sigma(x)=xa\\
\sigma(a) & =\sigma(x^{-1}\sigma(x)) \\
\sigma(a) & =\sigma(x)^{-1}x \\
\sigma(a)\sigma(x) & =x \\
\sigma(a)xa & =x
\end{align}
$$