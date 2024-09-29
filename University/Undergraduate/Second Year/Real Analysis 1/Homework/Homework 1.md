---
tags:
  - homework
  - real_anal1
date: 2024-09-23
pset: 1
completed: false
---
[[Directory]], [[University/Undergraduate/Second Year/Real Analysis 1/Real Analysis 1|Subject Directory]]
[[University/Undergraduate/Second Year/Real Analysis 1/Homework/Homework 1|🞀🞀]] [[|◀]] [[University/Undergraduate/Second Year/Real Analysis 1/Homework/Homework 2|▶]] [[University/Undergraduate/Second Year/Real Analysis 1/Homework/Homework 11|🞂🞂]]

[[University/Undergraduate/Second Year/Real Analysis 1/Homework/Worksheets/real_anal_1.pdf|Worksheet]]
1. 
Let ${} p \in (a,\, b) {}$. Then let ${} d=\max(|p-a|,\, |p-b|) {}$. Now let ${} S=\left( p-\frac{d}{2} ,\, p+\frac{d}{2}\right) {}$. Note that ${} p-\frac{d}{2}>a {}$, and that ${} p+\frac{d}{2} <b {}$, so ${} S \subseteq (a,\, b) {}$.
2. 
a)
We have that ${} 3x-x^{3} \geq 0 {}$, so ${} 3x\geq x^{3} {}$. Now, if ${} x<0 {}$, then ${} 3\leq x^{2} {}$, or that ${} x\geq \sqrt{3} {}$ or ${} x\leq -\sqrt{3} {}$. Since ${} x<0 {}$, then we may simply write ${} x\leq  -\sqrt{3} {}$. 

Otherwise, if ${} x\geq 0 {}$, then ${} 3\geq x^{2} {}$, and so ${} x\leq \sqrt{3} {}$ or ${} x\geq -\sqrt{3} {}$. Since ${} x\geq 0 {}$, then we may simply write ${} x\leq \sqrt{3} {}$. Therefore, ${} x\leq \sqrt{3} {}$.

In total, the natural domain consists of 
$$
D=(-\infty,\, -\sqrt{3}] \cup [0,\, \sqrt{3}]
$$
b)
First, note that ${} x\neq 1 {}$. Then, we have that ${} \frac{ 1+x }{ 1-x }\geq 0 {}$. Then ${} 1+x\geq 0 {}$, or ${} x\geq -1 {}$. Now the natural domain consists of
$$
D=[-1,\, \infty ) \setminus \{ 1 \}
$$
c)
We have that ${} \cos x\geq 0 {}$. Therefore, if ${} x \in [0,\, 2\pi] {}$, then ${} 0\leq x\leq \frac{\pi}{2} {}$ or ${} \frac{3\pi}{4}\leq x\leq 2\pi {}$. Therefore, the natural domain is
$$
D=\bigcup_{n\in \mathbb{Z}} \left[ 2\pi n,\, 2\pi n+\frac{\pi}{2} \right] \cup \left[ 2\pi n+\frac{3\pi}{4},\, 2\pi n+2\pi \right]
$$
d)
First, note that ${} x\geq 0 {}$. Now, if ${} \sin \pi x=0 {}$, then ${} f(x) {}$ is not defined. Therefore, if ${} x=n \in \mathbb{Z} {}$, then ${} f(x) {}$ is not defined. Therefore, the natural domain is
$$
D=[0,\, \infty) \setminus \mathbb{Z}
$$
3. 
a)
We have 
$$
f(x)=\frac{x}{1+x}=\frac{x+1-1}{1+x} =1-\frac{1}{1+x}
$$
So $f {}$ is bounded on the interval:
![[Pasted image 20240927231954.png]]
b)
We have that ${} f(x)=(\sqrt{x})^{-1} {}$, and since as ${} x\to{}0 {}$, ${} \sqrt{x}\to{}0 {}$, then ${} f(x)\to{}\infty {}$. Therefore, $f {}$ isn't bounded:
![[Pasted image 20240927232328.png]]
c)
This is clearly bounded, as for any finite interval, all of the constituent functions are bounded
![[Pasted image 20240927234913.png]]
d)
Since ${} \sqrt{1+x^{2}}>x {}$, then as ${} x\to{}\infty {}$, then ${} \sqrt{1+x^{2}}\to{}\infty {}$, therefore, $f {}$ is unbounded:
![[Pasted image 20240927235200.png]]
e)
Since ${} \sin x=1 {}$ when ${} x=\frac{\pi}{2}+2\pi n {}$ for all ${} n \in \mathbb{Z} {}$, then $f {}$ is unbounded, as given a upper bound $M {}$, ${} f(2\pi M+\pi /2)=2\pi M+ \pi /2 >M {}$:
![[Pasted image 20240928000219.png]]
f)
Note that ${} f(x)=g\left( \frac{1}{x} \right) {}$, where ${} g=x\sin x {}$ from ${} 3. {}$e. Therefore, $f {}$ is unbounded:
![[Pasted image 20240928001421.png]]
4. 
a)
We say that
$$
\lim_{x\tto x_{0}} f(x)=\infty
$$
iff for all ${} M \in \mathbb{R} {}$ there exists some ${} \delta>0 {}$ such that for all ${} x \in \mathbb{R} {}$ such that ${} 0<|x_{0}-x|< \delta {}$, we have ${} f(x)>M {}$.

