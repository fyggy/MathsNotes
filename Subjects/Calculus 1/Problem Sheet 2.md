---
tags:
  - homework
  - calculus1
date: 2023-10-10
pset: 2
---
[[Directory]], [[Calculus 1|Subject Directory]]
# Tutors Example
if $f:A\to{} B$ is not injective, is it not invertible
Maybe $\exists A'\subseteq A$ such that $f:A'\to{} B$ *is* injective. 
Define $B':=$ image of $f$ as a function of $A'$
So $B'=\{ f(x)\mid x \in A' \}$, $f:A'\to{} B'$ is surjective and injective, so it is invertible.


Let $f:\mathbb{R}\to{} \mathbb{R}$, $f(x)=(x+1)(x-2)(x+3)$. $f$ is clearly not injective, as $f(-1)=f(-3)=0$, 

![[Pasted image 20231010131712.png|450]]
In general, a good rule is to split at turning points and vertical asymptotes. This is because at these points, the function changes from monotonically increasing to decreasing, or vice versa.
We split this function into 3 parts:
![[Pasted image 20231010132045.png|450]]

We find the turning points.
$$
\begin{align}
f(x) & =(x^{2}-x-2)(x+3) \\
 & =x^{3}+3x^{2}-x^{2}-3x-2x-6 \\
 &=x^{3}+2x^{2}-5x-6 \\
 \\
\frac{df}{dx}  & =3x^{2}+4x-5
\end{align}
$$
To find the turning points, We set $\frac{df}{dx}=0$
$$
\begin{align}
3x^{2}+4x-5 & =0 \\
x & =\frac{-4\pm \sqrt{16+60}}{6} \\
 & =-\frac{2}{3}\pm \frac{\sqrt{19}}{3}
\end{align}
$$
And so, if we set $x_{1}=-\frac{2}{3}+\frac{\sqrt{19}}{3}$ and $x_{2}-\frac{2}{3}-\frac{\sqrt{19}}{3}$, and 
$$
\begin{align}
A_{1} & =(-\infty, x_{1}] \\
A_{2} & =[x_{1},\, x_{2}] \\
A_{3} & =[x_{2},\, \infty)
\end{align}
$$
Now $f$ is invertible over these domains
If you can show that a function is monotonically increasing, then it must be injective within its domain. This is clear.
7. 
a) There are no asymptotes of $f(x)$. Therefore, we are searching for turning points of $f(x)$.
$$
\begin{align}
 \frac{df}{dx} =-3x^{2}+2x+9&=0  \\
 x & =\frac{-2\pm \sqrt{4+4\cdot 3\cdot 9}}{-6} \\
 & =1\mp \frac{2\sqrt{7}}{3} 
 \end{align}
$$
Let $x_{1}=1-\frac{2\sqrt{7}}{3}$, $x_{2}=1+\frac{2\sqrt{7}}{3}$, and let
$$
\begin{align}
A_{1}=(-\infty,\, x_{1}] \\
A_{2}=[x_{1},\, x_{2}] \\
A_{3}=[x_{2},\, \infty)
\end{align}
$$
So over each $A_{n}$, $f_{n}:A_{n}\to{} \mathrm{Im}(f_{n})$ is invertible.
b) First, asymptotes of $\tan(x^{2})$.
$\tan$ is an asymptote when $\theta=k\pi+\frac{\pi}{2}$, for $k\in\mathbb{Z}$. So we set $\hat{x}_{k}=\sqrt{(k-1)\pi+\frac{\pi}{2}}$. So now we check for turning points:
$$
\begin{align}
 \frac{df}{dx} =2x \sec^{2}(x^{2}) & =0 \\
 \end{align}
$$
We have $\sec^{2}(x)>0$ for all $x \in \mathbb{R}$, as $1\geq\cos ^{2} x\geq0$. Therefore, $x=0$. So there is a single turning point at $x=0$
Define 
$$
x_{k}=\begin{cases}
-\sqrt{(k+1)\pi+\frac{\pi}{2}} & k\leq 1 \\
0 & k=0 \\
\sqrt{(k-1)\pi+\frac{\pi}{2}} & k\geq 1
\end{cases}
$$
And set $A_{k}=(x_{k},\,x_{k+1})$. Then $f$ is injective over every $A_{k}$

