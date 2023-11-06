---
tags:
  - homework
  - linear_algebra1
date: 2023-11-06
---
[[Directory]], [[Linear Algebra and Geometry 1|Subject Directory]]
[[LinearAlgGeo1 HW5.pdf|Problem Sheet]]
1. 
a)
This set is not linearly independent, as note that
$$
\begin{align}
 0 \begin{pmatrix} 3 \\ -2 \\ 4 \end{pmatrix} - \begin{pmatrix} 7 \\ -5 \\ -7 \end{pmatrix} +2\begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix} -3\begin{pmatrix} -1 \\ 1 \\ 3 \end{pmatrix}  & =\begin{pmatrix} -7+4+3 \\ 5-2-3  \\ 7+2-9 \end{pmatrix}   \\
 & =\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}  \\
 & =\mathbf{0}
 \end{align}
$$
Therefore, this set cannot be a basis. Now we show that it spans ${} \mathbb{R}^{3} {}$. 
Let $\mathbf{w}=(x,\, y,\, z)\in \mathbb{R}^{3} {}$. We set the coefficient on $\mathbf{v}_{4} {}$ to $0 {}$ as it is the "extraneous" term, and is not needed to span. Now we have
$$
a \begin{pmatrix} 3 \\ -2 \\ 4 \end{pmatrix} +b \begin{pmatrix} 7 \\ -5 \\ -7 \end{pmatrix} +c \begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix} =\begin{pmatrix} x \\ y \\ z \end{pmatrix} 
$$
I just take straight from my scratch work, and by setting ${} a=1 /6(-4x+3y+z) {}$, $b=1 /18 (-2x-5y-z) {}$, and ${} c=1 /9(22x+13y+2z) {}$, then we have
$$
\begin{align}
\frac{1}{6} \begin{pmatrix} -12x+9y+3z \\ 8x-6y-2z \\ -16x+12y+4z \end{pmatrix} +
\end{align}
$$
b) This set does not span ${} \mathbb{R}^{3} {}$, as note that, given ${} a,\, b \in \mathbb{R} {}$, we have
$$
a \begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix} +b \begin{pmatrix} -1 \\ 1 \\ 3 \end{pmatrix} =\begin{pmatrix} 2a-b \\ -a+b \\ a+3b \end{pmatrix} 
$$
Now we show that ${} \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}  {}$ is not in the span, if ${} -a+b=0 {}$, then ${} a=b {}$, so ${} 2a-b=a=1$, but $a+3b=4a=4\neq 1$. Therefore, they do not span $\mathbb{R}^{3}$, and cannot be a basis