---
tags:
  - homework
  - numtheory1
date: 2024-09-30
pset: 2
completed: false
---
[[Directory]], [[University/Undergraduate/Second Year/Introduction to Number Theory 1/Introduction to Number Theory 1|Subject Directory]]
[[University/Undergraduate/Second Year/Introduction to Number Theory 1/Homework/Homework 1|🞀🞀]] [[University/Undergraduate/Second Year/Introduction to Number Theory 1/Homework/Homework 1|◀]] [[University/Undergraduate/Second Year/Introduction to Number Theory 1/Homework/Homework 3|▶]] [[University/Undergraduate/Second Year/Introduction to Number Theory 1/Homework/Homework 11|🞂🞂]]

[[University/Undergraduate/Second Year/Introduction to Number Theory 1/Homework/Worksheets/number_theory_2.pdf|Worksheet]]
1. 
a)
Let ${} d \mid n {}$. Then we have
$$
d = q_{1}^{c_{1}} q_{2}^{c_{2}}\dots q_{s}^{c_{s}}
$$
for distinct primes ${} q_{i}$ and positive integers ${} c_{i} \in \mathbb{Z}^{+} {}$. Note that ${} dk=n {}$ for some $k>0 {}$. Now
$$
k=q_{s+1}^{c_{s+1}}\dots q_{s+t}^{c_{s+t}}
$$
for distinct primes ${} r_{i}$ and positive integers ${} d_{i} \in \mathbb{Z}^{+} {}$. 
$$
p_{1}^{a_{1}}\dots p_{r}^{a_{r}}=n=dk=q_{1}^{c_{1}}\dots q_{s}^{c_{s}}\cdot q_{s+1}^{c_{s+1}}\dots q_{s+t}^{c_{s+t}}
$$
By the fundamental theorem of arithmetic, then given some ${} 1\leq i\leq s {}$, then there exists some $1\leq j\leq r$ such that ${} q_{i}=p_{j} {}$, and that ${} a_{j}=c_{i}+c_{\ell} {}$ for some $\ell$. Then ${} c_{i}\leq a_{i} {}$. Therefore, 
$$
d=p_{1}^{b_{1}} p_{2}^{b_{2}}\dots p_{r}^{b_{r}}
$$
for some ${} b_{j}=c_{i} {}$ or ${} b_{j}=0 {}$. 
b)
Set ${} A=\prod _{i=1}^{r} \{ 0\leq n\leq a_{i} \mid n \in \mathbb{N} \} {}$. Note that the map 
$$
f:A\to{}\mathbb{Z}^{+}
$$
mapping
$$
(b_{1},\,\dots,\,b_{r})\mapsto p_{1}^{b_{1}} \dots p_{r}^{b_{r}}
$$
maps surjectively between $A$ and ${} \{ d \mid n \mid d \in \mathbb{Z}^{+} \} {}$, due to part a. Now suppose that
$$
f((b_{1},\,\dots,\,b_{r}))=f((c_{1},\,\dots,\,c_{r}))
$$
Then 
$$
p_{1}^{b_{1}}\dots p_{r}^{b_{r}}=p_{1}^{c_{1}}\dots p_{r}^{c_{r}}
$$
and by the fundamental theorem of arithmetic, then ${} b_{i}=c_{i} {}$, and $f$ is injective. Since
$$
|\{ 0 \leq n<a_{i} \mid  n \in \mathbb{N} \}|=a_{i}+1
$$
then
$$
|A|=\prod _{i=1}^{r}(a_{i}+1)=|\{ d \mid  n \mid  d \in \mathbb{Z}^{+} \}|
$$
2. 
We see that
$$
100000=10^{5}=2^{5}5^{5}
$$
and so the number of divisors is ${} (5+1)(5+1)=36 {}$. Also, 
$$
40000=2^{2}\cdot 10^{4}=2^{6}5^{4}
$$
and so the number of divisors is ${} (6+1)(4+1)=35 {}$
2. 
a)
If ${} \gcd(a,\, p^{2})=p {}$, then ${} p \mid a {}$, and so ${} p^{2} \mid a^{2} {}$, and clearly ${} p^{2} \mid  p^{2} {}$, so ${} \gcd(a^{2},\, p^{2}) {}$
b)
Let ${} p=2 {}$, ${} a=2 {}$, ${} b=8 {}$. Then ${} \gcd(a,\, p^{2})=p {}$, ${} \gcd(b,\, p^{2})=p^{2} {}$, but ${} \gcd(ab,\, p^{4})=p^{4}\neq p^{3} {}$
c)
If ${} \gcd(a,\, p^{2})=p {}$, then ${} a=xp {}$. Likewise, ${} b=yp {}$. Then ${} ab=p^{2}xy {}$, so ${} p^{2} \mid ab {}$. Now suppose that ${} p^{3} \mid ab {}$. Then ${} p \mid xy {}$. WLOG, suppose that ${} p \mid x {}$. Then ${} a=p^{2}z {}$, and ${} \gcd(a,\, p^{2})=p^{2} {}$, which is a contradiction. Therefore, ${} \gcd(ab,\, p^{4})=p^{2} {}$.
d)
Let ${} a=6 {}$ and ${} p=2 {}$. Then ${} \gcd(a,\, p^{2})=p {}$, but ${} \gcd(a+p,\, p^{2})=p^{2} {}$.
3. 
Given some residue system ${} A=(a_{1},\,\dots,\,a_{17}) {}$, we may turn this into the required form in the following process. Let ${} k_{i}\equiv a_{i} \:(\mathrm{mod}\  3)  {}$, with ${} 0\leq k_{i}\leq 2$. Then Since ${} 17\equiv 2 \:(\mathrm{mod}\  3)  {}$, then we set
$$
A'=\{ a_{i}+17k_{i} \}=\{ b_{i} \}
$$
Note that now ${} b_{i} \equiv a_{i}+17k_{i}\equiv k_{i}+2k_{i}\equiv 3k_{i}\equiv 0\:(\mathrm{mod}\  3)  {}$, and ${} b_{i}\equiv a_{i}+17k_{i}\equiv a_{i} \:(\mathrm{mod}\  17)   {}$.