c) $f(x)=2^{x}+2^{-x}$. There are no asymptotes of $f$, so we search for turning points.
$$
\begin{align}
\frac{df}{dx}=\ln 2 \cdot2^{x}-\ln 2 \cdot 2^{-x} & =0 \\
 2^{x} & =2^{-x} \\
x & =-x \\
x & =0
\end{align}
$$
Therefore, the only turning point is at $x=0$, and so if we let $A_{1}=(\infty, 0]$ and $A_{2}=[0, \infty)$, then $f$ is injective over each of these sets.

8. $$
\begin{align}
 4^{\frac{x}{y}+\frac{y}{x}} & =32   \\
2\left( \frac{x}{y}+\frac{y}{x} \right) & =5 \\
\frac{x}{y}+\frac{y}{x} & =\frac{5}{2}
 \end{align}
$$
Let $s=y/x$. Now we have 
$$
\begin{align}
 s+\frac{1}{s} & =\frac{5}{2}   \\
\frac{s^{2}+1}{s} & =\frac{5}{2}   \\
s^{2}-\frac{5}{2}s+1 & =0 \\
s & =\frac{ \frac{5}{2}\pm \sqrt{\frac{25}{4}-4} }{ 2 } \\
 & =\frac{5}{4}\pm \frac{ \sqrt{\frac{9}{4}} }{ 2 } \\
 & =\frac{5}{4}\pm \frac{3}{4} \\
\end{align}
$$
So $s=2$ or $s=\frac{1}{2}$. Therefore
$$
\begin{align}
y=2x \\
\text{or} \\
y=\frac{x}{2}
\end{align}
$$
Working the other equation, we have
$$
\begin{align} \\
\log_{3}(x+y)+\log_{3}(x-y) & =1 \\
\log_{3}((x-y)(x+y)) & =1 \qquad x>y,\, x>-y\\ 
\log_{3}(x^{2}-y^{2}) & =1 \\
x^{2}-y^{2} & =3
\end{align}
$$
Plugging our identities for $y$ into the above we get:
$y=2x$
$$
\begin{align}
 x^{2}-4x^{2} & =3   \\
-3x^{2} & =3 \\
 x^{2} & = -1
 \end{align}
$$
For which there are no solutions within the real numbers
$y=\frac{1}{2}x$
$$
\begin{align}
 x^{2}-\frac{x^{2}}{4} & =3   \\
\frac{3x^{2}}{4} & =3 \\
x^{2} & =4 \\
x=2 & \text{ or } x=-2
 \end{align}
$$
Since, if $x=-2$, the $y=-1$, and so we have $y<x$, then $x=-2$ cannot be a solution.

9. a
$$
\begin{align}
 \prod_{k=2}^{n} \log_{k}(k+1) & =\prod_{k=2}^{n} \frac{\ln(k+1)}{\ln(k)} \\
 & =\frac{ \prod_{k=2}^{n} \ln(k+1) }{ \prod_{k=2}^{n} \ln(k) } \\
 & =\frac{\prod_{k=3}^{n} \ln(k)\cdot \ln(n)}{\prod_{k=3}^{n} \ln(k)\cdot \ln(2)} \\
 & =\log_{2}(n)
 \end{align}
$$
now if we set
$$
\begin{align}
 \log_{2}(n) & =10   \\
n & =2^{10} \\
 & =1024
 \end{align}
$$
10. a) if we start with 
$$
\begin{align}
 \sin ^{2}x+\cos ^{2}x & =1   \\
\frac{\sin ^{2}x}{\cos ^{2}x}+\frac{\cos ^{2}x}{\cos ^{2}x} & =\frac{1}{\cos ^{2}x} \\
\tan ^{2}x+1 & =\sec^{2}x
 \end{align}
$$
b) if we start with
$$
\begin{align}
 \sin ^{2}x+\cos ^{2}x  & =1  \\
\frac{\sin ^{2}x}{\sin ^{2}x}+\frac{\cos ^{2}x}{\sin ^{2}x} & =\frac{1}{\sin ^{2}x} \\
1+\cot ^{2}x & =\csc ^{2}x
 \end{align}
$$
11. a)
$$
\begin{align}
 e^{x}e^{y} & =\sum_{k=0}^{\infty} \frac{x^{k}}{k!} \sum_{k=0}^{\infty} \frac{y^{k}}{k!}   \\
 & =\sum_{k=0}^{\infty} \sum_{n=0}^{k} \frac{x^{k}y^{n-k}}{n!(k-n)!} \\
 & =\sum_{k=0}^{\infty} \sum_{n=0}^{k} \frac{x^{k}y^{n-k}\cdot k!}{n!(k-n)!\cdot k!} \\
