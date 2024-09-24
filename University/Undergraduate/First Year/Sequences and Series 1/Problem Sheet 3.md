---
tags:
  - homework
  - seq_and_series1
date: 2023-10-19
completed: true
---
[[Directory]], [[Sequences and Series 1|Subject Directory]]
1. 
a) 
$$
\begin{align}
\frac{1}{10n^{3}} & \leq 7 \\
10n^{3} & \geq \frac{1}{7} \\
n^{3} & \geq \frac{1}{70} \\
n & \ge \frac{1}{\sqrt[3]{70}}
\end{align}
$$
b)
$$
\begin{align}
\frac{3}{n\sqrt{n}} & <5 \\
n\sqrt{n} & >\frac{3}{5} \\
n^{3/2} & >\frac{3}{5} \\
n & >\sqrt[3/2]{\frac{3}{5}}
\end{align}
$$
c) 
$$
\begin{align}
2^{-n} & \leq 20 \\
-n & \leq \log_{2}(20) \\
n & \geq-2\log_{2}(5)
\end{align}
$$
d) 
$$
\begin{align}
2^{n} & \leq 20 \\
n & \leq  2\log_{2}5
\end{align}
$$
e)
$$
\begin{align}
\left(  \frac{1}{2}  \right)^{5n} & \geq \frac{1}{8} \\
5n & \leq \log_{\frac{1}{2}}\left( \frac{1}{8} \right) \\
 & \leq-\log_{2}  \left( \frac{1}{8} \right) \\
 & \leq \log_{2}(8) \\
 & \leq 3 \\
n & \leq \frac{3}{5}
\end{align}
$$
f)
$$
\begin{align}
\left(  \frac{1}{2}  \right)^{5n} & \leq \frac{1}{8} \\
5n &\geq\log_{\frac{1}{2}}\left( \frac{1}{8} \right) \\
 & \geq-\log_{2}  \left( \frac{1}{8} \right) \\
 & \geq \log_{2}(8) \\
 & \geq 3 \\
n & \geq \frac{3}{5}
\end{align}
$$

2. 
a) 
$$
\begin{align}
|x-3| & =1 \\
x-3=1 & \text{ or } 3-x=1 \\
x=4 & \text{ or }x=2
\end{align}
$$
b) 
$$
\begin{align}
 |x+1| & \leq 3  \\
-3\leq x+1 & \leq 3 \\
-4\leq x & \leq 2
 \end{align}
$$
c)
$$
\begin{align}
 |x+2| & >5   \\
x+2>5 & \text{ or } x+2<-5 \\
x>3 & \text{ or } x<-7
 \end{align}
$$
d)
$$
\begin{align}
|x+10| & <10 \\
-10<x+10 & <10 \\
-20<x & <0
\end{align}
$$

3. 
a) $S$ is bounded from below and above. The set of lower bounds is ${} (-\infty,\, -10] {}$, and the set of upper bounds is ${} [5,\, \infty) {}$. The minimum is ${} -10 {}$, and the maximum does not exist

b) $S {}$ is bounded from below and above. The set of lower bounds is ${} (-\infty,\, 1] {}$, and the set of upper bounds is ${} [3,\, \infty) {}$. The minimum is $1$ and the maximum does not exist

c) $S$ is bounded from below and above. The set of lower bounds is ${} (-\infty,\, 0] {}$, and the set of upper bounds is ${} [1,\, \infty) {}$. The minimum does not exist, and the maximum is ${} 1 {}$

d) $S$ is bounded from below and above. The set of lower bounds is ${} (-\infty,\, -1] {}$, and the set of upper bounds is ${} \left[ \frac{1}{2},\, \infty \right) {}$. The minimum is $-1 {}$, and the maximum is ${} 1/2 {}$

e) $S$ is bounded from below and above. The set of lower bounds is ${} (-\infty, -2] {}$, and the set of upper bounds is ${} \left[ \frac{1}{2},\, \infty \right)$. The minimum is $-2$, and the maximum is ${} 1 / 2 {}$.

