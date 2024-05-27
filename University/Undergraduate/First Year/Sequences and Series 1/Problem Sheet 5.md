---
tags:
  - homework
  - seq_and_series1
date: 2023-11-09
pset: 5
---
[[Directory]], [[Sequences and Series 1|Subject Directory]]
[[SeqSeries HW5.pdf|Problem Sheet]]
1. 
a) Let ${} \varepsilon>0$. Then if we have $n_{0}=\ceil*{\sqrt[3]{\frac{3}{\varepsilon}}} +1$, then for all $n\geq n_{0}$, we have 
$$
\begin{align}
n & \geq \ceil*{\sqrt[3]{\frac{3}{\varepsilon}}} +1 \\
  & >\sqrt[3]{\frac{3}{\varepsilon}} \\
n^{3}  & >\frac{3}{\varepsilon} \\
\varepsilon & >\frac{3}{n^{3}} \\
\varepsilon & >\left| \frac{3}{n^{3}}-0 \right| 
\end{align}
$$
Therefore, by the definition of the limit, we have
$$
\lim_{n\tto \infty} s_{n}=0
$$
b) Let ${} \varepsilon>0 {}$. Then if we have ${} n_{0}=\ceil*{\frac{25}{\varepsilon^{2}}}+1 {}$, then for all $n\geq n_{0}$, we have
$$
\begin{align}
n & \geq \ceil*{\frac{25}{\varepsilon^{2}}} +1 \\
  & >\frac{25}{\varepsilon^{2}} \\
\varepsilon^{2} & >\frac{25}{n} \\
\varepsilon & >\frac{5}{\sqrt{n}} \\
 & >\left| \frac{5}{\sqrt{n}}-0 \right|  \\
\end{align}
$$
Therefore, by the definition of the limit, we have
$$
\begin{align}
\lim_{n\tto \infty} s_{n}=0
\end{align}
$$
d) Let ${} \varepsilon>0 {}$. Then if we have $n_{0}=\ceil*{e^{\sqrt{10/\varepsilon}}} +1$, then for all ${} n \geq n_{0} {}$, we have
$$
\begin{align}
n & \ge \ceil*{e^{\sqrt{10/\varepsilon}}} +1 \\
 & >e^{\sqrt{10/\varepsilon}} \\
\ln n & >\sqrt{\frac{10}{\varepsilon}} \\
(\ln n)^{2} & >\frac{10}{\varepsilon} \\
\varepsilon & >\frac{10}{(\ln n)^{2}} \\
 & >\left| \frac{10}{(\ln n)^{2}}-0 \right| 
\end{align}
$$
Therefore, by the definition of a limit, we have
$$
\lim_{n\tto \infty} s_{n}=0
$$
e) Let $\varepsilon>0$. Then if we have ${} n_{0}=\ceil*{\frac{1}{9\varepsilon}-27} +1 {}$, then for all $n\geq n_{0} {}$, we have
$$
\begin{align}
n & \geq \ceil*{\frac{1}{9\varepsilon}-\frac{1}{3}} +1 \\
n & >\frac{1}{9\varepsilon}-\frac{1}{3} \\
9n & >\frac{1}{\varepsilon}-3 \\
9n+3 & >\frac{1}{\varepsilon} \\
\varepsilon & >\frac{1}{9n+3} \\
 & > \left| \frac{1}{9n+3} \right| \\
 & > \left| \frac{-1}{9n+3} \right|  \\
 & > \left|\frac{3n-3n-1}{9n+3} \right|  \\
 & >\left| \frac{n}{3n+1}-\frac{1}{3} \right| 
\end{align}
$$
Therefore, by the definition of the limit, we have
$$
\lim_{n\tto \infty} s_{n}=0
$$
2. 
Let ${} \{ s_{n} \}_{n=1}^{\infty} {}$ be a sequence with $\lim_{n\tto \infty} s_{n}=\ell$, and let ${} \{ t_{n} \}^{\infty}_{n=1} {}$ be defined by ${} t_{n}=2s_{n} {}$. Then, given $\varepsilon>0$, we have a ${} n_{0} \in \mathbb{N}$ such that for all $n\geq n_{0}$, we have
$$
|s_{n}-\ell|<\varepsilon
$$
Therefore, we have a $n_{0}$ such that for all $n\geq n_{0}$, we have
$$
\begin{align}
 |s_{n}-\ell| & <\frac{\varepsilon}{2}   \\
2|s_{n}-\ell| & <\varepsilon \\
|2s_{n}-2\ell| & <\varepsilon \\
|t_{n}-2\ell| & <\varepsilon
 \end{align}
$$
For all ${} \varepsilon>0 {}$. Therefore, 
$$
\lim_{n\tto \infty} t_{n}=2\ell
$$
As required
3. 
skip
4. 
Let ${} \{ s_{n} \}_{n=1}^{\infty} {}$ such that 
$$
\lim_{n\tto \infty} s_{n}=0
$$
and let ${} \{t_{s}\}_{s=1}^{\infty}  {}$ such that
$$
t_{n}=\begin{cases}
1 & \text{ if } n\leq 1000 \\
s_{n} & \text{ if } n>1000
\end{cases}
$$
Now let ${} \varepsilon>0$. Then let $S(\varepsilon)$ be the ${} n_{0}\in \mathbb{N}$ such that for all $n\geq n_{0}$, ${} |s_{n}-0|<\varepsilon {}$. 

