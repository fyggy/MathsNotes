---
tags:
  - linear_algebra2
  - homework
date: 2024-01-19
pset: 1
completed: true
---
[[Directory]], [[Linear Algebra and Geometry 2|Subject Directory]]
[[LAG2_HW1.pdf|Problem Sheet]]
1. skip
2. 
a)
Let ${} A\simeq B$ be matrices. Then
$$
A=QBQ^{-1}
$$
for some invertible matrix $Q {}$. Then
$$
\begin{align}
 \det(A) & =\det(QBQ^{-1})   \\
 & =\det(Q)\det (B) \det Q^{-1} \\
 & =\det (Q) \frac{1}{\det Q} \det (B) \\
 & =\det (B)
 \end{align}
$$
b)
Consider
$$
A=\begin{pmatrix}
0 & \phantom{0} & \phantom{0} & \phantom{0} \\
\phantom{0} & 0 & \phantom{0} & \phantom{0} \\
\phantom{0} & \phantom{0} & \ddots & \phantom{0} \\
\phantom{0} & \phantom{0} & \phantom{0} & 0
\end{pmatrix}
$$
and
$$
B=\begin{pmatrix}
1 \\
 & 1 \\
 &  & \ddots \\
 &  &  & 1 \\
 &  &  &  & 0
\end{pmatrix}
$$
Then ${} \det A=\det B=0 {}$, but ${} A\not\simeq B {}$, as ${} QAQ^{-1}=A {}$ for all $Q$.
c)
Let $A\simeq B$. Then
$$
A=QBQ^{-1}
$$
so
$$
A^{n}=\underbrace{ QBQ^{-1}QBQ^{-1}\dots QBQ^{-1} }_{ n\text{ times} }=QB^{n}Q^{-1}
$$
so ${} A^{n}\simeq B^{n} {}$
3. 
a)
$$
A\mathbf{v}=\lambda \mathbf{v}
$$

b)
Consider that
$$
A^{k}\mathbf{v}=A^{k-1}A\mathbf{v}=A^{k-1}\lambda \mathbf{v}=\lambda(A^{k-1}\mathbf{v})
$$
Therefore, the theorem follows from induction.
4. 
Let $A$ a matrix with ${} A^{k}=0 {}$ for some number $k$. Suppose $A$ is complex. Now, if $\mathbf{v}$ is an eigenvector of $A$ with eigenvalue $\lambda$, then $\mathbf{v}$ is an eigenvector of ${} A^{k}=0 {}$ with eigenvalue ${} \lambda^{k} {}$. Now ${} A^{k}\mathbf{v}=0 {}$, so ${} \lambda^{k}=0 {}$, so ${} \lambda=0 {}$.
5. 
a)
$$
A=\begin{pmatrix}1 & 4 \\ 3 & 2 \end{pmatrix} 
$$
so
$$
\begin{align}
 \chi_{A}(\lambda) & =\det(A-I\lambda)   \\
 & =\det \begin{pmatrix}
	1-\lambda & 4 \\
3 & 2-\lambda
\end{pmatrix} \\
 & =(1-\lambda)(2-\lambda)-4\cdot 3 \\
 & =2-3\lambda+\lambda^{2}-12 \\
 & =\lambda^{2}-3\lambda-10
 \end{align}
$$
Now if ${} \lambda^{2}-3\lambda-10=0 {}$, then 
$$
\begin{align}
 \lambda & =\frac{3\pm \sqrt{9+4\cdot 10}}{2}    \\
 & =\frac{ 3\pm7 }{ 2 }
 \end{align}
$$
so
$$
\lambda=5 \qquad \text{ or } \qquad \lambda=-2
$$
b)
$$
B= \begin{pmatrix}2024 & 2023 & 2022 \\ 0 & 2023 & 2022 \\ 0 & 0 & 2022 \end{pmatrix} 
$$
so
$$
\begin{align}
 \chi_{B}(\lambda) & =\det(B-\lambda I)   \\
 & =\det \begin{pmatrix}2024-\lambda & 2023 & 2022 \\ 0 & 2023-\lambda & 2022 \\ 0 & 0 & 2022-\lambda \end{pmatrix}  \\
 & =(2024-\lambda)(2023-\lambda)(2022-\lambda) \\
 \end{align}
$$
and the eigenvectors of $B$ are ${} 2024,\, 2023,\, 2022 {}$.
c)