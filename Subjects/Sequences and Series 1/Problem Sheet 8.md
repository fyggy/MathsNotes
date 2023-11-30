---
tags:
  - seq_and_series1
  - homework
date: 2023-11-30
---
[[Directory]], [[Sequences and Series 1|Subject Directory]]
[[SeqSeries HW8.pdf|Exercise Sheet]]
1. 
b)
Note that
$$
\begin{align}
 \lim_{n\tto \infty} \frac{ n^{2}+5n+3 }{ 2^{n} } & =\lim_{n\tto \infty} n^{2}2^{-n}+\lim_{n\tto \infty} 5n 2^{-n}+\lim_{n\tto \infty} 3\cdot  2^{-n}   \\
 & =0+0+0
 \end{align}
$$
As exponentials dominate powers, and ${} \lim_{n\tto \infty} 2^{-n}=0 {}$. 
Therefore, ${} n^{2}+5n+3=o(2^{n}) {}$ as ${} n\to{}\infty {}$
c)
$$
\lim_{n\tto \infty} \frac{(-5)^{n}}{4^{n}}=\lim_{n\tto \infty} \left( -\frac{5}{4} \right)^{n}
$$
Note that ${} |(-5 /4)^{n}|=\left( 5 /4 \right)^{n} {}$, and ${} 5 /4 >1 {}$, so ${} \lim_{n\tto \infty} ( 5 /4 )^{n} {}$ diverges. Therefore,
$$
\lim_{n\tto \infty} \left( -\frac{5}{4} \right)^{n}
$$
Diverges, so is not equal to $0$.
d)
$$
\begin{align}
 \lim_{n\tto \infty} \frac{(n+1)^{3}-n^{3}}{n^{3}}  & =\lim_{n\tto \infty} \frac{n^{3}+3n^{2}+3n+1-n^{3}}{n^{3}}   \\
 & =\lim_{n\tto \infty} 3n^{-1}+\lim_{n\tto \infty} 3n^{-2}+\lim_{n\tto \infty} n^{-3} \\
 & =0+0+0 \\
 & =0
 \end{align}
$$
Therefore, ${} (n+1)^{3}-n^{3}=o(n^{3}) {}$
e)
$$
\begin{align}
 \lim_{n\tto \infty} \frac{\frac{ 2^{-n}+3^{-n} }{ n-\frac{1}{2} }}{2^{-n}}  & =\lim_{n\tto \infty} \frac{1+3^{-n}2^{n}}{n-\frac{1}{2}}  \\
 & =\lim_{n\tto \infty} \frac{1}{n-\frac{1}{2}}+\lim_{n\tto \infty} \frac{ 3^{-n}2^{n} }{ n-\frac{1}{2} }  \\
 & =0+\lim_{n\tto \infty} \left(  \frac{2}{3}  \right)^{n}\cdot \frac{1}{n-\frac{1}{2}} \\
 & =0
 \end{align} 
$$
As ${} \frac{2}{3}<0 {}$, and ${} \lim_{n\tto \infty} \frac{1}{n-\frac{1}{2}}=0 {}$
f)
$$
\begin{align}
 \lim_{n\tto \infty} \frac{\frac{ n^{2}-n }{ n^{2}+n }}{1}  & =\lim_{n\tto \infty} \frac{ n^{2}-n }{ n^{2}+n }  \\
 & =\lim_{n\tto \infty} \frac{ n-1 }{ n+1 } \\
 & =\lim_{n\tto \infty} \frac{n}{n+1}-\lim_{n\tto \infty} \frac{1}{n+1} \\
 & =1-0=1\neq 0
 \end{align} 
$$
So it does not hold
2. 
Let ${} s_{n},\, t_{n} {}$ be sequences with ${} s_{n}\leq t_{n} {}$ for all ${} n \in \mathbb{N} {}$. We have
$$
\lim_{n\tto \infty} s_{n}=\infty
$$
Therefore, for all $M \in \mathbb{R} {}$, we have some ${} n_{0} \in \mathbb{N} {}$ such that for all ${} n\geq n_{0} {}$, ${} s_{n}>M {}$. Therefore, for all ${} M \in \mathbb{R} {}$, we have some ${} n_{0} \in \mathbb{N} {}$ such that for all $n\geq n_{0}$, ${} t_{n}\geq s_{n}>M {}$. Therefore, $t_{n}>M$, so 
$$
\lim_{n\tto \infty} t_{n}=\infty
$$
3. 
$$
\begin{align}
 \sum_{k=0}^{n} a^{k} & =1+\sum_{k=1}^{n} a^{k}   \\
 & =1+\sum_{k=1}^{n} a\cdot a^{k-1} \\
 & =1+a\left( \sum_{k=0}^{n-1} a^{k} \right) \\
 & =1+a\left( \sum_{k=0}^{n-1} a^{k}+a^{n}-a^{n} \right) \\
 & =1+a\left( \sum_{k=0}^{n} a^{k} -a^{n}\right)
 \end{align}
$$
So
$$
\begin{align}
 \sum_{k=0}^{n} a^{k}-a\sum_{k=0}^{n} a^{k} & =1-a^{n+1}   \\
 (1-a)\sum_{k=0}^{n} a^{k} & =1-a^{n+1} \\
\sum_{k=0}^{n} a^{k} & =\frac{1-a^{n+1}}{1-a} 
 \end{align}
$$
As required
4. 
Let ${} a \in \mathbb{R} {}$. 
$$
\begin{align}
 \lim_{n\tto \infty} \sum_{k=0}^{n} \frac{a^{k}}{k!} & \geq\lim_{n\tto \infty} \frac{1}{n!} \sum_{k=0}^{n} a^{k}   \\
 & =\lim_{n\tto \infty} \frac{1}{n!} \frac{1-a^{n+1}}{1-a}  \\
 & =0
 \end{align}
$$
and
$$
\lim_{n\tto \infty} \sum_{k=0}^{n} \frac{a^{k}}{k!}\leq \lim_{n\tto \infty} \sum_{k=0}^{n} \frac{a^{k}}{(2a)^{k}}=
$$
