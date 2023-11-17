---
tags:
  - calculus1
  - homework
date: 2023-11-14
---
[[Directory]], [[Calculus 1|Subject Directory]]
[[Calculus 1 HW6.pdf|Problem Sheet]]
# Tutors example
Let ${} f(x)=\sqrt{1+\sin x} {}$, with $x \in  [-\pi,\, \pi]$. We calculate
$$
\begin{align}
 \frac{df}{dx}  & =\frac{d}{dx} g(h(x))   \\
 & =g'(h(x))h'(x) \\
 & =\frac{\cos x}{2\sqrt{1+\sin x}}
 \end{align}
$$
Note that when ${} x=-\pi /2 {}$, this function does not exist. So we want to know if the derivative exists at all at $-\pi / 2$.
so we have
$$
\lim_{h\tto 0^{+}} \frac{f(x_{0}+h)-f(x_{0})}{h}\qquad \text{ where }x_{0}=-\frac{\pi}{2}
$$
So we have
$$
\begin{align}
 \lim_{h\tto 0^{+}} \frac{\sqrt{1+\sin\left( -\frac{\pi}{2}+h \right)}-\sqrt{1+\sin\left( -\frac{\pi}{2} \right)}}{h}  & =\lim_{h\tto 0^{+}} \frac{\sqrt{1+\sin\left( h-\frac{\pi}{2} \right)}}{h}  \\
	 & =\lim_{h\tto 0^{+}} \frac{\sqrt{1+\sin(h)\cos\left( -\frac{\pi}{2} \right)+\cos(h)\sin\left( -\frac{\pi}{2} \right)}}{h} \\
 & =\lim_{h\tto 0^{+}} \frac{\sqrt{1-\cos(h)}}{h} \\
 & =\lim_{h\tto 0^{+}} \frac{\sqrt{1-\left( 1-\frac{h^{2}}{2}+\frac{h^{4}}{24}-\frac{h^{6}}{6!}+\dots \right)}}{h}
 \end{align}
$$
This is a *prime* time to use big O notation.
so we have
$$
\lim_{h\tto 0^{+}} \frac{\sqrt{1-\left( 1-\frac{h^{2}}{2}+O(h^{4}) \right)}}{h}
$$
Since ${} h>0 {}$, then ${} h=\sqrt{h^{2}} {}$, then
$$
\begin{align}
 \lim_{h\tto 0^{+}}\frac{ \sqrt{\frac{h^{2}}{2}+O(h^{4})}  }{ \sqrt{h^{2}} }  & =\lim_{h\tto 0^{+}} \sqrt{\frac{1}{2}+O(h^{2})}=\frac{1}{\sqrt{2}} 
 \end{align}
$$
We see that if ${} \lim_{h\tto 0^{-}} {}$, then the only difference is that ${} -h=\sqrt{h^{2}} {}$, so we have
$$
\lim_{h\tto 0^{-}} \frac{f(x_{0}+h)+f(x_{0})}{h}=-\frac{1}{\sqrt{2}}
$$
So the limit does not exist, mean girls style.

45. a) 
$$
\frac{d}{dx} e^{-x^{2}}=e^{-x^{2}}\cdot (-2x)=-2xe^{-x^{2}}
$$
b)
$$
\frac{d}{dx}  \ln (\tan x)=\frac{1}{\tan x}\sec ^{2} x=\frac{1}{\sin x\cos x}=\frac{2}{\sin 2x}=2\csc 2x
$$
c)
$$
\frac{d}{dx}(x\ln x-x)=x\cdot \frac{1}{x}+\ln x-1=1-1+\ln x=\ln x
$$
d) 
$$
\frac{d}{dx} \arcsin (x^{2})=\frac{2x}{\sqrt{1-x^{4}}}
$$
e) 
$$
\frac{d}{dx} \arctan(e^{x})=\frac{e^{x}}{1+e^{2x}}
$$
f) 
$$
\frac{d}{dx} e^{\sin x}=e^{\sin x}\cos x
$$
g)
$$
\begin{align}
 \frac{d}{dx} (xe^{x\arctan x}) & =e^{x\arctan x}+xe^{x\arctan x}\left( \arctan x+\frac{x}{1+x^{2}} \right) \\
 & =e^{x\arctan x}\left( 1+x\arctan x+\frac{x^{2}}{1+x^{2}} \right)
 \end{align}
