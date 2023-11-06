---
tags:
  - homework
  - seq_and_series1
date: 2023-10-12
---
[[Directory]], [[Sequences and Series 1|Subject Directory]]
1. 
a)
$$
\begin{align}
(-\infty,\, 1)\cap(-1,\, 3)\cap(2,\, \infty) & =(-1,\, 3) \cap \varnothing \\
 & = \varnothing
\end{align}
$$
b)
$$
\begin{align}
 ([0, \infty)\cap[1,\, 10))\setminus(1,\, 2)  & = [1,\, 10)\setminus(1,\, 2) \\
	 & =\{ 1 \} \cup(2,\, 10)
 \end{align}
$$
c)
$$
\begin{align}
 ([0,\, \infty)\setminus(1,\, 3))\cap[2,\, 10]  & = ([0,\, 1]\cup[3,\, \infty))\cap[2,\, 10] \\
 & =([0,\, 1]\cap[2,\, 10])\cup([3,\, \infty)\cap[2,\, 10]) \\
 & =\varnothing \cup [3,\, 10] \\
 & =[3,\, 10]
 \end{align}
$$
d)
$$
\begin{align}
\{ x \in  \mathbb{R}\mid x^{2}\geq 10 \text{ and }2x+1<0 \} & =\left\{  x \in  \mathbb{R}\mid (\sqrt{10}\leq x\text{ or }x\leq-\sqrt{10})\text{ and } x<-\frac{1}{2}  \right\} \\
  & =\left\{  x \in  \mathbb{R}\mid \sqrt{10}<x<-\frac{1}{2} \text{ or }\left( x\leq-\sqrt{10}\text{ and }x<-\frac{1}{2} \right)  \right\} \\
 & =\{ x \in  \mathbb{R}\mid x\leq -\sqrt{10} \} \\
 & =(-\infty,\, -\sqrt{10}]
\end{align}
$$
e)
$$
\begin{align}
\{ x \in  \mathbb{R}\mid x^{2}\leq 1 \text{ or }x>0 \} & =\{ x \in  \mathbb{R}\mid-1<x<1 \text{ or } 0<x \} \\
 & = \{ x \in  \mathbb{R}\mid-1<x \} \\
 & =[-1,\, \infty)
\end{align}
$$
2. First, we show that ${} A\cap(B\cup C)\subseteq(A\cap B)\cup(A\cap C)$. Take an element $x \in A\cap(B\cup C)$. Therefore, $x \in A$ and ($x \in B$ or $x \in C$). We have 2 cases:
	Case 1: $x \in B$. Then we have $x \in A$ and $x \in B$, therefore, $x \in A\cap B$, $x \in (A\cap B)\cup(A\cap C)$
	Case 2: $x \in C$. Then we have $x \in A$ and $x \in C$, therefore, $x \in A\cap C$,$x \in (A\cap B)\cup(A\cap C)$
	 
	Therefore, $x \in (A\cap B)\cup(A\cap C)$.
	
	Now we show that $(A\cap B)\cup(A\cap C)\subseteq A\cap(B\cup C)$. Take an element $x \in (A\cap B)\cup(A\cap C)$. Therefore, ($x \in A$ and $x \in B$) or ($x \in A$ and $x \in C$). We have 2 cases:
	Case 1: $x \in A$ and $x \in B$. Therefore, $x \in B \cup C$, so $x \in A\cap(B\cup C)$
	Case 2: $x \in A$ and $x \in C$. Therefore, $x \in B \cup C$, so $x \in A\cap(B\cup C)$
	
	Therefore, $x \in A\cap(B\cup C)$.

	Since $A\cap(B\cup C)\subseteq(A\cap B)\cup(A\cap C)$, and $(A\cap B)\cup(A\cap C)\subseteq A\cap(B\cup C) {}$, then we have
 $$
A\cap(B\cup C)=(A\cap B)\cup(A\cap C)
$$

