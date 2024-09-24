---
tags:
  - linear_algebra2
  - homework
date: 2024-02-04
pset: 2
completed: true
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
So $A {}$ has eigenvalues ${} 1,\, 3 {}$. Now note that 
$$
\begin{align}
 (A-I)(A-3I) & =A^{2}-4A+3I   \\
 & =\begin{pmatrix}1 & 1 & 0 \\ 1 & 2 & 1 \\ 1 & -1 & 2 \end{pmatrix} ^{2}-\begin{pmatrix}4 & 4 & 0 \\ 4 & 8 & 4 \\ 4 & -4 & 8 \end{pmatrix} +\begin{pmatrix}3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3 \end{pmatrix}  \\
 & =\begin{pmatrix}2-4+3 &  &  \\  &  &  \\  &  &  \end{pmatrix} \substack{\text{ other values not }\\\text{ included for brevity}}  \\ 
 & =\begin{pmatrix}1 &  &  \\  &  &  \\  &  &  \end{pmatrix} \neq 0
 \end{align}
$$
Therefore, ${} (A-I)(A-3I)\neq 0 {}$, so the minimal polynomial $\mu {}$ of ${} A {}$ is $\chi$. Therefore, $A$ is not semisimple, so $A {}$ is not diagonalisable.
b)
We see that the characteristic polynomial of $A$ is 
$$
\begin{align}
\chi(\lambda) & =\det(A-\lambda I) \\
 & =\det \begin{pmatrix}-\lambda & 3 & -2 \\ 2 & -1-\lambda & 2 \\ 1 & -3 & 3-\lambda \end{pmatrix}  \\
 & =-\lambda \det \begin{pmatrix}-1-\lambda & 2 \\ -3 & 3-\lambda \end{pmatrix} -3 \det \begin{pmatrix}2 & 2 \\ 1 & 3-\lambda \end{pmatrix} -2 \det \begin{pmatrix}2 & -1-\lambda \\ 1 & -3 \end{pmatrix}  \\
 & =\lambda((1+\lambda)(3-\lambda)-6)-3(6-2\lambda-2)+2(6-(1+\lambda)) \\
 & =\lambda(3+2\lambda-\lambda^{2}-6)-12+6\lambda+10-2\lambda \\
 & =-\lambda^{3}+2\lambda^{2}-3\lambda-2+4\lambda \\
 & =-\lambda+2\lambda^{2}+1\lambda-2 \\
 & =-(\lambda-2)(\lambda-1)(\lambda+1)
\end{align}
$$
Therefore, $A$ has $3$ distinct eigenvalues, so there exist $3 {}$ linearly independent eigenvectors of $A$. Therefore, $A {}$ has an eigenbasis, so it is diagonalisable. Now we find appropriate eigenvectors. For ${} \lambda=2 {}$ we solve
$$
\begin{align}
\left(\begin{array}{ccc|ccc}
-2 & 3 & -2 & 0 \\
2 & -1-2 &  2 & 0 \\
1 & -3 & 3-2 & 0
\end{array}\right)\Rightarrow  \left(\begin{array}{ccc|c}
-2 & 3 & -2 & 0 \\
0 & 0 & 0 & 0 \\
0 & -3 & 0 & 0
\end{array}\right)\Rightarrow \left(\begin{array}{ccc|c}
-2 & 0 & -2 & 0 \\
0 & 0 & 0 & 0 \\
0 & -3 & 0 & 0
\end{array}\right)
 \end{align}
$$
So now ${} x+z=0 {}$ and ${} y=0 {}$. Therefore, ${} (1,\, 0,\, -1) {}$ is an eigenvalue corresponding to the eigenvalue ${} 2 {}$.

Now for ${} \lambda=1 {}$ we solve
$$
\begin{gather}
\left(\begin{array}{ccc|c}
-1 & 3 & -2 & 0 \\
2 & -1-1 & 2 & 0 \\
1 & -3 & 3-1 & 0
\end{array}\right)
\Rightarrow 
\left(\begin{array}{ccc|c}
-1 & 3 & -2 & 0 \\
0 & 4 & -2 & 0 \\
0 & 0 & 0 & 0
\end{array}\right)\Rightarrow 
\left(\begin{array}{ccc|c}
-1 & -3 & -2 & 0 \\
0 & 1& -0.5 & 0 \\
0 & 0 & 0 & 0
\end{array}\right)
\\
\Rightarrow \left(\begin{array}{ccc|c}
1 & 0 & 0.5 & 0 \\
0 & 1 & -0.5 & 0 \\
0 & 0 & 0 & 0
\end{array}\right)
\end{gather}
$$
So we have ${} 2x+z=0 {}$ and ${} 2y-z=0 {}$. Therefore, ${} (-1,\, 1,\, 2) {}$ is an eigenvector corresponding to the eigenvalue ${} 1$.

Finally, for ${} \lambda=-1 {}$ we solve
$$
\begin{gather}
\left(\begin{array}{ccc|c}
1 & 3 & -2 & 0 \\
2 & 0 & 2 & 0 \\
1 & -3 & 4 & 0
\end{array}\right)\Rightarrow 
\left(\begin{array}{ccc|c}
1 & 3 & -2  & 0\\
0 & -6 & 6  & 0\\
0 & -6 & 6 & 0
\end{array}\right)
\Rightarrow \left(\begin{array}{ccc|c}
1 & 3 & -2 & 0 \\
0 & 1 & -1 & 0 \\
0 & 0 & 0 & 0
\end{array}\right) \\
\Rightarrow  \left(\begin{array}{ccc|c}
1 & 0 & 1 & 0 \\
0 & 1 & -1 & 0 \\
 0& 0 & 0 & 0
\end{array}\right)
\end{gather}
$$
Therefore, ${} x+z=0 {}$ and ${} y=z {}$. Therefore, ${} (-1,\, 1,\, 1) {}$ is an eigenvector corresponding to the eigenvalue ${} -1 {}$. 

Therefore, let ${} Q=\begin{pmatrix}1 & -1 & -1 \\ 0 & 1 & 1 \\ -1 & 2 & 1 \end{pmatrix}  {}$. Now
$$
Q^{-1}AQ=\begin{pmatrix}2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{pmatrix} 
$$
is diagonal.