& =\sum_{k=0}^{\infty} \sum_{n=0}^{k} \binom{k}{n}\frac{x^{k}y^{n-k}}{k!} \\
& =\sum_{k=0}^{\infty} \frac{(x+y)^{k}}{k!} \\
 & =e^{x+y}
 \end{align}
$$
b) Note how above, there are no restrictions on $x$ and $y$, as long as they are real (or complex). Now note that:
$$
e^{-x}\cdot e^{x}=e^{-x+x}=e^{0}=1
$$
Therefore
$$
e^{-x}=\frac{1}{e^{x}}
$$

12. i) Since $\sin(x+y)=\sin x\cos y+\cos x\sin y$, and $\cos(x+y)=\cos x\cos y-\sin x\sin y$, we have
$$
\begin{align}
\tan(x+y) & =\frac{\sin(x+y)}{\cos(x+y)}  \\
& =\frac{\sin x\cos y+\cos x\sin y}{\cos x\cos y-\sin x\sin y} \\
& =\frac{\frac{\sin x\cos y}{\cos x\cos y}+\frac{\cos x\sin y}{\cos x\cos y}}{\frac{\cos x\cos y}{\cos x\cos y}-\frac{\sin x\sin y}{\cos x\cos y}} \\
& = \frac{\tan x+\tan y}{1-\tan x\tan y}
\end{align}
$$
Note that $\arctan(\tan (x))=x$ if and only if $-\pi/2 <x<\pi/2$, but $\tan(\arctan(x))=x$ for all $x \in\mathbb{R}$. Now plug $\arctan x$ and $\arctan y$ into the above equation, we now have
$$
\begin{align}
 \tan(\arctan(x)+\arctan(y))  & =\frac{ \tan(\arctan(x))+\tan(\arctan(y)) }{ 1-\tan(\arctan(x))\tan(\arctan(y)) } \\
 & =\frac{ x+y }{ 1-xy } \\
\arctan(x)+\arctan(y) & =\arctan\left( \frac{ x+y }{ 1-xy } \right)
 \end{align}
$$
As stated above, this final step only holds if $-\pi/2<\arctan x+\arctan y<\pi/2$, as the argument must fall in those bounds.

ii)
More carefully, we have that $\tan x=\tan(x+\pi)=\tan(x+k\pi)$ for all $k \in \mathbb{Z}$, So $\arctan$ is defined in such a way that it restricts the domain of $\tan$ to between the first positive asymptote, and the first negative asymptote. These occur at $\pi/2$ and $-\pi/2$ respectively. Therefore, if $-\pi/2<x<\pi/2$, then it falls within this restricted domain, and so can be inverted properly. 

If $x$ falls outside this domain, then we must add a multiple of $\pi$ to correct. That is, if $x \in (\frac{\pi}{2}+(k-1)\pi, \frac{\pi}{2}+k\pi)$, then we must subtract $k\pi$ to correct. Since $-\pi<\arctan x+\arctan y<\pi$, then define
$$
f(x, y)=\begin{cases}
\pi & \arctan x+\arctan y> \frac{\pi}{2} \\
-\pi & \arctan x+\arctan y< \frac{\pi}{2} \\
0 & \text{otherwise}
\end{cases}
$$

So the final equation for any value of $x, y \in \mathbb{R}$ is
$$
\arctan(x)+\arctan(y) =\arctan\left( \frac{ x+y }{ 1-xy } \right)+f(x,\, y)
$$

iii)
$$
\begin{align}
	 \arctan(1)+\arctan(2)+\arctan(3) &=\arctan\left( \frac{1+2}{1-2} \right)+f(1, 2)+\arctan(3) \\
	 & =\arctan(-3)+\arctan(3)+f(1,\, 2) \\
 & =\arctan\left( \frac{ 3-3 }{ 1+9 } \right)+f(1,\, 2) \\
 & =f(1,\, 2)
 \end{align}
$$
Since $\arctan1=\frac{\pi}{2}$, and $\arctan 2 > \arctan 1$, then $\arctan 1+ \arctan 2>2\arctan1>\pi/2$. Therefore, $f(x,\,y)=\pi$.
Therefore, $$
\arctan(1)+\arctan(2)+\arctan(3)=\pi
$$
