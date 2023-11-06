---
tags:
  - homework
  - linear_algebra1
date: 2023-09-28
---
[[Directory]], [[Linear Algebra and Geometry 1|Subject Directory]]
### Problem 1
$$
\begin{align}
 S & =\sum_{j=1}^{n} ( 3j+1 )^{2}  \\
 &  =\sum_{j=0}^{n-1} (3j+4)^{2} \\
 & = \sum_{j=2}^{n+1} (3j-2)^{2} \\
 & =(3n+1)^{2}+\sum_{j=1}^{n-1} ( 3j+1 )^{2} \\
 & =3n(3n+2)+1+\sum_{j=1}^{n-1} (3j+1)^{2} \\
 & =3n(3n+2)+\sum_{j=0}^{n-1} (3j+1)^{2}
 \end{align}
$$
Therefore, B, C, D

### Problem 2
$$
\begin{align}
\sum_{j=0}^{n} \sum_{k=0}^{n} (j+2k+3) & =\sum_{j=0}^{n} \left( \sum_{k=0}^{n} j+2\sum_{k=0}^{n} k +3\sum_{k=0}^{n} 1\right) \\
 & =\sum_{j=0}^{n} ((n+1)j+n(n+1)+3(n+1)) \\
 & =(n+1)\left( \sum_{j=0}^{n} j+n\sum_{j=0}^{n} 1+3\sum_{j=0}^{n} 1 \right) \\
 & =(n+1)\left( \sum_{j=0}^{n} j+n(n+1)+3(n+1) \right) \\
 & =(n+1)\left( \sum_{k=0}^{n} k+2\sum_{k=0}^{n} k+3(n+1) \right) \\
 & =3(n+1)\sum_{k=0}^{n} k \\
 & =\frac{3}{2} n(n+1)^{2}
\end{align}
$$

$$
\begin{align}
 \sum_{j=1}^{n} \sum_{k=1}^{n} jk & = \sum_{j=1}^{n} j\sum_{k=1}^{n} k \\
 & =\left(  \sum_{k=1}^{n} k  \right)^{2} 
 \end{align}
$$

### Problem 3
$$
\begin{align}
 \sum_{k=0}^{n} k\sin^{2}\left( \frac{k\pi}{2} \right)  & = \sum_{\substack{k=0\\k \text{ odd}} }^{n} \\
 
 \end{align}
$$
