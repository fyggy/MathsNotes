---
tags:
  - homework
  - calculus1
date: 2023-10-03
completed: true
---
[[Directory]], [[Calculus 1|Subject Directory]]

# Tutors example
$$
\begin{align} \\
f:A & \to{} B\\
 f(x) & =\frac{ \sin x }{ x }=\mathrm{sinc} \ x  
\end{align}
$$
We want to know what the largest domain $A$ that we can use to define $f$
Find the minimum value of $n$ such that for $B=(-\infty, n]$, $f$ is well defined
Finally, sketch $f$.

First, $A=\mathbb{R}\setminus \{ 0 \}$. This is the largest because it only differs by one element from $\mathbb{R}$, and $f$ is not defined for $0$.

Second, we can see that $\theta\geq \sin \theta$. However, the difference between $\theta$ and $\sin\theta$ gets smaller and smaller as $\theta$ gets smaller. So therefore we have $\displaystyle \frac{ \sin\theta }{ \theta }<1$, but as $\theta\to{} 0$, $\displaystyle \frac{ \sin\theta }{ \theta }$

So the minimum $n$ for which $(-\infty, n]$ is a valid codomain of $f$ is $1$

for a sketch:

![[export1-crop.pdf#height=300]]

1. 
	1. $f:\mathbb{R}\setminus\{ 2 \}\to{}[0, \infty)$
	2. $g:\mathbb{R}\setminus\{ 0 \}\to{} \mathbb{R}\setminus\{  0\}$
	3. $h:\mathbb{R}\to{} \left\{  0, \frac{1}{2}, 1  \right\}$
2. 
	1. a)
![[Pasted image 20231003135506.png]]
2. 
	2.  b)
![[Pasted image 20231005133509.png]]
2. 
	3. c)
![[Pasted image 20231005134221.png]] 
3. a
	1. a) is not well defined
	2. b) is not well defined, unless the domain does not include $-5$, in which case it is. The function would then be bijective, as it seems to be positive and monotonically decreasing for $x>-5$ and negative and monotonically increasing for $x<-5$. The function appears to be rational.
	3. c)The function is well defined, and is not a bijection. It appears to be a trigonometric function
	4. d) The function is well defined, is not bijective and appears be be an absolute value function
	5. e) The function is well defined, is not bijective, and appears to be a polynomial
	6. f) the function is well defined, is bijective, and appears to be trigonometric plus a polynomial
4. 
	1. a)This function is bijective, and well defined
![[Pasted image 20231009175457.png]]
b) This function is bijective and is well defined
![[Pasted image 20231009175613.png]]
c) This function is neither well defined, or injective, but it is surjective if we pretend that it is well defined
![[Pasted image 20231009175729.png]]
d) This function is not injective, but it is surjective and well defined
![[Pasted image 20231009175746.png]]
e) This function is neither injective or surjective, but it is well defined
![[Pasted image 20231009180020.png]]
f) This function is neither injective or surjective, but it is well defined
![[Pasted image 20231009180059.png]]
g) This function is injective, surjective, and is well defined
![[Pasted image 20231009180501.png]]
h) This function is injective, surjective, and is well defined
![[Pasted image 20231009180807.png]]
5. -
a)
![[Pasted image 20231009181406.png|300]]
![[Pasted image 20231009181432.png|300]]
![[Pasted image 20231009181450.png|300]]
![[Pasted image 20231009181507.png|300]]
Since $p$ has only 1 real root, then configuration #3 is impossible. Since $p$ can only cross the $x$-axis once, after $x_{0}$, it cannot become negative again. Since the coefficient of the $x^{3}$ term is positive, $p$ is eventually negative as $x\to{}-\infty$, and eventually positive as $x\to{} \infty$. Therefore, it must cross the $x$-axis from the negative to the positive side. Therefore, the maximum domain of $\eta$ is $[x_{0}, \infty)$. This is also clear from the graph

b) Its minimum range is $\mathbb{R}$
![[Pasted image 20231009182731.png]]
c) $\eta(x)=\pm\sqrt{p(x)}$, so injective iff $p(x)$ is injective in the domain. Let $D=[x_{0}, \infty)$ as defined above. Take $x, y \in D$ and suppose $b>0$. If $p(x)=p(y)$, then we have 
$$
\begin{align}
x^{3}+ax+b & =y^{3}+ax+b
\end{align}
$$