We apply this process to the trivial residue:
$$
\begin{align}
 & (0,\, 1,\, 2,\, 3,\, 4,\, 5,\, 6,\, 7,8,\, 9,\, 10,\, 11,\, 12,\, 13,\, 14,\, 15,\, 16,\, 17) \\
 &\qquad \qquad \qquad \qquad \qquad \qquad  \downarrow  \\
 & (0,\, 18,\, 36,\, 3,\, 21,\, 39,\, 6,\, 24,\, 42,\, 9,\, 27,\, 45,\, 12,\, 30,\, 48,\, 15,\, 33,\, 51)
\end{align}
$$
4. 
a)
First, note that $105=15 \cdot 7 {}$. Since ${} \gcd(15,\, 7)=1 {}$, then we may set
$$
\begin{align}
 x^{3}+x^{2}+x & \equiv 0 \:(\mathrm{mod}\  15)  \\
 x^{3}+x^{2}+x & \equiv 0 \:(\mathrm{mod}\  7)  
 \end{align} 
$$
In ${} \:(\mathrm{mod}\  7)  {}$, we have
$$
\begin{align}
 x=0 & \Rightarrow f(x)=0\equiv 0 \:(\mathrm{mod}\  7)   \\
x=1  & \Rightarrow f(x)=3\not\equiv 0 \:(\mathrm{mod}\  7)  \\
x=2 & \Rightarrow f(x)=14\equiv 0 \:(\mathrm{mod}\  7)  \\
x=3 & \Rightarrow f(x)=39\not\equiv 0 \:(\mathrm{mod}\  7)  \\
x=4 & \Rightarrow f(x)=84\equiv 0 \:(\mathrm{mod}\  7)  \\
x=5 & \Rightarrow f(x)=155\not\equiv 0\:(\mathrm{mod}\  7)  \\
x=6 & \Rightarrow f(x)=258 \not\equiv 0\:(\mathrm{mod}\  7) 
 \end{align}
$$
Now in ${} \:(\mathrm{mod}\  15)  {}$, note that ${} 15=3\cdot 5 {}$, and since ${} \gcd(3,\, 5)=1 {}$, then we may set
$$
\begin{align}
 x^{3}+x^{2}+x & \equiv 0 \:(\mathrm{mod}\  3)  \\
 x^{3}+x^{2}+x & \equiv 0 \:(\mathrm{mod}\  5)  
 \end{align} 
$$
In ${} \:(\mathrm{mod}\  3)  {}$, we have
$$
\begin{align}
 x=0 & \Rightarrow f(x)=0\equiv 0 \:(\mathrm{mod}\  3)   \\