For example, ${} \lim_{x\tto 1} \frac{1}{1-2x+x^{2}}=\infty {}$, as for all ${} M>0 {}$, if we pick ${} \delta=\frac{1}{\sqrt{M}} {}$, then if ${} x \in \mathbb{R} {}$ such that ${} 0<|x-1|< \delta {}$, then 
$$
\begin{align}
 f(x) & =\frac{1}{(x-1)^{2}}   \\
  & >\frac{1}{\left( \frac{1}{\sqrt{M}} \right)^{2}} \\
 & >\frac{1}{\frac{1}{M}} \\
 & >M
 \end{align}
$$
b)
We say that
$$
\lim_{x\tto x_{0}} f(x)=-\infty
$$
iff for all ${} M \in \mathbb{R} {}$, there exists some ${} \delta>0 {}$ such that for all ${} x \in \mathbb{R} {}$ with ${} 0 < |x_{0}-x|< \delta {}$, then we have ${} f(x) <M {}$. 

For example, ${} \lim_{x\tto 0} -\cot^{2}(x)=-\infty {}$ since for all ${} M \in \mathbb{R} {}$, if we assume that ${} M<0 {}$, then we may pick ${} \delta=\arccot(\sqrt{-M}) {}$, and so for all ${} x \in \mathbb{R} {}$ with ${} 0<|x|< \delta {}$, we have
$$
\begin{align}
f(x) & =-\cot^{2}(x) \\
 & =-\cot ^{2}(|x|) \qquad \text{ by symmetry} \\
 & <-\cot ^{2}(\arccot(\sqrt{-M})) \\
 & <M
\end{align}
$$
c)
We say that
$$
\lim_{x\tto \infty} f(x)=-\infty
$$
iff for all ${} M \in \mathbb{R} {}$, there exists some ${} R \in \mathbb{R} {}$ such that for all ${} x\geq R {}$, ${} f(x)<M {}$.

For example, ${} \lim_{x\tto \infty} \ln (x^{-x})=-\infty {}$, since for all ${} M \in \mathbb{R} {}$, we may assume that ${} M<-e {}$, and so if we set ${} R=-M {}$, then for all ${} x \in \mathbb{R} {}$ such that ${} x\geq R {}$
$$
\begin{align}
f(x) & =\ln (x^{-x}) \\
	 & =-x \ln x \\
	  & < -x\qquad \text{ if } x>e \\
 & <M
\end{align}
$$
5. 
a) i)
We have that ${} \frac{ 2x-x^{2} }{ x }=2-x {}$ is bounded around $0 {}$, clearly.
ii)
We have that ${} 2-x\to{}-\infty {}$ as ${} x\to{} \infty {}$, as if ${} M \in \mathbb{R} {}$, then if ${} R = -M+3 {}$, then for all ${} x\geq R {}$, we have
$$
2-x \leq 2-(-M+2)=M-1 <M
$$
and so