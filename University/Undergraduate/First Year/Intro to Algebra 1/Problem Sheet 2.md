---
tags:
  - homework
  - intro_algebra1
date: 2023-10-13
pset: 2
---
[[Directory]], [[Intro to Algebra 1|Subject Directory]]
1. Let $a,\, b,\,c\in\mathbb{Z}$, and let $a\mid b$ and $b\mid c$. Therefore, there exist $x,\,y\in\mathbb{Z}$ such that 
$$
\begin{align}
b & =xa \tag{1}\\
c & =yb \tag{2}
\end{align}
$$
Now if we plug $(1)$ into $(2)$, then we have
$$
c=yxa
$$
and $yx \in\mathbb{Z}$, therefore we have that $a\mid c\qquad \square$

2. Let $a,\,b \in \mathbb{Z}$ with $a\neq 0$ or $b\neq 0$. Let $n \in\mathbb{Z}$. Since $a$ and $b$ are relatively prime, then there must exist some $\hat{x},\,\hat{y}\in\mathbb{Z}$ such that $a\hat{x}+b\hat{y}=\gcd(a,\,b)=1$. Therefore, we have $n(a\hat{x}+b\hat{y})=n$. Distributing, we get $a(n\hat{x})+b(n\hat{y})=n$. Therefore, $f((n\hat{x},\,n\hat{y}))=n$. Since $n \in \mathbb{Z}$, then we have that for all $n \in\mathbb{Z}$, there exists an element $(x,\,y)=(n\hat{x},\,n\hat{y})$ such that $f((x,\,y))=n$. Therefore, $f$ is surjective. 

	Now suppose that $f$ is surjective. So we have that for all $n \in\mathbb{N}$, there exists $x,\,y \in \mathbb{Z}$ such that $ax+by=n$. Therefore, there exists $\hat{x},\,\hat{y} \in \mathbb{Z}$ such that $a\hat{x}+b\hat{y}=1$. By [[4. GCD and Euclidian Algorithm#Theorem 1.1 Uniqueness of $\\gcd$|the uniqueness of gcd]], we have that therefore $\gcd(x,\,y)=1$, so therefore $x$ and $y$ are relatively prime.
	

3. Let $a,\,b \in \mathbb{Z}$, with $a\neq 0$ or $b\neq 0$. Let $d=\gcd(a,\,b)$. Therefore by definition, $d\mid a$ and $d\mid b$. Let $x=a/d$, and $y=b/d$. Now suppose that $k\mid x$ and $k\mid y$. Therefore, $kd\mid a$ and $kd\mid b$. Therefore, $kd\mid d$, by definition of $\gcd$. Therefore, $k=1$, therefore $x$ and $y$ are relatively prime.

4. Let $a,\,b,\,c \in \mathbb{Z}$, with $\gcd(a,\,b)=1$
i) Assume that $a\mid c$ and $b\mid c$. so we have 
$$
\begin{align}
c & =xa \\
c & =yb
\end{align}
$$
With $x,\,y\in\mathbb{Z}$. Now consider 
$$
\begin{align}
ax & =by \\
 y & =a\left( \frac{x}{b} \right)
\end{align}
$$
$x/b$ must be an integer because $y$ is an integer and $a/b$ cannot be an integer, as they are relatively prime. Therefore, we have
$$
c=by=ab\left( \frac{x}{b} \right)
$$
Since $x/b\in\mathbb{Z}$, then we have that $ab\mid c$, as required

ii) Consider: $c=4$, $a=2$, $b=4$. Then, $ab=8\nmid 4$. Therefore, it does not hold if $\gcd(a,\,b)\neq 1$