3. First we show that $\bigcup_{n\in \mathbb{N}}(0,\,3^{n})\subseteq(0,\,\infty)$. Let ${} x \in \bigcup_{n\in \mathbb{N}}(0,\,3^{n})$. Therefore, $x \in (0,\,3^{n})$ for some $n \in \mathbb{N}$. Since $(0,\,3^{n})\subset(0,\,\infty)$, then $x \in (0,\,\infty)$.

	Next we show that $(0,\,\infty)\subseteq \bigcup_{n\in \mathbb{N}}(0,\,3^{n})$. Let $x \in (0,\, \infty)$. Now let $k=\ceil*{\log_{3}(x)} +1\in \mathbb{N}$. Therefore, $3^{k}>x>0$. Therefore, $x \in  (0,\, 3^{k})$, so $x \in  \bigcup_{n\in \mathbb{N}} (0,\, 3^{n})$
 Therefore, $\bigcup_{n\in \mathbb{N}} (0,\, 3^{n})=(0,\, \infty) {}$.

 4. First we show that ${} \{ 1 \}\subseteq\bigcap_{n\in \mathbb{N}} \left( 1-\frac{1}{n^{2}},\, 1+\frac{1}{n^{2}} \right) {}$. Suppose that ${} x \in \{ 1 \}  {}$. Then $x=1$ Take $k \in  \mathbb{N} {}$. Since ${} \frac{1}{k^{2}}>0 {}$, then ${} 1-\frac{1}{k^{2}}<1 {}$, and ${} 1+\frac{1}{k^{2}}>1$. Therefore, ${} 1 \in  \left( 1-\frac{1}{k^{2}},\, 1+\frac{1}{k^{2}} \right)$ for all ${} k \in  \mathbb{N}$. Therefore, ${} 1 \in  \bigcap_{n\in \mathbb{N}}\left( 1-\frac{1}{k^{2}},\, 1+\frac{1}{k^{2}} \right)  {}$

	 Now we show that ${} \bigcap_{n\in \mathbb{N}} \left( 1-\frac{1}{n^{2}},\, 1+\frac{1}{n^{2}} \right)\subseteq \{ 1 \} {}$. We do this by contrapositive; suppose we have ${} x \in  \mathbb{R} {}$ such that ${} x\notin\{ 1 \} {}$. Then we have 2 cases:
	 Case 1: ${} x<1$. Then let ${} k=\ceil*{\frac{1}{\sqrt{1-x}}}+1 {}$. Then we have
$$
\begin{align}
1-\frac{1}{k^{2}} & =1-\frac{1}{\left(  \ceil*{\frac{1}{\sqrt{1-x}}}+1  \right)^{2} } \\
 & >1-\frac{1}{\left( \frac{1}{\sqrt{1-x}}\right)^{2}} \\
 & =1-(1-x) \\
 & =x
\end{align}
$$
	Therefore, there exists a ${} k\in \mathbb{N} {}$ such that ${} x\notin\left( 1-\frac{1}{k^{2}},1+\frac{1}{k^{2}} \right)$, so $x \notin \bigcap_{n\in \mathbb{N}} \left( 1-\frac{1}{n^{2}},\, 1+\frac{1}{n^{2}} \right) {}$.
	Case 2: ${} x>1 {}$. Then let ${} k=\floor*{\frac{1}{\sqrt{x-1}}} -1 {}$. Observe that
$$
\begin{align}
 1+\frac{1}{k^{2}} & =1+\frac{1}{\left( \floor*{\frac{1}{\sqrt{x-1}}} -1 \right)^{2}}   \\
 & <1+\frac{1}{\left( \frac{1}{\sqrt{x-1}} \right)^{2}} \\
 & =1+x-1 \\
 & =x
 \end{align}
