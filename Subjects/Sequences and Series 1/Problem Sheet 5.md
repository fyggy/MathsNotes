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
Let ${} \{ s_{n} \}_{n=1}^{\infty} {}$ be a sequence with ${} \lim_{n\tto \infty} s_{n}=\ell {}$