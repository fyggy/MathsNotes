---
tags:
  - linear_algebra1
  - homework
date: 2023-10-15
pset: 3
completed: true
---
[[Directory]], [[Linear Algebra and Geometry 1|Subject Directory]]
1. 
a) Is not defined, as you cannot add a scalar and a vector
b) Is defined
c) Is not defined, as vector division is not defined
d) not defined, as you cannot subtract a vector from a scalar
e) is defined
f) is not defined, as you cannot take the dot product of a scalar and a vector

2. 
a) i)
$$
\begin{align}
\frac{1}{3}(3\mathbf{v}_{1}-4\mathbf{v}_{2}+2\mathbf{v}_{3}) & =\frac{1}{3}\left( \begin{pmatrix} 6 \\ -3 \\ 3 \end{pmatrix} +\begin{pmatrix} 12 \\ -20 \\ 0 \end{pmatrix} +\begin{pmatrix} 0 \\ 0 \\ 12 \end{pmatrix}  \right) \\
 & =\frac{1}{3}\left( \begin{pmatrix} 6+12+0 \\ -3-20+0 \\ 3+0+12 \end{pmatrix}  \right) \\
 &= \frac{1}{3}\begin{pmatrix} 18 \\ -23 \\ 15 \end{pmatrix} \\
 & =\begin{pmatrix} 6 \\ -\frac{23}{3} \\ 5 \end{pmatrix} 
\end{align}
$$
ii) 
$$
\begin{align}
\frac{1}{2}(\mathbf{v}_{2}-\mathbf{v}_{1})+4(\mathbf{v}_{4}-\mathbf{v}_{1}) & =\frac{1}{2}\left( \begin{pmatrix} -3 \\ 5 \\ 0 \end{pmatrix} -\begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix}  \right)+4\left( \begin{pmatrix} 4 \\ -3 \\ -1 \end{pmatrix} -\begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix}  \right) \\
 & =\frac{1}{2}\begin{pmatrix} -5 \\ 6 \\ -1 \end{pmatrix} +4\begin{pmatrix} 2 \\ -2 \\ -2 \end{pmatrix}  \\
 & =\begin{pmatrix} -5/2 \\ 3 \\ -1/2 \end{pmatrix} +\begin{pmatrix} 8 \\ -8 \\ -8 \end{pmatrix}  \\
 & =\begin{pmatrix} 11 / 2 \\ -5 \\ -17 / 2 \end{pmatrix} 
\end{align}
$$
b) 
$$
\begin{align}
2\mathbf{v}_{1}-\mathbf{v}_{2}-\mathbf{x} & =3(\mathbf{x}+2\mathbf{v}_{4}) \\
2\mathbf{v}_{1}-\mathbf{v}_{2}-6\mathbf{v}_{4} & =4\mathbf{x} \\
4\mathbf{x} & =2\mathbf{v}_{1}-\mathbf{v}_{2}-6\mathbf{v}_{4} \\
4\mathbf{x} & =2\begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix} -\begin{pmatrix} -3 \\ 5 \\ 0 \end{pmatrix} -6 \begin{pmatrix} 4 \\ -3 \\- 1 \end{pmatrix}  \\
4\mathbf{x} & =\begin{pmatrix} 4 \\ -2 \\ 2 \end{pmatrix} +\begin{pmatrix} 3 \\ -5 \\ 0 \end{pmatrix} +\begin{pmatrix} -24 \\ 18 \\ 6 \end{pmatrix}  \\
 & =\begin{pmatrix} -17 \\ 11 \\ 8 \end{pmatrix}  \\
\mathbf{x} & =\begin{pmatrix} -17 / 4 \\ 11 / 4 \\ 2 \end{pmatrix} 
\end{align}
$$
3. a) i)
$$
\begin{align}
3\mathbf{u} -i\mathbf{v}+2\mathbf{w} & =3\begin{pmatrix} -1+2i \\ 2i \\ 1 \end{pmatrix} -i \begin{pmatrix} 0 \\ i \\ 1-i \end{pmatrix} +2 \begin{pmatrix} -i \\ 3 \\ 4 \end{pmatrix}  \\
 & =\begin{pmatrix} -3+6i \\ 6i \\ 3 \end{pmatrix} +\begin{pmatrix} 0 \\ 1 \\ -1-i \end{pmatrix} +\begin{pmatrix} -2i \\ 6 \\ 4 \end{pmatrix}  \\
 & =\begin{pmatrix} -3+6i-2i \\ 6i+1+6 \\ 3-1-i+4 \end{pmatrix}  \\
 & =\begin{pmatrix} -3+4i \\ 7+6i \\ 6-i \end{pmatrix} 
