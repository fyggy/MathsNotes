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
a (3−24) +b (2−11) +c (−113) =(3a+2b−c−2a−b+c4a+b+3c) =\mathbf{0}
$$
Then we have 
$$
\begin{align}
3a+2b-c & =0 \
-2a-b+c & =0 \
 \
a+b & =0
\end{align}
$$
and 
$$
\begin{align}
3a+2b-c & =0 \
4a+b+3c & =0 \
 \
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
a (3−24) +b (2−11) +c (−113) =(3a+2b−c−2a−b+c4a+b+3c) =(xyz) 
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
-2a-b+c=-2\cdot \frac{1}{6}(-4x-7y+z)-\frac{1}{6}(10x+13y-z)+c=y
\end{align}
$$
$$
\begin{align}
8x+14y-2z-10x-13y+z+6c & =6y \\
6c & =2x+5y+z \\
 c & =\frac{1}{6}(2x+5y+z)
\end{align}
$$
We now check:
$$
\begin{align}
 & \qquad a\mathbf{v}_{1} +b\mathbf{v}_{3}+c\mathbf{v}_{4}  \\
 & =\frac{1}{6}\left(\begin{pmatrix} -12x-21y+3z \\ 8x+14y-2z \\ -16x-28y+4z \end{pmatrix}+ \begin{pmatrix} 20x+26y-2z \\ -10x-13y+z \\ 10x+13y-z \end{pmatrix} +\begin{pmatrix} -2x-5y-z \\ 2x+5y+z \\ 6x+15y+3z \end{pmatrix} \right) \\
 & =\frac{1}{6} \begin{pmatrix} 6x \\ 6y \\ 6z \end{pmatrix}  \\
 & =\begin{pmatrix} x \\ y \\ z \end{pmatrix} 
\end{align}
$$
Therefore, ${} \mathbf{v}_{1},\, \mathbf{v}_{3},\, \mathbf{v}_{4} {}$ spans $\mathbb{R}^{3} {}$, so it is a basis of $\mathbb{R}^{3} {}$
d)
We showed in part a) that ${} \mathbf{v}_{2},\, \mathbf{v}_{3},\, \mathbf{v}_{4}$ is linearly dependent, as ${} 2\mathbf{v}_{3}-\mathbf{v}_{2}=3\mathbf{v}_{4} {}$. Now we show that it doesn't span ${} \mathbb{R}^{3} {}$. We can discard $\mathbf{v}_{2}$, as it is already in the span $\mathbf{v}_{3}$ and $\mathbf{v}_{4}$. However, we already saw in b) that $\mathbf{v}_{3}$ and $\mathbf{v}_{4}$ don't span $\mathbb{R}^{3} {}$.