$$
h) 
$$
\begin{align}
\frac{d}{dx} \ln |\arcsin x| & =\frac{ |\arcsin x|' }{ \sqrt{1-x^{2}} }\cdot \frac{1}{|\arcsin x|} \\
 & =\frac{\operatorname{sgn}(\arcsin x)}{\sqrt{1-x^{2}}|\arcsin x|} \\
 & =\frac{\operatorname{sgn}(x)}{\sqrt{1-x^{2}}|\arcsin x|}
\end{align}
$$
46. 
c)
![[Pasted image 20231117134145.png]]
47. 
h)
$$
\begin{align}
 \frac{d}{dx} \ln\left( \sqrt{\frac{ 1+x^{2} }{ 1-x^{2} }} \right) & =\frac{1}{2}\frac{d}{dx} \ln{\frac{1+x^{2}}{1-x^{2}}} \\
 & =\frac{1}{2}\frac{d}{dx} \left( \frac{ 1+x^{2} }{ 1-x^{2} } \right) \frac{1-x^{2}}{1+x^{2}} \\
 & =\frac{1}{2}\frac{2x(1-x^{2})-(-2x)(1+x^{2})}{(1-x^{2})^{2}} \frac{1-x^{2}}{1+x^{2}} \\
 & =\frac{2x}{(1-x^{2})(1+x^{2})} \\
 & =\frac{2x}{1-x^{4}} \\
 \end{align}
 $$
 48. 
 c)
 Let $\mathcal{E}=\{ x^{k}e^{x}\mid k \in  \mathbb{N}_{0}, k\leq n \} {}$, and let ${} V_{n}=\span\{\mathcal{E}\}$. First note that ${} V_{n} {}$ is a vector space over $\mathbb{R} {}$, as it is a subspace of the vector space of functions, and given some ${} f, g \in V_{n} {}$, and ${} \alpha,\, \beta \in \mathbb{R} {}$, then ${} \alpha f+\beta g\in V_{n} {}$. Now observe that, if there exist some ${} \alpha_{1},\,\dots,\,\alpha_{n} {}$ such that
 $$
\sum_{k=0}^{\infty} \alpha_{n}x^{k}e^{x}=\mathbf{0}
$$then ${} \alpha_{n}$ must be $0$. All these properties also follow fairly easily from the properties of $\mathbb{P}_{n}$. Now we take the linear map defined by ${} \frac{d}{dx}  {}$, call it $D$. We calculate the matrix $D$. 
$$
\begin{align}
 D(x^{0}e^{x}) & =e^{x} & &  =1x^{0}e^{x}  \\
D(x^{1}e^{x}) & =xe^{x}+e^{x} & &  =1x^{0}e^{x}+1x^{1}e^{x} \\
D(x^{2}e^{x}) & =x^{2}e^{x}+2xe^{x} &  & =0x^{0}e^{x}+2xe^{x}+1x^{2}e^{x}  \\
\vdots \\
D(x^{k}e^{x}) & =x^{k}e^{x}+kx^{k-1}e^{x} &  & =0x^{0}e^{x}+\dots+k x^{k-1}e^{x}+x^{k}e^{x}
 \end{align}
$$
Therefore, the matrix of $D$ with respect to the basis $\mathcal{E}$ in the standard basis of $\mathbb{R}^{n}$ is
$$
M=\begin{pmatrix}
1 & 0 & 0 & \dots  & 0&  0 & \dots& 0 & 0 \\
1 & 1 & 0 & \dots & 0 & 0  & \dots  & 0& 0\\
0 & 2 & 1 & \dots & 0 & 0  & \dots  & 0& 0\\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots  & \ddots & \vdots& \vdots\\
0 & 0 & 0 & \dots & k & 1 & \dots &  0& 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots  & \vdots\\
0 & 0 & 0 & \dots & 0 & 0 & \dots  & n& 1
\end{pmatrix}
$$
We want to calculate ${} M^{n}$. Since we want to calculate $M^{n}x^{n}e^{x} {}$, then we only care about the final column. Given a matrix such that
$$
M^{k}=\begin{pmatrix}a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \dots & a_{nn} \end{pmatrix}
$$
We see that
$$
M^{k}M=
$$