\end{align}
$$
ii) 
$$
\begin{align}
\frac{\mathbf{u}+\mathbf{v}}{\lVert \mathbf{u}+\mathbf{v} \rVert } & =\frac{1}{\left\lVert \begin{pmatrix} -1+2i \\ 3i \\ 2-i \end{pmatrix}  \right\rVert }\begin{pmatrix} -1+2i \\ 3i \\ 2-i \end{pmatrix}  \\
 & =\frac{1}{\sqrt{|-1+2i|^{2}+|3i|^{2}+|2-i|^{2}}}\begin{pmatrix} -1+2i \\ 3i \\ 2-i \end{pmatrix}  \\
 & =\frac{1}{\sqrt{5+9+5}}\begin{pmatrix} -1+2i \\ 3i \\ 2-i \end{pmatrix}  \\
 & =\frac{1}{4}\begin{pmatrix} -1+2i \\ 3i \\ 2-i \end{pmatrix}  \\
 & =\begin{pmatrix} -\frac{1}{4}+\frac{i}{2} \\ \frac{3i}{4} \\ \frac{1}{2}-\frac{i}{4} \end{pmatrix} 
\end{align}
$$
iii)
$$
\begin{align}
\left( \sqrt{2}e^{i\pi/4}\mathbf{u}+\mathbf{v} \right)\cdot \mathbf{w} & = ((1+i)\mathbf{u}+\mathbf{v})\cdot \mathbf{w}  \\
 & =\left( \begin{pmatrix} -3+i \\ -2+2i \\ 1+i \end{pmatrix}+\begin{pmatrix} 0 \\ i \\ 1-i \end{pmatrix}   \right)\cdot \mathbf{w} \\
 & =\begin{pmatrix} -3+i \\ -2+3i \\ 2 \end{pmatrix} \cdot \begin{pmatrix} -i \\ 3 \\ 4 \end{pmatrix}  \\
 & =(-3+i)(\conj{-i})+(-2+3i)(\conj{3})+(2)(\conj{4}) \\
 & =-i-3i-6+9i+6 \\
 & =5i
\end{align}
$$

b) 
i) 
$$
\begin{align}
\begin{pmatrix} 2-3i \\ 9+6i \\ 12+8i \end{pmatrix}  & =a\mathbf{v}+b\mathbf{w} \\
 & =\begin{pmatrix} 0 \\ ai \\ a-ai \end{pmatrix} +\begin{pmatrix} -bi \\ 3b \\ 4b \end{pmatrix}  \\
 & =\begin{pmatrix} -bi \\ 3b+ai \\ (a+4b)-ai \end{pmatrix} 
\end{align}
$$
So we have
$$
\begin{align}
2-3i & =-bi \\
b & =3+2i
\end{align}
$$
and
$$
\begin{align}
 9+6i  & =3b+ai \\
 & =3(3+2i)+ai \\
 & =9+(6+a)i \\
 6& = 6+a \\
a & =0
 \end{align}
$$
We now check if this satisfies:
$$
\begin{align}
 12+8i  & =(a+4b)-ai \\
 & =4(3+2i) \\
 & =12+8i 
 \end{align}
$$
As required. Therefore, ${} \begin{pmatrix} 2-3i \\ 9+6i \\ 12+8i \end{pmatrix} \in \span\{\mathbf{u},\, \mathbf{v}\} {}$
ii) 
$$
\begin{pmatrix} 1+7i \\ 2-3i \\ 2+3i \end{pmatrix} =\begin{pmatrix} -bi \\ 3b+ai \\ (a+4b)-ai \end{pmatrix} 
$$
So we have
$$
\begin{align}
1+7i & =-bi \\
 b & =-7+i
\end{align}
$$
and
$$
\begin{align}
2-3i & =3b+ai \\
 & =-21+(3+a)i \\
23-3i & =(3+a)i \\
-3-23i & =3+a \\
a & =-6-23i
\end{align}
$$
We now check if this satisfies:
$$
\begin{align}
 2+3i  & =a+4b-ai \\
 & =-6-23i-28+4i+6i-23 \\
 & =-57-13i 
 \end{align}
