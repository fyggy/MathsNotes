---
tags:
  - homework
  - intro_algebra1
pset: 1
date: 2023-09-26
---
[[Directory]], [[Intro to Algebra 1|Subject Directory]] 
1. 
	1. $A \cap C$ is all elements of $C$ which are an integer multiple of 3. therefore, $A \cap C=\{ -3,\,9 \}$. The exact elements of $B$ are $$B=\{ -6,\, -5,\,-4,\,-3,\,-2,\,-1,\,0,\,1,\,2,\,3,\,4,\,5,\,6 \}$$
	   $-3$ is contained within this, but $9$ is not, so $$
	   B\cup(A\cap C) = \{ -6,\, -5,\,-4,\,-3,\,-2,\,-1,\,0,\,1,\,2,\,3,\,4,\,5,\,6,\, 9\}
	   $$
	2. Since this set will be intersected with $C$, which has a finite number of elements, we instead want to look at elements from $A$ or $B$ which are also in $C$. So $A \cap C=\{ -3,\, 9 \}$, as established above, and $B \cap C=\{ -3,\,2,\,4 \}$ by inspection. Now we take the union of these sets, so $$
	   \begin{align}
 (B\cup A) \cap C&=\{ -3,\, 9,\,-3,\,2,\,4 \} \\
 & =\{ -3,\,2,\,4,\,9 \}  
 \end{align}
	   $$
	3. $B\setminus A$ is the set of all numbers in $B$ that are **not** a multiple of 3. Therefore, by inspection, $B\setminus A=\{-5,\,-4,\,-2,\,-1,\,1,\,2,\,4,\,5\}$. Intersecting that with $C$ yields $$
\begin{align}
(B\setminus A)\cap C=\{ 2,\, 4 \}
\end{align}
$$
2. $A \cap B=\{-6,\, -3,\, 0,\, 3,\, 6\}$ using similar logic used above, and $A\cap C=\{ -3,\, 9 \}$, as established above. Therefore, $$
\begin{align}
(A \cap B) \times (A \cap C)=\{ &(-6,\,  -3),\, (-3,\, -3),\, (0,\, -3),\, (3,\, -3),\, (6,\, -3),\,  \\
&(-6,\,9),\, (-3,\, 9),\, (0,\, 9),\, (3,\, 9),\, (6,\, 9) \}
\end{align}
$$
3. For some propositions $p_{1},\, p_{2},\, p_{3}$ take the 2 statements $s_{1}=(p_{1} \vee p_{2}) \wedge p_{3}$, and $s_{2}=(p_{1}\wedge p_{3})\vee (p_{2} \wedge p_{3})$. They have the truth tables

| $p_{1}$ | $p_{2}$ | $p_{3}$ | $s_{1}$ | $s_{2}$ |
| ------- | ------- | ------- | ------- | ------- |
| 0       | 0       | 0       | 0       | 0       |
| 0       | 0       | 1       | 0       | 0       |
| 0       | 1       | 0       | 0       | 0       |
| 0       | 1       | 1       | 1       | 1       |
| 1       | 0       | 0       | 0       | 0       |
| 1       | 0       | 1       | 1       | 1       |
| 1       | 1       | 0       | 0       | 0       |
| 1       | 1       | 1       | 1       | 1       |

   This shows that $s_{1}\leftrightarrow s_{2}$.
   Now observe that
   $$
   \begin{align}
 (A\cup B)\cap C&=\{ a \mid a \in A \vee a \in B \} \cap C   \\
 & =\{ a\mid (a \in A \vee a \in B) \wedge a \in C \} \\
 & =\{a \mid (a \in A \wedge a \in C) \vee (a \in B \wedge a \in C)\} \qquad \text{as per above} \\
 & =\{ a\mid a \in A \wedge a \in C \} \cup \{ a \mid a \in B \wedge a \in C \} \\
 & = (A \cap C) \cup (B \cap C)
 \end{align}
   $$
4. Observe that
$$
\begin{align}
 (A_{1} \times Y) \cap(A_{2} \times Y)&=\{(a_{1},\,  y)\mid a_{1} \in A_{1},\,  y \in Y  \} \cap \{ (a_{2},\, y) \mid a_{2} \in A_{2},\,  y \in Y\}   \\
 & = \{ (a,\,  y) \mid (a \in A_{1},\,  y \in Y) \wedge (a \in A_{2},\,  y \in Y) \}
 \end{align}