2. 
a) i)
I claim that ${} \mathbf{e}_{1}={} (1,\, 0,\, -1),\, \mathbf{e}_{2}=(0,\, 1,\, -1) {}$ is a basis. Suppose we have some ${} \mathbf{v}=(x,\, y,\, z) \in  S {}$, therefore, ${} x+y+z=0 {}$. Therefore, ${} z=-x-y {}$, so we have ${} \mathbf{v}=(x,\, y,\, -x-y) {}$. 
We now show that the list spans. Note that ${} x (1,\, 0,\, -1)+y(0,\, 1,\, -1)=(x,\, y,\, -x-y)=\mathbf{v} {}$. Therefore, for some arbitrary vector $\mathbf{v}$ in ${} S$, there is a linear combination ${} \alpha \mathbf{e}_{1}+\beta \mathbf{e}_{2}=\mathbf{v} {}$. Therefore, ${} \span\{\mathbf{e}_{1},\, \mathbf{e}_{2}\}=S {}$. 
We now show linear independence. Suppose we have ${} a,\, b\in \mathbb{R} {}$ such that 
$$
a\mathbf{e}_{1}+b\mathbf{e}_{2}=a \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} +b \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}=\begin{pmatrix} a \\ b \\ -a-b \end{pmatrix} =\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} =\mathbf{0}
$$
Then we have ${} a=0 {}$ and ${} b=0$. Therefore, ${} \mathbf{e}_{1},\, \mathbf{e}_{2}$ are linearly independent. Therefore, ${} \mathbf{e}_{1},\, \mathbf{e}_{2}$ is a basis for $S$
ii)
I claim that ${} \mathbf{e}_{1}=(4,\, 2,\, 1) {}$ is a basis for $S$. 
First we show span. Note that if ${} \mathbf{v}=(x,\, y,\, z) \in  S {}$, then ${} \mathbf{v}=(4z,\, 2z,\, z) {}$. It is clear that ${} z (4,\, 2,\, 1)=\mathbf{v} {}$, so $\span\{\mathbf{e}_{1}\}=S$. Now since it is a singular vector, it must be linearly independent.
iii)
Given a vector ${} \mathbf{v}=(x,\, y,\, z) {}$, in order to be perpendicular to ${} (1,\, 1,\, 0) {}$, we must have
$$
\mathbf{v}\cdot (1,\, 1,\, 0)=x+y=0
$$
and in order to be perpendicular to ${} (2,\, 0,\, -1) {}$, we must have
$$
\mathbf{v}\cdot (2,\, 0,\, -1)=2x-z=0
$$
Therefore, we have
$$
y=-x
$$
and
$$
z=2x
$$
Therefore, we have 
$$
\mathbf{v}=\begin{pmatrix} x \\ -x \\ 2x \end{pmatrix}
$$
Therefore, i claim that ${} \mathbf{e}_{1}=\begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}  {}$ is a basis of $S$. Since every vector is of the form ${} \mathbf{v}=\begin{pmatrix} x \\ -x \\ 2x \end{pmatrix}  {}$, then we can write ${} \mathbf{v}=\begin{pmatrix} x \\ -x \\ 2x \end{pmatrix} =x \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix} =x\mathbf{e}_{1} {}$. Therefore, ${} \span\{\mathbf{e}_{1}\}=S {}$. Since it is just one vector, $\mathbf{e}_{1} {}$ is linearly independent. Therefore, ${} \mathbf{e}_{1} {}$ is a basis of $S$

b) i) we have 
$$
\mathbf{e}_{1}=\begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} ,\, \mathbf{e}_{2}=\begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix} 
$$
If we add another vector that is not in ${} S$, then it must necessarily still be linearly independent. We can repeat this until our vectors span $\mathbb{R}^{3}$. Observe that $(0,\, 0,\, 1)\notin S {}$, as if we have ${} a,\, b \in \mathbb{R} {}$ such that
$$
a \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} +b \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix} =\begin{pmatrix} a \\ b \\ -a-b \end{pmatrix} =\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} 
$$
Then ${} a=b=0$, but ${} -a-b=0\neq1 {}$. Therefore, we have a contradiction. Therefore, ${} (0,\, 0,\, 1)\notin S {}$. Therefore, we have a basis of size $3$ in $\mathbb{R}^{3}$, so it must be a basis of $\mathbb{R}^{3}$. 
ii)
We have
$$
\mathbf{e}_{1}=\begin{pmatrix} 4 \\ 2 \\ 1 \end{pmatrix} 
$$
We then see that $(1,\, 0,\, 0)\notin S$, as that would require ${} a \in  \mathbb{R} {}$ such that ${} a=0 {}$, ${} 2a=0$, and $4a=1$, which is clearly impossible. Now we see that ${} (0,\, 1,\, 0)\notin\span\{\mathbf{e}_{1},\, (1,\, 0,\, 0)\} {}$. Suppose we have ${} a,\, b \in \mathbb{R} {}$ such that
$$
a \begin{pmatrix} 4 \\ 2 \\ 1 \end{pmatrix} +b \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 4a+b \\ 2a \\ a \end{pmatrix} =\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} 
$$
Then we would have ${} a=0$, but ${} 2a=1 {}$, which is clearly impossible. Therefore, $$
\begin{pmatrix} 4 \\ 2 \\ 1 \end{pmatrix} ,\, \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} ,\, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
$$
Is linearly independent 3 dimensional basis inside ${} \mathbb{R}^{3}$. Therefore, it is a basis of $\mathbb{R}^{3}$
iii)
We have
$$
\mathbf{e}_{1}=\begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix} 
$$
We see that ${} (0,\, 1,\, 0)\notin S {}$, as that would require a ${} a \in \mathbb{R} {}$ such that ${} a=0 {}$, but ${} -a=1 {}$. We now see that $(0,\, 0,\, 1)\notin \span\{\mathbf{e}_{1},\, (0,\, 1,\, 0)\}$. Suppose we have ${} a,\, b \in  \mathbb{R} {}$ such that
$$
a \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} +b\mathbf{e}_{1}=\begin{pmatrix} b \\ a-b \\ 2b \end{pmatrix} =\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} 
$$
This requires ${} b=0$, but ${} 2b=1 {}$, which is impossible. Therefore, ${} \mathbf{e}_{1},\, (0,\, 1,\, 0),\, (0,\, 0,\, 1) {}$ is linearly independent inside $\mathbb{R}^{3}$, so we have ${} \mathbf{e}_{1},\, (0,\, 1,\, 0),\, (0,\, 0,\, 1) {}$ as a basis of $\mathbb{R}^{3}$.