4. 
a) Suppose that ${} x \in \mathbb{R} {}$ bounds ${} S {}$ from above. Let ${} a \in S {}$. Then we have that $x\geq a {}$. We now have 2 cases:
- Case 1: ${} x\leq3 {}$. Then let ${} a=4\in S {}$, with ${} 4>3>x$. Therefore, $x$ is not an upper bound of $S$.
- Case 2: $x>3$. Then let ${} a=x+1\in S {}$, as ${} a>3$, and therefore, ${} a\in (3,\, \infty) {}$ by definition. Therefore, ${} a=x+1>x {}$. Therefore, ${} x {}$ is not an upper bound of $S {}$, and $S {}$ can have no upper bound

b) Suppose that ${} x \in \mathbb{R} {}$ bounds ${} \mathbb{Q}$ from below. Now note that ${} a=\floor*{x}-1<x  {}$, and ${} a\in \mathbb{Q}$, as $a {}$ is an integer. Therefore, $x {}$ cannot be a lower bound of $\mathbb{Q} {}$, and $\mathbb{Q}$ has no lower bound

c) Suppose that ${} x \in  \mathbb{R} {}$ bounds $S {}$ from above. Since ${} 4\in S {}$, we may assume $x\geq 4 {}$. Now let $n=2(\ceil*{\log_{4}(x)} +1)\in \mathbb{N} {}$. This is defined due to the bound on $x {}$. Observe that
$$
(-2)^{n}=(-2)^{2(\ceil*{\log_{4}(x)} +1)}=4^{\ceil*{\log_{4}(x)} +1}>4^{\log_{4}(x)}=x
$$
So we have
$$
(-2)^{n}>x
$$
But ${} (-2)^{n}\in S {}$, so $x$ cannot be an upper bound of $S$, and BWOC, $S$ has no upper bound

d) Suppose $x \in \mathbb{R}$ bounds $S$ from above. Then let ${} n=\ceil*{x} +1\in \mathbb{N} {}$. Then we have
$$
2n=2(\ceil*{x} +1)>2x>x
$$
Therefore, $2n>x$, and we have $n$ such that $x<2n \in[2n-1,\, 2n]\subseteq S$. Therefore, $x<2n \in S$, and $x$ is not a upper bound of $S$, and so $S$ has no greatest upper bound

5. 
a) Take ${} m \in S {}$ such that $m$ is a lower bound of $S$. Note that, as $m>0 {}$, then ${} m/2>0$, so ${} m /2\in S$. Also note that $m /2<m$. Therefore, $m$ cannot be a lower bound of $S$. Therefore, $S$ has no minimum

b) Take ${} m \in  S {}$ such that $m$ is a lower bound of $S$. Therefore, ${} m=2^{n} {}$ for some $n \in\mathbb{Z} {}$. Note that $S {}$ is bounded below by 0, as $2^{n}>0 {}$ for all $n \in\mathbb{Z} {}$. Therefore we may assume that ${} m>0 {}$ Now note that $m/2=2^{n-1}\in S$, and since $m>0$, then ${} m /2<m {}$. Therefore, $m$ cannot be a lower bound, so $S$ has no minimum

c) Take ${} m \in  S$ such that $m$ is a lower bound of $S$. Therefore, ${} m=\frac{1}{\ln n} {}$ for some ${} n \in \mathbb{N},\, n\geq2$. Since ${} \ln x>0$ for all ${} x\geq 2 {}$, then we may assume that $m>0 {}$. Now note that $\frac{1}{2}m=\frac{1}{2\ln n}=\frac{1}{\ln n^{2}}\in S$, and $m /2<m$. Therefore, $m$ cannot be a lower bound, so $S$ has no minimum. 

6. Let ${} S\subseteq \mathbb{R} {}$ be a set. First we prove "if". Suppose $S$ is bounded. Therefore, there exist $a$ and $b$ such that, for all $x \in S {}$, we have ${} a\geq x {}$ and $b\leq x$. Now take ${} R=\max(a,\, b) {}$. Therefore, $R\geq a$ and ${} b\geq-R {}$. Therefore, for all ${} R\geq x\geq-R {}$, so ${} R\geq |x| {}$, as required.

Now we prove "only if". Suppose we have ${} R \in \mathbb{R}$ such that for all ${} x \in  S {}$, ${} |x|\leq R$. Then we have $R\geq x$ so $R$ is an upper bound of $S$, and we have $x\geq-R {}$, so $-R$ is a lower bound of $S$. Therefore, $S$ is bounded.

Therefore, we have equivalence.