Now if we have $\varepsilon>0 {}$, then let ${} n_{0}=\max(S(\varepsilon),\, 1001) {}$. Then for all $n\geq n_{0}$, we have 2 cases: 
Case 1: ${} S(\varepsilon)\leq 1000 {}$. Then ${} n\geq 1001 {}$. Therefore, $t_{n}=s_{n}$, and ${} n\geq S(\varepsilon)$, so ${} |t_{n}-0|=|s_{n}-0|<\varepsilon {}$
Case 2: ${} S(\varepsilon)>1000 {}$. Then ${} t_{n}=s_{n} {}$, and ${} n\geq S(\varepsilon) {}$, so $|t_{n}-0|=|s_{n}-0|<\varepsilon$
Therefore
$$
\lim_{n\tto \infty} t_{n}=0
$$
As required
5. Let ${} \{s_{n}\}_{n=1}^{\infty}  {}$ and ${} \{t_{n}\}_{n=1}^{\infty}  {}$ such that ${} \exists \ell \in \mathbb{R} {}$ such that
$$
\lim_{n\tto \infty} s_{n}=\ell=\lim_{n\tto \infty} t_{n}
$$
Then let ${} \{r_{n}\}_{n=1}^{\infty}  {}$ such that
$$
r_{n}=\begin{cases}
s_{n} & \text{if } n\text{ is odd} \\
t_{n} & \text{if } n \text{ is even}
\end{cases}
$$
Let ${} S(\varepsilon) {}$ be the $n_{0}$ such that for all $n\geq n_{0}$, we have $|s_{n}-\ell|<\varepsilon$
Let ${} T(\varepsilon) {}$ be the $n_{0}$ such that for all $n\geq n_{0}$, we have ${} |t_{n}-\ell|<\varepsilon {}$
Let $\varepsilon>0$. Then we have $n_{0}=\max(S(\varepsilon),\, T(\varepsilon))$ such that for all $n\geq n_{0}$, we have 2 cases:
Case 1: $n$ odd. Then ${} r_{n}=s_{n} {}$, and since $n\geq n_{0}\geq S(\varepsilon)$, we have ${} |r_{n}-\ell|=|s_{n}-\ell|<\varepsilon {}$
Case 2: ${} n {}$ even. Then ${} r_{n}=t_{n} {}$, and since ${} n\geq n_{0}\geq T(\varepsilon)$, we have ${} |r_{n}-\ell|=|t_{n}-\ell|<\varepsilon$
Therefore, 
$$
\lim_{n\tto \infty} r_{n}=\ell
$$
as required.
6. a)
Let ${} \{s_{n}\}_{n=1}^{\infty}  {}$, with ${} s_{n}=n^{2}(-1)^{n} {}$. Suppose that ${} k\geq s_{n} {}$ ${} \forall n \in \mathbb{N}$. Note that ${} s_{2k}=4k^{2}>k {}$. So this cannot hold. Now suppose that ${} k\leq s_{n},\, \forall n \in \mathbb{N} {}$. Note that ${} s_{2k+1}=-4k^{2}-4k-1<k {}$, so this cannot hold. Therefore, ${} s_{n}$ is unbounded
b) 
skip
c)
Let ${} \{s_{n}\}_{n=1}^{\infty}  {}$ with $s_{n}=\sqrt{n}\cos\left( \frac{\pi n}{2} \right)$. This sequence is unbounded. Suppose that ${} k\geq s_{n},\, \forall n \in \mathbb{N} {}$.
Note $s_{4k^{2}}=2k\cos(2\pi k^{2})=2k>k$. Therefore, $s_{n}$ is unbounded.
7. 
c) 
Let ${} \{s_{n}\}_{n=1}^{\infty}  {}$ such that $s_{n}=n^{2}-n {}$. First note that ${} a^{2}-a\geq b^{2}-b {}$ if $a\geq b {}$ and $b>1 {}$, as the function is monotonic for values greater than $1 {}$, as if $x>1 {}$, then $x^{2}>x {}$.
Let $M>0 {}$. Then let ${} n_{0}=\ceil*{M+1} {}$, so ${} n_{0}>1 {}$, and for all ${} n\geq n_{0} {}$, we have
$$
\begin{align}
 s_{n} & =n^{2}-n\geq n_{0}^{2}-n_{0}   \\
 & =\ceil*{2M+1} ^{2}-\ceil*{2M+1}  \\
 & >(2M+1)^{2}-2M+1 \\
 & =4M^{2}+4M+1-2M-1 \\
 & = 4M^{2}+2M\\
  & >M
 \end{align}
$$
Therefore, this sequence diverges to infinity as required.