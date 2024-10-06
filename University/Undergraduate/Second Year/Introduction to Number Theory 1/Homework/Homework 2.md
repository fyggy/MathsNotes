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

