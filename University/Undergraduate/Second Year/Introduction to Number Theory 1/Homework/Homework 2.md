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
