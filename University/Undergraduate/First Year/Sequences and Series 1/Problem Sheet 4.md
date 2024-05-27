---
tags:
  - homework
  - seq_and_series1
date: 2023-10-26
---
[[Directory]], [[Sequences and Series 1|Subject Directory]]
1. 
$$
		\exists \delta>0:\forall m \in \mathbb{N}:\exists n\geq m:-\delta\geq\frac{(-1)^{n}}{n}\text{ or } \frac{(-1)^{n}}{n}\geq \delta
$$
2. 
a) skip
b) i) ${} S_{-}=(-\infty,\, -1] {}$, ii), $\inf S=-1$, iii) $S_{+}=\left[ 1/\sqrt{2}+1,\, \infty \right)$, iv) $\sup S=\frac{1}{\sqrt{2}}+1$
c) i) ${} S_{-}=(-\infty,\, -2] {}$, ii) ${} \inf S=-2$, iii) ${} S_{+}=[1,\, \infty)$, iv) $\sup S=1$
3. 
a) 
Claim: ${} \inf \left\{  \frac{ 2\sqrt{n}+1 }{ \sqrt{n} }\mid n \in\mathbb{N}  \right\}=2 {}$.
Proof: Let ${} n \in  \mathbb{N} {}$. Then 
$$
\frac{ 2\sqrt{n} +1}{ \sqrt{n} }=2+\frac{1}{\sqrt{n}}
$$
Since ${} \frac{1}{\sqrt{n}}>0$, then $\frac{2\sqrt{n}+1}{\sqrt{n}}>2$. So $2 {}$ is a lower bound. 
Now let $\varepsilon>0 {}$. Let $n=\ceil*{\frac{1}{\varepsilon^{2}}} +1$. Then we have
$$
\begin{align}
x & =2+\frac{1}{\sqrt{n}} \\
 & =2+\frac{1}{\sqrt{\ceil*{\frac{1}{\varepsilon^{2}}}+1}} \\
 & <2+\frac{1}{\sqrt{\frac{1}{\varepsilon^{2}}}} \\
 & <2+\varepsilon
\end{align}
$$
Note that ${} n \in \mathbb{N}$, so $x \in S {}$. Therefore,  the claim is true.

b)
Claim: ${} \sup \left\{  \frac{\log(n /2)}{\log(n)} \mid n \in\mathbb{N} \text{ and } n\neq 1 \right\}=1 {}$
Proof: Let $n \in  \mathbb{N}$. Then
$$
\frac{\log(n /2)}{\log(n)}=\frac{\log n-\log2}{\log n}=1-\frac{\log2}{\log n}
$$
Since ${} \log n>0 {}$, and ${} \log 2 {}$ is a constant, then $1-\frac{ \log2 }{ \log n }<1$. Therefore, $1$ is an upper bound
Now let $\varepsilon>0 {}$. Let ${} n=\ceil*{2^{1/\varepsilon}} +1 {}$. Note that as ${} 2^{1/\varepsilon}>0$, then $n\neq 1 {}$. Then we have
$$
\begin{align}
 x & =1-\frac{\ln2}{\ln n} \in S  \\
 & =1-\frac{ \ln2 }{ \ln(\ceil*{2^{1/\varepsilon}}+1 ) } \\
 & >1-\frac{\ln2}{\ln(2^{1/\varepsilon})} \\
 & >1-\frac{\ln2}{(1 /\varepsilon) \ln(2)} \\
 & >1-\varepsilon
 \end{align}
$$
Therefore, the claim is true.
c) 
Claim: $\inf \left\{  \frac{1}{\sqrt{n}}+(-1)^{n}\mid n \in \mathbb{N}  \right\}=-1$
Proof: Let ${} n \in \mathbb{N} {}$. Now we have 2 cases:
Case ${} n$ is even: Now ${} \frac{1}{\sqrt{n}}+1\in S {}$, and as ${} \frac{1}{\sqrt{n}}>0 {}$, then ${} \frac{1}{\sqrt{n}}+1>1>-1$
Case $n$ is odd : Now $\frac{1}{\sqrt{n}}-1 \in S$, and as ${} \frac{1}{\sqrt{n}}>0 {}$, then $\frac{1}{\sqrt{n}}-1>-1$
Therefore, $-1 {}$ is an upper bound

Now let $\varepsilon>0 {}$. let ${} n=2\ceil*{\frac{1}{{\varepsilon}^{2}}} +1\in \mathbb{N} {}$. Note that $n {}$ is odd. Now we have
$$
\begin{align}
x & =(-1)^{n}+\frac{1}{\sqrt{n}} \in S \\
 & =-1+\frac{1}{\sqrt{2\ceil*{\frac{1}{\varepsilon^{2}}} +1}} &  & \text{as }n\text{ is odd} \\
 & <-1+\frac{1}{\sqrt{\frac{1}{\varepsilon^{2}}}} \\
 & <-1+\varepsilon
\end{align}
$$
Therefore, the claim is true.
d) 
Claim: ${} \sup \left\{  (-1)^{n}-\frac{1}{n^{2}}\mid n \in \mathbb{N}  \right\}=1 {}$
Proof: Let $n \in \mathbb{N}$. Now we have 2 cases:
Case ${} n {}$ is even: then ${} 1-\frac{1}{n^{2}}\in S {}$, and since ${} -\frac{1}{n^{2}}<0 {}$, then ${} 1-\frac{1}{n^{2}}<1 {}$, so $1$ is an upper bound
Case $n$ is odd: then ${} -1-\frac{1}{n^{2}}\in S$, and since ${} -\frac{1}{n^{2}}<0 {}$, then ${} -1-\frac{1}{n^{2}}<-1<1$, so $1$ is an upper bound
Therefore, $-1 {}$ is an upper bound.

Now let $\varepsilon>0$. Let $n=2\left( \ceil*{\frac{1}{\sqrt{\varepsilon}}}+1  \right)$. Note that $n$ is even, and $n \in S$. Let ${} x =(-1)^{n}-\frac{1}{n^{2}}\in S {}$. Since $n$ is even, then ${} x=1-\frac{1}{n^{2}} {}$. Now observe that
$$
\begin{align}
x & =1-\frac{1}{n^{2}} \\
 & =1-\frac{1}{\left(  2\left( \ceil*{\frac{1}{\sqrt{\varepsilon}}} +1 \right)  \right)^{2}} \\
 & >1-\frac{1}{\left( \frac{1}{\sqrt{\varepsilon}} \right)^{2}} \\
 & >1-\varepsilon
\end{align}
$$