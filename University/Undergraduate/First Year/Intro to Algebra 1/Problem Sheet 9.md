---
tags:
  - intro_algebra1
  - homework
date: 2023-12-03
completed: true
---
[[Directory]], [[Intro to Algebra 1|Subject Directory]]
[[IntroAlgebra HW9.pdf|Exercise Sheet]]
1. 
Let $G$ be a group, and let ${} \sim:G \times G\to{}G {}$ be a binary relation, with $x\sim y$ if there exists an isomorphism $\varphi:G\to{}G {}$ with ${} \varphi(x)=y {}$. We show that $\sim$ is an equivalence relation.

First, note that the identity isomorphism ${} \iota:G\to{}G {}$ with ${} \forall x \in G:\iota(x)=x {}$ implies that 
$$
x\sim x
$$
so $\sim$ is reflexive.
Then, if $x\sim y$, then there exists an isomorphism $\varphi:G\to{}G {}$ with ${} \varphi(x)=y {}$. Therefore, there exists an inverse of $\varphi$, $\varphi ^{-1}$, with ${} \varphi ^{-1}(y)=x {}$. Therefore, $y\sim x$, so $\sim$ is symmetric
Finally, if $x\sim y$ and $y\sim z$, then we have ${} \varphi,\, \psi:G\to{}G {}$ isomorphisms with ${} \varphi(x)=y {}$ and ${} \psi(y)=z {}$. Therefore, ${} \psi(\varphi(x))=z {}$. Since ${} \varphi,\, \psi {}$ are both isomorphisms, then $\psi \circ \varphi {}$ is also an isomorphism. Therefore, $x\sim z$, so $\sim$ is transitive. Therefore, $\sim$ is an equivalence relation.
2. 
Let $G$ and $H$ be groups with $\varphi:G\to{}H {}$ a group homomorphism. Let ${} K=\ker \varphi {}$. Let ${} g_{1},\, g_{2} \in G. {}$ 

First suppose that ${} g_{1} \in g_{2} K {}$. Then there exists some element ${} h \in G {}$ with ${} \varphi(h)=1 {}$ such that ${} g_{1}=g_{2}h {}$. Therefore, ${} \varphi(g_{1})=\varphi(g_{2} h)=\varphi(g_{2})\varphi (h)=\varphi(g_{2}) {}$. Therefore, ${} \varphi(g_{1})=\varphi (g_{2}) {}$.

Conversely, suppose ${} \varphi(g_{1})=\varphi (g_{2}) {}$. Then ${} \varphi(g_{2})^{-1}\varphi(g_{1})=1 {}$, so ${} \varphi(g_{2} ^{-1}g_{1})=1 {}$. Therefore, ${} g_{2} ^{-1}g_{1} \in K {}$. Therefore, ${} g_{1} = g_{2}h {}$ for some ${} h=g_{2} ^{-1}g_{1} \in K {}$. Therefore, ${} g_{1} \in g_{2} K {}$.

Therefore, ${} g_{1} \in g_{2} K {}$ if and only if ${} \varphi(g_{1})=\varphi (g_{2}) {}$.
