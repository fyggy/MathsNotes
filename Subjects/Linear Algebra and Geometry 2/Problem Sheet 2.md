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
So we see that $\lambda$ is an eigenvalue, repeated twice. Now the associated eigenspace is 
$$
\ker (A-I\lambda)=\ker \begin{pmatrix}0 & 2 \\ 0 & 0 \end{pmatrix} 
$$
has dimension 1. Therefore, there can be at most 1 linearly independent eigenvector, so there is no eigenbasis for $A$, so $A$ is not diagonalisable. 
b)
We see that the characteristic polynomial of ${} A=\begin{pmatrix}1 & 5 \\ 5 & 1 \end{pmatrix}  {}$ is
$$
\chi(\lambda)=\det(A-I\lambda)=\det \begin{pmatrix}1 - \lambda & 5   \\ 5 & 1-\lambda \end{pmatrix} =(1-\lambda)^{2}-25=\lambda^{2}-2\lambda-24
$$
So ${} \chi(\lambda)=(\lambda-6)(\lambda-4) {}$. Now we have 2 distinct eigenvalues, so we must have 2 linearly independent eigenvectors. Therefore, there exists an eigenbasis for $A$, and so $A {}$ is diagonalisable. 
b)
We see that the characteristic polynomial of ${} A=\begin{pmatrix}-1 & 4 \\ 2 & 1 \end{pmatrix}  {}$ is
$$
\chi(\lambda)=\det(A-I\lambda )=\det \begin{pmatrix}-1-\lambda & 4 \\ 2 & 1-\lambda \end{pmatrix} =\lambda^{2}-1-8=\lambda^{2}-9
$$
So ${} \chi(\lambda)=(\lambda-3)(\lambda+3) {}$ so there are ${} 2 {}$ distinct eigenvalues, so there must exist 2 linearly independent eigenvectors. Therefore, there exists an eigenbasis for ${} A$, and so $A$ is diagonalisable.
5. 
We see that the characteristic polynomial of $A$ is 
$$
\begin{align}
\chi(\lambda) & =\det (A-\lambda I ) \\
 & =\det \begin{pmatrix}1-\lambda & 1 & 0 \\ 1 & 2-\lambda & 1 \\ 1 & -1 & 2-\lambda \end{pmatrix}  \\
 & =0 \cdot \det \begin{pmatrix}1 & 2-\lambda \\  1& -1 \end{pmatrix} -1\cdot  \det \begin{pmatrix}1 & 1 \\ 1 & 2-\lambda \end{pmatrix} +(1-\lambda)\cdot  \det \begin{pmatrix}2-\lambda & 1 \\ -1 & 2-\lambda \end{pmatrix}  \\
 & =(1-\lambda)((2-\lambda)^{2})-((2-\lambda)-1) \\
 & =(\lambda^{2}-4\lambda+4)(1-\lambda)-(1-\lambda) \\
 & =(\lambda^{2}-4\lambda+3)(1-\lambda) \\
 & =\lambda^{2}-4\lambda+3-\lambda^{3}+4\lambda^{2}-3\lambda \\
 & =-\lambda+5\lambda^{2}-7\lambda+3 \\
 & =\left(\lambda-1\right)^{2}\left(3-\lambda\right)
\end{align}
$$