3.
a)
We start with all of the vectors, and reduce until they're linearly independent. Notice that 
$$
\mathbf{v}_{1}+\mathbf{v}_{5}=\begin{pmatrix} 1 \\ -1 \\ 0 \\ 0 \end{pmatrix} +\begin{pmatrix} 0 \\ 1 \\ 0 \\ -1 \end{pmatrix} =\begin{pmatrix} 1 \\ 0 \\ 0 \\ -1 \end{pmatrix} =\mathbf{v}_{3}
$$
So we can eliminate ${} \mathbf{v}_{3} {}$. Now notice that
$$
\mathbf{v}_{1}+\mathbf{v}_{4}=\begin{pmatrix} 1 \\ -1 \\ 0 \\ 0 \end{pmatrix} +\begin{pmatrix} 0 \\ 1 \\ -1 \\ 0 \end{pmatrix} =\begin{pmatrix} 1 \\ 0 \\ -1 \\ 0 \end{pmatrix} =\mathbf{v}_{2}
$$
So we can eliminate ${} \mathbf{v}_{2} {}$. Finally, notice that 
$$
\mathbf{v}_{5}-\mathbf{v}_{4}=\begin{pmatrix} 0 \\ 1 \\ 0 \\ -1 \end{pmatrix} -\begin{pmatrix} 0 \\ 1 \\ -1 \\ 0 \end{pmatrix} =\begin{pmatrix} 0 \\ 0 \\ 1 \\ -1 \end{pmatrix} =\mathbf{v}_{6}
$$
So we can eliminate $\mathbf{v}_{6} {}$. Now let ${} a_{1},\, a_{4},\, a_{5}$ such that
$$
\begin{align}
a_{1}\mathbf{v}_{1}+a_{4}\mathbf{v}_{4}+a_{5}\mathbf{v}_{5}=\begin{pmatrix} a_{1} \\ -a_{1}+a_{4}+a_{5} \\ -a_{4} \\ -a_{5} \end{pmatrix}  =\begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} 
\end{align}
$$
Now we have ${} a_{1}=0$, ${} a_{4}=0 {}$ and ${} a_{5}=0 {}$, clearly. Therefore, this list in linearly independent. 
b)
Since the largest list of linearly independent vectors in ${} \mathbf{v}_{1},\,\dots,\,\mathbf{v}_{6}$ is of size 3, then the dimension of ${} \span\{\mathbf{v}_{1},\,\dots,\,\mathbf{v}_{6}\}$ must be $3$.

4. The dimension can either be:
Dimension 1: ${} \mathbf{v}_{1}=(1,\, 0,\, 0,\, 0) {}$, ${} \mathbf{v}_{2}=(2,\, 0,\, 0,\, 0) {}$, ${} \mathbf{v}_{3}=(3,\, 0,\, 0,\, 0)$
Dimension 2: ${} \mathbf{v}_{1}=(1,\, 0,\, 0,\, 0) {}$, ${} \mathbf{v}_{2}=(0,\, 1,\, 0,\, 0) {}$, ${} \mathbf{v}_{3}=(2,\, 0,\, 0,\, 0) {}$
Dimension 3: ${} \mathbf{v}_{1}=(1,\, 0,\, 0,\, 0) {}$, ${} \mathbf{v}_{2}=(0,\, 1,\, 0,\, 0) {}$, ${} \mathbf{v}_{3}=(0,\, 0,\, 1,\, 0)$