$$

Since the above condition requires that $y \in Y$ both times, then necessarily it is true iff $a \in A_{1} \wedge a \in A_{2},\, y \in Y$. Therefore, we have
$$
\begin{align}
(A_{1} \times Y) \cap(A_{2} \times Y)&=\{ (a,\,  y) \mid a \in A_{1} \wedge a \in A_{2} ,\,  y \in Y\} \\
 & =\{ (a,\,  y) \mid a \in (A_{1} \cap A_{2}),\,  y \in Y \} \\
 & =(A_{1} \cap A_{2}) \times Y
\end{align}
$$
5. For any number $k \in \mathbb{Z}$, take $z=k-1$. Therefore, $z \in \mathbb{Z}$ as well. We also have $1 \in \mathbb{N}$ Now we have $$
f((1,\,  z))=1+z=1+k-1=k
			$$  Therefore, for any $k$ in the codomain of $f$, we can find an element of the domain, $n=(1,\, z)$, such that $f(n)=k$. Therefore, $f$ is surjective.

6. Given 2 numbers $x,\, y \in \mathbb{R}$, if $f(x)=f(y)$, then we have
	1. $x^{2}=y^{2}$
	2. $g(x)=g(y)$
(1) is true iff $x =y$ or $x=-y$, and (2) is true iff both $x$ and $y$ are greater than $0$, or both are less than or equal to 0. That is, they are the same sign. 
Therefore, $x\neq-y$ unless $x=y=0$. 
Therefore, $x=y$, or $x=y=0$, or simply, $x=y$. Therefore $f$ is injective.

7. Given an element $c \in C$, since $g$ is surjective, then there exists an element $b\in B$ such that $g(b)=c$. 
   Since $f$ is surjective, then there exists an element $a \in A$ such that $f(a)=b$. 
   Therefore, $g(f(a))=(g\circ f)(a)=c$. 
   Therefore, there exists an element in $A$ such that $(g\circ f)(a)=c$. Therefore, $g \circ f$ is surjective too.

8. Base case: for $n=1$, we have 
$$
\begin{align}
 \sum_{k=1}^{1} (2k-1)^{2}=1  \\
		\frac{1}{3}(4\cdot1^{3}-1)=\frac{1}{3} (3)=1 \\
1=1 
 \end{align} 
$$
Therefore, the statement holds for the base case.
Suppose the statement holds for $n=k$
now we have 
$$
\begin{align}
 \sum_{i=1}^{k+1} (2i-1)^{2}&= (2k+1)^{2} +\sum_{i=1}^{k} (2i-1)^{2}\\
 & =  (2k+1)^{2}+\frac{1}{3}(4k^{3}-k) \\
 & = \frac{1}{3}(12k^{2}+12k+3 +4k^{3}-k) \\
 & =\frac{1}{3}(4(k^{3}+3k^{2}+3k+1)-k-1) \\
 & =\frac{1}{3}(4(k+1)^{3}-(k+1))
 \end{align}
$$
Therefore, if the statement holds for $n=k$, then it will hold for $n=k+1$. Since the base case holds, then necessarily it must hold for all $n \in \mathbb{N}$.

9. 
	1. Consider
	$$

f(x)=
\begin{cases}
x+1,\,  & x>0 \\
x,\,  & x\leq 0
\end{cases}
$$
	$f$ is injective because, given $f(x)=f(y),\, x,\, y \in \mathbb{Z}$, then either:
	- $x>0$, meaning $f(x)>1$, meaning $f(y)>1$, meaning $y>0$, as if it were not, then $y$ can be at most $0$, and then $f(y)$ can be at most $0$. Therefore, $f(x)=x+1,\, f(y)=y+1$, so we have $x+1=y+1,\quad x=y$. Therefore $f$ is injective for this case
	- $x\leq 0$, meaning $f(x)\leq 0$, meaning $f(y)\leq 0$, meaning $y\leq 0$, as $f(k)\geq k$ for all $k \in \mathbb{Z}$. Therefore, $f(x)=x$, and $f(y)=y$, therefore $x=y$. Therefore $f$ is injective for this case 
	Therefore $f$ is injective
	
	$f$ is not surjective, as there is no way to obtain $1$. Observe that $f$ is increasing, that is, $x>y \implies f(x)>f(y)$. Now observe that $f(0)=0$, and $f(1)=2$. Therefore, $1$ is "skipped"
	2. consider 
	$$
	f(x)=
	\begin{cases}
