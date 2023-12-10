---
tags:
  - linear_algebra1
  - homework
date: 2023-12-10
---
[[Directory]], [[Linear Algebra and Geometry 1|Subject Directory]]
3. 
Let ${} a=\det A {}$. Then
a) 
${} \det (B)=2\cdot 3\cdot 5\det(A)=30\det(A) {}$
b)
${} \det (B)=3\cdot 4\cdot 5\det(A)=60\det(A) {}$
4. 
a)
False, as 
$$
\det\left(  \begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}+\begin{pmatrix}a & b \\ c & d \end{pmatrix}  \right)=(a+1)(d+1)-bc=ad+a+d+1-bc
$$
and
$$
1+\det \begin{pmatrix}a & b \\ c & d \end{pmatrix} =ad-bc+1
$$we have that
$$
ad-bc+1=ad-bc+a+d+1
$$
iff ${} a+d=0 {}$. Therefore, this does not hold.
b)
Observe that ${} AB=D {}$ for some matrix ${} D {}$. Then
$$
\det(ABC)=\det(DC)=\det(AB)\det(C)=\det(A)\det(B)\det(C)
$$
c)
False, note that
$$
\det \left(4\begin{pmatrix}1 & 0 \\ 0 & 1 \end{pmatrix} \right)=16\neq 4=4\det \begin{pmatrix}1 & 0 \\ 0 & 1 \end{pmatrix} 
$$
d)
False. Set 
$$
A= \begin{pmatrix} 0& 1 \\ 0 & 1 \end{pmatrix} ,\, B=\begin{pmatrix}0 & 0 \\ 1 & 1 \end{pmatrix} 
$$
and observe that
$$
AB-BA=\begin{pmatrix}1 & 1 \\ 1 & 1 \end{pmatrix} -\begin{pmatrix}0 & 0 \\ 0 & 2 \end{pmatrix} =\begin{pmatrix}1 & 1 \\ 1 & -1 \end{pmatrix}
$$
and 
$$
\det \begin{pmatrix}1 & 1 \\ 1 & -1 \end{pmatrix} =-2\neq 0
$$
