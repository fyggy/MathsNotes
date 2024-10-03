---
tags:
  - homework
  - numtheory1
date: 2024-09-23
pset: 1
completed: true
---
[[Directory]], [[University/Undergraduate/Second Year/Introduction to Number Theory 1/Introduction to Number Theory 1|Subject Directory]]
[[University/Undergraduate/Second Year/Introduction to Number Theory 1/Homework/Homework 1|🞀🞀]] [[|◀]] [[University/Undergraduate/Second Year/Introduction to Number Theory 1/Homework/Homework 2|▶]] [[University/Undergraduate/Second Year/Introduction to Number Theory 1/Homework/Homework 11|🞂🞂]]

[[University/Undergraduate/Second Year/Introduction to Number Theory 1/Homework/Worksheets/number_theory_1.pdf|Worksheet]]
1.
a)
$$
\begin{align}
359 & =2 \cdot  133 +93 \\
133 & =1 \cdot 93 +40 \\
93 & =2\cdot 40+13 \\
40 & =3\cdot 13+1 \\
13 & =13\cdot 1
\end{align}
$$
Therefore ${} \gcd(359,\, 133)=1 {}$. Now
$$
\begin{align}
 1 & =40-3 \cdot 13 \\
 & =40-3\cdot (93-2\cdot 40)  \\
 & =7\cdot 40 - 3 \cdot 93 \\
 & =7\cdot (133-1\cdot 93)-3\cdot 93 \\
 & =7\cdot 133-10\cdot 93 \\
 & =7\cdot 133-10\cdot (359-2\cdot 133) \\
 & =27\cdot 133-10\cdot 359
 \end{align}
$$
b)
$$
\begin{align}
1771 & =9\cdot 179+160 \\
179 & =1 \cdot  160+19 \\
160 & = 8\cdot 19+8 \\
 19& =2\cdot 8 +3 \\
8 & =2\cdot 3+2 \\
3 & =1\cdot 2+1 \\
2 & =2\cdot 1
\end{align}
$$
Therefore, ${} \gcd(1771, 179)=1 {}$. Now
$$
\begin{align}
1 & =3-1\cdot 2 \\
 & =3-1\cdot (8-2\cdot 3) \\
 & =3\cdot 3-1\cdot 8 \\
 & =3\cdot (19-2\cdot 8)-1\cdot 8 \\
 & =3\cdot 19-7\cdot 8 \\
 & =3\cdot 19-7\cdot (160-8\cdot 19) \\
  & =59\cdot 19-7\cdot 160 \\
 & =59\cdot (179-1\cdot 160)-7\cdot 160 \\
 & =59\cdot 179-66\cdot 160 \\
 & =59\cdot 179-66\cdot (1771-9\cdot 179) \\
 & =653 \cdot 179-66\cdot 1771
\end{align}
$$
c)
$$
\begin{align}
2437 & =2\cdot 875+687 \\
 875 & =1\cdot 687+188 \\
 687 & =3\cdot 188+123 \\
 188 & =1\cdot 123+65 &  \\
123 & =1\cdot 65+58 \\
 65 & =1\cdot 58+7 &  \\
58 & =8\cdot 7+2 \\
7 & =3\cdot 2+1 \\
2 & =2\cdot 1
\end{align}
$$
Therefore, ${} \gcd(2437,\, 875)=1 {}$. Now
$$
\begin{align}
1 & =7-3\cdot 2 \\
 & =7-3\cdot (58-8\cdot 7) \\
 & =25\cdot 7-3\cdot 58 \\
  & =25\cdot (65-1\cdot 58)-3\cdot 58 \\
 & =25\cdot 65-28\cdot 58 \\
 & =25\cdot 65-28\cdot (123-1\cdot 65) \\
 & =53\cdot 65-28\cdot 123 \\
 & =53\cdot (188-1\cdot 123)-28\cdot 123 \\
 & =53\cdot 188-81\cdot 123 \\
 & =53\cdot 188-81\cdot (687-3\cdot 188) \\
 & =296\cdot 188-81\cdot 687 \\
 & =296\cdot (875-1\cdot 687)-81\cdot 687 \\
 & =296\cdot 875-377\cdot 687 \\
 & =296\cdot 875-377\cdot (2437-2\cdot 875) \\
 & =1050\cdot 875-377\cdot 2437
\end{align}
$$
2. 
a)
Let ${} m \in \mathbb{Z} {}$, ${} m\neq 0 {}$. Let ${} a,\, b \in \mathbb{Z} {}$, and ${} d=\gcd(a,\, b) {}$. Since $d \mid a {}$, then ${} md \mid  ma {}$, and since ${} d \mid b {}$, then ${} m d \mid  mb {}$. Therefore, ${} md \mid \gcd(ma,\, mb) {}$. Now suppose that ${} d'=\gcd(ma,\, mb) {}$. Then ${} m \mid d' {}$, so we have ${} d'=mk {}$. Now ${} mk \mid ma {}$, so ${} k \mid a {}$ and ${} mk \mid  mb {}$, so ${} k \mid  b {}$. Therefore, ${} k \mid d {}$, so ${} mk=d'\mid md {}$, and ${} d'=\pm md {}$. Therefore, ${} d'=|m d|=|m|d {}$, as required.