x=1  & \Rightarrow f(x)=3\equiv 0 \:(\mathrm{mod}\  3)  \\
x=2 & \Rightarrow f(x)=14\not\equiv 0 \:(\mathrm{mod}\  3)  \\
 \end{align}
$$
and in ${} \:(\mathrm{mod}\  5)  {}$, we have
$$
\begin{align}
 x=0 & \Rightarrow f(x)=0\equiv 0 \:(\mathrm{mod}\  5)   \\
x=1  & \Rightarrow f(x)=3\not\equiv 0 \:(\mathrm{mod}\  5)  \\
x=2 & \Rightarrow f(x)=14\not\equiv 0 \:(\mathrm{mod}\  5)  \\
x=3 & \Rightarrow f(x)=39\not\equiv 0 \:(\mathrm{mod}\  5)  \\
x=4 & \Rightarrow f(x)=84\not\equiv 0 \:(\mathrm{mod}\  5)  \\
 \end{align}
$$
Therefore, the only solution is when 
$$
x \equiv 0\:(\mathrm{mod}\  5) \qquad x\equiv 0,\, 1 \:(\mathrm{mod}\  3) \qquad x\equiv 0,\, 2,\, 4 \:(\mathrm{mod}\  7) 
$$
First note that ${} 7-2\cdot 3=1 {}$, and so we have by the CRT, we have $6 {}$ possibilities for $x$:
$$
\begin{align}
x & =0\cdot 7-0\cdot 2\cdot 3=0 &  x & =0\cdot 7-2\cdot 2\cdot 3=-12 & x & =0\cdot 7-4\cdot 2\cdot 3=-24 \\
x & =1\cdot 7-0\cdot 2\cdot 3=7 & x & =1\cdot 7-2\cdot 2\cdot 3 =-5 & x & =1\cdot 7-4\cdot 2\cdot 3 =-17
\end{align}
$$
so, ${} \:(\mathrm{mod}\  21) {}$, we have
$$
x\equiv 0,\, 9,\, 18,\, 7,\, 16,\, 4 \:(\mathrm{mod}\  21) 
$$
Finally, ${} 21-4\cdot 5=1 {}$, and so by the CRT, we have $6$ possibilities for $x$:
$$
\begin{align}
 x & =-20  \cdot 0=0 & x & =-20\cdot 9=-180 & x & =-20\cdot 18=-360 \\
x & =-20\cdot 7=-140 & x & =-20\cdot 16=-320 & x & =-20\cdot 4=-80
 \end{align}