5. 
a) Since ${} \mathbf{v}_{1},\,\dots,\,\mathbf{v}_{m} {}$ are linearly independent, then if there exist ${} \alpha_{1},\,\dots,\,\alpha_{m}\in \mathbb{F}$ such that 
$$
\alpha_{1}\mathbf{v}_{1}+\alpha_{2}\mathbf{v}_{2}+\dots+\alpha_{m}\mathbf{v}_{m}=\mathbf{0}
$$then ${} \alpha_{1}=\alpha_{2}=\dots=\alpha_{m}=0 {}$. Now if ${} \beta=0 {}$, then
$$
\alpha_{1}\mathbf{v}_{1}+\alpha_{2}\mathbf{v}_{2}+\dots+\alpha_{m}\mathbf{v}_{m}+\beta \mathbf{u}=\alpha_{1}\mathbf{v}_{1}+\dots+\alpha_{m}\mathbf{v}_{m}=\mathbf{0}
$$so by above, then ${} \alpha_{1}=\alpha_{2}=\dots=\alpha_{m}=0$.

b)
Suppose that $\beta\neq 0 {}$. Then we can rearrange such that
$$
-\beta \mathbf{u}=\alpha_{1}\mathbf{v}_{1}+\dots+\alpha_{m}\mathbf{v}_{m}
$$
so
$$
\mathbf{u}=-\frac{\alpha_{1}}{\beta}\mathbf{v}_{1}-\frac{\alpha_{2}}{\beta}\mathbf{v}_{2}-\dots-\frac{\alpha_{m}}{\beta}\mathbf{v}_{m}
$$
Since ${} -{} \frac{\alpha_{n}}{\beta}\in \mathbb{F}$ for all $n$, then this implies that ${} \mathbf{u} \in  \span\{\mathbf{v}_{1},\,\dots,\,\mathbf{v}_{m}\}$. However, this is a contradiction. Therefore, $\beta=0$.

c)
Since $\beta$ necessarily must be $0$, by b), then by a), we have ${} \alpha_{1}=\alpha_{2}=\dots=\alpha_{m}=0 {}$, so all the coefficients must be $0$. Therefore, ${} \mathbf{v}_{1},\, \mathbf{v}_{2},\,\dots,\,\mathbf{v}_{m},\, \mathbf{u}$ must be linearly independent.

6. 
The proof is not correct. In particular, the step that any basis of $V$ can be reduced to a basis of $U {}$ is incorrect. It is in fact possible that ${} U {}$ contains none of the vectors of a chosen basis of ${} V$, for example. Consider the space ${} \mathbb{R}^{2} {}$, and a subspace $\{ (x,\, y)\in \mathbb{R}^{2}\mid x=y \}$. If you chose the basis ${} \{ (1,\, 0),\, (0,\, 1) \} {}$ for $\mathbb{R}^{2}$, then this is not in the subspace.

Instead, we work the other way, and show that any basis of $U$ can be completed to be a basis of $V$. The proof will look like this:
Let ${} \{ \mathbf{e}_{1},\,\dots,\,\mathbf{e}_{n} \} {}$ be a basis of $U$ so that $\dim U=n {}$. 
If ${} \span\{\mathbf{e}_{1},\,\dots,\,\mathbf{e}_{n}\}=V$, then we're done, and ${} U=V {}$, so $\dim U=\dim V$. Otherwise, we can add a vector ${} \mathbf{u}\in V\setminus U {}$. By above, ${} \{ \mathbf{e}_{1},\,\dots,\,\mathbf{e}_{n},\, \mathbf{u} \} {}$ is still linearly independent in ${} V$. 
We now repeat this, adding more and more vectors until the vectors span $V$. Then, we will have a basis of $V$ such that a subset is a basis of $U$. Therefore, $\dim V\geq n=\dim U$, as required.
