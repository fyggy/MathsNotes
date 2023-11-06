---
tags:
  - homework
  - intro_algebra1
date: 2023-10-14
pset: 3
---
[[Directory]], [[Intro to Algebra 1|Subject Directory]]
1. First, we show that ${} (A \cup B)\times C\subseteq(A\times C)\cup(B\times C)$. Let ${} x \in (A\cup B)\times C {}$. Therefore, ${} x=(x_{1},\, x_{2}) {}$, with ${} x_{1}\in A\cup B {}$ and ${} x_{2} \in  C {}$. We have 2 cases:
	Case 1: ${} x_{1} \in  A$. Then ${} x \in A\times C {}$, so ${} x \in  (A\times C)\cup(B\times C) {}$. 
	Case 2: ${} x_{1} \in  B {}$. Then ${} x \in  B\times C {}$, so ${} x \in  (A\times C)\cup(B\times C)$.
	Therefore, we have ${} (A \cup B)\times C\subseteq(A\times C)\cup(B\times C) {}$

	Next, we show that ${} (A\times C)\cup(B\times C)\subseteq{} (A \cup B)\times C {}$. Let ${} x \in  (A\times C)\cup(B\times C) {}$. Therefore, ${} x \in A\times C {}$ or ${} x \in  B\times C {}$. We have 2 cases:
	Case 1: ${} x \in  A\times C {}$. Then ${} x=(x_{1},\, x_{2})$, with ${} x_{1}\in  A$ and ${} x_{2}\in C {}$. Therefore, ${} x_{1}\in A\cup B {}$, so ${} x \in  (A\cup B)\times C {}$. 
	Case 2: ${} x \in B\times C {}$. Then ${} x=(x_{1},\, x_{2}) {}$, with ${} x_{1}\in B {}$ and ${} x_{2}\in C {}$. Therefore, ${} x_{1} \in  A\cup B {}$, so ${} x \in  (A\cup B)\times C {}$. 
	Therefore, we have $(A\times C)\cup(B\times C)\subseteq(A\cup B)\times C$, so ${} (A \cup B)\times C=(A\times C)\cup(B\times C) {}$

 2. We have
 $$
\begin{align}
2022 & =40\cdot 50+22 \\
50 & =2\cdot 22+6 \\
22 & =3\cdot 6+4 \\
6 & =1\cdot 4+2 \\
4 & =2\cdot 2+0
\end{align}
$$
	Therefore, ${} \gcd(50,\, 2022)=2$. Now constructing Bézout's identity, we get 
 $$
\begin{align}
2 & =6-1\cdot 4 \\
 & =6-1\cdot (22-3\cdot 6) \\
 & =4\cdot 6-22 \\
 & =4\cdot (50-2\cdot 22)-22 \\
 & =4\cdot 50-9\cdot 22 \\
 & =4\cdot 50-9\cdot (2022-40\cdot 50) \\
 & =364\cdot 50-9\cdot 2022
\end{align}
$$
	Therefore, ${} x=364,\, y=-9 {}$.

 3. Let ${} a,\, p \in  \mathbb{Z} {}$, with $p$ prime, and ${} p\nmid a$. Suppose that $k\mid p$ and $k\mid a$. Since $k\mid p$, then ${} k=1$ or ${} k=p {}$. If ${} k=p {}$, then $p\mid a$, but this is a contradiction, so $k\neq p$. Therefore, ${} k=1 {}$. This is the greatest common divisor, as any other number would not divide $p$. Therefore, ${} \gcd(a,\, p)=1. {}$

 4. We have
 $$
\begin{align}
98 & =2\cdot 40+18 \\
40 & =2\cdot 18+4 \\
18 & =4\cdot 4+2 \\
4 & =2\cdot 2+0
\end{align}
$$
	Therefore, $\gcd(98,\, 40)=2$. Now, constructing Bézout's identity, we get
 $$
\begin{align}
2 & =18-4\cdot 4 \\
 & =18-4\cdot (40-2\cdot 18) \\
 & =9\cdot 18-4\cdot 40 \\
 & =9\cdot (98-2\cdot 40)-4\cdot 40 \\
 & =9\cdot 98-22\cdot 40