$$
that is, 
$$
x\equiv 0,\, 30,\, 60,\, 70,\, 100,\, 25
$$
b)
Note that ${} 143=11\cdot 13 {}$, and ${} \gcd(11,\, 13)=1 {}$. Now
$$
\begin{align}
x=0 & \Rightarrow f(x)=1 \not\equiv 0 \:(\mathrm{mod}\  11) \quad \not\equiv 0 \:(\mathrm{mod}\  13)  \\
x=1 & \Rightarrow f(x)=4 \not\equiv 0 \:(\mathrm{mod}\  11) \quad \not\equiv 0 \:(\mathrm{mod}\  13)  \\
x=2 & \Rightarrow f(x)=15 \not\equiv 0 \:(\mathrm{mod}\  11) \quad \not\equiv 0 \:(\mathrm{mod}\  13)  \\
x=3 & \Rightarrow f(x)=40 \not\equiv 0 \:(\mathrm{mod}\  11) \quad \not\equiv 0 \:(\mathrm{mod}\  13)  \\
x=4 & \Rightarrow f(x)=85 \not\equiv 0 \:(\mathrm{mod}\  11) \quad \not\equiv 0 \:(\mathrm{mod}\  13)  \\
x=5 & \Rightarrow f(x)=156 \not\equiv 0 \:(\mathrm{mod}\  11) \quad \equiv 0 \:(\mathrm{mod}\  13)  \\
x=6 & \Rightarrow f(x)=259 \not\equiv 0 \:(\mathrm{mod}\  11) \quad \not\equiv 0 \:(\mathrm{mod}\  13)  \\
x=7 & \Rightarrow f(x)=400 \not\equiv 0 \:(\mathrm{mod}\  11) \quad \not\equiv 0 \:(\mathrm{mod}\  13)  \\
x=8 & \Rightarrow f(x)=585 \not\equiv 0 \:(\mathrm{mod}\  11) \quad \equiv 0 \:(\mathrm{mod}\  13)  \\
x=9 & \Rightarrow f(x)=820 \not\equiv 0 \:(\mathrm{mod}\  11) \quad \not\equiv 0 \:(\mathrm{mod}\  13)  \\
x=10 & \Rightarrow f(x)=1111 \equiv  \:(\mathrm{mod}\  11) \quad \not\equiv 0 \:(\mathrm{mod}\  13)  \\
x=11 & \Rightarrow f(x)=1464  \not\equiv 0 \:(\mathrm{mod}\  13)  \\
x=12 & \Rightarrow f(x)=1885  \equiv 0 \:(\mathrm{mod}\  13)  
\end{align}
$$
Therefore, ${} x\equiv 10 \:(\mathrm{mod}\  11)  {}$, and ${} x\equiv 5,\, 8,\, 12 \:(\mathrm{mod}\  13)  {}$. Now note that ${} 6\cdot11-5\cdot13=1 {}$, so by the CRT, we have
$$
\begin{align}
x & =5\cdot 6\cdot 11-10\cdot 5\cdot 13=-320 & x & =8\cdot 6\cdot 11-10\cdot 5\cdot 13=-122  \\
x & =12\cdot 6\cdot 11-10\cdot 5\cdot 13=142
\end{align}
$$
and so
$$
x\equiv 109,\, 21,\, 142
$$
c)
Let ${} f(x)=x^{3}+x^{2}-x+3 {}$. First, note that, if ${} x\geq -2 {}$, then ${} f(x)>0 {}$. As, if ${} x=-2 {}$, then ${} f(x)=1 {}$, if ${} x=-1 {}$, then ${} f(x)=4 {}$, if ${} x=0 {}$, then ${} f(x)=3 {}$ and if ${} x=1 {}$, then ${} f(x)=4 {}$. 

Now if ${} x>1 {}$, then we have that ${} f(x)>x^{2}-x {}$, and ${} x^{2}>x {}$, so ${} f(x)>0 {}$

Now note that if ${} x \leq -3 {}$, then ${} f(x)<0 {}$. In particular, ${} f'(x)=3x^{2}+2x-1>0 {}$, so if $x\leq -3 {}$, then ${} f(x)\leq f(-3)=-12 {}$, and so ${} f(x)<0 {}$.

Therefore, the only root for $f$ is between $-2 {}$ and $-3 {}$, and so there are no integer solutions.
5. 
First note that ${} 6k-1=6k'+5 {}$ where ${} k' \in \mathbb{N} {}$ is a non-negative integer. Now note that if ${} n \in \mathbb{Z}^{+} {}$, then ${} n=6k,\, 6k+1,\, 6k+2,\, 6k+3,\, 6k+4,\, 6k+5 {}$. However, if $n$ is prime, then ${} n=6k+1 {}$ or ${} n=6k+5 {}$, as all other forms have a common divisor. 

Now let ${} x=6a+1 {}$, and ${} y=6b+1 {}$. Then we have
$$
\begin{align}
xy & =(6a+1)(6b+1) \\
 & =36ab+6a+6b+1 \\
 & =6(6ab+a+b)+1
\end{align}
$$
so ${} xy=6c+1 {}$ for some ${} c \in \mathbb{N} {}$. 

Now suppose that there are finitely many primes of the form ${} 6k-1 {}$. List them as
$$
P=(p_{1},\,\dots,\,p_{r})
$$
Let ${} n=6(p_{1}\dots p_{r}) {}$, and let ${} N=n-1 {}$. Let a prime $p {}$ such that ${} p \mid N {}$. We know that since $N$ is odd, then ${} p=6a+1 {}$ or ${} p=6a-1 {}$. However, if ${} p=6a-1 {}$, then ${} p \mid n {}$, which is a contradiction. Therefore, ${} p=6a+1 {}$, and all prime divisors of $N$ are of the form ${} 6a+1 {}$. Therefore, ${} N=6a+1 {}$, and ${} n=6a+2 {}$, so ${} 2\equiv n\equiv 0 \:(\mathrm{mod}\  6)  {}$, which is a contradiction. Therefore, there are infinitely many primes of the form ${} 6k-1 {}$.