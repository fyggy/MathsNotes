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
I just take straight from my scratch work, and by setting ${} a=1 /6(-4x-7y+z) {}$, $b=1 /18 (-2x-5y-z) {}$, and ${} c=1 /18(34x+49y-z) {}$, then we have
$$
\begin{align}
 &\qquad   \frac{1}{6} \begin{pmatrix} -12x-21y+3z \\ 8x+14y-2z \\ -16x-28y+4z \end{pmatrix} +\frac{1}{18}\begin{pmatrix} -14x-35y-7z \\ 10x+25y+5z \\ 14x+35y+7z \end{pmatrix} +\frac{1}{18}\begin{pmatrix} 68x+98y-2z \\ -34x-49y+z \\ 34x+49y-z \end{pmatrix}  \\
 & =\frac{1}{18}\left( \begin{pmatrix} -36x-63y+9z \\ 24x+42y-6z \\ -48x-84y+12z \end{pmatrix} +\begin{pmatrix} -14x-35y-7z \\ 10x+25y+5z \\ 14x+35y+7z \end{pmatrix} +\begin{pmatrix} 68x+98y-2z \\ -34x-49y+z \\ 34x+49y-z \end{pmatrix} \right) \\
 & =\frac{1}{18} \begin{pmatrix} 18x \\ 18y \\ 18z \end{pmatrix}  \\
 & =\begin{pmatrix}  x \\ y \\ z \end{pmatrix} 
\end{align}
$$
Therefore, it does span.
b) This set does not span ${} \mathbb{R}^{3} {}$, as note that, given ${} a,\, b \in \mathbb{R} {}$, we have
$$
a \begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix} +b \begin{pmatrix} -1 \\ 1 \\ 3 \end{pmatrix} =\begin{pmatrix} 2a-b \\ -a+b \\ a+3b \end{pmatrix} 
$$
Now we show that ${} \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}  {}$ is not in the span, if ${} -a+b=0 {}$, then ${} a=b {}$, so ${} 2a-b=a=1$, but $a+3b=4a=4\neq 1$. Therefore, they do not span $\mathbb{R}^{3}$, and cannot be a basis. Now we show that they are linearly independent. Suppose we have $a,\, b \in  \mathbb{R}$ such that
$$
\begin{align}
a \begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix} +b \begin{pmatrix} -1 \\ 1 \\ 3 \end{pmatrix} =\begin{pmatrix} 2a-b \\ -a+b \\ a+3b \end{pmatrix} =\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} =\mathbf{0}
\end{align}
$$
Then we have ${} a=b {}$, and ${} 2a-b=2a-a=a=0$, so $b=a=0 {}$. Therefore, this is only possible if $a=b=0$, so $\mathbf{v}_{3}$ and $\mathbf{v}_{4}$ are linearly independent.
c)
First we show that ${} \mathbf{v}_{1},\, \mathbf{v}_{3},\, \mathbf{v}_{4} {}$ are linearly independent. Suppose we have ${} a,\, b,\,  c \in \mathbb{R} {}$ such that
$$
a \begin{pmatrix} 3 \\ -2 \\ 4 \end{pmatrix} +b \begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix} +c \begin{pmatrix} -1 \\ 1 \\ 3 \end{pmatrix} =\begin{pmatrix} 3a+2b-c \\ -2a-b+c \\ 4a+b+3c \end{pmatrix} =\mathbf{0}
$$
Then we have 
$$
\begin{align}
3a+2b-c & =0 \\
-2a-b+c & =0 \\
 \\
a+b & =0
\end{align}
$$
and 
$$
\begin{align}
3a+2b-c & =0 \\
4a+b+3c & =0 \\
 \\
13a+7b & =0
\end{align}
$$
so
$$
6a=0,\, a=0
$$
and
$$
0+b=0,\, b=0
$$
Therefore, we have
$$
4a+b+3c=0+0+c=c=0
$$
So ${} a=b=c=0 {}$, so the list is linearly independent.
Now we show spanning. Let ${} \mathbf{w}=(x,\, y,\, z)\in \mathbb{R}^{3} {}$. Now we have
$$
\begin{align}
a \begin{pmatrix} 3 \\ -2 \\ 4 \end{pmatrix} +b \begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix} +c \begin{pmatrix} -1 \\ 1 \\ 3 \end{pmatrix} =\begin{pmatrix} 3a+2b-c \\ -2a-b+c \\ 4a+b+3c \end{pmatrix} =\begin{pmatrix} x \\ y \\ z \end{pmatrix} 
\end{align}
$$
So we have ${} a+b=x+y {}$ and $13a+7b=3x+z$. Therefore, ${} -7a-7b=-7x-7y {}$, so
$$
\begin{align}
6a & =-4x-7y+z \\
a & =\frac{1}{6}(-4x-7y+z)
\end{align}
$$
Now we have 
$$
\begin{align}
a+b=\frac{1}{6}(-4x-7y+z)+b & =x+y \\
-4x-7y+z+6b & =6x+6y \\
 6b & =10x+13y-z \\
b & =\frac{1}{6}(10x+13y-z)
\end{align}
$$
Finally we have
$$
\begin{align}
-2a-b+c=-2\cdot \frac{1}{6}(-4x-7y+z)-\frac{1}{6}(10x-y-z)+c=y
\end{align}
$$
$$
\begin{align}
8x+14y-2z-10x+y+z+6c & =6y \\
6c & =2x-9y+z \\
 c & =\frac{1}{6}(2x-9y+z)
\end{align}
$$
We now check:
$$
\begin{align}
 & \qquad a\mathbf{v}_{1} +b\mathbf{v}_{3}+c\mathbf{v}_{4}  \\
 & =\frac{1}{6}\left(\begin{pmatrix} -12x-21y+3z \\ 8x+14y-2z \\ -16x-28y+4z \end{pmatrix}+ \begin{pmatrix} 20x-2y-2z \\ -10x+y+z \\ 10x-y-z \end{pmatrix} +\begin{pmatrix} -2x+9y-z \\ 2x-9y+z \\ 6x-27y+3z \end{pmatrix} \right) \\
 & =\frac{1}{6} \begin{pmatrix} 6x-14y \\ 6y \\ -56y+6z \end{pmatrix} 
\end{align}
$$