---
tags:
  - homework
  - linear_algebra1
date: 2023-10-09
pset: 2
---
[[Directory]], [[Linear Algebra and Geometry 1|Subject Directory]]
1. a) 
i) $e^{3\pi i}=e^{i\pi}=-1$. $\Arg(e^{3i\pi})=\pi$. $|e^{3i\pi }|=1$
ii)$\Arg=\pi/4$, $|\cdot|=2$
iii) $\Arg=\pi/2$, $|\cdot|=e^{2}$
1. b) ]
i) $15i=15e^{i\pi/2}$
ii) $1-i=\sqrt{2}e^{-i\pi/4}$
iii) $-1-i\sqrt{3}=2e^{2\pi i/3}$
2. a) The sixth roots of unity are
$$
1,\,  \frac{1}{2}+\frac{\sqrt{3}}{2}i,\,  -\frac{1}{2}+\frac{\sqrt{3}}{2}i,\,  -1,\, -\frac{1}{2}-\frac{\sqrt{3}}{2}i,\, \frac{1}{2}-\frac{\sqrt{3}}{2}i
$$
b) Note that $|z|=z\conj{z}$, and $2\mathrm{Re}(z)=z+\conj{z}$. So we have $-z-\conj{z}=1=z\conj{z}$
$$
\begin{align}
z & =-\frac{z}{\conj{z}}-1 \\
 -z& =z^{2}+1 \\
z^{2}+z+1 & =0 \\
z & =\frac{-1\pm \sqrt{1-4}}{2} \\
 & =-\frac{1}{2}\pm i\frac{ \sqrt{3} }{ 2 } \\ \\
\text{note that } |z|=1, \text{ and } \Arg(z) & = \pm \frac{2\pi}{3} \\
 z &= e^{\pm 2\pi/3} \\
z^{3} & =e^{\pm 2\pi} \\
 & =1
\end{align}
$$

3. a)
$$
\begin{align}
 z & =\frac{4\pm \sqrt{16-4\cdot 2\cdot 12}}{4}   \\
 & =1\pm \sqrt{1-3} \\
 & =1\pm i\sqrt{2}
 \end{align}
$$
So we have
![[Pasted image 20231010124544.png|450]]
b)
$$
\begin{align}
(z-i)^{6} & =64 \\
z-i & =2\omega \\
z & =2\omega+i
\end{align}
$$
Where $\omega$ is a $6^{th}$ root of unity. So now we have $z=2e^{2\pi k/6}+i$. When plotted, it looks like this:
![[Pasted image 20231010125545.png|450]]
c) If we let $z=a+bi$, $a,\,\,b \in \mathbb{R}$, then we have


$$
\begin{align}
\frac{ a+bi }{ a-bi } & =i \\
a+bi & =i(a-bi) \\
 & =b+ai
\end{align}
$$
Therefore, $a=b$. So we have
$$
\begin{align}
 \frac{ a+ai }{ a-ai } & =\frac{1+i}{1-i}   \\
 & =\frac{ 1+2i-1 }{ 2 } \\
 & =i
 \end{align}
$$
Therefore, this works for all $a \in \mathbb{R}$, unless $a=0$. The plot of this is
![[Pasted image 20231011194020.png|450]]
4. a)
$$
\begin{align}
e^{iz} & =e^{i(\pi/6-i\log 2)} \\
 & =e^{\log2}e^{i\pi/6} \\
 & =2\left( \frac{\sqrt{3}}{2}+i\cdot \frac{1}{2} \right) \\
 & =\sqrt{3}+i
\end{align}
$$
b) i)
$$
\begin{align}
(e^{a+bi})^{2} & =e^{2a}e^{2bi} \\
 & =e^{2a}(\cos(2b)+i\sin(2b))
\end{align}
$$
Therefore, $\mathrm{Re}((e^{a+bi})^{2})=e^{2a}\cos(2b)$ and $\mathrm{Im}((e^{a+bi})^{2})=e^{2a}\sin(2b)$
ii)
$$
\begin{align}
\frac{e^{a}e^{bi}}{a+bi} & =\frac{ e^{a}e^{bi}(a-bi) }{ a^{2}+b^{2} } \\
 & =\frac{e^{a}}{a^{2}+b^{2}} (\cos b+i\sin b)(a-bi) \\
 & =\frac{e^{a}}{a^{2}+b^{2}}(a\cos b+ib\cos b+ia\sin b+b\sin b) \\
 & = \frac{e^{a}}{a^{2}+b^{2}} (a\cos b+b\sin b)+i\frac{e^{a}}{a^{2}+b^{2}}(b\cos b+a\sin b)
\end{align}
$$

iii)
$$
\begin{align}
 e^{e^{ia}}  & =e^{\cos a+i\sin a} \\
 & =e^{\cos a}(\cos(\sin a)+i\sin(\sin a)) \\
 & =e^{\cos a}\cos(\sin a)+e^{\cos a} \sin(\sin a)
 \end{align}
$$
5. 
$$
\begin{align}
 \cos(3\theta)+i\sin(3\theta)  & =(\cos(\theta)+i\sin(\theta))^{3} \\
 & =\cos ^{3}(\theta)+3i\cos ^{2}(\theta)\sin(\theta)-3\cos(\theta)\sin ^{2}(\theta)-i\sin ^{3}(\theta) \\ 
 \end{align}
 
$$
Therefore, we have 
$$
\begin{align}
 \cos(3\theta)  & =\cos ^{3}(\theta)-3\cos(\theta)\sin ^{2}(\theta) \\
 & =\cos ^{3}(\theta) -3\cos(\theta)(1-\cos ^{2}(\theta)) \\
 & =4\cos ^{3}(\theta)-3\cos(\theta)
 \end{align}
$$
and
$$
\begin{align}
\sin(3\theta) & =3\cos ^{2}(\theta)\sin(\theta)-\sin ^{3}(\theta) \\
 & =3(1-\sin ^{2}(\theta))\sin(\theta)-\sin ^{3}(\theta) \\
 & =3\sin(\theta)-4\sin ^{3}(\theta)
\end{align}
$$
As required

6. These are the generators of $C_{n}$ lol
a)
n=4: $e^{i\pi/2},\,e^{3i\pi/2}$
n=5: $e^{i\pi/5},\,e^{2i\pi/5},\,e^{3i\pi/5},\,e^{4i\pi/5}$
n=6: $e^{i\pi/6},\,e^{5i\pi/6}$

b) If $\gcd(k, n)=1$, then the smallest $m$ such that $\omega^{m}=1$ is $n$. Therefore, $\langle \omega \rangle\cong C_{n}$, which has $n$ elements. Since $\omega$ is a root of unity, and any power of a root of unity is a root of unity, then all the powers less that $n$ of $\omega$ must be distinct. Therefore, $\omega$ is a primitive root of unity

c) Using $b)$, then if every $n^{\text{th}}$ root of unity except 1 is primitive, then $\gcd(n,\,k)=1$ for all $k=1,\,2,\,\dots,\,n-1$. Therefore, no number divides $n$, so therefore $n$ is prime.