\end{align}
$$
	Therefore, ${} x=9,\, y=-22 {}$

 5. Let ${} a,\, p \in  \mathbb{Z} {}$, with $p\mid a$. Since $a {}$ is prime, then by definition, if ${} k\mid a$, then ${} k=1 {}$ or $k=a$, for some ${} k\in \mathbb{N} {}$. Since $1$ is not a prime, then since $p\mid a$, then ${} p=a {}$.

 6. Let ${} a_{1},\, a_{2},\,\dots,\,a_{k}\in \mathbb{Z} {}$, and ${} p \in \mathbb{Z} {}$ is prime. Suppose that $p\mid a_{1}a_{2}\dots a_{k}$. We work by induction on $k$. First, the base case for ${} k=1 {}$. This is trivial; $p\mid a_{1}\Rightarrow p\mid a_{1} {}$. Next, we set the induction hypothesis. Suppose that this statement is true for ${} k=n {}$, that is, for all ${} a_{1},\,\dots,\,a_{n}\in \mathbb{Z} {}$ and $p \in  \mathbb{Z}$ prime with ${} p\mid a_{1}\dots a_{n} {}$, then ${} p\mid a_{i}$ for some ${} i\in \{ 1,\dots n \}$. 
 
	 Now let ${} a_{1},\,\dots,\,a_{n+1}\in \mathbb{Z} {}$, and let $p \in  \mathbb{Z}$ prime with ${} p\mid a_{1}\dots a_{n+1} {}$. By [[5. Primes and Binary Operations#Lemma 1.3|Lemma 1.3]], we have that either ${} p\mid a_{1}\dots a_{n} {}$ or ${} p\mid a_{n+1}$. By induction hypothesis, for the first case, then there exists ${} i\in \{ 1,\, \dots,\, n \} {}$ such that ${} p\mid a_{i}$. For the second case, let ${} i=n+1$. Therefore, there exists an ${} i \in  \{ 1,\,\dots,\,n+1 \} {}$ such that ${} p\mid a_{i}$. Therefore, the statement holds for ${} k=n+1 {}$

	  By the induction principle, then the statement holds for all $k\geq 1$

7. 
i) The operation ${} * {}$ is not associative. Let ${} a=b=1 {}$, and $c=0$. Note that ${} a*(b*c)=1*(1*0)=1*1=2$ and $(a*b)*c=(1*1)*0=2*0=1$. We have $1\neq 0$, therefore, $*$ is not associative. 

The operation $*$ is commutative. For some ${} a,\,  b \in  \mathbb{R} {}$, we have ${} a*b=ab+1=ba+1=b*a {}$. This follows from the commutativity of multiplication over ${} \mathbb{R} {}$

ii) The operation $*$ is associative. For some ${} a,\, b,\, c \in  \mathbb{R} {}$, we have
$$
\begin{align}
a*(b*c) & =a*(b+c+1) \\
 & =a+(b+c+ 1)+1 \\
 & =(a+b+1)+c+1 \\
 & =(a*b)*c
\end{align}
$$
This follows from the associativity of addition. 
The operation $*$ is commutative. For some ${} a,\, b \in  \mathbb{R} {}$, we have
$$
\begin{align}
a*b & =a+b+1 \\
 &=b+a+1 \\
 &=b*a
\end{align}
$$

iii) The operation $*$ is associative. Consider ${} a,\, b,\, c \in  \mathbb{Z} {}$. Then we have
$$
\begin{align}
a*(b*c) & =a*b \\
 & =a \\
 & =a*b \\
 & =(a*b)*c
\end{align}
$$
The operation $*$ is not commutative. Consider ${} a=1,\, b=0 {}$. Then $a*b=1\neq 0=b*a$.

iv) The operation $*$ is associative. Consider ${} f:\mathbb{Z}\to{} \mathbb{Z},\, g:\mathbb{Z}\to{} \mathbb{Z},\, h:\mathbb{Z}\to{} \mathbb{Z} {}$. Then we have
$$
\begin{align}
(f+(g+h))(n) & =f(n)+(g+h)(n) \\
	 & =f(n)+g(n)+h(n) \\
	 & =(f+g)(n)+h(n) \\
 & =((f+g)+h)(n)
\end{align}
$$
The operation $*$ is commutative. Consider ${} f:\mathbb{Z}\to{} \mathbb{Z},\, g:\mathbb{Z}\to{} \mathbb{Z} {}$. Then we have
$$
\begin{align}
(f+g)(n) & =f(n)+g(n) \\
 & =g(n)+f(n) \\
 & =(g+f)(n)