$$
	Therefore, there a exists a ${} k \in  \mathbb{N} {}$ such that ${} x \notin \left( 1-\frac{1}{k^{2}},\, 1+\frac{1}{k^{2}} \right) {}$, so ${} x \notin \bigcap_{n\in \mathbb{N}} \left( 1-\frac{1}{k^{2}},\, 1+\frac{1}{k^{2}} \right) {}$. 
	Therefore, if ${} x \in  \bigcap_{n\in \mathbb{N}} \left( 1-\frac{1}{k^{2}},\, 1+\frac{1}{k^{2}} \right) {}$, then $x \in \{ 1 \}$. 
	${}$ 
	Therefore, ${} \bigcap_{n\in \mathbb{N}} \left( 1-\frac{1}{k^{2}},\, 1+\frac{1}{k^{2}} \right)=\{ 1 \}$

 5. First we show that that ${} \bigcup_{n\in \mathbb{N}} (-2n^{3},\, 2n^{3})\subseteq\mathbb{R}$. Let ${} x \in  \bigcup_{n\in \mathbb{N}} (-2n^{3},\, 2n^{3}) {}$. Then ${} x \in  (-2n^{3},\, 2n^{3})$ for some $n \in  \mathbb{N}$. Since ${} (-2n^{3},\, 2n^{3})\subset \mathbb{R}$, as it is an interval, then ${} x \in  \mathbb{R} {}$. Therefore, ${} \bigcup_{n\in \mathbb{N}} (-2n^{3},\, 2n^{3})\subseteq \mathbb{R} {}$. 

	 Next we show that $\mathbb{R}\subseteq \bigcup_{n\in \mathbb{N}} (-2n^{3},\, 2n^{3})$. Let $x \in  \mathbb{R}$, and let ${} k=\ceil*{\sqrt[3]{\frac{|x|}{2}}}+1 {}$. Observe that 
  $$
\begin{align}
2k^{3} & =2\left( \ceil*{\sqrt[3]{\frac{|x|}{2}}}+1  \right)^{3} \\
 & >2\left( \sqrt[3]{\frac{|x|}{2}} \right)^{3} \\
 & =|x|
\end{align}
$$

	 Therefore, $|x|<2k^{3}$, so we have ${} -2k^{3}<x<2k^{3} {}$. Therefore, ${} x \in  (-2k^{3},\, 2k^{3})$, so ${} x \in  \bigcup_{n\in \mathbb{N}} (-2n^{3},\, 2n^{3})$, and ${} \mathbb{R}\subseteq \bigcup_{n\in \mathbb{N}} (-2n^{3},\, 2n^{3}) {}$.
	Therefore, we have that ${} \bigcup_{n\in \mathbb{N}} (-2n^{3},\, 2n^{3})=\mathbb{R}$.

 6. First we show that ${} \{ 0 \}\subseteq\bigcap_{n=0}^{\infty} [0,\, 2^{-n}] {}$. Let ${} x \in  \{ 0 \} {}$. Therefore, ${} x=0$. Pick some ${} k \in  \mathbb{N}_{0} {}$. It is clear that ${} 0 \in  [0,\, 2^{-n}] {}$, as $0$ is included in the lower bound of the interval, and it is inclusive. Therefore, ${} \{ 0 \}\subseteq \bigcap_{n=0}^{\infty} [0,\, 2^{-n}] {}$.

	 Next we show that $\bigcap_{n=0}^{\infty} [0,\, 2^{-n}]\subseteq \{ 0 \}$. We do this by contrapositive. First note that $\mathbb{R}$ clearly contains all sets in question here, so we can treat it as our universe. Therefore, pick some ${} x \in  \mathbb{R} {}$ such that ${} x\notin\{ 0 \}$. Therefore, $x\neq 0$. We have 2 cases: 

	  Case 1: $x<0 {}$. If $x<0$, then it is clearly not a member of any ${} [0,\, 2^{-n}] {}$, as they have a lower bound of $0$. Therefore, ${} x \notin\bigcap_{n=1}^{\infty} [0,\, 2^{-n}] {}$. 

	 Case 2: $x>0 {}$. Let ${} k=\ceil*{-\log_{2}(x)} +1 {}$. Observe that ${} 2^{-k}=2^{\ceil*{-\log_{2}(x)} +1}<2^{-\log_{2}(x)}=x {}$. Therefore, $x>2^{-k}$, so there exists some ${} k \in  \mathbb{N}_{0} {}$ such that ${} x\notin [0,\, 2^{-k}] {}$. Therefore, ${} x\notin \bigcap_{n=0}^{\infty} [0,\, 2^{-n}]$. By contrapositive, we have that if $x \in  \bigcap_{n=0}^{\infty} [0,\, 2^{-n}] {}$, then ${} x \in \{ 0 \} {}$.

	  Therefore, we have ${} \bigcap_{n=0}^{\infty} [0,\, 2^{-n}]\subseteq \{ 0 \}$. Therefore, ${} \bigcap_{n=0}^{\infty} [0,\, 2^{-n}]=\{ 0 \} {}$

