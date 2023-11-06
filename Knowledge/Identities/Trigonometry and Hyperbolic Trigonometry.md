---
tags:
  - trigonometry
  - identities
  - formulae
---
[[Directory]]
# Trigonometry
## Basic
### Definitions
#### Traditional
Define${} \cos \theta {}$ and ${} \sin \theta {}$ as the horizontal and vertical components of a section of area $x {}$ of the unit circle, like so.
![[unit-circle-with-trig.svg|400]]
The angle may be thought of as an area, due to the properties of radians. 
In this diagram, the blue angle $\theta {}$, corresponding to the area of the sector centred at $0 {}$, and bounded by ${} 1 {}$ and ${} P {}$. The red length is ${} \cos \theta {}$, the purple length is ${} \sin \theta {}$, and the orange length is $\tan\theta {}$.

#### Power Series
We define 
$$
\begin{align}
 \sin x & =\sum_{n=0}^{\infty} \frac{(-1)^{n}}{(2n+1)!}x^{2n+1}   \\
 & =x-\frac{x^{3}}{3!}+\frac{x^{5}}{5!}-\frac{x^{7}}{7!} +\dots
 \end{align}
$$
and 
$$
\begin{align}
 \cos x & =\sum_{n=0}^{\infty} \frac{(-1)^{n}}{(2n)!}x^{2n}   \\
 & =1-\frac{x^{2}}{2!}+\frac{x^{4}}{4!}-\frac{x^{6}}{6!}+\dots
 \end{align}
$$
There is no good power series definition of $\tan {}$, but here is the best one
$$
\begin{align}
 \tan x & =\sum_{n=1}^{\infty} \frac{(-1)^{n-1}2^{2n}(2^{2n}-1)B_{2n}}{(2n)!} x^{2n-1}   \\
 & =x+\frac{x^{3}}{3}+\frac{2x^{5}}{15}+\frac{17x^{7}}{315}+\dots
 \end{align}
$$

#### Right Triangle
In a right triangle, which has an angle ${} \theta {}$, and 3 sides: $h {}$, the hypotenuse, ${} a {}$, the side adjacent to the angle ${} \theta {}$, and ${} p$, the angle opposite the angle $\theta {}$, like so
![[Pasted image 20231017164730.png|200]]
So we define 
$$
\sin \theta=\frac{p}{h}
$$
and
$$
\cos\theta=\frac{a}{h}
$$
and
$$
\tan \theta=\frac{p}{a}
$$
#### Complex Exponential
If we use $\exp (x) {}$ extended to the complex domain, then we can define
$$
\sin x=\frac{e^{ix}-e^{-ix}}{2i}
$$
and
$$
\cos x=\frac{e^{ix}+e^{-ix}}{2}
$$
and consequently
$$
\begin{align}
 \tan x&= \frac{e^{ix}-e^{-ix}}{i(e^{ix}+e^{-ix})} \\
 & =\frac{e^{2ix}-1}{i(e^{2ix}+1)} 
 \end{align}
$$
#### Differential Equations
Given the differential equation
$$
f''(x)=-f(x)
$$
- ${} \sin x {}$ is the solution when ${} f(0)=0 {}$ and $f'(0)=1$
- ${} \cos x$ is the solution when ${} f(0)=1 {}$ and ${} f'(0)=0 {}$
There is no reasonable differential definition of tangent, but one is given anyway
$$
f'(x)=1+f(x)^{2}
$$
where ${} f(0)=0 {}$.
#### Inverse Trigonometric Functions
Define
$$
\begin{align}
\csc x & =\frac{1}{\sin x} \\
\sec x & =\frac{1}{\cos x} \\
\cot x & =\frac{1}{\tan x}
\end{align}
$$
In right triangle definition, this gives
$$
\begin{align}
\csc x & =\frac{h}{p} \\ \\

\sec x & =\frac{h}{a} \\ \\

\cot & =\frac{a}{p}
\end{align}
$$
Geometrically, they can be viewed on this diagram, although there are many such diagrams
![[trigonometric-functions.svg|400]]
They also have the following complex definitions
$$
\begin{align}
\csc x & =\frac{2i}{e^{ix}-e^{-ix}} \\
\sec x & = \frac{2}{e^{ix}+e^{-ix}} \\
\cot x & =\frac{i(e^{ix}+e^{-ix})}{e^{ix}-e^{-ix}} \\
 & =i \frac{e^{2ix}+1}{e^{2ix}-1}
\end{align}
$$
## Phase Identities
### Sine and Cosecant
#### Reflections
${} \sin(-\theta)=-\sin\theta {}$
${} \csc(-\theta)=-\csc\theta {}$

