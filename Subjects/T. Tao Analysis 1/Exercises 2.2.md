---
tags:
  - exercises
  - ttao_analysis1
date: 2023-10-21
---
[[Directory]], [[T. Tao Analysis 1|Subject Directory]]
[[1. The Natural Numbers|Relevant Notes]]
[[Analysis I - Terence Tao.pdf#page=24|Exercises in Textbook]]
1. Suppose that ${} a,\, b,\, c\in \mathbb{N} {}$. We induct on $a$, fixing $b$ and $c$. First, the base case: if ${} a=0 {}$, then we have
$$
\begin{align}
a+(b+c) & =0+(b+c) \\
 & =b+c & & \text{ by 2.1} \\
 & =(0+b)+c &  & \text{ by 2.1}
\end{align}
$$
Now suppose by induction that ${} a+(b+c)=(a+b)+c {}$. Then we have
$$
\begin{align}
(a{+}{+})+(b+c) & =(a+(b+c)){+}{+} &  & \text{ by 2.1} \\
 & =((a+b)+c){+}{+} &  & \text{ by hypothesis} \\
 & =((a+b){+}{+})+c &  & \text{ by 2.1} \\
 & =((a{+}{+})+b)+c &  & \text{ by 2.1}
\end{align}
$$
Therefore, by the induction principle, we have that ${} a+(b+c)=(a+b)+c {}$ for all ${} a,\, b,\, c\in \mathbb{N} {}$.

2. We work by induction on $a$. Base case: if $a=1$, then suppose that ${} b{+}{+}=1$. Note that $1=0{+}{+} {}$. Therefore, by Axiom 4, we have ${} b=0$. Therefore, there exists a unique $b$ such that $b{+}{+}=a {}$.

Now suppose we have for some ${} a \in \mathbb{N} {}$, we have a unique ${} b\in \mathbb{N} {}$ such that ${} a=b{+}{+} {}$. Now we have $a{+}{+}=a{+}{+} {}$, as ${} a\in \mathbb{N} {}$. Suppose we also have ${} a{+}{+}=c{+}{+} {}$ for some ${} c \in  \mathbb{N}$. Then by Axiom 4, we have $a=c {}$, so $a {}$ is unique. Therefore, by the induction hypothesis, for all positive ${} a \in  \mathbb{N} {}$, we have a ${} b\in \mathbb{N} {}$ such that ${} a=b{+}{+} {}$.

3. 
Part 1:
Let ${} a\in \mathbb{N} {}$. Then we have $a=a+0 {}$ by ${} 2.2 {}$, and ${} 0\in \mathbb{N} {}$ by Axiom 1. Therefore, by ${} 2.11 {}$, we have ${} a\geq a {}$

Part 2:
Let ${} a,\, b,\, c\in \mathbb{N} {}$ such that $a\geq b$ and $b\geq c {}$. Then, by ${} 2.11 {}$, we have ${} x,\, y \in  \mathbb{N}$ such that ${} a=b+x {}$ and ${} b=c+y {}$. Substituting, we have ${} a=c+x+y=c+(x+y) {}$, and ${} x+y\in \mathbb{N} {}$ by ${} 2.1 {}$, so we have ${} a\geq c$ by ${} 2.11$.

Part 3: 
Let $a,\, b\in \mathbb{N}$ such that $a\geq b$ and $b\geq a {}$. Then, by ${} 2.11 {}$ we have $x,\, y \in \mathbb{N}$ such that ${} a=b+x$ and ${} b=a+y {}$. Substituting, we have ${} a=a+x+y {}$, so by ${} 2.6 {}$ we have ${} x+y=0 {}$. Therefore, by ${} 2.9$, we have ${} x=y=0$, and so, ${} a=b+y=b+0=b {}$ by ${} 2.2 {}$.

Part 4:
Working ${} (\Rightarrow )$. Let $a,\, b\in \mathbb{N}$ such that $a\geq b$. Now let ${} c \in \mathbb{N} {}$. By ${} 2.11 {}$, we have $x \in \mathbb{N}$ such that ${} a=b+x {}$. By ${} 2.6 {}$, we have $a+c=b+c+x=(b+c)+x$. Therefore, by ${} 2.11 {}$, ${} a+c\geq b+c$

Now working $(\Leftarrow )$. Let $a,\, b,\, c\in \mathbb{N}$ such that ${} a+c\geq b+c {}$. Then by ${} 2.11 {}$, there exists $x \in \mathbb{N}$ such that $a+c=(b+c)+x=b+c+x$, by ${} 2.5$. Then, by ${} 2.6 {}$, we have ${} a=b+x {}$, so by ${} 2.11 {}$, we have $a\geq b$.
Therefore $a\geq b$ iff ${} a+c\geq b+c {}$, for all ${} a,\, b,\, c \in \mathbb{N} {}$.

Part 5:
Working ${} (\Rightarrow ) {}$. Suppose we have ${} a,\, b\in \mathbb{N} {}$ such that $a<b {}$. By ${} 2.11 {}$, we have some $x \in \mathbb{N} {}$ such that ${} b=a+x {}$, and that $b\neq a {}$. Suppose that ${} x=0 {}$. Therefore, we have $b=a+x=a+0=a {}$, by $2.2 {}$. However, we assumed that $b\neq a {}$. This is a contradiction, therefore, $x\neq 0$, and so $x {}$ is positive. 

Working ${} (\Leftarrow ) {}$. Suppose we have ${} a,\, b,\, x \in \mathbb{N} {}$ with $x {}$ positive such that ${} b=a+x {}$. Therefore, we have $b\geq a {}$ by ${} 2.11 {}$. Suppose we have ${} b=a {}$. Then we would have
$$
\begin{align}
b & =a+x \\
a & =a+x \\
x & =0  &  & \text{ by 2.6}
\end{align}
$$
However, we assumed that ${} x {}$ is positive, so this is a contradiction. Therefore, ${} b\neq a {}$, and so ${} b>a {}$.
Therefore, ${} a<b {}$ iff there exists a positive ${} x \in \mathbb{N} {}$ such that $b=a+x {}$.

Part 6: 
Working ${} (\Rightarrow )$. Suppose we have ${} a,\, b\in \mathbb{N} {}$ such that $a<b {}$. By ${} 2.12.5 {}$, there exists some positive ${} x \in \mathbb{N}$ such that ${} b=a+x$. Since $x {}$ is positive, then by ${} 2.10 {}$, we have some ${} y \in \mathbb{N}$ such that ${} x=y{+}{+}$. Now we have 
$$
\begin{align}
b & =a+x \\
 & =a+(y{+}{+}) \\
 & =(a+y){+}{+}  &  &  \text{ by 2.3} \\
 & =(a{+}{+})+y &  & \text{ by 2.1} \\
\end{align}
$$
Therefore, by ${} 2.11 {}$, we have $b\geq a{+}{+}$.

Working ${} (\Leftarrow ) {}$. Suppose we have ${} a,\, b\in \mathbb{N} {}$ such that $a{+}{+}\leq b {}$. By ${} 2.11 {}$, we have some ${} x \in \mathbb{N} {}$ such that
$$
\begin{align}
b & =(a{+}{+})+x \\
 & =(a+x){+}{+} &  & \text{ by 2.1} \\
 & =a+(x{+}{+}) &  & \text{ by 2.3} \\
\end{align}
$$
By Axiom 3, we have $x{+}{+}\neq 0$, so $x{+}{+}$ is positive. Therefore, by ${} 2.12.5 {}$, we have $b>a$.
Therefore, $a<b$ iff $a{+}{+}\leq b$.

4. 
First we show that at most 1 of the statements hold. Let $a,\, b \in \mathbb{N}$. If $a<b {}$ or $a>b {}$, the $a\neq 0$ by ${} 2.11 {}$. Now suppose we have ${} a<b$ and $b>a {}$, then by ${} 2.11 {}$ we have $a\leq b {}$ and $b\geq a$. By ${} 2.12.3 {}$, we then have ${} a=b {}$. This is a contradiction, as $a\neq b$. Therefore, at most 1 statement holds.

Next we show that at least 1 statement is true. We induct on $a$, keeping $b {}$ fixed. For the base case, when ${} a=0 {}$, then by ${} 2.1 {}$, we have ${} b=0+b$. Since ${} b\in \mathbb{N} {}$, then we have $b\geq 0$. We now have 2 cases: if ${} b=0 {}$, then $b=a$. Otherwise, $b\neq 0$, and so ${} b>0=a {}$. Therefore, the base case holds.

Now suppose the trichotomy holds for $a {}$. Then we have 3 cases:

Case 1: $a>b$. Then, by ${} 2.12.5 {}$, we have some positive ${} x \in \mathbb{N}$ such that $a=b+x$. Therefore, we have 
$$
\begin{align}
a & =b+x \\
	a{+}{+} & =(b+x){+}{+} \\
a{+}{+} & =b+(x{+}{+})
\end{align}
$$
Since ${} x {}$ is positive, then $x{+}{+}$ is positive by, $2.8$. Therefore, $a{+}{+}>b$, by $2.12.5 {}$.

Case 2: ${} a=b {}$. Then we have ${} a{+}{+}=a+1=b+1 {}$. Therefore, since $1 {}$ is positive, we have ${} a{+}{+}>b {}$ by ${} 2.12.5 {}$. 

Case 3: $a<b {}$. By ${} 2.12.6 {}$, we have $a{+}{+}\leq b$. Therefore, if ${} a{+}{+}=b {}$, then ${} a{+}{+}=b {}$. Otherwise, $a{+}{+}\neq b$, and so by ${} 2.11 {}$, we have $a{+}{+}<b$.
Therefore, by the induction principle, we have that for all ${} a,\, b\in \mathbb{N}$, either ${} a<b {}$ or ${} a=b {}$ or ${} a>b. {}$

5. 
Let ${} m_{0}\in \mathbb{N}$, and let $P:\mathbb{N}\to{}\{ \bot,\, \top \}$ be a statement on the natural numbers. Let $Q:\mathbb{N}\to{}\{ \bot,\, \top \}$ such that 
$$
Q(n)=\bigwedge_{k=m_{0}}^{n-1}P(n)
$$
That is, ${} Q(n)=\top$ iff ${} P(m)=\top {}$ for all ${} n-1\geq m>m_{0} {}$, or by $$ $$