$$
Which is not true. Therefore, ${} \begin{pmatrix} 1+7i \\ 2-3i \\ 2+3i \end{pmatrix} \notin\span\{\mathbf{u},\, \mathbf{v}\} {}$
iii)
$$
\begin{pmatrix} -3i \\ 12+i \\ 10-4i \end{pmatrix} =\begin{pmatrix} -bi \\ 3b+ai \\ (a+4b)-ai \end{pmatrix} 
$$
So we have
$$
\begin{align}
-3i & =-bi \\
b & = 3
\end{align}
$$
and
$$
\begin{align}
12+i & =3b+ai \\
 & =9+ai \\
ai & =3+i \\
 a & =1-3i
\end{align}
$$
We now check if this satisfies:
$$
\begin{align}
10-4i & =a+4b-ai \\
 & =1-3i+12-i-3 \\
 & =10-4i
\end{align}
$$
As required. Therefore, ${} \begin{pmatrix} -3i \\ 12+i \\ 10-4i \end{pmatrix} \in \span\{\mathbf{u},\, \mathbf{v}\} {}$
4. 
a) i) Recall we have for some ${} \mathbf{v},\, \mathbf{u}\in \mathbb{R}^{3} {}$, 
$$
\mathbf{v}\cdot \mathbf{u}=\lVert \mathbf{v} \rVert \lVert \mathbf{u} \rVert \cos\theta
$$
Where ${} \theta {}$ is the planar angle between $\mathbf{v} {}$ and $\mathbf{u} {}$. By this, we have that
$$
\mathbf{u}\cdot \mathbf{v}=\begin{pmatrix} 1 \\ -2 \\ 3 \end{pmatrix} \cdot \begin{pmatrix} 3 \\ 0 \\ 1 \end{pmatrix} =1\cdot 3+(-2)\cdot 0+3\cdot 1=6
$$
We also have
$$
\begin{align}
\lVert \mathbf{u} \rVert  & =\left\lVert  \begin{pmatrix} 1 \\  -2\\ 3 \end{pmatrix} \right\rVert  \\
 & =\sqrt{1^{2}+(-2)^{2}+3^{2}} \\
 & =\sqrt{1+4+9} \\
 & =\sqrt{14}
\end{align}
$$
and
$$
\begin{align}
 \lVert \mathbf{v} \rVert  & =\left\lVert  \begin{pmatrix} 3 \\ 0 \\ 1 \end{pmatrix} \right\rVert   \\
 & =\sqrt{3^{2}+0^{2}+1} \\
 & =\sqrt{9+1} \\
 & =\sqrt{10} 
 \end{align}
$$
So we have 
$$
\mathbf{u}\cdot \mathbf{v}=6=\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert \cos\theta=2\sqrt{35}\cos\theta
$$
Therefore
$$
\cos\theta=\frac{3}{\sqrt{35}}
$$
ii) we have
$$
\mathbf{v}\cdot \mathbf{w}=\begin{pmatrix} 3 \\ 0 \\ 1 \end{pmatrix} \cdot \begin{pmatrix} -2 \\ 2 \\ 1 \end{pmatrix} =3\cdot (-2)+0+0\cdot 2+1\cdot 1=-5
$$

We also have ${} \lVert \mathbf{v} \rVert =\sqrt{10} {}$, from above, and 
$$
\begin{align}
\lVert \mathbf{w} \rVert &  =\left\lVert  \begin{pmatrix} -2 \\ 2 \\ 1 \end{pmatrix} \right\rVert  \\
 & =\sqrt{(-2)^{2}+2^{2}+1^{2}} \\
 & =\sqrt{4+4+1} \\
 & =3
\end{align}
$$
So we have
$$
\mathbf{v}\cdot \mathbf{w}=-5=\lVert \mathbf{v} \rVert \lVert \mathbf{w} \rVert \cos\theta=3\sqrt{10}\cos\theta
$$
Therefore
$$
\cos\theta=-\frac{5}{3\sqrt{10}}
$$
b)
$$
\begin{align}
 \mathbf{u}+\alpha \mathbf{v}  & =\begin{pmatrix} 1 \\ -2 \\ 3 \end{pmatrix} +\begin{pmatrix}  3\alpha \\ 0 \\ \alpha \end{pmatrix}  \\
 & =\begin{pmatrix} 3\alpha+1 \\ -2 \\ \alpha+3 \end{pmatrix} 
 \end{align}
$$
In order to be perpendicular, ${} (\mathbf{u}+\alpha \mathbf{v})\cdot \mathbf{w}=0 {}$. Therefore, we have
$$
\begin{align}
0=\begin{pmatrix} 3\alpha+1 \\ -2 \\ \alpha+3 \end{pmatrix} \cdot \begin{pmatrix} -2 \\ 2 \\ 1 \end{pmatrix}  & =-6\alpha-2-4+\alpha+3 \\ \ \\
 & =-5\alpha-3 \\