x,\,  & x\geq 0 \\
x+1,\,  & x<0
\end{cases}
$$
	$f$ is surjective because, given a number $y \in \mathbb{Z}$, 2 cases:
	- if $y\geq 0$, then $f(y)=y$, so $f$ is surjective for this case
	- if $y<0$, then $f(y-1)=y$, so $f$ is surjective for this case
	Therefore, $f$ is surjective.
	$f$ is not injective, as $f(-1)=f(0)=0$, with $-1\neq 0$

10. 
	1. This statement is true. Observe that
	   $$
\begin{align}
(A_{1} \times B_{1})\cap (A_{2} \times B_{2})&=\{ (a,\,  b) \mid a \in A_{1},\, b \in b_{1} \} \cap \{ (a,\,  b) \mid a \in A_{2},\, b \in b_{2} \} \\
 & =\{ (a,\,  b)\mid (a \in A_{1},\,  b \in B_{1}) \wedge (a \in A_{2},\,  b \in B_{2}) \}
\end{align}
$$
	Note that like before, the statements are entirely disjoint, so we can split the specifier like this:
	$$
\begin{align}
(A_{1} \times B_{1})\cap (A_{2} \times B_{2})&=\{ (a,\,  b)\mid a \in A_{1} \wedge a \in A_{2},\,  b\in B_{1} \wedge b \in B_{2} \} \\
 & =\{ (a,\,  b)\mid a\in A_{1} \cap A_{2} ,\,  b \in B_{1} \cap B_{2}\} \\
 & =(A_{1} \cap A_{2}) \times (B_{1} \cap B_{2}) 
\end{align}
$$
	As required
	2. This statement is False. Consider the following counter example:
	$$
\begin{align}
 \text{Let } A_{1}=\{ 1 \},\,  A_{2}&=\{ 2 \},\,  B_{1}=\{ -1 \},\,  B_{2}=\{ -2 \}  \\
(A_{1} \cup A_{2}) \times (B_{1} \cup B_{2}) &= \{ (1,\,  -1),\,  (1,\,  -2),\,  (2,\,  -1),\,  (2,\,  -2) \} \\
(A_{1}\times B_{1}) \cup (A_{2} \times B_{2})&=\{ (-1,\,  1) \} \cup \{{(-2,\,  2)}\} \\
&=\{ (-1,\,  1),\,  (-2,\,  2) \}
 \end{align}
$$
	These are not equal, therefore the statement is false

11. 
	1. For a given subset of $X$, you make a choice for each element; weather to include it or not. This means that there are $n$ binary choices to be made, each of which create a unique subset. The subsets are unique because if 2 different sets of choices could be made, then the subsets would contain different elements. Therefore, there are $2^{n}$ subsets
	2. Since each element must either be sent to $0$ or $1$, to construct a function we must make $n$ binary choices again. likewise from above, these functions are unique because if they weren't, and 2 different choices could be made leading to the same function, then these functions necessarily must differ at at least 1 value. This means that there are $2^{n}$ possible functions
	3. Every subset of $X$ is uniquely specified by a function in the following way: given a function $f:X\to{} \{0,\, 1  \}$, define $X_{f}=\{ x \in X\mid f(x)=1 \} \subseteq X$. If given another function $g:X\to{} \{ 0,\, 1 \}$, with $f\neq g$, then $f$ and $g$ must differ on at least 1 element of $X$, meaning that their respective subsets must differ on at least 1 element. Therefore, by definition of set (in)equality, $X_{g}\neq X_{f}$. 
	
12. If $f:A\to{} B$ is injective, then it must pick $n$ elements from $B$. If $n>m$, then there can be no injective functions, so the number is 0. Otherwise, fix a permutation of $A$ .We want to choose a subset of size $n$, call it $B'$  of $B$. For each $B'$,  take the set of its permutations. For each permutation there is a unique function that maps the first element of the permutation of $A$ to the first element of that permutation of $B'$, and so on. Therefore, for each subset $B'$, there are $n!$ such functions. The number of subsets is given by the choose function, $m \text{ choose } n$ Therefore, the formula is 
$$
n! \cdot \frac{m!}{n!(m-n!)}=\frac{m!}{(m-n)!}
$$