b)
Let ${} a,\, b \in \mathbb{Z} {}$, and let ${} d=\gcd(a,\, b) {}$. Then ${} a=dm {}$ and ${} b=dn {}$. Now 
$$
d=\gcd(a,\, b)=\gcd(dm,\, dn)=d\gcd(m,\, n)
$$
so ${} \gcd(m,\, n)=1 {}$, and ${} a /d {}$ and ${} b /d {}$ are coprime
3.
Let ${} a,\, b \in \mathbb{Z}^{+} {}$ with ${} \gcd(a,\, b)=\lcm(a,\, b) {}$. Since ${} \lcm(a,\, b)=ab /\gcd(a,\, b) {}$, then ${} \gcd(a,\, b)^{2}=ab {}$. WLOG, suppose that ${} a\geq b {}$. Then ${} \gcd(a,\, b)^{2}\geq b^{2} {}$, or ${} \gcd(a,\, b)\geq b {}$ (since ${} b {}$ is positive). Therefore, ${} \gcd(a,\, b)=b {}$, so ${} b^{2}=ab {}$, and ${} a=b {}$.
4.
First, we calculate ${} \gcd(1485,\, 1745) {}$:
$$
\begin{align}
1745 & =1\cdot 1485+260 \\
1485 & =5\cdot 260 +185 \\
 260 & =1\cdot 185 +75 \\
 185 & =2\cdot 75 +35 \\
75 & =2\cdot 35+5 \\
35 & =7\cdot 5
\end{align}
$$
so ${} \gcd(1485,\, 1745)=5 {}$. Next we find ${} u,\, v {}$ such that ${} 1485u+1745v=5 {}$:
$$
\begin{align}
5 & =75-2\cdot 35 \\
 & =75-2\cdot (185-2\cdot 75) \\
 & =5\cdot 75-2\cdot 185 \\
 & =5\cdot (260-1\cdot 185)-2\cdot 185 \\
 & =5\cdot 260-7\cdot 185 \\
 & =5\cdot 260 - 7\cdot (1485-5\cdot 260) \\
 & =40\cdot 260-7\cdot 1485 \\
 & =40\cdot (1745-1\cdot 1485)-7\cdot 1485 \\
 & =40\cdot 1745-47\cdot 1485
\end{align}
$$
and so ${} u=47 {}$, and ${} v=40 {}$. Now the solutions ${} (x,\, y) {}$ are given by 
$$
\{ (141+351n,\, 120+297n)\mid n \in \mathbb{Z} \}
$$
5.
a)
We see that since ${} q_{2}\geq 1 {}$, and ${} r_{1}> r_{2} {}$, then
$$
b=q_{2} r_{1} +r_{2} \geq r_{1} + r_{2} >   2r_{2}
$$
and so ${} r_{2} < \frac{b}{2} {}$
b)
We proceed by strong induction. First, note that ${} \lambda(a,\, 2)\leq 2\ceil*{\log_{2}(2)}=2  {}$, as either ${} 2 \mid a {}$ and ${} r_{1}=0 {}$, or ${} r_{1}=1 {}$, so ${} r_{2}=0 {}$. Now suppose that ${} \lambda(a,\, b)\leq 2 \ceil*{\log_{2}(b)}  {}$ for all ${} b\leq n {}$. 

Then, we take the fact that ${} \gcd(a,\, b)=\gcd(r_{1},\, r_{2}) {}$. Therefore, ${} \lambda(a,\, n+1)=2+\lambda(r_{1},\, r_{2}) {}$. Since ${} r_{2} < (n+1) /2 {}$, then ${} \lambda(r_{1},\, r_{2})\leq 2\ceil*{\log _{2}\left( \frac{n+1}{2} \right)} =2\ceil*{\log _{2}(n+1)}-2  {}$. Therefore, ${} \lambda(a,\, n+1)\leq 2 \ceil*{\log_{2}(n+1)}  {}$, and by induction the hypothesis holds.
6.
a)
First note that ${} f_{n+2}<2f_{n+1} {}$, so ${} q_{1}=1 {}$. Therefore, ${} r_{1}=f_{n} {}$, and by induction, ${} \lambda (f_{n+2},\, f_{n+1})=n {}$
b)
Suppose that ${} \lambda(a,\, b)=n {}$, and that ${} \lambda(c,\, d)=n\Rightarrow c\geq a {}$. First, note that ${} \gcd(a,\, b)=1 {}$, as otherwise, we have ${} 1\neq d=\gcd(a,\, b) {}$ and so ${} \lambda(a /d,\, b /d)=n {}$, but ${} a /d <a {}$. Therefore, ${} \gcd(a,\, b)=1 {}$, and so ${} r_{n-1}=1 {}$. In order to minimise $a {}$, then we shall pick the smallest possible numbers at each step. Therefore, we shall pick ${} q_{1}=\dots=q_{n}=1 {}$, and pick ${} r_{n-2}=1 {}$. Now we get that ${} r_{n-k}=r_{n-k+1}+r_{n-k+2} {}$, and so clearly ${} a,\, b {}$ are consecutive Fibonacci numbers.