5. let $a,\,b,\,c,\,d\in\mathbb{Z}$, with $a\neq 0$, and $\gcd(a,\,b)=1$
i) If $d\mid a$, then we have $a=xd$ for some $x \in\mathbb{Z}$. Since $a$ and $b$ are relatively prime, then there exist 2 numbers $n,\,k \in \mathbb{Z}$ such that $an+bk=1$. Substituting, we get $d(xn)+bk=1$. Therefore, by [[4. GCD and Euclidian Algorithm#Theorem 1.1 Uniqueness of $\\gcd$|the uniqueness of gcd]], we have $\gcd(d,\,b)=1$, so therefore, $b$ and $d$ are relatively prime.

ii) Let $d=\gcd(a,\,c)$. Let $k=\gcd(a,\,bc)$. Therefore, $k\mid a$ and $k\mid bc$. Since $k\mid a$, and $\gcd(a,\,b)=1$ then $\gcd(k,\,b)=1$. Therefore, we have that $k\mid bc\Rightarrow k\mid c$, as otherwise it must share at least 1 factor with $b$. Since $k\mid a$ and $k\mid c$, then $k\mid d$. Also note that $k\geq d$, as every number that is a divisor of $c$ is a divisor of $bc$.

Now we have $k\mid d$ and $k\geq d$. Therefore, $k=d$. So we have
$$
\gcd(a,\, c)=\gcd(a,\, bc)
$$
iii) This follows directly as a corollary from above. Since $a$ and $b$ are relatively prime, then we have
$$
\gcd(a,\, b)=\gcd(a,\, b\cdot b)=\gcd(a,\, b^{2})=1
$$
Since $a$ and $b^{2}$ are relatively prime, then we have
$$
\gcd(a,\, b^{2})=\gcd(a^{2},\, b^{2})=1
$$
as required

6. First, we form a useful lemma:
### Lemma 1.1: Addition in $\gcd$
Suppose $\gcd(a,\,b)=1$. In the first line of the Euclidian algorithm, we have
$$
a=q_{0}b+r_{0}\qquad q_{0},\, r_{0}\in \mathbb{Z},\,  b>r_{0}\geq 0
$$
This then continues on to calculate $\gcd(a,\,b)$. If we now consider the first line of the Euclidian algorithm of $\gcd(a+b,\,b)$, then we have
$$
a+b=p_{0}b+s_{0}\qquad p_{0},\, r_{0}\in \mathbb{Z},\, b>s_{0}\geq 0
$$
Note that we can rearrange this to
$$
a=(p_{0}-1)b+s_{0}
$$
Since the division algorithm is unique, then we must have $q_{0}=p_{0}-1$ and $r_{0}=s_{0}$. From here since only the quotient is changed, then the Euclidian algorithm continues unaffected, and gives the same result at the end. By symmetry, this also works with $\gcd(a+b,\,a)$. Therefore,
$$
\gcd(a+b,\, b)=\gcd(a+b,\, a)=\gcd(a,\, b)=1
$$
Now to prove 6.:
We work by induction. First, we see that $F_{1}=1$, and $F_{2}=2$. 
$$
\gcd(F_{1},\, F_{2})=\gcd(1,\, 2)=1
$$
Therefore, the statement holds for $n=1$.
Now, we create an induction hypothesis: 
Suppose $\gcd(F_{n},\,F_{n-1})=1$. Now we have
$$
\gcd(F_{n+1},\, F_{n})=\gcd(F_{n}+F_{n-1},\, F_{n})
$$
By the induction hypothesis, and lemma 1.1, then we have
$$
\gcd(F_{n}+F_{n-1},\, F_{n})=1
$$
Therefore, 
$$
\gcd(F_{n+1},\, F_{n})=1
$$
Thus by the induction principle, we have that 
$$
\gcd(F_{n+1},\, F_{n})=1
$$
For all $n\geq 1$

7. First we form a useful Lemma
### Lemma 1.2: Multiples of Bézout's Identity 
Let $a,\,b \in \mathbb{Z}$, with $a\neq 0$ or $b\neq 0$. Let $d=\gcd(a,\,b)$. Then, for all $x,\,y \in \mathbb{Z}$, 
$$
d\mid ax+by
$$
#### Proof:
Since $d\mid a$ and $d\mid b$, then we have
$$
\begin{align}
 ax+by & =dnx+dmy   \\
 & =d(nx+my)
 \end{align}
$$
Therefore, $$
d\mid ax+by
$$

Ever table will have a linear combination of the 2 meals; therefore, the bill must be of the form
$$
B=126a+108b
$$
For some $a,\,b \in \mathbb{N}$. Therefore, by Lemma 1.2, then we have that
$$
\gcd(126,\, 108)\mid B
$$
We note that $108=18\cdot 6$ and $126=18\cdot 7$. Since $6$ and $7$ are relatively prime, then by 3), $\gcd(108,\,126)=18$.
Therefore, $18\mid B$ as required


