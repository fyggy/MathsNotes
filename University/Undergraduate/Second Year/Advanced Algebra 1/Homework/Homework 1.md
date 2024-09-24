---
tags:
  - homework
  - advalg1
date: 2024-09-23
pset: 1
completed: false
---
[[Directory]], [[University/Undergraduate/Second Year/Advanced Algebra 1/Advanced Algebra 1|Subject Directory]]
[[University/Undergraduate/Second Year/Advanced Algebra 1/Homework/Homework 1|🞀🞀]] [[|◀]] [[University/Undergraduate/Second Year/Advanced Algebra 1/Homework/Homework 2|▶]] [[University/Undergraduate/Second Year/Advanced Algebra 1/Homework/Homework 11|🞂🞂]]

[[University/Undergraduate/Second Year/Advanced Algebra 1/Homework/Worksheets/advanced_algebra_1.pdf|Worksheet]]
1. Let $G {}$ be a group and let ${} S \subseteq G {}$
a)
Let $\mathcal{A} {}$ be a non-empty set of subgroups of $G {}$. Set
$$
A=\bigcap_{H\in \mathcal{A}}H 
$$
Now let ${} x,\, y \in A {}$. Then ${} x,\, y \in H {}$ for all ${} H \in \mathcal{A} {}$. Since all the $H {}$ are subgroups, then ${} xy^{-1} \in H {}$, and therefore ${} xy^{-1} \in A {}$. Therefore, $A {}$ is a subgroup of $G {}$
b)
Let ${} \mathcal{A}_{S}=\{ H\leq G \mid S \subseteq H \} {}$, and set
$$
\langle S \rangle =\bigcap_{H\in \mathcal{A}_{S}} H 
$$
First note that since ${} S \subseteq H {}$ for all ${} H \in  \mathcal{A}_{S} {}$, then ${} S \subseteq  \langle S \rangle  {}$. Now suppose that ${} H\leq G {}$ with ${} S\subseteq H {}$. Since ${} H \in  \mathcal{A}_{S} {}$, then ${} \langle S \rangle \subseteq H {}$. Therefore, ${} \langle S \rangle  {}$ is the smallest subgroup of $G {}$ containing $S {}$.
c)
Since ${} \varnothing \subseteq H {}$ for all subgroups ${} H\leq G {}$, then ${} A_{\varnothing}=\{ S \subseteq G \mid  S\leq  G \} {}$. Therefore, ${} \langle \varnothing \rangle=\bigcup_{S\leq  G}  S=\{ 1 \}=1 {}$ 
d)
Clearly, ${} \langle S \rangle \leq  \mathrm{SL}_{2}(\mathbb{R}) {}$. Now suppose that ${} \langle S \rangle \leq H {}$ for some ${} H\leq \mathrm{GL}_{2}(\mathbb{R}) {}$
$$
d=\frac{ 1+bc }{ a }
$$
$$
\begin{align}
 \det  \begin{pmatrix}a-\lambda & b \\ c & d-\lambda \end{pmatrix}  & =(a-\lambda)(d-\lambda)-bc   \\
 & =ad-(a+d)\lambda +\lambda^{2}-b c \\
 & =\lambda^{2}-(a+d)\lambda+1 \\ \\

 \end{align}
$$
$$
\begin{align}
\lambda^{2}-(a+d)\lambda+1  & =0 \\
\lambda & =\frac{ (a+d)\pm \sqrt{(a+d)^{2}-4} }{ 2 }
\end{align}
$$
$$
\begin{pmatrix}a & b \\ c & d \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} =\lambda \begin{pmatrix} x \\ y \end{pmatrix} =\begin{pmatrix} ax+by \\ cx+dy \end{pmatrix} 
$$