\end{align}
$$

v) The operation $*$ is associative. Consider ${} \vec{v}=\begin{pmatrix} x_{1} \\ y_{1} \\ z_{1} \end{pmatrix}$ , ${} \vec{w}=\begin{pmatrix} x_{2} \\ y_{2} \\ z_{2} \end{pmatrix}  {}$, and $\vec{u}=\begin{pmatrix} x_{3} \\ y_{3} \\ z_{3} \end{pmatrix} {}$, with ${} \vec{v},\, \vec{w},\, \vec{u}\in \mathbb{R}^{3} {}$. Then we have
$$
\begin{align}
\vec{v}*(\vec{w}*\vec{u}) & =\begin{pmatrix} x_{1} \\ y_{1} \\ z_{1} \end{pmatrix} +\begin{pmatrix} x_{2}+x_{3} \\ y_{2}+y_{3} \\ z_{2}+z_{3} \end{pmatrix}  \\
 & =\begin{pmatrix} x_{1}+(x_{2}+x_{3}) \\ y_{1}+(x_{2}+y_{3}) \\ z_{1}+(z_{2}+z_{3}) \end{pmatrix}  \\
 & =\begin{pmatrix} (x_{1}+x_{2})+x_{3} \\ (y_{1}+y_{2})+y_{3} \\ (z_{1}+z_{2})+z_{3} \end{pmatrix}  \\
 & =\begin{pmatrix} x_{1}+x_{2} \\ y_{1}+y_{2} \\ z_{1}+z_{2} \end{pmatrix} +\begin{pmatrix} x_{3} \\ y_{3} \\ z_{3} \end{pmatrix}  \\
 & =(\vec{v}*\vec{w})*\vec{u}
\end{align}
$$
As required
The operation $*$ is commutative. Consider ${} \vec{v}=\begin{pmatrix} x_{1} \\ y_{1} \\ z_{1} \end{pmatrix}  {}$, and ${} \vec{u}=\begin{pmatrix} x_{2} \\ y_{2} \\ z_{2} \end{pmatrix}  {}$. Then we have
$$
\begin{align}
\vec{v}*\vec{u} & =\begin{pmatrix} x_{1} \\ y_{1} \\ z_{1} \end{pmatrix} +\begin{pmatrix} x_{2} \\ y_{2} \\ z_{2} \end{pmatrix}  \\
 & =\begin{pmatrix} x_{1}+x_{2} \\ y_{1}+y_{2} \\ z_{1}+z_{2} \end{pmatrix}  \\
 & =\begin{pmatrix} x_{2}+x_{1} \\ y_{2}+y_{1} \\ z_{2}+z_{1} \end{pmatrix}  \\
 & =\begin{pmatrix} x_{2} \\ y_{2} \\ z_{2} \end{pmatrix} +\begin{pmatrix} x_{1} \\ y_{1} \\ z_{1} \end{pmatrix}  \\
 & =\vec{u}*\vec{v}
\end{align}
$$
vi) The operation $*$ is not associative. consider ${} \vec{v}=\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} {}$, and $\vec{w}=\vec{u}=\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$. Then we have
$$
\begin{align}
\vec{v}*(\vec{w}*\vec{u}) & =\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \times \left( \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} \times \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}  \right)  \\
 & =\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \times \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}  \\
 & =\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}  \\
 \\
(\vec{v}*\vec{w} ) *\vec{u} & =\left( \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \times\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}  \right) \times \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}  \\
 & =\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \times \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}  \\
 & =\begin{pmatrix} -1 \\ 0 \\ 0 \end{pmatrix} 
\end{align}
$$
Since ${} \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \neq \begin{pmatrix} -1 \\ 0 \\ 0 \end{pmatrix}$, then $*$ is not associative. 

The operation $*$ is not commutative. Consider ${} \vec{v}=\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}  {}$, and ${} \vec{u}=\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}  {}$. Then we have
$$
\begin{align}
\vec{v}*\vec{u} & =\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \times \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}  \\
 & =\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}  \\
 \\
\vec{u}*\vec{v} & =\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} \times \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}  \\
 & =\begin{pmatrix} 0 \\ 0 \\ -1 \end{pmatrix} 
\end{align}
$$
Since ${} \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \neq \begin{pmatrix} 0 \\ 0 \\ -1 \end{pmatrix}  {}$, then $*$ is not commutative. 
