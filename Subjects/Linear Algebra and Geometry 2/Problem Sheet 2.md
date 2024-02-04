---
tags:
  - linear_algebra2
  - homework
date: 2024-02-04
pset: 2
completed:
---
[[Directory]], [[Linear Algebra and Geometry 2|Subject Directory]]
[[LinearAlgGeo2 HW2.pdf|Problem Sheet]]
2. 
a)
We see that the characteristic polynomial of ${} A=\begin{pmatrix}2 & 2 \\ 0 & 2 \end{pmatrix}  {}$ is
$$
\det(A-I\lambda)=\det \begin{pmatrix}2-\lambda & 2   \\ 0 & 2-\lambda \end{pmatrix} =\lambda^{2}-4\lambda+4
$$
Which has roots ${} \lambda=2 {}$, repeated twice. Now if ${} \mathbf{v}=\begin{pmatrix} x \\ y \end{pmatrix}  {}$, we have
$$
\begin{align}
 A\mathbf{v} & =2\mathbf{v}  \\
 \begin{pmatrix}2 & 2 \\ 0 & 2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}  &  = \begin{pmatrix} 2x \\ 2y \end{pmatrix}  \\
 \begin{pmatrix} 2x+2y \\ 2y \end{pmatrix} & =\begin{pmatrix} 2x \\ 2y \end{pmatrix} 
 \end{align}
$$
Therefore, ${} 2y=0 {}$, and $x$ is free. Therefore