5\alpha & =-3 \\
\alpha & =-\frac{3}{5}
\end{align}
$$
Therefore, $\mathbf{u}-\frac{3}{5} \mathbf{v}$ perpendicular to $\mathbf{w}$

5. a)
$$
L=\begin{pmatrix} 4 \\ 1 \\ 5 \end{pmatrix} +t \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} 
$$
b) 
$$
\begin{align}
 L & =\begin{pmatrix} 2 \\ -7 \\ 12 \end{pmatrix} +t\left( \begin{pmatrix} 2 \\ -7 \\ 12 \end{pmatrix} -\begin{pmatrix} 2 \\ 9 \\ -6 \end{pmatrix}  \right)\\
   & =\begin{pmatrix} 2 \\ -7 \\ 12 \end{pmatrix} +t \begin{pmatrix} 0 \\ -16 \\ 18 \end{pmatrix} 
 \end{align}$$
We find ${} s,\, {} t\in \mathbb{R} {}$ such that
$$
\begin{align}
 \begin{pmatrix} 4 \\ 1 \\ 5 \end{pmatrix} +t \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}   & = \begin{pmatrix} 2 \\ -7 \\ 12 \end{pmatrix} +s \begin{pmatrix} 0 \\ -16 \\ 18 \end{pmatrix}   \\
t \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}  & =\begin{pmatrix} -2 \\ -8 \\ 7 \end{pmatrix} +s\begin{pmatrix} 0 \\ -16 \\ 18 \end{pmatrix}  \\
 \begin{pmatrix} t \\ 0 \\ t \end{pmatrix}  & =\begin{pmatrix} -2 \\ -16s-8 \\ 18s+7 \end{pmatrix}  \\
 \end{align}
$$
Therefore, we have ${} t=-2$, and
$$
\begin{align}
-16s-8 & =0 \\
2s+1 & =0 \\
s & =-\frac{1}{2}
\end{align}
$$
We now check if this satisfies the last line:
$$
\begin{align}
 18s -7 & =18\cdot -\frac{1}{2}+7 \\
 & =-9+7 \\
 & =-2=t 
 \end{align}
$$
Therefore, they intersect when ${} t=-2 {}$, and ${} s=-\frac{1}{2} {}$. The point is
$$
\begin{align}
P & =\begin{pmatrix} 4 \\ 1 \\ 5 \end{pmatrix} +(-2)\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}  \\
 & = \begin{pmatrix} 4 \\ 1 \\ 5 \end{pmatrix} +\begin{pmatrix} -2 \\ 0 \\ -2 \end{pmatrix}  \\
 & =\begin{pmatrix} 2 \\ 1 \\ 3 \end{pmatrix} 
\end{align}
$$
6. a)
We need to show that for ${} \mathbf{r}=\begin{pmatrix} 13 \\ 2 \\ -8 \end{pmatrix}  {}$ , we have ${} \mathbf{p}\cdot \mathbf{r}=0=\mathbf{q}\cdot \mathbf{r} {}$.
$$
\begin{align}
 \mathbf{p}\cdot   \mathbf{r} & =\begin{pmatrix} -2 \\ 1 \\ -3 \end{pmatrix} \cdot \begin{pmatrix} 13 \\ 2 \\ -8 \end{pmatrix}  \\
 & =-26+2+24 \\
 & =0
 \end{align}
$$
Therefore $\mathbf{p}$ and $\mathbf{r} {}$ are orthogonal.

$$
\begin{align}
 \mathbf{q}\cdot \mathbf{r}  & =\begin{pmatrix} 0 \\ 4 \\ 1 \end{pmatrix} \cdot \begin{pmatrix} 13 \\ 2 \\ -8 \end{pmatrix}  \\
 & =0+8-8 \\
 & =0 
 \end{align}
$$
Therefore, $\mathbf{q}$ and $\mathbf{r} {}$ are orthogonal

b)
Set
$$
d=\begin{pmatrix} 13 \\ 2 \\ -8 \end{pmatrix} \cdot \begin{pmatrix} 1 \\ 5 \\ -2 \end{pmatrix} =13+10+16=39
$$
Then
$$
\begin{align}
 \begin{pmatrix} 13 \\ 2 \\ -8 \end{pmatrix} \cdot \mathbf{v}  & =13x+2y-8z 
 \end{align}
