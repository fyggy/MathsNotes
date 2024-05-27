---
tags:
  - homework
  - calculus1
date: 2023-10-24
---
[[Directory]], [[Calculus 1|Subject Directory]]
27. 
a)
$$
\begin{align}
 \lim_{ x \to{} 3 } \frac{x^{2}+2x-15}{x-3} & =\lim_{ x \to{} 3 } \frac{(x-3)(x+5)}{x-3}   \\
 & =\lim_{ x \to{} 3 } (x+5) \\
 & =8
 \end{align}
$$
So we need ${} k\in \mathbb{R} {}$ such that 
$$
\begin{align}
\left. x^{2}-kx+1 \right|_{x=3} & =8 \\
3^{2}-3k+1 & =8 \\
10-3k & =8 \\
3k & =2 \\
k & =\frac{3}{2}
\end{align}
$$
c)
$$
\begin{align}
\left. 2e^{3x} \right|_{x=0}=2e^{0}=2
\end{align}
$$
So we need ${} k \in \mathbb{R} {}$ such that
$$
\begin{align}
\lim_{ x \to{} 0 } \frac{\sin(kx)}{x} & =2 \\ \\\ \\

 \lim_{ x \to{} 0 } k\frac{\sin(kx)}{kx} & = k\lim_{ x \to{} 0 } \frac{\sin kx}{kx} \\
 & =k
\end{align}
$$
So ${} k=2 {}$

28. 
a) 
$$
\begin{align}
 \lim_{ x \to{} \infty } \left( \frac{ 27x^{26}+24x^{17}-5 }{ 9x^{26}-27x^{17}-5 } \right) & =\lim_{ x \to{} \infty } \frac{27+24x^{-11}-5x^{-26}}{9-27x^{-11}-5x^{-26}}   \\
 & =\frac{\displaystyle \lim_{ x \to{} \infty }27+\lim_{ x \to{} \infty } 24x^{-11}-\lim_{ x \to{} \infty } 5x^{-26}   }{ \displaystyle\lim_{ x \to{} \infty }9 -\lim_{ x \to{} \infty } 27x^{-11}-\lim_{ x \to{} \infty } 5x^{-26}  } \tag{1} \\
 & =\frac{27}{9} \\
 & =3
 \end{align}
$$