$$
and
$$
\begin{align}
\begin{pmatrix} 13 \\ 2 \\ -8 \end{pmatrix} \cdot \left( \begin{pmatrix} 1 \\ 5 \\ -2 \end{pmatrix} +t\mathbf{p}+s \mathbf{q} \right)=d
\end{align}
$$
by the orthogonality. Therefore, 
$$
13x+2y-8z=39
$$
Is the cartesian equation of the plane

7. a) Consider ${} (\mathbf{u}+\mathbf{v})\cdot (\mathbf{u}+\mathbf{v}) {}$
$$
\begin{align}
(\mathbf{u}+\mathbf{v})\cdot (\mathbf{u}+\mathbf{v}) &=\mathbf{u}\cdot \mathbf{u}+\mathbf{u}\cdot \mathbf{v}+\mathbf{v}\cdot \mathbf{u}+\mathbf{v}\cdot \mathbf{v} \\
\lVert \mathbf{u}+\mathbf{v} \rVert ^{2} & = \lVert \mathbf{u} \rVert ^{2}+\lVert \mathbf{v} \rVert^{2} +2\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert \cos\theta \\
 & \leq\lVert \mathbf{u} \rVert ^{2}+\lVert \mathbf{v} \rVert ^{2}+2\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert  \\
 & =(\lVert \mathbf{u} \rVert +\lVert \mathbf{v} \rVert )^{2} \\
 \\
\lVert \mathbf{u}+\mathbf{v} \rVert  & \leq\lVert \mathbf{u} \rVert +\lVert \mathbf{v} \rVert 
\end{align}
$$

b) 
We use the same approach as above. Working ${} (\Rightarrow ) {}$, suppose that $\mathbf{u}\cdot \mathbf{v}=\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert {}$. Then we have
$$
\begin{align}
 (\mathbf{u}+\mathbf{v})\cdot (\mathbf{u}+\mathbf{v})  & =\mathbf{u}\cdot \mathbf{u}\cdot \mathbf{v}\cdot \mathbf{v}+\mathbf{u}\cdot \mathbf{v}+\mathbf{v}\cdot \mathbf{u}  \\
\lVert \mathbf{u}+\mathbf{v} \rVert ^{2} & =\lVert \mathbf{u} \rVert ^{2}+\lVert \mathbf{v} \rVert ^{2}+2(\mathbf{u}\cdot \mathbf{v}) \\
 & =\lVert \mathbf{u} \rVert ^{2}+2\lVert \mathbf{u} \rVert \lVert\mathbf{v} \rVert +\lVert \mathbf{v} \rVert ^{2} \\
 & =(\lVert \mathbf{u} \rVert +\lVert \mathbf{v} \rVert )^{2} \\
\lVert \mathbf{u}+\mathbf{v} \rVert  & =\phantom{(}\lVert \mathbf{u} \rVert +\lVert \mathbf{v} \rVert 
 \end{align}
$$
Now working ${} (\Leftarrow )$. Suppose that ${} \lVert \mathbf{u}+\mathbf{v} \rVert =\lVert \mathbf{u} \rVert +\lVert \mathbf{v} \rVert  {}$. Then we have
$$
\begin{align}
\lVert \mathbf{u}+\mathbf{v} \rVert  & =\lVert \mathbf{u} \rVert +\lVert \mathbf{v} \rVert  \\
\lVert \mathbf{u}+\mathbf{v} \rVert ^{2} & =\lVert \mathbf{u} \rVert^{2} +\lVert \mathbf{v} \rVert ^{2}+2\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert  \\
(\mathbf{u}+\mathbf{v})\cdot (\mathbf{u}+\mathbf{v}) & =(\mathbf{u}\cdot \mathbf{u})+(\mathbf{v}\cdot \mathbf{v})+2\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert  \\
\mathbf{u}\cdot \mathbf{u}+\mathbf{v}\cdot \mathbf{v}+\mathbf{u}\cdot \mathbf{v}+\mathbf{v}\cdot \mathbf{u} -\mathbf{u}\cdot \mathbf{u}-\mathbf{v}\cdot \mathbf{v}& =2\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert \\
2\mathbf{u}\cdot \mathbf{v} & =2\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert   \\
\mathbf{u}\cdot \mathbf{v} & =\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert  
\end{align}
$$
As required Therefore, ${} \lVert \mathbf{u}+\mathbf{v} \rVert =\lVert \mathbf{u} \rVert +\lVert \mathbf{v} \rVert {}$ iff ${} \mathbf{u}\cdot \mathbf{v}=\lVert \mathbf{v} \rVert \lVert \mathbf{u} \rVert \ \square {}$. 